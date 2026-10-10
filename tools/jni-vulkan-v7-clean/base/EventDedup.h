#pragma once
#include <array>
#include <cstdint>
#include <cstddef>
#include <mutex>

namespace overlay_input {
struct EventIdentity {
    std::int64_t downTime = 0;
    std::int64_t eventTime = 0;
    std::uint64_t pointerHash = 0; // IDs and tool types only: transforms differ in copied events.
    std::int32_t fullAction = 0;
    std::int32_t deviceId = -1;
    std::int32_t source = 0;
    std::uint32_t pointerCount = 0;
    bool operator==(const EventIdentity&) const = default;
};
class EventDeduplicator {
public:
    void clear() {
        std::lock_guard<std::mutex> lock(mutex_);
        next_ = valid_ = 0;
    }
    bool isDuplicate(const EventIdentity& identity) {
        if (identity.eventTime <= 0) return false;
        std::lock_guard<std::mutex> lock(mutex_);
        for (std::size_t i = 0; i < valid_; ++i)
            if (history_[i] == identity) return true;
        history_[next_] = identity;
        next_ = (next_ + 1) % history_.size();
        if (valid_ < history_.size()) ++valid_;
        return false;
    }
private:
    std::mutex mutex_;
    std::array<EventIdentity, 128> history_{};
    std::size_t next_ = 0;
    std::size_t valid_ = 0;
};
inline EventDeduplicator& eventDeduplicator() {
    static EventDeduplicator cache;
    return cache;
}
} // namespace overlay_input
