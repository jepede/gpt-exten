#pragma once
#include <cstdint>
#include <string>

namespace screenbackdrop {
struct Texture {
    unsigned id=0;
    int width=0,height=0,screenWidth=0,screenHeight=0,rotation=0;
    bool topLeftOrigin=true;
    uint64_t sequence=0;
    double ageMs=0;
};
// Call Start only after an explicit action in the visible owner UI.
// Files default to <directory of executable>/capture_runtime/. Override with
// YTBL_CAPTURE_DIR when installing somewhere else. The child is not persistent.
bool Start();
void Configure(int maxEdge=1280,int fps=24);
// Render thread, before enqueuing any ImGui/glass commands in a frame.
// Imports a completed AHardwareBuffer and GPU-copies it into an owned RGBA8 texture.
void UpdateTexture();
Texture GetTexture();
std::string GetStatus();
uint64_t CapturedFrames();
// Render thread, BEFORE EGL context destruction. Stops/reaps the helper.
void Stop();
} // namespace screenbackdrop
