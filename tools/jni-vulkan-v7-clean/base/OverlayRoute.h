#pragma once
// Pure selection policy: attach to SurfaceView's public parent SurfaceControl,
// not to the BLAST buffer producer, to avoid inheriting its dynamic scale/crop.
namespace ys_overlay {
inline int surfaceRoutePriority(bool isSurfaceView, int nativeFormatPriority) {
    return isSurfaceView ? 1000 : nativeFormatPriority;
}
inline bool submitToParent(bool sourceIsSurfaceView, bool hasLiveSurfaceView,
                           int selectedMode, bool isPrimary, bool isLatest,
                           unsigned long long effectiveId,
                           unsigned long long parentId) {
    if(effectiveId > 0) return parentId == effectiveId;
    if(hasLiveSurfaceView && !sourceIsSurfaceView) return false;
    if(selectedMode == 0) return isPrimary;
    if(selectedMode == 1) return isLatest;
    return true;
}
}
