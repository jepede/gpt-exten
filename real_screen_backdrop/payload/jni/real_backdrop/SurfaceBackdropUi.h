#pragma once
#include "NativeBackdrop.h"
#include "ytbl.h"
#include <imgui.h>

// Header-only adapter: changes take effect at the next window Begin, before
// any draw callback is enqueued. Toggling a checkbox must not delete textures
// already referenced by this frame's glass jobs.
namespace screenbackdrop_ui {
inline bool requested=false;
inline bool attempted=false;
inline bool active=false;
inline bool flipVertical=false;
inline int maxEdge=1280;
inline int captureFps=24;
inline screenbackdrop::Texture texture;
inline bool Requested(){return requested;}
inline bool Prepare() {
    auto options=ytbl::GetOptions();
    const bool desired=requested && !options.reduceTransparency;
    if(desired!=attempted) {
        attempted=desired;
        if(desired)screenbackdrop::Start();else screenbackdrop::Stop();
    }
    screenbackdrop::Configure(maxEdge,captureFps);
    if(desired)screenbackdrop::UpdateTexture();
    texture=screenbackdrop::GetTexture();
    active=desired && texture.id!=0;
    if(active) {
        ytbl::ExternalBackdrop background;
        background.texture=texture.id;
        background.width=texture.width;background.height=texture.height;
        background.displayPos=ImGui::GetMainViewport()->Pos;
        // The Surface project may allocate a SQUARE native window. Do not map
        // the portrait screenshot to that square; map the real display extent.
        background.displaySize=ImVec2(float(texture.screenWidth),float(texture.screenHeight));
        background.topLeftOrigin=texture.topLeftOrigin != flipVertical;
        background.premultiplied=true;
        ytbl::SetExternalBackdrop(background);
        options.backdrop=ytbl::BackdropMode::ExternalTexture;
    } else {
        ytbl::SetExternalBackdrop(ytbl::ExternalBackdrop{});
        options.backdrop=ytbl::BackdropMode::FrameSnapshot;
    }
    ytbl::SetOptions(options);
    return active;
}
inline void Shutdown() {
    requested=attempted=active=false;
    screenbackdrop::Stop();texture={};
}
inline void DrawSettings() {
    ImGui::PushID("real_screen_background");
    ImGui::Separator();
    ImGui::TextUnformatted("真实屏幕背景 / Local screen backdrop");
    ImGui::Checkbox("启用真实屏幕背景（仅本机使用）",&requested);
    if(requested) {
        ImGui::TextUnformatted(active ? "LIVE：正在折射其他应用的可采集画面" : "NOT LIVE：等待采集或已降级，未使用旧画面");
        ImGui::TextWrapped("%s",screenbackdrop::GetStatus().c_str());
        if(ytbl::GetOptions().reduceTransparency)
            ImGui::TextWrapped("减少透明度已开启：屏幕采集暂停。");
        if(active) {
            ImGui::Text("%d x %d -> %d x %d | rotation=%d | age=%.0f ms",
                texture.screenWidth,texture.screenHeight,texture.width,texture.height,texture.rotation,texture.ageMs);
            ImGui::Text("Captured frames: %llu",static_cast<unsigned long long>(screenbackdrop::CapturedFrames()));
        }
        ImGui::SliderInt("采集长边",&maxEdge,640,2560);
        ImGui::SliderInt("采集目标 FPS",&captureFps,5,60);
        ImGui::Checkbox("上下翻转校准",&flipVertical);
        if(ImGui::Button("停止并重新连接"))requested=false; // explicit re-enable starts a fresh child next frame
    }
    ImGui::TextWrapped("采集在进程内使用，不保存、不上传。安全/DRM 画面不采集。"
                       "悬浮窗已设置排除截图；系统截图或录屏通常也不会显示本窗口。");
    ImGui::PopID();
}
} // namespace screenbackdrop_ui
