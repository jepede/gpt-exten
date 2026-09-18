#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, shutil, stat, tempfile, zipfile
from pathlib import Path, PurePosixPath

def safe_extract(src: Path, dst: Path):
    with zipfile.ZipFile(src) as z:
        total=0
        for i in z.infolist():
            p=PurePosixPath(i.filename)
            total += i.file_size
            if p.is_absolute() or ".." in p.parts or "\\" in i.filename or stat.S_ISLNK(i.external_attr>>16):
                raise ValueError("unsafe zip member: "+i.filename)
            if total > 512*1024*1024:
                raise ValueError("archive too large")
        z.extractall(dst)

def locate(root: Path)->Path:
    c=[p.parent.parent for p in root.rglob("jni/Android.mk") if (p.parent/"liquid_glass/ytbl.cpp").is_file()]
    if len(c)!=1: raise ValueError(f"expected one v3.3 project, found {len(c)}")
    return c[0]

def one(s,a,b,label):
    n=s.count(a)
    if n!=1: raise ValueError(f"{label}: expected one anchor, found {n}")
    return s.replace(a,b,1)

def patch(root: Path):
    changed=[]

    # 1) New clean-room material preset, inspired by the visible behavior/parameters
    # of KernelSU's liquid-glass bottom bar. No KernelSU source is copied here.
    h=root/"jni/liquid_glass/ytbl.h"
    s=h.read_text(encoding="utf-8")
    s=one(s,
        "enum class Material { Clear, Regular, Reading };",
        "enum class Material { Clear, Regular, Reading, KernelSU };",
        "Material enum")
    h.write_text(s,encoding="utf-8"); changed.append(str(h.relative_to(root)))

    cpp=root/"jni/liquid_glass/ytbl.cpp"
    s=cpp.read_text(encoding="utf-8")
    old="""GlassParams MakeMaterial(Material kind){
    GlassParams p;
    p.shape=GlassShape(Dp(24));
    p.effects.SetVibrancyEnabled(true);
    float blur=kind==Material::Clear?2.2f:kind==Material::Regular?4.6f:10.0f;
    float lens=kind==Material::Reading?8.0f:(kind==Material::Regular?15.0f:13.5f);
    float chroma=kind==Material::Reading?0.05f:0.09f;
"""
    new="""GlassParams MakeMaterial(Material kind){
    GlassParams p;
    p.shape=GlassShape(Dp(24));
    p.effects.SetVibrancyEnabled(true);
    const bool ksu = kind==Material::KernelSU;
    float blur=ksu?4.0f:(kind==Material::Clear?2.2f:kind==Material::Regular?4.6f:10.0f);
    float lens=ksu?24.0f:(kind==Material::Reading?8.0f:(kind==Material::Regular?15.0f:13.5f));
    float chroma=ksu?0.12f:(kind==Material::Reading?0.05f:0.09f);
"""
    s=one(s,old,new,"MakeMaterial prelude")
    s=one(s,
        """.SetLens(Dp(16),Dp(lens),true,true)
        .SetChromaticAberration(chroma)
        .SetColorControls(0.008f,1.025f,1.08f);""",
        """.SetLens(Dp(ksu?24.0f:16.0f),Dp(lens),true,true)
        .SetChromaticAberration(chroma)
        .SetColorControls(ksu?0.010f:0.008f,ksu?1.04f:1.025f,ksu?1.50f:1.08f);""",
        "effect chain")
    s=one(s,
        """p.surfaceColor=s.light
        ? ImVec4(1.0f,1.0f,1.0f,kind==Material::Clear?0.045f:(kind==Material::Regular?0.072f:0.115f))
        : ImVec4(0.10f,0.13f,0.19f,kind==Material::Clear?0.055f:(kind==Material::Regular?0.095f:0.16f));""",
        """p.surfaceColor=s.light
        ? ImVec4(1.0f,1.0f,1.0f,ksu?0.060f:(kind==Material::Clear?0.045f:(kind==Material::Regular?0.072f:0.115f)))
        : ImVec4(0.10f,0.13f,0.19f,ksu?0.075f:(kind==Material::Clear?0.055f:(kind==Material::Regular?0.095f:0.16f)));""",
        "surface tint")
    s=one(s,
        """p.highlight=Highlight(1.0f,0.3f,1.0f,HighlightStyle::Default((int)0x68FFFFFFu,GlassBlendMode::PLUS,72.0f,1.2f));
    p.readability=kind==Material::Reading?0.18f:0;
    p.grain=0.0004f;""",
        """p.highlight=Highlight(ksu?1.2f:1.0f,ksu?0.4f:0.3f,1.0f,
        HighlightStyle::Default(ksu?(int)0x74FFFFFFu:(int)0x68FFFFFFu,
                                GlassBlendMode::PLUS,ksu?76.0f:72.0f,ksu?1.1f:1.2f));
    p.readability=kind==Material::Reading?0.18f:0;
    p.grain=ksu?0.00025f:0.0004f;""",
        "highlight/grain")
    cpp.write_text(s,encoding="utf-8"); changed.append(str(cpp.relative_to(root)))

    # 2) Bottom-tab glass-over-glass: first draw the bar from the real backdrop;
    # then render the selected capsule from CurrentFramebuffer so it refracts
    # the already-glassed bar underneath.
    w=root/"jni/liquid_glass/ytbl_widgets.cpp"
    s=w.read_text(encoding="utf-8")
    s=one(s,
        "auto container=MakeMaterial(Material::Clear);container.shape=GlassShape();",
        "auto container=MakeMaterial(Material::KernelSU);container.shape=GlassShape();",
        "bottom bar material")
    old="""auto thumb=Thumb(animation.GetPressProgress());thumb.hasShadow=false;thumb.surfaceColor=IsLightTheme()?ImVec4(1,1,1,.34f):ImVec4(.92f,.95f,1.0f,.18f);DrawGlass(indicator,thumb);"""
    new="""auto thumb=MakeMaterial(Material::KernelSU);
    const float press=animation.GetPressProgress();
    thumb.hasShadow=false;
    thumb.shape=GlassShape();
    thumb.effects.SetBlurRadiusPx(Dp(Lerpf(4.0f,1.5f,press)));
    thumb.effects.SetLens(Dp(10.0f)*press,Dp(14.0f)*press,true,true)
                 .SetChromaticAberration(0.50f*press);
    thumb.surfaceColor=IsLightTheme()?ImVec4(1,1,1,Lerpf(.15f,.07f,press))
                                     :ImVec4(.90f,.95f,1.0f,Lerpf(.12f,.06f,press));
    thumb.hasInnerShadow=press>0.001f;
    thumb.innerShadow=InnerShadow(Dp(8.0f)*press,0,0,(int)0x26000000u,press);
    // KernelSU-like glass-over-glass: this job snapshots what has already been
    // rendered in the framebuffer, including the container glass.
    Options savedBackdrop=GetOptions();
    Options localBackdrop=savedBackdrop;
    localBackdrop.backdrop=BackdropMode::CurrentFramebuffer;
    SetOptions(localBackdrop);
    DrawGlass(indicator,thumb);
    SetOptions(savedBackdrop);"""
    s=one(s,old,new,"selected capsule")
    # Stronger elastic press, matching the visible ~78/56 ratio at full press.
    s=one(s,
        "indicator=ScaleRect(indicator,animation.GetScaleX(),animation.GetScaleY());",
        """const float capsulePress=animation.GetPressProgress();
    const float ksuScale=1.0f+0.392857f*capsulePress;
    indicator=ScaleRect(indicator,animation.GetScaleX()*ksuScale,
                                  animation.GetScaleY()*ksuScale);""",
        "capsule press scale")
    w.write_text(s,encoding="utf-8"); changed.append(str(w.relative_to(root)))

    # 3) Add an explicit preset in the demo/settings material combo without
    # changing default Clear behavior elsewhere.
    sg=root/"jni/src/Android_draw/SurfaceGlass.cpp"
    s=sg.read_text(encoding="utf-8")
    s=one(s,
        'ImGui::Combo(\n            "材质", &materialIndex, "Clear\\0Regular\\0Reading\\0"\n        );',
        'ImGui::Combo(\n            "材质", &materialIndex, "Clear\\0Regular\\0Reading\\0KernelSU\\0"\n        );',
        "material combo")
    sg.write_text(s,encoding="utf-8"); changed.append(str(sg.relative_to(root)))

    note=root/"README_KERNELSU_STYLE_V34.md"
    note.write_text("""# v3.4 KernelSU-style liquid glass port

Clean-room reimplementation for the existing C++/ImGui/Ytbl renderer. It does
not copy KernelSU Kotlin/Compose source.

Changes:
- Material::KernelSU preset
- 4dp-class blur / 24px-class lens / ~1.5x saturation
- selected bottom-tab capsule uses glass-over-glass CurrentFramebuffer sampling
- press scale reaches about 78/56 at full press
- press-driven 10/14 lens, 0.5 chroma and inner shadow
- KernelSU preset exposed in the material combo

This is intended for Surface_RealBackdrop_v3_3_iOS26Style_Source.zip.
""",encoding="utf-8")
    changed.append(str(note.relative_to(root)))
    return changed

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source",type=Path)
    ap.add_argument("-o","--output",type=Path,default=Path("Surface_RealBackdrop_v3_4_KernelSUGlass.zip"))
    a=ap.parse_args()
    if a.output.exists(): raise ValueError("refusing to overwrite output")
    sha=hashlib.sha256(a.source.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); safe_extract(a.source,td/"in"); root=locate(td/"in")
        changed=patch(root)
        manifest={"source":a.source.name,"source_sha256":sha,"changed_files":changed,
                  "kernel_su_source_copied":False,"full_ndk_build":"not_run","android_runtime":"not_run"}
        (root/"V34_PATCH_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        with zipfile.ZipFile(a.output,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for p in sorted(root.rglob("*")):
                if p.is_file(): z.write(p,Path("Surface_RealBackdrop_v3_4_KernelSUGlass")/p.relative_to(root))
    with zipfile.ZipFile(a.output) as z:
        bad=z.testzip()
        if bad: raise ValueError("output zip corrupt at "+bad)
    print(a.output)
    print("sha256",hashlib.sha256(a.output.read_bytes()).hexdigest())
    print("NDK build and Android runtime: NOT RUN by patcher")

if __name__=="__main__":
    main()
