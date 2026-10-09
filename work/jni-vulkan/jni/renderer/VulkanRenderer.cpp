#include "VulkanCore.h"
#include "Renderer.h"
#include "../InputBridge.h"
#include "../Logger.h"
#include "../Menu.h"
#include <android/hardware_buffer.h>
#include <android/native_window.h>
#include <android/surface_control.h>
#include <android/data_space.h>
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <cerrno>
#include <memory>
#include <mutex>
#include <poll.h>
#include <thread>
#include <unistd.h>

namespace {
using namespace overlay_vk;
using Clock = std::chrono::steady_clock;
std::atomic<bool> requested_stop{false};

// Callback-side state contains NO renderer/device/ImGui pointers.
// It remains valid if Android delivers completion after the render thread exits.
struct ReuseState {
    std::mutex mutex;
    bool released = true;
    int fd = -1;
    ~ReuseState() { if (fd >= 0) close(fd); }
    bool CanWrite() {
        std::lock_guard<std::mutex> lock(mutex);
        if (!released) return false;
        if (fd < 0) return true;
        pollfd pfd{fd, POLLIN, 0};
        int result;
        do { result = poll(&pfd, 1, 0); } while (result < 0 && errno == EINTR);
        if (result < 0 || (pfd.revents & (POLLERR | POLLNVAL)))
            throw std::runtime_error("Invalid compositor release fence; buffer will not be reused");
        if (result == 0 || !(pfd.revents & POLLIN)) return false;
        close(fd); fd = -1;
        return true;
    }
    void MarkSubmitted() {
        std::lock_guard<std::mutex> lock(mutex);
        released = false;
    }
    void Released(int fence_fd) {
        std::lock_guard<std::mutex> lock(mutex);
        if (fd >= 0) close(fd);
        fd = fence_fd; released = true;
    }
};
struct Completion {
    std::mutex mutex;
    std::condition_variable cv;
    bool done = false;
    bool Wait(std::chrono::milliseconds duration) {
        std::unique_lock<std::mutex> lock(mutex);
        return cv.wait_for(lock, duration, [&] { return done; });
    }
    void Finish() {
        { std::lock_guard<std::mutex> lock(mutex); done = true; }
        cv.notify_all();
    }
};
struct Callback {
    ASurfaceControl* control;
    std::shared_ptr<ReuseState> previous;
    std::shared_ptr<Completion> completion;
    Callback(ASurfaceControl* c, std::shared_ptr<ReuseState> p, std::shared_ptr<Completion> done)
        : control(c), previous(std::move(p)), completion(std::move(done)) { ASurfaceControl_acquire(control); }
    ~Callback() { ASurfaceControl_release(control); }
    static void OnComplete(void* opaque, ASurfaceTransactionStats* stats) noexcept {
        std::unique_ptr<Callback> self(static_cast<Callback*>(opaque));
        try {
            if (self->previous) {
                const int fd = ASurfaceTransactionStats_getPreviousReleaseFenceFd(stats, self->control);
                self->previous->Released(fd); // Caller owns and eventually closes this fd.
            }
            self->completion->Finish();
        } catch (...) {
            LOGE("Vulkan surface completion failed; affected buffers remain unavailable");
        }
    }
};
struct Transaction {
    ASurfaceTransaction* p = ASurfaceTransaction_create();
    Transaction() { if (!p) throw std::bad_alloc(); }
    ~Transaction() { ASurfaceTransaction_delete(p); }
    Transaction(const Transaction&) = delete;
    Transaction& operator=(const Transaction&) = delete;
};
struct Target {
    VkDevice device = VK_NULL_HANDLE;
    AHardwareBuffer* buffer = nullptr;
    VkImage image = VK_NULL_HANDLE;
    VkDeviceMemory memory = VK_NULL_HANDLE;
    VkImageView view = VK_NULL_HANDLE;
    VkFramebuffer framebuffer = VK_NULL_HANDLE;
    VkImageLayout layout = VK_IMAGE_LAYOUT_UNDEFINED;
    std::shared_ptr<ReuseState> reuse = std::make_shared<ReuseState>();
    Target() = default;
    Target(const Target&) = delete;
    Target& operator=(const Target&) = delete;
    ~Target() {
        // GPU work must be complete before the owner destroys a Target. Imported memory
        // releases its own AHB reference; SurfaceFlinger retains its independent reference.
        if (framebuffer) vkDestroyFramebuffer(device, framebuffer, nullptr);
        if (view) vkDestroyImageView(device, view, nullptr);
        if (image) vkDestroyImage(device, image, nullptr);
        if (memory) vkFreeMemory(device, memory, nullptr);
        if (buffer) AHardwareBuffer_release(buffer);
    }
};

class AndroidRenderer {
    Core core;
    ASurfaceControl* control = nullptr;
    std::array<std::unique_ptr<Target>, 3> targets;
    std::shared_ptr<ReuseState> previous;
    std::shared_ptr<Completion> pending;
    Clock::time_point submitted_at{};
    uint32_t width = 0, height = 0;
    size_t next = 0;
    PFN_vkGetAndroidHardwareBufferPropertiesANDROID get_ahb_properties = nullptr;
public:
    AndroidRenderer() = default;
    AndroidRenderer(const AndroidRenderer&) = delete;
    AndroidRenderer& operator=(const AndroidRenderer&) = delete;
    ~AndroidRenderer() {
        overlay_input::queue().disable();
        if (core.device) (void)vkDeviceWaitIdle(core.device);
        if (control) {
            // Releasing a control alone does not necessarily remove its visible layer.
            ASurfaceTransaction* tx = ASurfaceTransaction_create();
            if (tx) {
                ASurfaceTransaction_setVisibility(tx, control, ASURFACE_TRANSACTION_VISIBILITY_HIDE);
                ASurfaceTransaction_reparent(tx, control, nullptr);
                ASurfaceTransaction_apply(tx);
                ASurfaceTransaction_delete(tx);
            }
            ASurfaceControl_release(control); control = nullptr;
        }
        for (auto& target : targets) target.reset();
        // Core is destroyed last, after all imported images/framebuffers are gone.
    }

    void Init(ANativeWindow* parent, uint32_t w, uint32_t h) {
        core.Init(true);
        LOGI("Vulkan GPU: %s; API %u.%u.%u; ImGui %s", core.properties.deviceName,
            VK_VERSION_MAJOR(core.properties.apiVersion), VK_VERSION_MINOR(core.properties.apiVersion),
            VK_VERSION_PATCH(core.properties.apiVersion), IMGUI_VERSION);
        get_ahb_properties = reinterpret_cast<PFN_vkGetAndroidHardwareBufferPropertiesANDROID>(
            vkGetDeviceProcAddr(core.device, "vkGetAndroidHardwareBufferPropertiesANDROID"));
        if (!get_ahb_properties) throw std::runtime_error("Missing Vulkan Android hardware-buffer import entry point");
        control = ASurfaceControl_createFromWindow(parent, "JNI Vulkan Overlay");
        if (!control) throw std::runtime_error("Cannot create overlay SurfaceControl from parent window");
        {
            Transaction tx;
            ASurfaceTransaction_setZOrder(tx.p, control, 1000);
            ASurfaceTransaction_setPosition(tx.p, control, 0, 0);
            ASurfaceTransaction_setBufferAlpha(tx.p, control, 1.0f);
            ASurfaceTransaction_setBufferTransparency(tx.p, control, ASURFACE_TRANSACTION_TRANSPARENCY_TRANSLUCENT);
            ASurfaceTransaction_setBufferDataSpace(tx.p, control, ADATASPACE_SRGB);
            ASurfaceTransaction_setBufferTransform(tx.p, control, 0);
            ASurfaceTransaction_setEnableBackPressure(tx.p, control, true);
            ASurfaceTransaction_apply(tx.p);
        }
        Resize(w, h);
        ImGui::StyleColorsClassic();
        ImGui::GetStyle().ScaleAllSizes(3.0f);
        LoadSystemFont();
        overlay_input::queue().enable();
    }

    bool PresentationReady() {
        if (!pending) return true;
        if (pending->Wait(std::chrono::milliseconds(5))) { pending.reset(); return true; }
        if (Clock::now() - submitted_at > std::chrono::seconds(5))
            throw std::runtime_error("Surface presentation stalled for 5s; stopping without reusing busy buffers");
        return false;
    }

    void Resize(uint32_t w, uint32_t h) {
        if (!w || !h || w > core.properties.limits.maxFramebufferWidth ||
            h > core.properties.limits.maxFramebufferHeight)
            throw std::runtime_error("Invalid or unsupported overlay dimensions");
        Check(vkDeviceWaitIdle(core.device), "wait GPU before resize");
        // Do not overwrite old buffers: create a new generation. Android retains old
        // displayed buffers independently until a later transaction replaces them.
        std::array<std::unique_ptr<Target>, 3> replacement;
        for (auto& target : replacement) target = MakeTarget(w, h);
        targets.swap(replacement);
        width = w; height = h; next = 0;
        Transaction tx;
        const ARect crop{0, 0, static_cast<int32_t>(w), static_cast<int32_t>(h)};
        ASurfaceTransaction_setCrop(tx.p, control, crop); // NDK C++ API takes const ARect&.
        ASurfaceTransaction_apply(tx.p);
        LOGI("Vulkan target pool rebuilt: %u x %u, 3 AHardwareBuffers", width, height);
    }

    bool Frame(uint32_t w, uint32_t h, float delta) {
        if (!PresentationReady()) return false;
        if (w != width || h != height) Resize(w, h);
        Target* chosen = nullptr;
        for (size_t i = 0; i < targets.size(); ++i) {
            size_t index = (next + i) % targets.size();
            if (targets[index]->reuse->CanWrite()) {
                chosen = targets[index].get(); next = (index + 1) % targets.size(); break;
            }
        }
        if (!chosen) return false; // Release fences have not signaled; never draw into a busy image.
        ImGui::SetCurrentContext(core.context);
        ImGuiIO& io = ImGui::GetIO();
        io.DisplaySize = ImVec2(static_cast<float>(width), static_cast<float>(height));
        io.DisplayFramebufferScale = ImVec2(1, 1);
        io.DeltaTime = std::clamp(delta, 0.000001f, 0.1f);
        ImGui_ImplVulkan_NewFrame();
        DrainOverlayInput();
        ImGui::NewFrame();
        BeginDraw(static_cast<float>(width), static_cast<float>(height));
        ImGui::Render();
        core.Begin(chosen->image, chosen->framebuffer, width, height, chosen->layout, true);
        core.End(chosen->image, true);
        core.SubmitAndWait();
        chosen->layout = VK_IMAGE_LAYOUT_GENERAL;
        Present(*chosen);
        return true;
    }

private:
    std::unique_ptr<Target> MakeTarget(uint32_t w, uint32_t h) {
        VkPhysicalDeviceExternalImageFormatInfo external_query{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_IMAGE_FORMAT_INFO};
        external_query.handleType = VK_EXTERNAL_MEMORY_HANDLE_TYPE_ANDROID_HARDWARE_BUFFER_BIT_ANDROID;
        VkPhysicalDeviceImageFormatInfo2 query{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2};
        query.pNext = &external_query; query.format = Core::Format;
        query.type = VK_IMAGE_TYPE_2D; query.tiling = VK_IMAGE_TILING_OPTIMAL;
        query.usage = VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_SAMPLED_BIT;
        VkAndroidHardwareBufferUsageANDROID usage{VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID};
        VkExternalImageFormatProperties external_properties{VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES};
        external_properties.pNext = &usage;
        VkImageFormatProperties2 supported{VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2};
        supported.pNext = &external_properties;
        Check(vkGetPhysicalDeviceImageFormatProperties2(core.physical, &query, &supported), "query AHB render-target support");
        if (!(external_properties.externalMemoryProperties.externalMemoryFeatures & VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT))
            throw std::runtime_error("RGBA8 AHardwareBuffer import is not supported");
        if (w > supported.imageFormatProperties.maxExtent.width || h > supported.imageFormatProperties.maxExtent.height)
            throw std::runtime_error("AHardwareBuffer image extent is unsupported");
        auto target = std::make_unique<Target>();
        target->device = core.device;
        AHardwareBuffer_Desc desc{};
        desc.width = w; desc.height = h; desc.layers = 1;
        desc.format = AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM;
        desc.usage = usage.androidHardwareBufferUsage | AHARDWAREBUFFER_USAGE_GPU_COLOR_OUTPUT |
            AHARDWAREBUFFER_USAGE_GPU_SAMPLED_IMAGE | AHARDWAREBUFFER_USAGE_COMPOSER_OVERLAY;
        if (AHardwareBuffer_allocate(&desc, &target->buffer) != 0 || !target->buffer)
            throw std::runtime_error("AHardwareBuffer_allocate failed for Vulkan render target");
        VkAndroidHardwareBufferFormatPropertiesANDROID format{VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_ANDROID};
        VkAndroidHardwareBufferPropertiesANDROID properties{VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID};
        properties.pNext = &format;
        Check(get_ahb_properties(core.device, target->buffer, &properties), "get AHardwareBuffer properties");
        if (format.format != Core::Format || !(format.formatFeatures & VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BIT))
            throw std::runtime_error("AHardwareBuffer format cannot be rendered as RGBA8");
        VkExternalMemoryImageCreateInfo external{VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO};
        external.handleTypes = VK_EXTERNAL_MEMORY_HANDLE_TYPE_ANDROID_HARDWARE_BUFFER_BIT_ANDROID;
        VkImageCreateInfo image{VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO};
        image.pNext = &external; image.imageType = VK_IMAGE_TYPE_2D; image.format = Core::Format;
        image.extent = {w, h, 1}; image.mipLevels = 1; image.arrayLayers = 1;
        image.samples = VK_SAMPLE_COUNT_1_BIT; image.tiling = VK_IMAGE_TILING_OPTIMAL;
        image.usage = query.usage; image.sharingMode = VK_SHARING_MODE_EXCLUSIVE;
        image.initialLayout = VK_IMAGE_LAYOUT_UNDEFINED;
        Check(vkCreateImage(core.device, &image, nullptr, &target->image), "create imported Vulkan image");
        VkMemoryDedicatedAllocateInfo dedicated{VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO};
        dedicated.image = target->image;
        VkImportAndroidHardwareBufferInfoANDROID import{VK_STRUCTURE_TYPE_IMPORT_ANDROID_HARDWARE_BUFFER_INFO_ANDROID};
        import.pNext = &dedicated; import.buffer = target->buffer;
        VkMemoryAllocateInfo alloc{VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO};
        alloc.pNext = &import; alloc.allocationSize = properties.allocationSize;
        // For AHB images, obtain allocation size/type bits from AHB properties, NOT
        // vkGetImageMemoryRequirements before binding (which is invalid for this import).
        alloc.memoryTypeIndex = core.MemoryType(properties.memoryTypeBits, 0, VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT);
        Check(vkAllocateMemory(core.device, &alloc, nullptr, &target->memory), "import AHardwareBuffer memory");
        Check(vkBindImageMemory(core.device, target->image, target->memory, 0), "bind imported AHB image");
        VkImageViewCreateInfo view{VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO};
        view.image = target->image; view.viewType = VK_IMAGE_VIEW_TYPE_2D; view.format = Core::Format;
        view.subresourceRange = {VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1};
        Check(vkCreateImageView(core.device, &view, nullptr, &target->view), "create AHB image view");
        VkFramebufferCreateInfo fb{VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO};
        fb.renderPass = core.render_pass; fb.attachmentCount = 1; fb.pAttachments = &target->view;
        fb.width = w; fb.height = h; fb.layers = 1;
        Check(vkCreateFramebuffer(core.device, &fb, nullptr, &target->framebuffer), "create AHB framebuffer");
        return target;
    }

    void Present(Target& target) {
        Transaction tx;
        auto complete = std::make_shared<Completion>();
        auto callback = std::make_unique<Callback>(control, previous, complete);
        ASurfaceTransaction_setBuffer(tx.p, control, target.buffer, -1);
        ASurfaceTransaction_setVisibility(tx.p, control, ASURFACE_TRANSACTION_VISIBILITY_SHOW);
        ASurfaceTransaction_setOnComplete(tx.p, callback.get(), Callback::OnComplete);
        target.reuse->MarkSubmitted();
        pending = complete; submitted_at = Clock::now();
        previous = target.reuse;
        // Transfer callback ownership BEFORE apply, since it may complete promptly.
        callback.release();
        ASurfaceTransaction_apply(tx.p);
    }

    static void LoadSystemFont() {
        const char* candidates[] = {
            "/system/fonts/NotoSansCJK-Regular.ttc",
            "/system/fonts/NotoSansSC-Regular.otf",
            "/system/fonts/NotoSansCJKsc-Regular.otf",
            "/system/fonts/DroidSansFallback.ttf"
        };
        ImGuiIO& io = ImGui::GetIO();
        ImFontConfig cfg;
        cfg.OversampleH = 1; cfg.OversampleV = 1;
        for (const char* path : candidates) {
            if (access(path, R_OK) != 0) continue;
            if (auto* font = io.Fonts->AddFontFromFileTTF(path, 25.2f, &cfg)) {
                io.FontDefault = font;
                MenuUseChinese = true;
                LOGI("Vulkan UI uses device font: %s", path);
                return;
            }
        }
        // No external font binaries are packaged. Keep the menu readable on OEMs
        // without one of the known system fonts, rather than showing missing glyphs.
        cfg.SizePixels = 25.2f;
        io.FontDefault = io.Fonts->AddFontDefault(&cfg);
        MenuUseChinese = false;
        LOGW("CJK system font not found; using the built-in default font and English labels");
    }
};
} // namespace

extern "C" __attribute__((visibility("default"))) void Overlay_RequestStop() {
    requested_stop.store(true, std::memory_order_release);
}

void RunSurfaceControlOverlay(ANativeWindow* window) {
    if (!window) return;
    const auto release = [](ANativeWindow* p) { ANativeWindow_release(p); };
    std::unique_ptr<ANativeWindow, decltype(release)> owner(window, release);
    overlay_input::SessionInputGuard input_guard;
    requested_stop.store(false, std::memory_order_release);
    const int initial_width = ANativeWindow_getWidth(window);
    const int initial_height = ANativeWindow_getHeight(window);
    if (initial_width <= 0 || initial_height <= 0) return;
    AndroidRenderer renderer;
    renderer.Init(window, static_cast<uint32_t>(initial_width), static_cast<uint32_t>(initial_height));
    auto last = Clock::now();
    while (!requested_stop.load(std::memory_order_acquire)) {
        const auto frame_start = Clock::now();
        const int w = ANativeWindow_getWidth(window), h = ANativeWindow_getHeight(window);
        if (w <= 0 || h <= 0) break;
        const float delta = std::chrono::duration<float>(frame_start - last).count();
        if (renderer.Frame(static_cast<uint32_t>(w), static_cast<uint32_t>(h), delta)) last = frame_start;
        std::this_thread::sleep_until(frame_start + std::chrono::microseconds(16667));
    }
    LOGI("Vulkan overlay stopped");
}
