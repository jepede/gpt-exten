#pragma once
#include <array>
#include <cstddef>
#include <cstdint>
#include <mutex>

namespace crash_fix {
enum class PointerSource : std::uint8_t { Mouse, Touch, Pen };
struct PointerSnapshot {
    float x = 0.0f;
    float y = 0.0f;
    float wheel_x = 0.0f;
    float wheel_y = 0.0f;
    std::uint8_t buttons = 0;
    PointerSource source = PointerSource::Mouse;
    bool position_valid = false;
};

// Producers copy values, never AInputEvent pointers or ImGui objects.
// All queue state is protected by one mutex; the consumer releases it before
// calling ImGui. Overflow is bounded and explicitly resets stale button state.
template<std::size_t Capacity = 256>
class PointerQueue {
    static_assert(Capacity > 0, "The queue must not be empty");
public:
    struct Batch {
        std::array<PointerSnapshot, Capacity> events{};
        std::size_t size = 0;
        bool reset = false;
    };

    void SetReady(bool ready) {
        std::lock_guard<std::mutex> lock(mutex_);
        ready_ = ready;
        size_ = 0;
        reset_ = ready;
    }
    bool IsReady() const {
        std::lock_guard<std::mutex> lock(mutex_);
        return ready_;
    }
    bool Push(const PointerSnapshot& event) {
        std::lock_guard<std::mutex> lock(mutex_);
        if (!ready_) return false;
        if (size_ == Capacity) {
            dropped_ += size_;
            size_ = 0;
            reset_ = true;
        }
        events_[size_++] = event;
        return true;
    }
    void Drain(Batch& batch) {
        std::lock_guard<std::mutex> lock(mutex_);
        batch.size = ready_ ? size_ : 0;
        batch.reset = ready_ && reset_;
        for (std::size_t i = 0; i < batch.size; ++i)
            batch.events[i] = events_[i];
        size_ = 0;
        reset_ = false;
    }
    std::uint64_t Dropped() const {
        std::lock_guard<std::mutex> lock(mutex_);
        return dropped_;
    }
private:
    mutable std::mutex mutex_;
    std::array<PointerSnapshot, Capacity> events_{};
    std::size_t size_ = 0;
    std::uint64_t dropped_ = 0;
    bool ready_ = false;
    bool reset_ = false;
};
} // namespace crash_fix
