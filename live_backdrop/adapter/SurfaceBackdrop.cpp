#include "SurfaceBackdrop.h"
#include "LiveBackdrop.h"
#include "ytbl.h"
#include "ANativeWindowCreator.h"
#include <algorithm>
#include <cstdlib>
#include <limits.h>
#include <string>
#include <unistd.h>

namespace SurfaceBackdrop {
namespace {
livebg::Session session;
livebg::TextureFrame frozen;
bool desired=false,mode=false,valid=false,flipY=false;
int rate=15,lastFrame=-1;
float captureScale=.5f;
std::string runtime;
std::string RuntimeDirectory() {
    if(const char* overridePath=std::getenv("SURFACEGLASS_RUNTIME"))
        if(overridePath[0]=='/')return overridePath;
    char path[PATH_MAX];const ssize_t count=readlink("/proc/self/exe",path,sizeof(path)-1);
    if(count<=0)return {};
    path[count]=0;std::string directory(path);
    const auto slash=directory.find_last_of('/');
    if(slash==std::string::npos)return {};
    return directory.substr(0,slash)+"/live_backdrop";
}
}
void BeginFrame() {
    const int frame=ImGui::GetFrameCount();if(frame==lastFrame)return;lastFrame=frame;
    const auto info=android::ANativeWindowCreator::GetDisplayInfo();
    livebg::Config config;
    config.width=info.width;config.height=info.height;config.rotation=info.orientation;
    config.scale=captureScale;config.maxFps=rate;
    if(desired!=mode) {
        mode=desired;valid=false;frozen={};
        if(mode) {
            runtime=RuntimeDirectory();
            session.Start(runtime,config,android::ANativeWindowCreator::IsBackdropExclusionReady());
        } else {
            session.Stop();ytbl::SetExternalBackdrop({});
        }
    }
    valid=false;
    if(mode){session.Configure(config);valid=session.Poll(frozen);}
}
bool Requested(){return mode;}
void Bind() {
    auto options=ytbl::GetOptions();
    options.backdrop=mode?ytbl::BackdropMode::ExternalTexture:ytbl::BackdropMode::FrameSnapshot;
    ytbl::SetOptions(options);
    ytbl::SetBackdropEnabled(!mode || valid);
    if(mode && valid) {
        ytbl::ExternalBackdrop b;
        b.texture=frozen.texture;b.width=frozen.textureWidth;b.height=frozen.textureHeight;
        b.displayPos=ImGui::GetMainViewport()->Pos;
        const auto scale=ImGui::GetIO().DisplayFramebufferScale;
        b.displaySize=ImVec2(frozen.displayWidth/std::max(scale.x,.01f),frozen.displayHeight/std::max(scale.y,.01f));
        // AHardwareBuffer screenshot rows are treated as top-down. A calibration
        // toggle remains visible because the imported orientation is device-tested.
        b.topLeftOrigin=!flipY;b.premultiplied=true;
        ytbl::SetExternalBackdrop(b);
    } else if(mode)ytbl::SetExternalBackdrop({});
}
void Settings() {
    ImGui::PushID("live_cross_app_background");
    ImGui::Separator();
    ImGui::TextUnformatted("Cross-app background / 真实后层背景");
    ImGui::BeginDisabled(!ytbl::IsInitialized());
    ImGui::Checkbox("启用本机画面采集（不保存、不上传）",&desired);
    ImGui::EndDisabled();
    if(mode) {
        ImGui::TextUnformatted(valid?"CAPTURE ON - LIVE":"CAPTURE ON - WAITING / UNAVAILABLE");
        const auto state=session.GetStatus();
        ImGui::Text("Capture %.1f FPS | %u frames | %d x %d",state.captureFps,state.received,frozen.textureWidth,frozen.textureHeight);
        if(!state.error.empty())ImGui::TextWrapped("采集错误: %s",state.error.c_str());
        if(!valid)ImGui::TextWrapped("未显示过期画面；材质已降级。关闭再开启可重试。详情见启动终端。");
        ImGui::SliderInt("采集上限（非界面帧率）",&rate,5,30);
        ImGui::SliderFloat("采集分辨率比例",&captureScale,.25f,1.f,"%.2f");
        ImGui::Checkbox("校正纹理上下颠倒",&flipY);
        if(valid && frozen.hdr)ImGui::TextWrapped("捕获包含 HDR 图层；当前没有完整 HDR / 广色域色彩管理。");
    }
    ImGui::TextWrapped("为避免递归，本程序的 Surface 从系统截图中排除。此设置也会影响外部截图/录屏是否显示本窗口；不是捕获受保护内容。");
    ImGui::PopID();
}
void Shutdown() {
    session.Stop();mode=desired=valid=false;frozen={};lastFrame=-1;
    ytbl::SetExternalBackdrop({});ytbl::SetBackdropEnabled(true);
}
}
