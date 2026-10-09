#pragma once
// Shared by the Android renderer and the real offscreen Vulkan regression test.
#include <vulkan/vulkan.h>
#include <imgui.h>
#include <imgui_impl_vulkan.h>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <stdexcept>
#include <string>
#include <vector>

namespace overlay_vk {
inline void Check(VkResult result, const char* operation) {
    if (result != VK_SUCCESS)
        throw std::runtime_error(std::string(operation) + ": VkResult=" + std::to_string(result));
}
inline void BackendResult(VkResult result) {
    if (result < 0) Check(result, "ImGui Vulkan backend");
}

class Core final {
public:
    VkInstance instance = VK_NULL_HANDLE;
    VkPhysicalDevice physical = VK_NULL_HANDLE;
    VkDevice device = VK_NULL_HANDLE;
    VkQueue queue = VK_NULL_HANDLE;
    uint32_t family = UINT32_MAX;
    VkRenderPass render_pass = VK_NULL_HANDLE;
    VkCommandPool command_pool = VK_NULL_HANDLE;
    VkCommandBuffer command = VK_NULL_HANDLE;
    VkFence fence = VK_NULL_HANDLE;
    VkDescriptorPool descriptor_pool = VK_NULL_HANDLE;
    ImGuiContext* context = nullptr;
    VkPhysicalDeviceProperties properties{};
    static constexpr VkFormat Format = VK_FORMAT_R8G8B8A8_UNORM;
    Core() = default;
    Core(const Core&) = delete;
    Core& operator=(const Core&) = delete;
    ~Core() { Shutdown(); }

    void Init(bool require_android_external_memory) {
        VkApplicationInfo app{VK_STRUCTURE_TYPE_APPLICATION_INFO};
        app.pApplicationName = "JNI Vulkan UI";
        app.applicationVersion = VK_MAKE_VERSION(1, 0, 0);
        app.pEngineName = "Dear ImGui";
        app.apiVersion = VK_API_VERSION_1_1;
        VkInstanceCreateInfo info{VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO};
        info.pApplicationInfo = &app;
        Check(vkCreateInstance(&info, nullptr, &instance), "vkCreateInstance(Vulkan 1.1)");
        uint32_t count = 0;
        Check(vkEnumeratePhysicalDevices(instance, &count, nullptr), "enumerate GPU count");
        if (!count) throw std::runtime_error("No Vulkan physical device");
        std::vector<VkPhysicalDevice> devices(count);
        Check(vkEnumeratePhysicalDevices(instance, &count, devices.data()), "enumerate GPUs");
        const char* extensions[] = {
            "VK_ANDROID_external_memory_android_hardware_buffer",
            "VK_EXT_queue_family_foreign"
        };
        for (auto candidate : devices) {
            VkPhysicalDeviceProperties props{};
            vkGetPhysicalDeviceProperties(candidate, &props);
            if (props.apiVersion < VK_API_VERSION_1_1) continue;
            uint32_t ext_count = 0;
            Check(vkEnumerateDeviceExtensionProperties(candidate, nullptr, &ext_count, nullptr), "GPU extensions count");
            std::vector<VkExtensionProperties> exts(ext_count);
            Check(vkEnumerateDeviceExtensionProperties(candidate, nullptr, &ext_count, exts.data()), "GPU extensions");
            bool extensions_ok = true;
            if (require_android_external_memory) {
                for (const char* required : extensions) {
                    bool found = false;
                    for (const auto& ext : exts) if (!std::strcmp(ext.extensionName, required)) found = true;
                    extensions_ok = extensions_ok && found;
                }
            }
            if (!extensions_ok) continue;
            uint32_t q_count = 0;
            vkGetPhysicalDeviceQueueFamilyProperties(candidate, &q_count, nullptr);
            std::vector<VkQueueFamilyProperties> queues(q_count);
            vkGetPhysicalDeviceQueueFamilyProperties(candidate, &q_count, queues.data());
            for (uint32_t q = 0; q < q_count; ++q) {
                if (queues[q].queueCount && (queues[q].queueFlags & VK_QUEUE_GRAPHICS_BIT)) {
                    physical = candidate; family = q; properties = props; break;
                }
            }
            if (physical) break;
        }
        if (!physical) throw std::runtime_error(require_android_external_memory
            ? "GPU requires Vulkan 1.1 + Android hardware-buffer import + foreign queue ownership"
            : "No Vulkan 1.1 graphics queue");
        float priority = 1.0f;
        VkDeviceQueueCreateInfo qi{VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO};
        qi.queueFamilyIndex = family; qi.queueCount = 1; qi.pQueuePriorities = &priority;
        VkDeviceCreateInfo di{VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO};
        di.queueCreateInfoCount = 1; di.pQueueCreateInfos = &qi;
        if (require_android_external_memory) {
            di.enabledExtensionCount = 2; di.ppEnabledExtensionNames = extensions;
        }
        Check(vkCreateDevice(physical, &di, nullptr, &device), "vkCreateDevice");
        vkGetDeviceQueue(device, family, 0, &queue);
        VkAttachmentDescription attachment{};
        attachment.format = Format; attachment.samples = VK_SAMPLE_COUNT_1_BIT;
        attachment.loadOp = VK_ATTACHMENT_LOAD_OP_CLEAR;
        attachment.storeOp = VK_ATTACHMENT_STORE_OP_STORE;
        attachment.stencilLoadOp = VK_ATTACHMENT_LOAD_OP_DONT_CARE;
        attachment.stencilStoreOp = VK_ATTACHMENT_STORE_OP_DONT_CARE;
        attachment.initialLayout = attachment.finalLayout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
        VkAttachmentReference color{0, VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL};
        VkSubpassDescription subpass{};
        subpass.pipelineBindPoint = VK_PIPELINE_BIND_POINT_GRAPHICS;
        subpass.colorAttachmentCount = 1; subpass.pColorAttachments = &color;
        VkRenderPassCreateInfo ri{VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO};
        ri.attachmentCount = 1; ri.pAttachments = &attachment;
        ri.subpassCount = 1; ri.pSubpasses = &subpass;
        Check(vkCreateRenderPass(device, &ri, nullptr, &render_pass), "vkCreateRenderPass");
        VkCommandPoolCreateInfo pi{VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO};
        pi.queueFamilyIndex = family;
        pi.flags = VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT;
        Check(vkCreateCommandPool(device, &pi, nullptr, &command_pool), "vkCreateCommandPool");
        VkCommandBufferAllocateInfo ai{VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO};
        ai.commandPool = command_pool; ai.level = VK_COMMAND_BUFFER_LEVEL_PRIMARY; ai.commandBufferCount = 1;
        Check(vkAllocateCommandBuffers(device, &ai, &command), "vkAllocateCommandBuffers");
        VkFenceCreateInfo fi{VK_STRUCTURE_TYPE_FENCE_CREATE_INFO};
        Check(vkCreateFence(device, &fi, nullptr, &fence), "vkCreateFence");
        VkDescriptorPoolSize pool_size{VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER, 128};
        VkDescriptorPoolCreateInfo dpi{VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO};
        dpi.flags = VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT;
        dpi.maxSets = 128; dpi.poolSizeCount = 1; dpi.pPoolSizes = &pool_size;
        Check(vkCreateDescriptorPool(device, &dpi, nullptr, &descriptor_pool), "vkCreateDescriptorPool");
        IMGUI_CHECKVERSION();
        context = ImGui::CreateContext();
        ImGui::SetCurrentContext(context);
        ImGuiIO& io = ImGui::GetIO();
        io.IniFilename = nullptr; io.LogFilename = nullptr;
        io.BackendPlatformName = "android_snapshot_queue";
        ImGui_ImplVulkan_InitInfo vi{};
        vi.ApiVersion = VK_API_VERSION_1_1;
        vi.Instance = instance; vi.PhysicalDevice = physical; vi.Device = device;
        vi.QueueFamily = family; vi.Queue = queue; vi.DescriptorPool = descriptor_pool;
        vi.MinImageCount = 2; vi.ImageCount = 3;
        vi.PipelineInfoMain.RenderPass = render_pass;
        vi.PipelineInfoMain.MSAASamples = VK_SAMPLE_COUNT_1_BIT;
        vi.CheckVkResultFn = BackendResult;
        if (!ImGui_ImplVulkan_Init(&vi)) throw std::runtime_error("ImGui Vulkan initialization failed");
    }

    uint32_t MemoryType(uint32_t allowed, VkMemoryPropertyFlags required,
                        VkMemoryPropertyFlags preferred = 0) const {
        VkPhysicalDeviceMemoryProperties memory{};
        vkGetPhysicalDeviceMemoryProperties(physical, &memory);
        uint32_t fallback = UINT32_MAX;
        for (uint32_t i = 0; i < memory.memoryTypeCount; ++i) {
            if (!(allowed & (1u << i))) continue;
            const auto flags = memory.memoryTypes[i].propertyFlags;
            if ((flags & required) != required) continue;
            if ((flags & preferred) == preferred) return i;
            fallback = i;
        }
        if (fallback == UINT32_MAX) throw std::runtime_error("No compatible Vulkan memory type");
        return fallback;
    }

    void Begin(VkImage image, VkFramebuffer framebuffer, uint32_t width, uint32_t height,
               VkImageLayout previous_layout, bool foreign) {
        Check(vkResetCommandPool(device, command_pool, 0), "vkResetCommandPool");
        VkCommandBufferBeginInfo begin{VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO};
        begin.flags = VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT;
        Check(vkBeginCommandBuffer(command, &begin), "vkBeginCommandBuffer");
        VkImageMemoryBarrier acquire{VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER};
        acquire.srcAccessMask = 0;
        acquire.dstAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;
        acquire.oldLayout = previous_layout;
        acquire.newLayout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
        acquire.srcQueueFamilyIndex = foreign ? VK_QUEUE_FAMILY_FOREIGN_EXT : VK_QUEUE_FAMILY_IGNORED;
        acquire.dstQueueFamilyIndex = foreign ? family : VK_QUEUE_FAMILY_IGNORED;
        acquire.image = image;
        acquire.subresourceRange = {VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1};
        vkCmdPipelineBarrier(command, VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT,
            VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT, 0, 0, nullptr, 0, nullptr, 1, &acquire);
        VkClearValue clear{}; // Premultiplied transparent black, not opaque black.
        VkRenderPassBeginInfo rp{VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO};
        rp.renderPass = render_pass; rp.framebuffer = framebuffer;
        rp.renderArea.extent = {width, height}; rp.clearValueCount = 1; rp.pClearValues = &clear;
        vkCmdBeginRenderPass(command, &rp, VK_SUBPASS_CONTENTS_INLINE);
    }

    void End(VkImage image, bool foreign, bool readback = false) {
        ImGui_ImplVulkan_RenderDrawData(ImGui::GetDrawData(), command);
        vkCmdEndRenderPass(command);
        VkImageMemoryBarrier release{VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER};
        release.srcAccessMask = VK_ACCESS_COLOR_ATTACHMENT_WRITE_BIT;
        release.dstAccessMask = readback ? VK_ACCESS_TRANSFER_READ_BIT : 0;
        release.oldLayout = VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL;
        release.newLayout = readback ? VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL : VK_IMAGE_LAYOUT_GENERAL;
        release.srcQueueFamilyIndex = foreign ? family : VK_QUEUE_FAMILY_IGNORED;
        release.dstQueueFamilyIndex = foreign ? VK_QUEUE_FAMILY_FOREIGN_EXT : VK_QUEUE_FAMILY_IGNORED;
        release.image = image; release.subresourceRange = {VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1};
        vkCmdPipelineBarrier(command, VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT,
            readback ? VK_PIPELINE_STAGE_TRANSFER_BIT : VK_PIPELINE_STAGE_BOTTOM_OF_PIPE_BIT,
            0, 0, nullptr, 0, nullptr, 1, &release);
    }

    void SubmitAndWait() {
        Check(vkEndCommandBuffer(command), "vkEndCommandBuffer");
        Check(vkResetFences(device, 1, &fence), "vkResetFences");
        VkSubmitInfo submit{VK_STRUCTURE_TYPE_SUBMIT_INFO};
        submit.commandBufferCount = 1; submit.pCommandBuffers = &command;
        Check(vkQueueSubmit(queue, 1, &submit, fence), "vkQueueSubmit");
        // Conservative GPU->compositor handoff: -1 is passed to setBuffer only AFTER this succeeds.
        Check(vkWaitForFences(device, 1, &fence, VK_TRUE, 5'000'000'000ULL), "GPU fence wait");
    }

    void Shutdown() noexcept {
        if (device) (void)vkDeviceWaitIdle(device);
        if (context) {
            ImGui::SetCurrentContext(context);
            try {
                if (ImGui::GetIO().BackendRendererUserData) ImGui_ImplVulkan_Shutdown();
            } catch (...) { std::fputs("Vulkan backend shutdown reported an error\n", stderr); }
            ImGui::DestroyContext(context); context = nullptr;
        }
        if (device) {
            if (descriptor_pool) vkDestroyDescriptorPool(device, descriptor_pool, nullptr);
            if (fence) vkDestroyFence(device, fence, nullptr);
            if (command_pool) vkDestroyCommandPool(device, command_pool, nullptr);
            if (render_pass) vkDestroyRenderPass(device, render_pass, nullptr);
            vkDestroyDevice(device, nullptr); device = VK_NULL_HANDLE;
        }
        if (instance) { vkDestroyInstance(instance, nullptr); instance = VK_NULL_HANDLE; }
    }
};
} // namespace overlay_vk
