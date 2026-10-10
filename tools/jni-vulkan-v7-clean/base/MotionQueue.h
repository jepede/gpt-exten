#pragma once
#include <array>
#include <cstddef>
#include <cstdint>
#include <mutex>

namespace overlay_input {
struct Point { int id = -1; int tool = 0; float x = 0; float y = 0; };
struct Motion {
    int action = 3;
    std::size_t count = 0;
    std::size_t index = 0;
    int buttons = 0;
    float wheel_x = 0, wheel_y = 0;
    std::array<Point, 32> points{};
};

// Copies values only; never retains Android event pointers or calls ImGui.
// enable()/disable() are called on the render thread, not in the input callback.
template<std::size_t Capacity = 128> class Queue {
    static_assert(Capacity > 0);
public:
    struct Batch {
        std::array<Motion, Capacity> events{};
        std::size_t count = 0;
        bool reset = false;
    };
    void enable() {
        std::lock_guard<std::mutex> lock(mutex_);
        ++generation_; if (generation_ == 0) ++generation_;
        enabled_ = true; head_ = count_ = 0; reset_ = true;
    }
    void disable() {
        std::lock_guard<std::mutex> lock(mutex_);
        enabled_ = false; head_ = count_ = 0; reset_ = false;
    }
    std::uint64_t capture_generation() {
        std::lock_guard<std::mutex> lock(mutex_);
        return enabled_ ? generation_ : 0;
    }
    bool push(const Motion& value, std::uint64_t generation) {
        std::lock_guard<std::mutex> lock(mutex_);
        if (!enabled_ || generation == 0 || generation != generation_) return false;
        if (value.count > value.points.size()) return false;
        if (value.action != 3 && (value.count == 0 || value.index >= value.count)) return false;
        // Losing transitions must never leave a mouse button stuck down.
        if (count_ == Capacity) { head_ = count_ = 0; reset_ = true; }
        events_[(head_ + count_) % Capacity] = value;
        ++count_; return true;
    }
    Batch drain() {
        std::lock_guard<std::mutex> lock(mutex_);
        Batch result;
        if (!enabled_) return result;
        result.reset = reset_; result.count = count_;
        for (std::size_t i = 0; i < count_; ++i)
            result.events[i] = events_[(head_ + i) % Capacity];
        head_ = count_ = 0; reset_ = false;
        return result;
    }
private:
    std::mutex mutex_;
    std::array<Motion, Capacity> events_{};
    std::size_t head_ = 0, count_ = 0;
    std::uint64_t generation_ = 0;
    bool enabled_ = false, reset_ = false;
};
inline Queue<>& queue() { static Queue<> q; return q; }
struct SessionInputGuard {
    ~SessionInputGuard() { queue().disable(); }
};
} // namespace overlay_input
