#pragma once
#include <cstdint>
#include <cstddef>
#include <vector>

namespace ys_overlay {
// All candidates are supplied in stable observed order. Cycle one candidate
// every 5 seconds, avoiding interactive shell focus changes during gameplay.
// Pure helper for host tests; no Android dependency.
inline std::uint64_t selectProbeId(const std::vector<std::uint64_t>& validIds,
                                   std::uint64_t elapsedMs,
                                   std::uint64_t slotMs=5000) noexcept {
    if(validIds.empty())return 0;
    if(slotMs==0)slotMs=5000;
    return validIds[static_cast<std::size_t>((elapsedMs/slotMs)%validIds.size())];
}
} // namespace ys_overlay
