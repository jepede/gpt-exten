#pragma once
#include <cstdint>

namespace screenbackdrop::hosted {
// Java and native UI must be hosted in the SAME app_process. No pointer IPC.
bool Ready();
bool Launch(int ownedSocketFd); // Java owns/closes this endpoint only on success.
uint64_t Generation();
int ExcludedCount();
bool Register(void* nativeWindow,void* nativeSurfaceControl,int width,int height);
void Unregister(void* nativeWindow);
}
