#pragma once
namespace SurfaceBackdrop {
// After ImGui::NewFrame and ytbl::BeginFrame. Resource changes occur here only.
void BeginFrame();
// Before the first glass draw job of the window. No resource release here.
void Bind();
bool Requested();
void Settings();
void Shutdown(); // Before ytbl/EGL shutdown, after queued draw callbacks finish.
}
