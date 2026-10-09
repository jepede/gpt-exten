#pragma once
// Vulkan-only offscreen renderer for Android SurfaceControl overlays.
// No EGL, GLES, GL context, VkSurfaceKHR or VkSwapchainKHR is used.
#include <vulkan/vulkan.h>
#include <android/hardware_buffer.h>
#include <android/native_window.h>
#include <android/surface_control.h>
#include <imgui.h>
#include <backends/imgui_impl_vulkan.h>
#include <backends/imgui_impl_android.h>
#include <font_zt.h>
#include <InputBridge.h>
#include <Logger.h>
#include <algorithm>
#include <cstdint>
#include <cstring>
#include <limits>

struct VulkanUiState {
    float ScreenWidth = 0;
    float ScreenHeight = 0;
};
inline VulkanUiState VulkanState{};

inline bool LoadFont(float pixels) {
    if (!ImGui::GetCurrentContext() || pixels <= 0) return false;
    ImGuiIO& io = ImGui::GetIO();
    ImFontConfig cfg;
    cfg.FontDataOwnedByAtlas = false;
    cfg.SizePixels = pixels;
    cfg.OversampleH = 1;
    ImFont* font = io.Fonts->AddFontFromMemoryTTF(
        (void*)Font, Font_len, pixels, &cfg, io.Fonts->GetGlyphRangesChineseFull());
    if (!font) font = io.Fonts->AddFontDefault();
    if (font) io.FontDefault = font;
    return font != nullptr;
}

class VulkanOffscreen {
public:
    VulkanOffscreen() = default;
    VulkanOffscreen(const VulkanOffscreen&) = delete;
    VulkanOffscreen& operator=(const VulkanOffscreen&) = delete;
    ~VulkanOffscreen() { shutdown(); }

    bool initialize(uint32_t width, uint32_t height) {
        if (!width || !height || width > 8192 || height > 8192) return false;
        VkApplicationInfo app{VK_STRUCTURE_TYPE_APPLICATION_INFO};
        app.pApplicationName = "Vulkan ImGui overlay";
        app.apiVersion = VK_API_VERSION_1_0;
        VkInstanceCreateInfo ic{VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO};
        ic.pApplicationInfo = &app;
        if (!check(vkCreateInstance(&ic, nullptr, &instance_), "vkCreateInstance")) return false;

        uint32_t count = 0;
        if (!check(vkEnumeratePhysicalDevices(instance_, &count, nullptr), "vkEnumeratePhysicalDevices") || !count) return false;
        // Android devices typically have a single graphics-capable physical device.
        VkPhysicalDevice devices[16]{};
        if (count > 16) count = 16;
        if (!check(vkEnumeratePhysicalDevices(instance_, &count, devices), "vkEnumeratePhysicalDevices(list)")) return false;
        for (uint32_t i = 0; i < count && !gpu_; ++i) {
            uint32_t familyCount = 0;
            vkGetPhysicalDeviceQueueFamilyProperties(devices[i], &familyCount, nullptr);
            if (!familyCount || familyCount > 128) continue;
            VkQueueFamilyProperties families[128]{};
            vkGetPhysicalDeviceQueueFamilyProperties(devices[i], &familyCount, families);
            for (uint32_t j = 0; j < familyCount; ++j) {
                if (families[j].queueCount && (families[j].queueFlags & VK_QUEUE_GRAPHICS_BIT)) {
                    gpu_ = devices[i];
                    queueFamily_ = j;
                    break;
                }
            }
        }
        if (!gpu_) { LOGE("Vulkan: no graphics queue"); return false; }
        vkGetPhysicalDeviceMemoryProperties(gpu_, &memProps_);
        vkGetPhysicalDeviceProperties(gpu_, &gpuProps_);
        VkFormatProperties formatProps{};
        vkGetPhysicalDeviceFormatProperties(gpu_, VK_FORMAT_R8G8B8A8_UNORM, &formatProps);
        if (!(formatProps.optimalTilingFeatures & VK_FORMAT_FEATURE_COLOR_ATTACHMENT_BIT)) {
            LOGE("Vulkan: RGBA8 color attachment unsupported");
            return false;
        }
        float priority = 1.0f;
        VkDeviceQueueCreateInfo qi{VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO};
        qi.queueFamilyIndex = queueFamily_; qi.queueCount = 1; qi.pQueuePriorities = &priority;
        VkDeviceCreateInfo di{VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO};
        di.queueCreateInfoCount = 1; di.pQueueCreateInfos = &qi;
        if (!check(vkCreateDevice(gpu_, &di, nullptr, &device_), "vkCreateDevice")) return false;
        vkGetDeviceQueue(device_, queueFamily_, 0, &queue_);

        VkAttachmentDescription attachment{};
        attachment.format = VK_FORMAT_R8G8B8A8_UNORM;
        attachment.samples = VK_SAMPLE_COUNT_1_BIT;
        attachment.loadOp = VK_ATTACHMENT_LOAD_OP_CLEAR;
        attachment.storeOp = VK_ATTACHMENT_STORE_OP_STORE;
        attachment.stencilLoadOp = VK_ATTACHMENT_LOAD_OP_DONT_CARE;
        attachment.stencilStoreOp = VK_ATTACHMENT_STORE_OP_DONT_CARE;
        attachment.initialLayout = VK_IMAGE_LAYOUT_UNDEFINED; // discard previous frame
        attachment.finalLayout = VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL;
        VkAttachmentReference attachmentRef{0, VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL};
        VkSubpassDescription subpass{};
        subpass.pipelineBindPoint = VK_PIPELINE_BIND_POINT_GRAPHICS;
        subpass.colorAttachmentCount = 1; subpass.pColorAttachments = &attachmentRef;
        VkSubpassDependency dependencies[2]{};
        dependencies[0].srcSubpass = VK_SUBPASS_EXTERNAL;
        dependencies[0].dstSubpass = 0;
        dependencies[0].srcStageMask = VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT;
        dependencies[0].dstStageMask = VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT;
        dependencies[0].dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;
        dependencies[1].srcSubpass = 0;
        dependencies[1].dstSubpass = VK_SUBPASS_EXTERNAL;
        dependencies[1].srcStageMask = VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT;
        dependencies[1].dstStageMask = VK_PIPELINE_STAGE_TRANSFER_BIT;
        dependencies[1].srcAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;
        dependencies[1].dstAccessMask = VK_ACCESS_TRANSFER_READ_BIT;
        VkRenderPassCreateInfo rp{VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO};
        rp.attachmentCount = 1; rp.pAttachments = &attachment;
        rp.subpassCount = 1; rp.pSubpasses = &subpass;
        rp.dependencyCount = 2; rp.pDependencies = dependencies;
        if (!check(vkCreateRenderPass(device_, &rp, nullptr, &renderPass_), "vkCreateRenderPass")) return false;

        VkDescriptorPoolSize sizes[] = {
            {VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER, 256},
            {VK_DESCRIPTOR_TYPE_SAMPLED_IMAGE, 256},
            {VK_DESCRIPTOR_TYPE_SAMPLER, 64},
        };
        VkDescriptorPoolCreateInfo dp{VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO};
        dp.flags = VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT;
        dp.maxSets = 512; dp.poolSizeCount = 3; dp.pPoolSizes = sizes;
        if (!check(vkCreateDescriptorPool(device_, &dp, nullptr, &descriptorPool_), "vkCreateDescriptorPool")) return false;
        VkCommandPoolCreateInfo cp{VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO};
        cp.queueFamilyIndex = queueFamily_;
        cp.flags = VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT;
        if (!check(vkCreateCommandPool(device_, &cp, nullptr, &commandPool_), "vkCreateCommandPool")) return false;
        VkCommandBufferAllocateInfo ca{VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO};
        ca.commandPool = commandPool_; ca.level = VK_COMMAND_BUFFER_LEVEL_PRIMARY; ca.commandBufferCount = 1;
        if (!check(vkAllocateCommandBuffers(device_, &ca, &command_), "vkAllocateCommandBuffers")) return false;
        VkFenceCreateInfo fc{VK_STRUCTURE_TYPE_FENCE_CREATE_INFO};
        fc.flags = VK_FENCE_CREATE_SIGNALED_BIT;
        if (!check(vkCreateFence(device_, &fc, nullptr, &fence_), "vkCreateFence")) return false;
        return createTarget(width, height);
    }

    bool initializeImGui() {
        ImGui_ImplVulkan_InitInfo info{};
        info.ApiVersion = VK_API_VERSION_1_0;
        info.Instance = instance_;
        info.PhysicalDevice = gpu_;
        info.Device = device_;
        info.QueueFamily = queueFamily_;
        info.Queue = queue_;
        info.DescriptorPool = descriptorPool_;
        info.MinImageCount = 2;
        info.ImageCount = 2;
        info.PipelineInfoMain.RenderPass = renderPass_;
        info.PipelineInfoMain.MSAASamples = VK_SAMPLE_COUNT_1_BIT;
        info.CheckVkResultFn = [](VkResult r) {
            if (r != VK_SUCCESS) LOGE("ImGui Vulkan backend error: %d", static_cast<int>(r));
        };
        backendReady_ = ImGui_ImplVulkan_Init(&info);
        return backendReady_;
    }

    bool resize(uint32_t width, uint32_t height) {
        if (width == width_ && height == height_) return true;
        if (!width || !height || width > 8192 || height > 8192) return false;
        if (!check(vkDeviceWaitIdle(device_), "vkDeviceWaitIdle(resize)")) return false;
        destroyTarget();
        return createTarget(width, height);
    }

    bool render(ImDrawData* drawData, AHardwareBuffer** result) {
        if (!result) return false;
        *result = nullptr;
        if (!backendReady_ || !framebuffer_ || !drawData) return false;
        if (!check(vkWaitForFences(device_, 1, &fence_, VK_TRUE, 3000000000ULL), "vkWaitForFences")) return false;
        if (!check(vkResetCommandBuffer(command_, 0), "vkResetCommandBuffer")) return false;
        VkCommandBufferBeginInfo cb{VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO};
        cb.flags = VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT;
        if (!check(vkBeginCommandBuffer(command_, &cb), "vkBeginCommandBuffer")) return false;

        VkClearValue clear{};
        clear.color.float32[0] = 0.0f;
        clear.color.float32[1] = 0.0f;
        clear.color.float32[2] = 0.0f;
        clear.color.float32[3] = 0.0f;
        VkRenderPassBeginInfo begin{VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO};
        begin.renderPass = renderPass_;
        begin.framebuffer = framebuffer_;
        begin.renderArea.extent = {width_, height_};
        begin.clearValueCount = 1; begin.pClearValues = &clear;
        vkCmdBeginRenderPass(command_, &begin, VK_SUBPASS_CONTENTS_INLINE);
        ImGui_ImplVulkan_RenderDrawData(drawData, command_);
        vkCmdEndRenderPass(command_);

        VkBufferImageCopy copy{};
        copy.imageSubresource.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT;
        copy.imageSubresource.layerCount = 1;
        copy.imageExtent = {width_, height_, 1};
        vkCmdCopyImageToBuffer(command_, image_, VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL, stagingBuffer_, 1, &copy);

        VkBufferMemoryBarrier barrier{VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER};
        barrier.srcAccessMask = VK_ACCESS_TRANSFER_WRITE_BIT;
        barrier.dstAccessMask = VK_ACCESS_HOST_READ_BIT;
        barrier.srcQueueFamilyIndex = VK_QUEUE_FAMILY_IGNORED;
        barrier.dstQueueFamilyIndex = VK_QUEUE_FAMILY_IGNORED;
        barrier.buffer = stagingBuffer_; barrier.offset = 0; barrier.size = VK_WHOLE_SIZE;
        vkCmdPipelineBarrier(command_, VK_PIPELINE_STAGE_TRANSFER_BIT,
                             VK_PIPELINE_STAGE_HOST_BIT, 0, 0, nullptr, 1, &barrier, 0, nullptr);
        if (!check(vkEndCommandBuffer(command_), "vkEndCommandBuffer")) return false;
        // Reset the fence only after command buffer recording has succeeded.
        if (!check(vkResetFences(device_, 1, &fence_), "vkResetFences")) return false;
        VkSubmitInfo submit{VK_STRUCTURE_TYPE_SUBMIT_INFO};
        submit.commandBufferCount = 1; submit.pCommandBuffers = &command_;
        if (!check(vkQueueSubmit(queue_, 1, &submit, fence_), "vkQueueSubmit")) return false;
        if (!check(vkWaitForFences(device_, 1, &fence_, VK_TRUE, 3000000000ULL), "vkWaitForFences(post-submit)")) return false;
        if (!hostCoherent_) {
            VkMappedMemoryRange invalid{VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE};
            invalid.memory = stagingMemory_; invalid.offset = 0; invalid.size = VK_WHOLE_SIZE;
            if (!check(vkInvalidateMappedMemoryRanges(device_, 1, &invalid), "vkInvalidateMappedMemoryRanges")) return false;
        }

        AHardwareBuffer_Desc desc{};
        desc.width = width_; desc.height = height_; desc.layers = 1;
        desc.format = AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM;
        desc.usage = AHARDWAREBUFFER_USAGE_GPU_SAMPLED_IMAGE |
                     AHARDWAREBUFFER_USAGE_GPU_COLOR_OUTPUT |
                     AHARDWAREBUFFER_USAGE_CPU_WRITE_OFTEN;
        AHardwareBuffer* output = nullptr;
        if (AHardwareBuffer_allocate(&desc, &output) != 0 || !output) {
            LOGE("AHardwareBuffer_allocate failed");
            return false;
        }
        AHardwareBuffer_describe(output, &desc);
        void* mapped = nullptr;
        if (AHardwareBuffer_lock(output, AHARDWAREBUFFER_USAGE_CPU_WRITE_OFTEN,
                                 -1, nullptr, &mapped) != 0 || !mapped) {
            AHardwareBuffer_release(output);
            LOGE("AHardwareBuffer_lock failed");
            return false;
        }
        const auto* source = static_cast<const uint8_t*>(stagingMapped_);
        auto* dest = static_cast<uint8_t*>(mapped);
        const size_t row = static_cast<size_t>(width_) * 4;
        const size_t dstRow = static_cast<size_t>(desc.stride) * 4;
        // Vulkan's positive viewport height follows top-to-bottom framebuffer rows;
        // unlike GLES glReadPixels(), no unconditional vertical flip is required.
        for (uint32_t y = 0; y < height_; ++y)
            std::memcpy(dest + y * dstRow, source + y * row, row);
        AHardwareBuffer_unlock(output, nullptr);
        *result = output; // Caller's reference must be released after setBuffer/apply.
        return true;
    }

    uint32_t width() const { return width_; }
    uint32_t height() const { return height_; }

    void shutdown() {
        if (device_) vkDeviceWaitIdle(device_);
        if (backendReady_ && ImGui::GetCurrentContext()) {
            ImGui_ImplVulkan_Shutdown();
            backendReady_ = false;
        }
        destroyTarget();
        if (device_) {
            if (fence_) vkDestroyFence(device_, fence_, nullptr);
            if (commandPool_) vkDestroyCommandPool(device_, commandPool_, nullptr);
            if (descriptorPool_) vkDestroyDescriptorPool(device_, descriptorPool_, nullptr);
            if (renderPass_) vkDestroyRenderPass(device_, renderPass_, nullptr);
            vkDestroyDevice(device_, nullptr);
        }
        if (instance_) vkDestroyInstance(instance_, nullptr);
        instance_ = VK_NULL_HANDLE;
        gpu_ = VK_NULL_HANDLE; device_ = VK_NULL_HANDLE; queue_ = VK_NULL_HANDLE;
        renderPass_ = VK_NULL_HANDLE; descriptorPool_ = VK_NULL_HANDLE;
        commandPool_ = VK_NULL_HANDLE; command_ = VK_NULL_HANDLE; fence_ = VK_NULL_HANDLE;
    }

private:
    bool check(VkResult r, const char* where) const {
        if (r == VK_SUCCESS) return true;
        LOGE("Vulkan failed: %s -> %d", where, static_cast<int>(r));
        return false;
    }
    uint32_t memoryType(uint32_t bits, VkMemoryPropertyFlags required,
                        VkMemoryPropertyFlags preferred = 0) const {
        for (uint32_t pass = 0; pass < 2; ++pass)
            for (uint32_t i = 0; i < memProps_.memoryTypeCount; ++i) {
                VkMemoryPropertyFlags flags = memProps_.memoryTypes[i].propertyFlags;
                if ((bits & (1u << i)) && (flags & required) == required &&
                    (pass || (flags & preferred) == preferred)) return i;
            }
        return UINT32_MAX;
    }
    bool createTarget(uint32_t width, uint32_t height) {
        width_ = width; height_ = height;
        VkImageCreateInfo ci{VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO};
        ci.imageType = VK_IMAGE_TYPE_2D; ci.format = VK_FORMAT_R8G8B8A8_UNORM;
        ci.extent = {width, height, 1}; ci.mipLevels = 1; ci.arrayLayers = 1;
        ci.samples = VK_SAMPLE_COUNT_1_BIT; ci.tiling = VK_IMAGE_TILING_OPTIMAL;
        ci.usage = VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_TRANSFER_SRC_BIT;
        ci.sharingMode = VK_SHARING_MODE_EXCLUSIVE;
        ci.initialLayout = VK_IMAGE_LAYOUT_UNDEFINED;
        if (!check(vkCreateImage(device_, &ci, nullptr, &image_), "vkCreateImage")) return false;
        VkMemoryRequirements ir{};
        vkGetImageMemoryRequirements(device_, image_, &ir);
        uint32_t im = memoryType(ir.memoryTypeBits, 0, VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT);
        if (im == UINT32_MAX) return false;
        VkMemoryAllocateInfo ai{VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO};
        ai.allocationSize = ir.size; ai.memoryTypeIndex = im;
        if (!check(vkAllocateMemory(device_, &ai, nullptr, &imageMemory_), "vkAllocateMemory(image)")) return false;
        if (!check(vkBindImageMemory(device_, image_, imageMemory_, 0), "vkBindImageMemory")) return false;
        VkImageViewCreateInfo vi{VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO};
        vi.image = image_; vi.viewType = VK_IMAGE_VIEW_TYPE_2D;
        vi.format = VK_FORMAT_R8G8B8A8_UNORM;
        vi.subresourceRange.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT;
        vi.subresourceRange.levelCount = 1; vi.subresourceRange.layerCount = 1;
        if (!check(vkCreateImageView(device_, &vi, nullptr, &imageView_), "vkCreateImageView")) return false;
        VkFramebufferCreateInfo fb{VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO};
        fb.renderPass = renderPass_; fb.attachmentCount = 1; fb.pAttachments = &imageView_;
        fb.width = width; fb.height = height; fb.layers = 1;
        if (!check(vkCreateFramebuffer(device_, &fb, nullptr, &framebuffer_), "vkCreateFramebuffer")) return false;

        VkBufferCreateInfo bi{VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO};
        bi.size = static_cast<VkDeviceSize>(width) * height * 4;
        bi.usage = VK_BUFFER_USAGE_TRANSFER_DST_BIT;
        bi.sharingMode = VK_SHARING_MODE_EXCLUSIVE;
        if (!check(vkCreateBuffer(device_, &bi, nullptr, &stagingBuffer_), "vkCreateBuffer")) return false;
        VkMemoryRequirements br{};
        vkGetBufferMemoryRequirements(device_, stagingBuffer_, &br);
        uint32_t bm = memoryType(br.memoryTypeBits, VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT,
                                 VK_MEMORY_PROPERTY_HOST_COHERENT_BIT);
        if (bm == UINT32_MAX) return false;
        hostCoherent_ = (memProps_.memoryTypes[bm].propertyFlags & VK_MEMORY_PROPERTY_HOST_COHERENT_BIT) != 0;
        VkMemoryAllocateInfo ba{VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO};
        ba.allocationSize = br.size; ba.memoryTypeIndex = bm;
        if (!check(vkAllocateMemory(device_, &ba, nullptr, &stagingMemory_), "vkAllocateMemory(staging)")) return false;
        if (!check(vkBindBufferMemory(device_, stagingBuffer_, stagingMemory_, 0), "vkBindBufferMemory")) return false;
        if (!check(vkMapMemory(device_, stagingMemory_, 0, VK_WHOLE_SIZE, 0, &stagingMapped_), "vkMapMemory")) return false;
        LOGI("Vulkan render target ready: %ux%u", width, height);
        return true;
    }
    void destroyTarget() {
        if (!device_) return;
        if (stagingMapped_) vkUnmapMemory(device_, stagingMemory_);
        stagingMapped_ = nullptr;
        if (stagingBuffer_) vkDestroyBuffer(device_, stagingBuffer_, nullptr);
        if (stagingMemory_) vkFreeMemory(device_, stagingMemory_, nullptr);
        if (framebuffer_) vkDestroyFramebuffer(device_, framebuffer_, nullptr);
        if (imageView_) vkDestroyImageView(device_, imageView_, nullptr);
        if (image_) vkDestroyImage(device_, image_, nullptr);
        if (imageMemory_) vkFreeMemory(device_, imageMemory_, nullptr);
        stagingBuffer_ = VK_NULL_HANDLE; stagingMemory_ = VK_NULL_HANDLE;
        framebuffer_ = VK_NULL_HANDLE; imageView_ = VK_NULL_HANDLE;
        image_ = VK_NULL_HANDLE; imageMemory_ = VK_NULL_HANDLE;
        width_ = 0; height_ = 0;
    }

    VkInstance instance_ = VK_NULL_HANDLE;
    VkPhysicalDevice gpu_ = VK_NULL_HANDLE;
    VkPhysicalDeviceMemoryProperties memProps_{};
    VkPhysicalDeviceProperties gpuProps_{};
    VkDevice device_ = VK_NULL_HANDLE;
    VkQueue queue_ = VK_NULL_HANDLE;
    uint32_t queueFamily_ = 0;
    VkRenderPass renderPass_ = VK_NULL_HANDLE;
    VkDescriptorPool descriptorPool_ = VK_NULL_HANDLE;
    VkCommandPool commandPool_ = VK_NULL_HANDLE;
    VkCommandBuffer command_ = VK_NULL_HANDLE;
    VkFence fence_ = VK_NULL_HANDLE;
    VkImage image_ = VK_NULL_HANDLE;
    VkDeviceMemory imageMemory_ = VK_NULL_HANDLE;
    VkImageView imageView_ = VK_NULL_HANDLE;
    VkFramebuffer framebuffer_ = VK_NULL_HANDLE;
    VkBuffer stagingBuffer_ = VK_NULL_HANDLE;
    VkDeviceMemory stagingMemory_ = VK_NULL_HANDLE;
    void* stagingMapped_ = nullptr;
    uint32_t width_ = 0, height_ = 0;
    bool hostCoherent_ = true;
    bool backendReady_ = false;
};
