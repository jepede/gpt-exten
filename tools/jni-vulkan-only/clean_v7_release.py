#!/usr/bin/env python3
"""Prune diagnostics from verified, user-tested Vulkan v7 project.

Keep SurfaceView root host, ANativeWindow hook fallback, Vulkan renderer,
parent lifecycle, event dedup, multi-touch, and input queue unchanged.
Freeze the user's successful defaults: mode2, flip0, offset0, probe0, only0.
"""
from pathlib import Path
import re,shutil,sys
root=Path(sys.argv[1]).resolve()
jni=root/"jni"
S=jni/"OverlaySupervisor.h"
I=jni/"InputBridge.h"
M=jni/"Android.mk"
assert all(x.is_file() for x in (S,I,M))

def cut(s,b,e,replace="",label=""):
    assert b in s and e in s[s.index(b):],f"{label}: missing boundary"
    start=s.index(b);end=s.index(e,start)
    return s[:start]+replace+s[end:]
def rep(s,old,new,label):
    n=s.count(old)
    assert n==1,f"{label}: expected 1 got {n}"
    return s.replace(old,new,1)
def strip_log(s,macro):
    pat=re.compile(r'(?<![\w])'+re.escape(macro)+r'\s*\(')
    out=[];start=0;cnt=0
    while True:
        m=pat.search(s,start)
        if m is None:out.append(s[start:]);break
        i=m.end();depth=1;quote=None;esc=False
        while i<len(s) and depth:
            ch=s[i]
            if quote:
                if esc:esc=False
                elif ch=="\\":esc=True
                elif ch==quote:quote=None
            elif ch in ('"',"'"):quote=ch
            elif ch=="(":depth+=1
            elif ch==")":depth-=1
            i+=1
        assert depth==0,f"unbalanced {macro} call"
        while i<len(s) and s[i] in " \t":i+=1
        assert i<len(s) and s[i]==";",f"non-statement {macro} call"
        out.append(s[start:m.start()]);out.append("(void)0")
        start=i;cnt+=1
    return ''.join(out),cnt

s=S.read_text(encoding="utf-8")
inp=I.read_text(encoding="utf-8")
s=rep(s,'#include "OverlayProbe.h"\n','',"probe header")
s=rep(s,'#include <sys/system_properties.h>\n','',"prop include")
s=cut(s,'inline int getPropertyInt(', 'struct Parent {',"","property getter")
s=cut(s,'// Snapshot immutable submission info','inline std::size_t countAlive(',"","transaction receipts")
s=cut(s,'inline void drawCalibration()', '// Per-frame Vulkan render loop',"","visual calibration")
s=rep(s,'''    int mirrorMode=-1,bufferFlip=-1, offsetX=0,offsetY=0;
    int debugOnly=-1, debugProbe=-1, debugTrace=-1;
    std::uint64_t lastEffectiveId=~0ULL;
    const Clock::time_point probeEpoch=Clock::now();
    std::uint64_t frames=0;
''','',"runtime debug state")
s=rep(s,'viewW=viewH=0;frames=0;','viewW=viewH=0;',"reset counters")
s=rep(s,'gui=true;retryMs=500;frames=0;lastFrame=Clock::now();','gui=true;retryMs=500;lastFrame=Clock::now();',"init counters")
s=cut(s,'        if (frames%120==0) {','        auto frameStart=Clock::now();',"","debug properties, probes and periodic logs")
s=cut(s,'        BeginDraw();\n        drawCalibration();',
      '        AHardwareBuffer* buffer=nullptr;',
      '        BeginDraw();\n        ImGui::Render();\n\n',"debug foreground widgets")
s=rep(s,'        const int selectedMode=mirrorMode<0?2:mirrorMode;',
         '        constexpr int selectedMode=2; // user-tested default mirror route',"mirror mode")
s=rep(s,'''        std::uint64_t publishedMask=0;
        std::array<std::uint64_t,kMaxParents> submittedIds{};
        std::array<ASurfaceControl*,kMaxParents> submittedLayers{};
''','',"receipt metadata")
s=rep(s,'                                           effectiveId,host.id))',
         '                                           0,host.id))',"fixed parent choice")
s=rep(s,'ASurfaceTransaction_setPosition(tx,host.layer,offsetX,offsetY);',
         'ASurfaceTransaction_setPosition(tx,host.layer,0,0);',"fixed position")
s=rep(s,'ASurfaceTransaction_setBufferTransform(tx,host.layer,bufferFlip<0?0:bufferFlip);',
         'ASurfaceTransaction_setBufferTransform(tx,host.layer,0);',"fixed transform")
s=cut(s,'            if(published<static_cast<int>(kMaxParents)) {',
      '            ++published;',"","remove receipt metadata, counters")
s=cut(s,'        if (published>0) {\n            if(frames==0||((frames+1)%120==0)) {',
      '        const auto elapsed=Clock::now()-frameStart;',
'''        if(published>0) ASurfaceTransaction_apply(tx);
        ASurfaceTransaction_delete(tx);
        AHardwareBuffer_release(buffer);
''',"remove per-frame onComplete")
s=rep(s,'''    Clock::time_point firstSeen=Clock::now();
    Clock::time_point lastSubmit{};
    std::uint64_t submitted=0;
''','',"diagnostic stats")
s=cut(s,'                LOGW("[diag] retire id=%llu submitted=%llu ever_attached=%d size=%dx%d fmt=%d layer=%p",',
      '                registerRemoval(p.window,p.anchor);',
'''                LOGW("[parent] retiring invalid parent id=%llu size=%dx%d",
                     static_cast<unsigned long long>(p.id),w,h);
''',"retire log no longer references counters")
for term in ('debug.ys.overlay','OverlayProbe','YS_SHOW_CALIBRATION','drawCalibration',
             'presentDone(', 'ASurfaceTransaction_setOnComplete','debugProbe','debugOnly',
             'debugTrace','publishedMask','statsLayers','YS TARGET','effectiveId',
             'offsetX','offsetY','bufferFlip','mirrorMode','firstSeen','lastSubmit'):
    assert term not in s,f"remaining debug item in OverlaySupervisor.h: {term}"

inp=cut(inp,'            const float localX = AMotionEvent_getX(input, i);',
    '            if (!std::isfinite(p.x) || !std::isfinite(p.y)) return;',
'''            p.x = AMotionEvent_getRawX(input, i);
            p.y = AMotionEvent_getRawY(input, i);
''',"raw display coordinates")
inp=cut(inp,'        if (overlay_input::eventDeduplicator().isDuplicate(identity)) {',
    '        overlay_input::queue().push(motion, generation);',
    '        if (overlay_input::eventDeduplicator().isDuplicate(identity)) return;\n',
    "remove touch logging")
inp=cut(inp,'        const auto flip = ys_overlay::configuredFlip().load(std::memory_order_acquire);',
    '        const auto source = changed.tool == AMOTION_EVENT_TOOL_TYPE_MOUSE',
'''        const auto mousePos = [&](float x, float y) {
            io.AddMousePosEvent(x,y);
        };
''',"remove touch diagnostic transformation")
for inc in ('#include "OverlayPolicy.h"\n','#include <bit>\n','#include <array>\n',
            '#include <mutex>\n','#include <atomic>\n'):
    inp=inp.replace(inc,'')
assert 'YS_USE_RAW_TOUCH_COORDS' not in inp
assert 'configuredFlip' not in inp
total=0
for f in sorted(set([S,I,*jni.glob("*.h"),*jni.glob("*.cpp")])):
    if f.name=="Logger.h":continue
    body = s if f==S else inp if f==I else f.read_text(encoding="utf-8")
    for macro in ("LOGI","LOGD"):
        body,n=strip_log(body,macro);total+=n
    f.write_text(body,encoding="utf-8")

for f in jni.glob("*.h"):
    if f.name=="Logger.h":continue
    body=f.read_text(encoding="utf-8")
    for t in ('[touchdiag]','[present.parent]','YS TARGET','YS TL (0,0)','debug.ys.overlay'):
        assert t not in body,f"{f.name} has {t}"
s=S.read_text(encoding="utf-8")
inp=I.read_text(encoding="utf-8")
assert 'overlay_input::eventDeduplicator().isDuplicate(identity)' in inp
assert 'io.AddMousePosEvent(x,y)' in inp
assert 'ASurfaceControl_create(parent.anchor' in s
assert 'ys_bridge::start();' in s
assert 'ys_overlay::submitToParent(' in s
assert 'ASurfaceTransaction_setBuffer(tx,host.layer,buffer,-1)' in s
assert 'ASurfaceTransaction_apply(tx);' in s
assert 'DobbyHook(symbol' in s and 'DobbyHook(input' in s
assert 'YS_RegisterSurfaceView(' in (jni/'Injector.cpp').read_text(encoding='utf-8')

mk=M.read_text(encoding="utf-8")
mk=rep(mk,"BUILD_MODE ?= debug\n","","remove default BUILD_MODE")
mk=cut(mk,'ifeq ($(BUILD_MODE),debug)','include $(BUILD_SHARED_LIBRARY)',
'''# Optimized stripped ARM64 build, no runtime diagnostic options.
LOCAL_CPPFLAGS += -O2 -fno-rtti -fvisibility=hidden -fomit-frame-pointer
LOCAL_LDFLAGS += -Wl,-s
''',"release build flags")
M.write_text(mk,encoding="utf-8")

lg=jni/"Logger.h"
x=lg.read_text(encoding="utf-8")
x=x.replace('#define LOGD(...) ((void)__android_log_print(oDEBUG, TAG, __VA_ARGS__))',
            '#define LOGD(...) ((void)0)')
x=x.replace('#define LOGI(...) ((void)__android_log_print(oINFO,  TAG, __VA_ARGS__))',
            '#define LOGI(...) ((void)0)')
x=x.replace('#define ALOGD(...) ((void)__android_log_print(ANDROID_LOG_DEBUG, "YS", __VA_ARGS__))',
            '#define ALOGD(...) ((void)0)')
lg.write_text(x,encoding="utf-8")

(jni/"OverlayProbe.h").unlink(missing_ok=True)
for dirname in ("docs","verification","tools","symbols","prebuilt","obj","libs","tests"):
    p=root/dirname
    if p.is_dir():shutil.rmtree(p)
for p in root.glob("README*"):p.unlink()
for filename in ("SHA256SUMS.txt","dynamic_dependencies.txt","original_jni1.sha256",
                 "build.sh","BUILD-REPORT.txt","SURFACE_FIX_VALIDATION.json"):
    (root/filename).unlink(missing_ok=True)
(root/"build.sh").write_text("""#!/bin/sh
set -eu
: "$ANDROID_NDK_HOME"
test -x "$ANDROID_NDK_HOME/ndk-build"
"$ANDROID_NDK_HOME/ndk-build" -j4 NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=./jni/Android.mk NDK_APPLICATION_MK=./jni/Application.mk
""",encoding="utf-8")
(root/"README.md").write_text("""# JNI Vulkan-only Overlay v7.1 Clean Production

Built from the **exact user-tested Vulkan v7** project.

Preserved:
- Activity/SurfaceView discovery and public YS_RegisterActivity /
  YS_RegisterSurfaceView JNI entrypoints
- SurfaceView.getSurfaceControl() root anchor (no BLAST scaling inheritance)
- Fallback ANativeWindow hook, multi-parent lifecycle, Vulkan render
- MotionEvent original callback, timestamp/device deduplication, multi-finger
  ImGui input, working raw display coordinates.

Removed from runtime and source:
- Auto probe, forced parent, live debug properties
- Touch logging, onComplete present receipts, per-frame statistics
- Calibration/crosshair overlay, YS TARGET indicator
- Old debug binaries, symbols, capture scripts and version history documents.

Fixed defaults: route=2 (broadcast), flip=0, x=0, y=0,
probe=0, only=0, trace=0.

To build: set ANDROID_NDK_HOME to r28c, then sh build.sh.
Output: libs/arm64-v8a/libAndroid.so

Error/warning Android log tag stays YS.
This cleaned version is compiled and analyzed separately; successful
Android 16 device testing applies to original v7, not automatically v7.1.
""",encoding="utf-8")
print("PRODUCTION_CLEANUP_SUCCESS")
print("REMOVED_INFO_DEBUG_CALLS",total)
print("SUPERVISOR_LINES",len(s.splitlines()))
print("INPUT_LINES",len(inp.splitlines()))
print("SOURCE_FILE_COUNT",len([f for f in jni.rglob("*") if f.is_file()]))
