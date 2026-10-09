#include "../jni/renderer/VulkanCore.h"
#include <fstream>
#include <iostream>
#include <memory>
#include <cstdlib>
using namespace overlay_vk;
constexpr uint32_t W = 512, H = 320;

struct Target {
    Core& c;
    VkImage image = VK_NULL_HANDLE;
    VkDeviceMemory image_memory = VK_NULL_HANDLE;
    VkImageView view = VK_NULL_HANDLE;
    VkFramebuffer framebuffer = VK_NULL_HANDLE;
    VkBuffer staging = VK_NULL_HANDLE;
    VkDeviceMemory staging_memory = VK_NULL_HANDLE;
    explicit Target(Core& core):c(core) {}
    ~Target() {
        if (c.device) (void)vkDeviceWaitIdle(c.device);
        if (framebuffer) vkDestroyFramebuffer(c.device, framebuffer, nullptr);
        if (view) vkDestroyImageView(c.device, view, nullptr);
        if (image) vkDestroyImage(c.device, image, nullptr);
        if (image_memory) vkFreeMemory(c.device, image_memory, nullptr);
        if (staging) vkDestroyBuffer(c.device, staging, nullptr);
        if (staging_memory) vkFreeMemory(c.device, staging_memory, nullptr);
    }
    void Init() {
        VkImageCreateInfo ii{VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO};
        ii.imageType=VK_IMAGE_TYPE_2D; ii.format=Core::Format; ii.extent={W,H,1};
        ii.mipLevels=1; ii.arrayLayers=1; ii.samples=VK_SAMPLE_COUNT_1_BIT;
        ii.tiling=VK_IMAGE_TILING_OPTIMAL;
        ii.usage=VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_TRANSFER_SRC_BIT;
        ii.sharingMode=VK_SHARING_MODE_EXCLUSIVE; ii.initialLayout=VK_IMAGE_LAYOUT_UNDEFINED;
        Check(vkCreateImage(c.device,&ii,nullptr,&image),"smoke image");
        VkMemoryRequirements req{};vkGetImageMemoryRequirements(c.device,image,&req);
        VkMemoryAllocateInfo alloc{VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO};
        alloc.allocationSize=req.size;alloc.memoryTypeIndex=c.MemoryType(req.memoryTypeBits,0,VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT);
        Check(vkAllocateMemory(c.device,&alloc,nullptr,&image_memory),"smoke image memory");
        Check(vkBindImageMemory(c.device,image,image_memory,0),"smoke bind image");
        VkImageViewCreateInfo vi{VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO};
        vi.image=image;vi.viewType=VK_IMAGE_VIEW_TYPE_2D;vi.format=Core::Format;
        vi.subresourceRange={VK_IMAGE_ASPECT_COLOR_BIT,0,1,0,1};
        Check(vkCreateImageView(c.device,&vi,nullptr,&view),"smoke image view");
        VkFramebufferCreateInfo fi{VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO};
        fi.renderPass=c.render_pass;fi.attachmentCount=1;fi.pAttachments=&view;fi.width=W;fi.height=H;fi.layers=1;
        Check(vkCreateFramebuffer(c.device,&fi,nullptr,&framebuffer),"smoke framebuffer");
        VkBufferCreateInfo bi{VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO};
        bi.size=W*H*4;bi.usage=VK_BUFFER_USAGE_TRANSFER_DST_BIT;bi.sharingMode=VK_SHARING_MODE_EXCLUSIVE;
        Check(vkCreateBuffer(c.device,&bi,nullptr,&staging),"smoke staging buffer");
        vkGetBufferMemoryRequirements(c.device,staging,&req);
        alloc.allocationSize=req.size;
        alloc.memoryTypeIndex=c.MemoryType(req.memoryTypeBits,VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT|VK_MEMORY_PROPERTY_HOST_COHERENT_BIT);
        Check(vkAllocateMemory(c.device,&alloc,nullptr,&staging_memory),"smoke staging memory");
        Check(vkBindBufferMemory(c.device,staging,staging_memory,0),"smoke bind staging");
    }
};
int main(int argc,char**argv) {
    try {
        Core c;c.Init(false);
        std::cout << "Vulkan device: " << c.properties.deviceName << '\n';
        Target target(c);target.Init();
        ImGui::StyleColorsDark();
        auto& io=ImGui::GetIO();io.DisplaySize=ImVec2(W,H);io.DeltaTime=1.0f/60;
        ImFontConfig config;config.SizePixels=17.0f;
        io.Fonts->AddFontDefault(&config);
        bool checked=true;float value=0.7f;
        for(int frame=0;frame<4;++frame) {
            ImGui_ImplVulkan_NewFrame();ImGui::NewFrame();
            auto* bg=ImGui::GetBackgroundDrawList();
            bg->AddRectFilled(ImVec2(10,10),ImVec2(80,80),IM_COL32(255,0,0,255));
            bg->AddRectFilled(ImVec2(90,10),ImVec2(160,80),IM_COL32(0,255,0,128));
            bg->AddText(ImVec2(180,20),IM_COL32(255,255,255,255),"Actual Vulkan offscreen render");
            bg->AddText(ImVec2(180,45),IM_COL32(190,190,190,255),"RGBA / alpha / dynamic font atlas");
            ImGui::SetNextWindowPos(ImVec2(20,110));ImGui::SetNextWindowSize(ImVec2(470,190));
            ImGui::Begin("Vulkan verification",nullptr,ImGuiWindowFlags_NoResize|ImGuiWindowFlags_NoMove);
            ImGui::Text("Renderer: %s",io.BackendRendererName);
            ImGui::Checkbox("Input queue preserved",&checked);
            ImGui::SliderFloat("Test slider",&value,0,1);
            ImGui::TextUnformatted("This is a GPU draw test, not an Android device screenshot.");
            ImGui::End();ImGui::Render();
            c.Begin(target.image,target.framebuffer,W,H,VK_IMAGE_LAYOUT_UNDEFINED,false);
            c.End(target.image,false,true);
            VkBufferImageCopy copy{};copy.imageSubresource={VK_IMAGE_ASPECT_COLOR_BIT,0,0,1};
            copy.imageExtent={W,H,1};
            vkCmdCopyImageToBuffer(c.command,target.image,VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL,target.staging,1,&copy);
            VkBufferMemoryBarrier barrier{VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER};
            barrier.srcAccessMask=VK_ACCESS_TRANSFER_WRITE_BIT;barrier.dstAccessMask=VK_ACCESS_HOST_READ_BIT;
            barrier.srcQueueFamilyIndex=barrier.dstQueueFamilyIndex=VK_QUEUE_FAMILY_IGNORED;
            barrier.buffer=target.staging;barrier.size=VK_WHOLE_SIZE;
            vkCmdPipelineBarrier(c.command,VK_PIPELINE_STAGE_TRANSFER_BIT,VK_PIPELINE_STAGE_HOST_BIT,
                                 0,0,nullptr,1,&barrier,0,nullptr);
            c.SubmitAndWait();
        }
        void* data=nullptr;
        Check(vkMapMemory(c.device,target.staging_memory,0,W*H*4,0,&data),"smoke readback map");
        const auto* pixels=static_cast<const unsigned char*>(data);
        auto pixel=[&](uint32_t x,uint32_t y) { return pixels+(y*W+x)*4; };
        auto require=[](bool ok,const char* message) { if(!ok)throw std::runtime_error(message); };
        const auto* clear=pixel(0,0);
        require(clear[0]==0 && clear[1]==0 && clear[2]==0 && clear[3]==0,"transparent clear pixel mismatch");
        const auto* red=pixel(20,20);
        require(red[0]>=254 && red[1]<=1 && red[2]<=1 && red[3]>=254,"opaque red draw mismatch");
        const auto* green=pixel(100,20);
        require(green[0]<=1 && std::abs(int(green[1])-128)<=2 && green[2]<=1 && std::abs(int(green[3])-128)<=2,
                "premultiplied half-alpha draw mismatch");
        size_t painted=0;
        for(size_t i=0;i<W*H;++i)if(pixels[i*4+3])++painted;
        require(painted>40000,"not enough UI pixels were rendered");
        const char* path=argc>1?argv[1]:"vulkan_smoke.rgba";
        std::ofstream out(path,std::ios::binary);out.write(reinterpret_cast<const char*>(pixels),W*H*4);
        if(!out)throw std::runtime_error("cannot save readback");
        vkUnmapMemory(c.device,target.staging_memory);
        std::cout << "PASS Vulkan core initialization and four submitted frames\n"
                  << "PASS transparent background (0,0,0,0)\n"
                  << "PASS opaque color and premultiplied alpha\n"
                  << "PASS dynamic font atlas and widgets; painted pixels=" << painted << '\n';
        return 0;
    } catch(const std::exception&e) {
        std::cerr << "FAIL " << e.what() << '\n';return 1;
    }
}
