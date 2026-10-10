#pragma once
// Android API 31+, VulKan-only (no GLES/EGL/GL). One ImGui context and one
// renderer publish to up to three valid parents.  A game-creation SurfaceView
// must not evict an already-visible application UI Surface by recency alone.
#include <android/native_window.h>
#include <android/native_window_jni.h>
#include <android/surface_control.h>
#include <android/log.h>
#include <sys/system_properties.h>
#include <algorithm>
#include <array>
#include <cstdio>
#include <atomic>
#include <chrono>
#include <cstdlib>
#include <cmath>
#include <condition_variable>
#include <cstdint>
#include <deque>
#include <memory>
#include <mutex>
#include <new>
#include <thread>
#include <unordered_set>
#include <vector>
#include <unistd.h>
#include "OverlayPolicy.h"
#include "OverlayProbe.h"
#include "OverlayRoute.h"

namespace overlay_runtime {
constexpr std::size_t kMaxParents = 3;
constexpr std::size_t kMaxKnownWindows = 8;
using Clock = std::chrono::steady_clock;

struct Registry {
    std::mutex mutex;
    std::condition_variable notified;
    struct Candidate {
        ANativeWindow* window=nullptr; // owns a native-window ref
        ASurfaceControl* anchor=nullptr; // optional SurfaceView's parent layer, owns ref
        int logicalWidth=0;
        int logicalHeight=0;
    };
    std::deque<Candidate> pending;
    std::unordered_set<ANativeWindow*> known; // original ANativeWindow hooks
    std::unordered_set<ASurfaceControl*> knownAnchors; // Java SurfaceView identity
    bool running = false;
    std::uint64_t nextId = 0;
};
inline Registry& registry() { static Registry r; return r; }

inline int getPropertyInt(const char* key, int fallback) {
    char buf[PROP_VALUE_MAX]{};
    if (__system_property_get(key, buf) <= 0) return fallback;
    char* end = nullptr;
    long value = std::strtol(buf, &end, 10);
    if (end == buf || *end || value < -10000 || value > 10000) return fallback;
    return static_cast<int>(value);
}

struct Parent {
    ANativeWindow* window = nullptr;
    ASurfaceControl* layer = nullptr;
    ASurfaceControl* anchor = nullptr;
    const int logicalWidth;
    const int logicalHeight;
    std::uint64_t id = 0;
    int format = 0;
    int width = 0;
    int height = 0;
    int zeroSamples = 0;
    Clock::time_point zeroSince{};
    Clock::time_point firstSeen=Clock::now();
    Clock::time_point lastSubmit{};
    std::uint64_t submitted=0;
    explicit Parent(Registry::Candidate candidate, std::uint64_t seq)
      : window(candidate.window), anchor(candidate.anchor),
        logicalWidth(candidate.logicalWidth), logicalHeight(candidate.logicalHeight), id(seq) {}
    bool isSurfaceView() const { return anchor!=nullptr; }
    Parent(const Parent&) = delete;
    Parent& operator=(const Parent&) = delete;
    ~Parent() {
        if (layer) ASurfaceControl_release(layer);
        if (anchor) ASurfaceControl_release(anchor);
        if (window) ANativeWindow_release(window);
    }
    bool connected() const { return layer != nullptr; }
};

inline void registerRemoval(ANativeWindow* p, ASurfaceControl* anchor=nullptr) {
    std::lock_guard<std::mutex> g(registry().mutex);
    if(anchor) registry().knownAnchors.erase(anchor);
    else registry().known.erase(p);
}

inline bool configureParent(Parent& parent) {
    if (!ys_overlay::validWindowSize(parent.width,parent.height)) return false;
    parent.layer = parent.isSurfaceView()
        ? ASurfaceControl_create(parent.anchor,"YS-VulkanOverlay")
        : ASurfaceControl_createFromWindow(parent.window,"YS-VulkanOverlay");
    if (!parent.layer) {
        LOGE("[parent] ASurfaceControl_createFromWindow failed id=%llu fmt=%d",
             static_cast<unsigned long long>(parent.id),parent.format);
        return false;
    }
    ASurfaceTransaction* tx = ASurfaceTransaction_create();
    if (!tx) { ASurfaceControl_release(parent.layer); parent.layer=nullptr; return false; }
    ASurfaceTransaction_setZOrder(tx,parent.layer,1000);
    ASurfaceTransaction_setPosition(tx,parent.layer,0,0);
    const ARect crop{0,0,parent.width,parent.height};
    ASurfaceTransaction_setCrop(tx,parent.layer,crop);
    ASurfaceTransaction_setBufferAlpha(tx,parent.layer,1.0f);
    ASurfaceTransaction_setBufferTransparency(
        tx,parent.layer,ASURFACE_TRANSACTION_TRANSPARENCY_TRANSLUCENT);
    ASurfaceTransaction_setVisibility(tx,parent.layer,ASURFACE_TRANSACTION_VISIBILITY_SHOW);
    // No compositor backpressure on potentially occluded mirror targets.
    // Backpressure may retain many unpresented buffers when a parent is hidden.
    ASurfaceTransaction_setEnableBackPressure(tx,parent.layer,false);
    ASurfaceTransaction_setBufferTransform(tx,parent.layer,0);
    ASurfaceTransaction_apply(tx);
    ASurfaceTransaction_delete(tx);
    LOGI("[parent] attached id=%llu win=%p layer=%p fmt=%d size=%dx%d priority=%d z=1000 vis=SHOW source=%s anchor=%p",
         static_cast<unsigned long long>(parent.id),parent.window,parent.layer,
         parent.format,parent.width,parent.height,
         ys_overlay::surfaceRoutePriority(parent.isSurfaceView(),ys_overlay::parentPriority(parent.format)),
         parent.isSurfaceView()?"SurfaceViewParent":"NativeWindow",parent.anchor);
    return true;
}

// Snapshot immutable submission info so callback can safely run after a
// SurfaceControl or Parent has been destroyed. Never dereference these ptrs.
struct Receipt {
    std::uint64_t frame=0;
    int submitted=0;
    int mode=0;
    std::uint64_t forcedId=0;
    std::uint64_t selectedMask=0;
    std::array<std::uint64_t,kMaxParents> parentIds{};
    std::array<ASurfaceControl*,kMaxParents> layers{};
};
inline void presentDone(void* opaque, ASurfaceTransactionStats* stats) {
    std::unique_ptr<Receipt> receipt(static_cast<Receipt*>(opaque));
    if (!receipt || !stats) return;
    const auto latch = ASurfaceTransactionStats_getLatchTime(stats);
    const int fence = ASurfaceTransactionStats_getPresentFenceFd(stats);
    ASurfaceControl** statsLayers=nullptr;
    size_t layerCount=0;
    ASurfaceTransactionStats_getASurfaceControls(stats,&statsLayers,&layerCount);
    // This mask is only address-matched evidence from the callback. Empty
    // mask does NOT prove a SurfaceControl was not composited: wrappers may differ.
    std::uint64_t matchedMask=0;
    std::array<bool,kMaxParents> matchedBySlot{};
    for (size_t i=0; i<layerCount && statsLayers; ++i)
        for (size_t j=0; j<kMaxParents; ++j)
            if (receipt->layers[j] && receipt->layers[j]==statsLayers[i]) {
                matchedBySlot[j]=true;
                if(receipt->parentIds[j]>0 && receipt->parentIds[j]<64)
                    matchedMask|=(1ULL<<receipt->parentIds[j]);
            }
    if(statsLayers)ASurfaceTransactionStats_releaseASurfaceControls(statsLayers);
    LOGI("[present] frame=%llu targets=%d submitted_ids=0x%llx stats_layers=%zu matched_ids=0x%llx "
         "mode=%d forced=%llu latch_ns=%lld fence=%d",
         static_cast<unsigned long long>(receipt->frame),receipt->submitted,
         static_cast<unsigned long long>(receipt->selectedMask),layerCount,
         static_cast<unsigned long long>(matchedMask),receipt->mode,
         static_cast<unsigned long long>(receipt->forcedId),
         static_cast<long long>(latch),fence>=0?1:0);
    // Per-parent result is a matched control in the transaction stats, not
    // proof of final visibility above unrelated SurfaceFlinger parents.
    for(int j=0; j<receipt->submitted && j<static_cast<int>(kMaxParents); ++j) {
        LOGI("[present.parent] frame=%llu id=%llu layer=%p included=%d stats_listed=%d",
             static_cast<unsigned long long>(receipt->frame),
             static_cast<unsigned long long>(receipt->parentIds[static_cast<size_t>(j)]),
             receipt->layers[static_cast<size_t>(j)],1,
             matchedBySlot[static_cast<size_t>(j)]?1:0);
    }
    if (fence>=0) close(fence);
}

inline std::size_t countAlive(const std::vector<std::unique_ptr<Parent>>& hosts) {
    std::size_t total=0;
    for(const auto& p:hosts) if(p->connected() && p->zeroSamples==0) ++total;
    return total;
}
inline Parent* choosePrimary(std::vector<std::unique_ptr<Parent>>& hosts) {
    Parent* selected=nullptr;
    for(auto& host:hosts) {
        if(!host->connected()||host->zeroSamples!=0)continue;
        const int hostPriority=ys_overlay::surfaceRoutePriority(host->isSurfaceView(),ys_overlay::parentPriority(host->format));
        const int selectedPriority=selected?(ys_overlay::surfaceRoutePriority(selected->isSurfaceView(),ys_overlay::parentPriority(selected->format))):-1;
        if (!selected || hostPriority>selectedPriority ||
            (hostPriority==selectedPriority && host->id<selected->id))
            selected=host.get();
    }
    return selected;
}

inline void drawCalibration() {
#ifndef YS_SHOW_CALIBRATION
#define YS_SHOW_CALIBRATION 1
#endif
#if YS_SHOW_CALIBRATION
    ImGuiIO& io=ImGui::GetIO();
    ImDrawList* fg=ImGui::GetForegroundDrawList();
    const ImVec2 v=io.DisplaySize;
    const ImU32 yellow=IM_COL32(255,222,55,255);
    fg->AddText(ImVec2(24,24),yellow,"YS TL (0,0)");
    fg->AddText(ImVec2(std::max(24.f,v.x-270),24),yellow,"YS TR");
    fg->AddText(ImVec2(24,std::max(24.f,v.y-50)),yellow,"YS BL");
    fg->AddText(ImVec2(std::max(24.f,v.x-270),std::max(24.f,v.y-50)),yellow,"YS BR");
    const ImVec2 m=io.MousePos;
    if(ys_overlay::finiteInBounds({m.x,m.y},v.x,v.y)) {
        const ImU32 red=IM_COL32(255,80,70,255);
        fg->AddCircle(m,20,red,32,3.0f);
        fg->AddLine(ImVec2(m.x-34,m.y),ImVec2(m.x+34,m.y),red,2.0f);
        fg->AddLine(ImVec2(m.x,m.y-34),ImVec2(m.x,m.y+34),red,2.0f);
    }
#endif
}

// Per-frame Vulkan render loop and lifecycle restart. No Android platform
// ImGui backend: custom InputBridge already drives IO, and its platform
// NewFrame previously cached a stale ANativeWindow across scene changes.
inline void workerLoop() {
    using namespace std::chrono_literals;
    Registry& r=registry();
    std::vector<std::unique_ptr<Parent>> hosts;
    VulkanOffscreen renderer;
    bool gui=false;
    int viewW=0,viewH=0;
    int mirrorMode=-1,bufferFlip=-1, offsetX=0,offsetY=0;
    int debugOnly=-1, debugProbe=-1, debugTrace=-1;
    std::uint64_t lastEffectiveId=~0ULL;
    const Clock::time_point probeEpoch=Clock::now();
    std::uint64_t frames=0;
    Clock::time_point lastFrame=Clock::now();
    int retryMs=500;
    LOGI("[supervisor] started: keeping up to %zu parents; one Vulkan device",kMaxParents);

    while (true) {
        // Wait without polling when nothing is active. This thread owns the
        // Vulkan device and is the only thread touching ImGui.
        {
            std::unique_lock<std::mutex> lk(r.mutex);
            if(hosts.empty() && r.pending.empty())
                r.notified.wait(lk,[&]{return !r.pending.empty();});
            while(!r.pending.empty()) {
                Registry::Candidate item=r.pending.front();r.pending.pop_front();
                ANativeWindow* win=item.window;
                if(hosts.size()>=kMaxParents) {
                    // Explicit SurfaceView roots are more useful than stale SDK surfaces.
                    auto old=std::find_if(hosts.begin(),hosts.end(),[](const auto& h){return !h->isSurfaceView();});
                    if(item.anchor && old!=hosts.end()) {
                        if((*old)->anchor)r.knownAnchors.erase((*old)->anchor);
                        else r.known.erase((*old)->window);
                        hosts.erase(old);
                    } else {
                        LOGW("[parent] candidate cap=%zu reached; ignoring window=%p",kMaxParents,win);
                        if(item.anchor) r.knownAnchors.erase(item.anchor);
                        else r.known.erase(win);
                        if(item.anchor)ASurfaceControl_release(item.anchor);
                        ANativeWindow_release(win);continue;
                    }
                }
                hosts.emplace_back(std::make_unique<Parent>(item,++r.nextId));
                LOGI("[parent] observed id=%llu win=%p format=%d native=%dx%d logical=%dx%d source=%s",
                     static_cast<unsigned long long>(r.nextId),win,
                     ANativeWindow_getFormat(win),ANativeWindow_getWidth(win),ANativeWindow_getHeight(win),
                     item.logicalWidth,item.logicalHeight,item.anchor?"SurfaceViewParent":"NativeWindow");
                LOGI("[diag] new_parent id=%llu win=%p reason=%s",
                     static_cast<unsigned long long>(r.nextId),win,
                     item.anchor?"SurfaceView.getSurfaceControl":"ANativeWindow_fromSurface");
            }
        }
        // Attach pending candidates and retire windows disconnected by the
        // game.  Negative ANativeWindow queries are error codes (-19 ENODEV).
        for(auto it=hosts.begin();it!=hosts.end();) {
            Parent& p=**it;
            const int w=ANativeWindow_getWidth(p.window);
            const int h=ANativeWindow_getHeight(p.window);
            bool drop=false;
            if(ys_overlay::windowQueryFailed(w,h)) {
                LOGW("[parent] disconnected id=%llu window=%p fmt=%d query=(%d,%d)",
                     static_cast<unsigned long long>(p.id),p.window,p.format,w,h);
                drop=true;
            } else if(!ys_overlay::validWindowSize(w,h)) {
                if(p.zeroSamples++==0)p.zeroSince=Clock::now();
                if(p.zeroSamples==1 || p.zeroSamples%50==0)
                    LOGW("[parent] waiting id=%llu size=%dx%d samples=%d",
                         static_cast<unsigned long long>(p.id),w,h,p.zeroSamples);
                if(Clock::now()-p.zeroSince>=5s) {
                    LOGW("[parent] zero-sized surface timed out id=%llu",
                         static_cast<unsigned long long>(p.id));
                    drop=true;
                }
            } else {
                p.width=p.isSurfaceView()?p.logicalWidth:w;
                p.height=p.isSurfaceView()?p.logicalHeight:h;
                p.zeroSamples=0;
                if (!p.layer) {
                    p.format=ANativeWindow_getFormat(p.window);
                    if(!configureParent(p))drop=true;
                }
            }
            if(drop) {
                LOGW("[diag] retire id=%llu submitted=%llu ever_attached=%d size=%dx%d fmt=%d layer=%p",
                     static_cast<unsigned long long>(p.id),
                     static_cast<unsigned long long>(p.submitted),p.connected()?1:0,
                     w,h,p.format,p.layer);
                registerRemoval(p.window,p.anchor);
                it=hosts.erase(it);  // RAII drops layer and native-window ref
            } else ++it;
        }
        Parent* primary=choosePrimary(hosts);
        if(!primary) {
            if(gui) {
                overlay_input::queue().disable();
                renderer.shutdown();
                ImGui::DestroyContext();gui=false;
                viewW=viewH=0;frames=0;
                LOGI("[supervisor] renderer stopped (no valid parent)");
            }
            // Zero-sized candidate may recover; check periodically.
            std::this_thread::sleep_for(100ms);
            continue;
        }
        if (!gui) {
            viewW=primary->width;viewH=primary->height;
            if(!renderer.initialize(static_cast<std::uint32_t>(viewW),static_cast<std::uint32_t>(viewH))) {
                LOGE("[supervisor] Vulkan init failed, retrying in %d ms",retryMs);
                renderer.shutdown();
                std::this_thread::sleep_for(std::chrono::milliseconds(retryMs));
                retryMs=std::min(retryMs*2,5000);continue;
            }
            IMGUI_CHECKVERSION();
            ImGui::CreateContext();
            if(!renderer.initializeImGui()) {
                LOGE("[supervisor] ImGui Vulkan init failed");
                renderer.shutdown();ImGui::DestroyContext();
                std::this_thread::sleep_for(std::chrono::milliseconds(retryMs));
                retryMs=std::min(retryMs*2,5000);continue;
            }
            ImGui::StyleColorsClassic();
            ImGui::GetStyle().ScaleAllSizes(3.0f);
            LoadFont(25.2f);
            overlay_input::eventDeduplicator().clear();
            overlay_input::queue().enable();
            VulkanState.ScreenWidth=static_cast<float>(viewW);
            VulkanState.ScreenHeight=static_cast<float>(viewH);
            gui=true;retryMs=500;frames=0;lastFrame=Clock::now();
            LOGI("[supervisor] Vulkan context created primary=%llu %dx%d source=%s",
                 static_cast<unsigned long long>(primary->id),viewW,viewH,
                 primary->isSurfaceView()?"SurfaceViewParent":"NativeWindow");
        }
        if (viewW!=primary->width || viewH!=primary->height) {
            if(!renderer.resize(static_cast<uint32_t>(primary->width),static_cast<uint32_t>(primary->height))) {
                LOGE("[supervisor] Vulkan resize failed");
                overlay_input::queue().disable();
                renderer.shutdown();ImGui::DestroyContext();gui=false;
                continue;
            }
            viewW=primary->width;viewH=primary->height;
            VulkanState.ScreenWidth=static_cast<float>(viewW);
            VulkanState.ScreenHeight=static_cast<float>(viewH);
            LOGI("[supervisor] resized target=%dx%d primary=%llu",viewW,viewH,
                 static_cast<unsigned long long>(primary->id));
        }
        if (frames%120==0) {
            const int newMode=ys_overlay::sanitizeMirrorMode(
                getPropertyInt("debug.ys.overlay.mode",2));
            const int newFlip=ys_overlay::sanitizeFlip(
                getPropertyInt("debug.ys.overlay.flip",0));
            const int newX=std::clamp(getPropertyInt("debug.ys.overlay.x",0),-viewW,viewW);
            const int newY=std::clamp(getPropertyInt("debug.ys.overlay.y",0),-viewH,viewH);
            if(newMode!=mirrorMode || newFlip!=bufferFlip || newX!=offsetX || newY!=offsetY) {
                mirrorMode=newMode;bufferFlip=newFlip;offsetX=newX;offsetY=newY;
                ys_overlay::configuredFlip().store(bufferFlip,std::memory_order_release);
                ys_overlay::configuredOffsetX().store(offsetX,std::memory_order_release);
                ys_overlay::configuredOffsetY().store(offsetY,std::memory_order_release);
                LOGI("[supervisor] mode=%d flip=%d pos=(%d,%d) parents=%zu (debug.ys.overlay.*)",
                     mirrorMode,bufferFlip,offsetX,offsetY,hosts.size());
            }
        }
        // Use logcat-only debugging: configure one parent to display at a
        // time without switching back to Termux mid-game. Property values:
        // only=0 auto; only=N specific ID; probe=1 cycles IDs every 5 seconds.
        if(frames%30==0) {
            const int newOnly=std::max(0,getPropertyInt("debug.ys.overlay.only",0));
#ifndef YS_DEFAULT_AUTO_PROBE
// Safe default: automatic parent switching is diagnostics-only and must opt in.
#define YS_DEFAULT_AUTO_PROBE 0
#endif
            const int newProbe=getPropertyInt("debug.ys.overlay.probe",YS_DEFAULT_AUTO_PROBE)!=0?1:0;
            const int newTrace=std::clamp(getPropertyInt("debug.ys.overlay.trace",1),0,2);
            if(newOnly!=debugOnly || newProbe!=debugProbe || newTrace!=debugTrace) {
                debugOnly=newOnly;debugProbe=newProbe;debugTrace=newTrace;
                LOGI("[diag] config only=%d probe=%d trace=%d (mode=%d)",
                     debugOnly,debugProbe,debugTrace,mirrorMode<0?2:mirrorMode);
            }
        }
        std::vector<std::uint64_t> aliveIds;
        aliveIds.reserve(hosts.size());
        for(const auto& host:hosts)
            if(host->connected() && host->zeroSamples==0)aliveIds.push_back(host->id);
        const std::uint64_t elapsedProbeMs=static_cast<std::uint64_t>(
            std::chrono::duration_cast<std::chrono::milliseconds>(Clock::now()-probeEpoch).count());
        const std::uint64_t effectiveId = debugProbe==1
            ? ys_overlay::selectProbeId(aliveIds,elapsedProbeMs)
            : (debugOnly>0 ? static_cast<std::uint64_t>(debugOnly) : 0ULL);
        if(effectiveId!=lastEffectiveId) {
            if(debugProbe==1 && aliveIds.size()>1)
                LOGW("[probe] DEBUG MODE: switching submitted SurfaceControl parent every 5s; "
                     "overlay visibility may alternate. Disable with setprop debug.ys.overlay.probe 0");
            LOGI("[probe] selected=%llu candidates=%zu probe=%d only=%d slot_ms=5000 "
                 "(0=normal broadcast, >0=one parent)",
                 static_cast<unsigned long long>(effectiveId),aliveIds.size(),
                 debugProbe,debugOnly);
            lastEffectiveId=effectiveId;
        }
        if(debugTrace>0 && (frames==0 || frames%(debugTrace==2?30:120)==0)) {
            LOGI("[diag] summary frame=%llu parents=%zu alive=%zu primary=%llu "
                 "mode=%d only=%d probe=%d effective=%llu target=%dx%d",
                 static_cast<unsigned long long>(frames),hosts.size(),aliveIds.size(),
                 static_cast<unsigned long long>(primary->id),
                 mirrorMode<0?2:mirrorMode,debugOnly,debugProbe,
                 static_cast<unsigned long long>(effectiveId),viewW,viewH);
            for(const auto& h:hosts) {
                const auto age=std::chrono::duration_cast<std::chrono::milliseconds>(
                    Clock::now()-h->firstSeen).count();
                LOGI("[diag] parent id=%llu fmt=%d win=%p layer=%p %dx%d priority=%d "
                     "connected=%d zero=%d age_ms=%lld submitted=%llu is_primary=%d effective=%d source=%s anchor=%p",
                     static_cast<unsigned long long>(h->id),h->format,h->window,h->layer,
                     h->width,h->height,ys_overlay::surfaceRoutePriority(h->isSurfaceView(),ys_overlay::parentPriority(h->format)),
                     h->connected()?1:0,h->zeroSamples,
                     static_cast<long long>(age),
                     static_cast<unsigned long long>(h->submitted),
                     h.get()==primary?1:0,
                     effectiveId>0 && h->id==effectiveId?1:0,
                     h->isSurfaceView()?"SurfaceViewParent":"NativeWindow",h->anchor);
            }
        }
        auto frameStart=Clock::now();
        const float delta=std::clamp(std::chrono::duration<float>(frameStart-lastFrame).count(),1.0e-6f,0.1f);
        lastFrame=frameStart;
        ImGuiIO& io=ImGui::GetIO();
        io.DisplaySize=ImVec2(static_cast<float>(viewW),static_cast<float>(viewH));
        io.DeltaTime=delta;
        ImGui_ImplVulkan_NewFrame();
        DrainOverlayInput();
        ImGui::NewFrame();
        BeginDraw();
        drawCalibration();
        if(debugProbe==1 || debugOnly>0) {
            char label[128];
            std::snprintf(label,sizeof(label),"YS TARGET %llu  %s",
                          static_cast<unsigned long long>(effectiveId),
                          debugProbe==1?"AUTO PROBE":"FORCED");
            ImDrawList* fg=ImGui::GetForegroundDrawList();
            fg->AddRectFilled(ImVec2(18,85),ImVec2(430,129),
                              IM_COL32(14,20,28,215),6.0f);
            fg->AddText(ImVec2(28,91),IM_COL32(255,210,55,255),label);
        }
        ImGui::Render();
        if(debugTrace>0 && (frames==0 || frames%120==0)) {
            LOGI("[touchdiag] mouse=(%.1f,%.1f) viewport=(%.1f,%.1f) want_capture=%d button0=%d "
                 "flip=%d offset=(%d,%d)",
                 io.MousePos.x,io.MousePos.y,io.DisplaySize.x,io.DisplaySize.y,
                 io.WantCaptureMouse?1:0,io.MouseDown[0]?1:0,bufferFlip,offsetX,offsetY);
        }

        AHardwareBuffer* buffer=nullptr;
        if(!renderer.render(ImGui::GetDrawData(),&buffer)) {
            LOGE("[supervisor] Vulkan frame error; reinitialize device");
            overlay_input::queue().disable();
            renderer.shutdown();ImGui::DestroyContext();gui=false;
            std::this_thread::sleep_for(100ms);
            continue;
        }
        ASurfaceTransaction* tx=ASurfaceTransaction_create();
        if(!tx){AHardwareBuffer_release(buffer);std::this_thread::sleep_for(100ms);continue;}
        Parent* latest=nullptr;
        for(auto& host:hosts)if(host->connected() && host->zeroSamples==0 &&
             (!latest || host->id>latest->id)) latest=host.get();
        const int selectedMode=mirrorMode<0?2:mirrorMode;
        int published=0;
        std::uint64_t publishedMask=0;
        std::array<std::uint64_t,kMaxParents> submittedIds{};
        std::array<ASurfaceControl*,kMaxParents> submittedLayers{};
        const bool hasSurfaceView=std::any_of(hosts.begin(),hosts.end(),[](const auto& p){
            return p->isSurfaceView() && p->connected() && p->zeroSamples==0;
        });
        for(auto& item:hosts) {
            Parent& host=*item;
            if(!host.connected())continue;
            if(host.zeroSamples!=0) {
                ASurfaceTransaction_setVisibility(tx,host.layer,
                                                  ASURFACE_TRANSACTION_VISIBILITY_HIDE);
                continue;
            }
            // Hide unused mirror layers as well: a previous buffer stays
            // visible after mode switches if it is merely skipped here.
            if(!ys_overlay::submitToParent(host.isSurfaceView(),hasSurfaceView,
                                           selectedMode,&host==primary,&host==latest,
                                           effectiveId,host.id)) {
                ASurfaceTransaction_setVisibility(tx,host.layer,
                                                  ASURFACE_TRANSACTION_VISIBILITY_HIDE);
                continue;
            }
            // Scale and crop the same offscreen AHardwareBuffer to another
            // candidate parent. For equal-sized game surfaces scale is 1.
            ASurfaceTransaction_setPosition(tx,host.layer,offsetX,offsetY);
            ASurfaceTransaction_setScale(tx,host.layer,
                static_cast<float>(host.width)/viewW,
                static_cast<float>(host.height)/viewH);
            const ARect crop{0,0,viewW,viewH};
            ASurfaceTransaction_setCrop(tx,host.layer,crop);
            ASurfaceTransaction_setBufferTransform(tx,host.layer,bufferFlip<0?0:bufferFlip);
            ASurfaceTransaction_setZOrder(tx,host.layer,1000);
            ASurfaceTransaction_setVisibility(tx,host.layer,ASURFACE_TRANSACTION_VISIBILITY_SHOW);
            ASurfaceTransaction_setBuffer(tx,host.layer,buffer,-1);
            if(published<static_cast<int>(kMaxParents)) {
                submittedIds[static_cast<size_t>(published)]=host.id;
                submittedLayers[static_cast<size_t>(published)]=host.layer;
            }
            if(host.id>0 && host.id<64) publishedMask|=(1ULL<<host.id);
            ++host.submitted;
            host.lastSubmit=Clock::now();
            ++published;
        }
        if (published>0) {
            if(frames==0||((frames+1)%120==0)) {
                auto* receipt=new(std::nothrow)Receipt{};
                if(receipt) {
                    receipt->frame=frames+1;
                    receipt->submitted=published;
                    receipt->mode=selectedMode;
                    receipt->forcedId=effectiveId;
                    receipt->selectedMask=publishedMask;
                    receipt->parentIds=submittedIds;
                    receipt->layers=submittedLayers;
                    ASurfaceTransaction_setOnComplete(tx,receipt,presentDone);
                }
            }
            ASurfaceTransaction_apply(tx);
        }
        ASurfaceTransaction_delete(tx);
        AHardwareBuffer_release(buffer);
        ++frames;
        if(frames==1||frames%120==0) {
            LOGI("[surface] frames=%llu parents_total=%zu targets=%d ids=0x%llx mode=%d "
                 "primary=%llu effective=%llu probe=%d size=%dx%d",
                 static_cast<unsigned long long>(frames),hosts.size(),published,
                 static_cast<unsigned long long>(publishedMask),selectedMode,
                 static_cast<unsigned long long>(primary->id),
                 static_cast<unsigned long long>(effectiveId),debugProbe,viewW,viewH);
            if(published==0 && effectiveId>0)
                LOGW("[diag] requested id=%llu not among valid parent candidates, NO BUFFER SUBMITTED",
                     static_cast<unsigned long long>(effectiveId));
        }
        const auto elapsed=Clock::now()-frameStart;
        const auto budget=std::chrono::duration<float>(1.f/60.f);
        if(elapsed<budget)std::this_thread::sleep_for(budget-elapsed);
    }
}

inline void observedWindow(ANativeWindow* candidate) {
    if(!candidate)return;
    Registry& r=registry();
    std::lock_guard<std::mutex> lk(r.mutex);
    if(r.known.find(candidate)!=r.known.end())return;
    if(r.known.size()>=kMaxKnownWindows) {
        LOGW("[parent] too many candidate windows; dropping %p",candidate);return;
    }
    ANativeWindow_acquire(candidate);
    r.known.insert(candidate);
    r.pending.push_back({candidate,nullptr,0,0});
    if(!r.running) {
        try {
            std::thread(workerLoop).detach();r.running=true;
        } catch(const std::exception& ex) {
            LOGE("[supervisor] cannot start worker: %s",ex.what());
            r.known.erase(candidate);r.pending.pop_back();ANativeWindow_release(candidate);
            return;
        } catch(...) {
            LOGE("[supervisor] cannot start worker");
            r.known.erase(candidate);r.pending.pop_back();ANativeWindow_release(candidate);
            return;
        }
    }
    r.notified.notify_one();
}
// Caller transfers an acquired ANativeWindow and ASurfaceControl reference.
// The SurfaceView root layer is a sibling parent of the BLAST buffer, so its
// children inherit the View coordinate system, not BLAST game resolution scaling.
inline void observedSurfaceView(ANativeWindow* ownedWindow, ASurfaceControl* ownedAnchor,
                                int viewW, int viewH) {
    if(!ownedWindow || !ownedAnchor || !ys_overlay::validWindowSize(viewW,viewH)) {
        if(ownedWindow)ANativeWindow_release(ownedWindow);
        if(ownedAnchor)ASurfaceControl_release(ownedAnchor);
        return;
    }
    Registry& r=registry();
    {
        std::lock_guard<std::mutex> lock(r.mutex);
        if(r.knownAnchors.count(ownedAnchor) || r.knownAnchors.size()>=kMaxKnownWindows) {
            ASurfaceControl_release(ownedAnchor);ANativeWindow_release(ownedWindow);return;
        }
        r.knownAnchors.insert(ownedAnchor);
        r.pending.push_back({ownedWindow,ownedAnchor,viewW,viewH});
        if(!r.running) {
            try { std::thread(workerLoop).detach();r.running=true; }
            catch(...) {
                LOGE("[bridge] supervisor startup failed");
                r.knownAnchors.erase(ownedAnchor);
                r.pending.pop_back();
                ASurfaceControl_release(ownedAnchor);ANativeWindow_release(ownedWindow);
                return;
            }
        }
    }
    LOGI("[bridge] discovered main SurfaceView view=%dx%d native=%dx%d anchor=%p",
         viewW,viewH,ANativeWindow_getWidth(ownedWindow),ANativeWindow_getHeight(ownedWindow),ownedAnchor);
    r.notified.notify_one();
}
} // namespace overlay_runtime

inline ANativeWindow* (*orig_ANativeWindow_fromSurface)(JNIEnv*,jobject)=nullptr;
inline ANativeWindow* Hook_ANativeWindow_fromSurface(JNIEnv* env,jobject surface) {
    if(!orig_ANativeWindow_fromSurface)return nullptr;
    ANativeWindow* window=orig_ANativeWindow_fromSurface(env,surface);
    if(window)overlay_runtime::observedWindow(window);
    return window;
}

#include "SurfaceBridge.h"

inline void hack_main() noexcept {
    void* symbol=DobbySymbolResolver("libandroid.so","ANativeWindow_fromSurface");
    if(!symbol){LOGE("[supervisor] unable to resolve ANativeWindow_fromSurface");return;}
    const int rc=DobbyHook(symbol,(void*)Hook_ANativeWindow_fromSurface,
                           (void**)&orig_ANativeWindow_fromSurface);
    if(rc!=0||!orig_ANativeWindow_fromSurface){
        LOGE("[supervisor] unable to install native window hook: %d",rc);return;
    }
    LOGI("[supervisor] NativeWindow hook installed (multi-parent Vulkan mode)");
    ys_bridge::start();
    void* input=DobbySymbolResolver("libinput.so","_ZN7android11MotionEvent8copyFromEPKS0_b");
    if(!input){LOGW("[supervisor] MotionEvent hook symbol not found");return;}
    const int irc=DobbyHook(input,(void*)hook_input,(void**)&orig_input);
    if(irc!=0||!orig_input) LOGE("[supervisor] MotionEvent hook failed %d",irc);
    else LOGI("[supervisor] MotionEvent input hook installed");
}
