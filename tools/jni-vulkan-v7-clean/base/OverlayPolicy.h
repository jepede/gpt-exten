#pragma once
// Shared by Android JNI and host tests; no Android-specific dependencies.
#include <atomic>
#include <algorithm>
#include <cmath>
#include <cstdint>

namespace ys_overlay {
constexpr int kPixelRgba8888 = 1;
constexpr int kPixelRgbx8888 = 2;
constexpr int kPixelRgb565 = 4;

// Pixel format is only a preference, not a proof of which window is visible.
inline int parentPriority(int format) noexcept {
    switch (format) {
    case kPixelRgba8888: return 100;
    case kPixelRgbx8888: return 90;
    case kPixelRgb565: return 40;
    default: return 50;
    }
}

struct Vec2 { float x, y; };
inline bool validWindowSize(int w, int h) noexcept {
    return w > 0 && h > 0 && w <= 8192 && h <= 8192;
}
inline bool windowQueryFailed(int w, int h) noexcept {
    return w < 0 || h < 0;
}

// 0 no flip, 1 flip vertically, 2 flip horizontally, 3 flip both.
// Same transform must be applied to the submitted buffer and touch mapping.
inline Vec2 screenToImage(float x, float y, float w, float h, int flip) noexcept {
    if (flip & 2) x = w - x;
    if (flip & 1) y = h - y;
    return {x, y};
}
inline bool finiteInBounds(Vec2 p, float w, float h) noexcept {
    return std::isfinite(p.x) && std::isfinite(p.y) &&
           p.x >= 0 && p.y >= 0 && p.x < w && p.y < h;
}
inline std::atomic<int>& configuredFlip() noexcept {
    static std::atomic<int> transform{0};
    return transform;
}
inline std::atomic<int>& configuredOffsetX() noexcept {
    static std::atomic<int> offset{0};
    return offset;
}
inline std::atomic<int>& configuredOffsetY() noexcept {
    static std::atomic<int> offset{0};
    return offset;
}

// 0 prioritizes the long-lived RGBA window, 1 latest only, 2 all valid
// candidate parents (default, minimizes lost overlay during Activity changes).
inline int sanitizeMirrorMode(int mode) noexcept {
    return mode < 0 || mode > 2 ? 2 : mode;
}
inline int sanitizeFlip(int mode) noexcept { return mode >= 0 && mode <= 3 ? mode : 0; }
}
