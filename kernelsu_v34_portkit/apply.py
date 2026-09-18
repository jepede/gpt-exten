#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, shutil, stat, tempfile, zipfile
from pathlib import Path, PurePosixPath

def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one match, found {n}")
    return text.replace(old, new, 1)

def safe_extract(src: Path, dst: Path) -> None:
    total = 0
    with zipfile.ZipFile(src) as z:
        for i in z.infolist():
            p = PurePosixPath(i.filename)
            if p.is_absolute() or ".." in p.parts or "\\" in i.filename or stat.S_ISLNK(i.external_attr >> 16):
                raise RuntimeError(f"unsafe ZIP member: {i.filename}")
            total += i.file_size
            if total > 512 * 1024 * 1024:
                raise RuntimeError("source archive is unexpectedly large")
        z.extractall(dst)

def locate(root: Path) -> Path:
    hits = [p.parent.parent for p in root.rglob("jni/Android.mk")
            if (p.parent / "liquid_glass/ytbl.h").is_file()]
    if len(hits) != 1:
        raise RuntimeError(f"expected exactly one v3.3 project, found {len(hits)}")
    project = hits[0]
    if not (project / "README_IOS26_STYLE.md").is_file():
        raise RuntimeError("this port kit expects Surface_RealBackdrop_v3_3_iOS26Style_Source.zip")
    return project

def patch(project: Path) -> list[str]:
    changed = []
    def edit(rel: str, fn):
        p = project / rel
        old = p.read_text(encoding="utf-8-sig")
        new = fn(old)
        if old == new:
            raise RuntimeError(f"{rel}: patch made no changes")
        p.write_text(new, encoding="utf-8")
        changed.append(rel)

    def patch_h(s: str) -> str:
        s = replace_once(s,
            "enum class Material { Clear, Regular, Reading };",
            "enum class Material { Clear, Regular, Reading, KernelSU };",
            "Material enum")
        s = replace_once(s,
            "    float readability=0, grain=0.003f;\n",
            "    float readability=0, grain=0.003f;\n"
            "    // Per-job override used for glass-over-glass composition.\n"
            "    bool forceCurrentFramebuffer=false;\n",
            "GlassParams per-job backdrop override")
        return s
    edit("jni/liquid_glass/ytbl.h", patch_h)

    def patch_cpp(s: str) -> str:
        s = replace_once(s,
            "    Job job;job.count=count;job.material=material;job.options=s.options;job.density=s.density;job.light=s.light;\n",
            "    Job job;job.count=count;job.material=material;job.options=s.options;job.density=s.density;job.light=s.light;\n"
            "    if(material.forceCurrentFramebuffer)job.options.backdrop=BackdropMode::CurrentFramebuffer;\n",
            "per-job backdrop selection")
        anchor = "    p.grain=0.0004f;\n    return p;\n"
        replacement = (
            "    p.grain=0.0004f;\n"
            "    if(kind==Material::KernelSU){\n"
            "        // Independent C++ reimplementation of the public visual recipe.\n"
            "        p.effects.SetBlurRadiusPx(Dp(4.0f))\n"
            "            .SetLens(Dp(24.0f),Dp(24.0f),true,true)\n"
            "            .SetChromaticAberration(0.12f)\n"
            "            .SetColorControls(0.0f,1.0f,1.50f);\n"
            "        p.surfaceColor=s.light?ImVec4(1.0f,1.0f,1.0f,0.055f):ImVec4(0.08f,0.11f,0.17f,0.075f);\n"
            "        p.highlight=Highlight(1.05f,0.30f,1.0f,\n"
            "            HighlightStyle::Default((int)0x70FFFFFFu,GlassBlendMode::PLUS,72.0f,1.15f));\n"
            "        p.shadow=Shadow(16,0,4,(int)0x16000000u);\n"
            "        p.readability=0.0f;\n"
            "        p.grain=0.00025f;\n"
            "        p.backdropScaleX=1.012f;p.backdropScaleY=1.012f;p.backdropMix=0.10f;\n"
            "    }\n"
            "    return p;\n"
        )
        s = replace_once(s, anchor, replacement, "KernelSU material preset")
        return s
    edit("jni/liquid_glass/ytbl.cpp", patch_cpp)

    def patch_widgets(s: str) -> str:
        old = """    auto container=MakeMaterial(Material::Clear);container.shape=GlassShape();container.surfaceColor=ImVec4(
        ((containerColor>>16)&255)/255.f,((containerColor>>8)&255)/255.f,(containerColor&255)/255.f,((static_cast<unsigned>(containerColor)>>24)&255)/255.f);
    container.hasShadow=false;container.ihProgress=interactive.GetPressProgress()*pressHighlightIntensity;
    container.ihX=interactive.GetPointerX();container.ihY=interactive.GetPointerY();
    container.ihBaseAlpha=interactive.baseAlpha_;container.ihSpotAlpha=interactive.spotAlpha_;container.ihRadiusMultiplier=interactive.radiusMultiplier_;
    DrawGlass(rect,container);
    ImRect indicator=RectAt(ImVec2(pos.x+pad+Clampf(animation.GetValue(),0,(float)count-1)*tabW,pos.y+pad),ImVec2(tabW,size.y-pad*2));
    indicator=ScaleRect(indicator,animation.GetScaleX(),animation.GetScaleY());
    auto thumb=Thumb(animation.GetPressProgress());thumb.hasShadow=false;thumb.surfaceColor=IsLightTheme()?ImVec4(1,1,1,.34f):ImVec4(.92f,.95f,1.0f,.18f);DrawGlass(indicator,thumb);
"""
        new = """    const float press=Clamp01(animation.GetPressProgress());
    auto container=MakeMaterial(Material::KernelSU);container.shape=GlassShape();
    container.surfaceColor=ImVec4(
        ((containerColor>>16)&255)/255.f,((containerColor>>8)&255)/255.f,(containerColor&255)/255.f,
        std::min(((static_cast<unsigned>(containerColor)>>24)&255)/255.f,0.10f));
    container.hasShadow=true;
    container.ihProgress=interactive.GetPressProgress()*pressHighlightIntensity;
    container.ihX=interactive.GetPointerX();container.ihY=interactive.GetPointerY();
    container.ihBaseAlpha=interactive.baseAlpha_;container.ihSpotAlpha=interactive.spotAlpha_;
    container.ihRadiusMultiplier=interactive.radiusMultiplier_;
    DrawGlass(rect,container);

    ImRect indicator=RectAt(
        ImVec2(pos.x+pad+Clampf(animation.GetValue(),0,(float)count-1)*tabW,pos.y+pad),
        ImVec2(tabW,size.y-pad*2));
    const float pressScale=Lerpf(1.0f,78.0f/56.0f,press);
    indicator=ScaleRect(indicator,animation.GetScaleX()*pressScale,
                                  animation.GetScaleY()*Lerpf(1.0f,1.08f,press));

    // Glass-over-glass: capture after base bar, before tab text.
    auto thumb=MakeMaterial(Material::KernelSU);
    thumb.forceCurrentFramebuffer=true;
    thumb.hasShadow=false;
    thumb.effects.SetBlurRadiusPx(Dp(Lerpf(3.2f,1.0f,press)))
        .SetLens(Dp(Lerpf(8.0f,10.0f,press)),Dp(Lerpf(6.0f,14.0f,press)),true,true)
        .SetChromaticAberration(Lerpf(0.10f,0.50f,press))
        .SetColorControls(0.0f,1.0f,1.50f);
    thumb.surfaceColor=IsLightTheme()?ImVec4(1,1,1,Lerpf(.22f,.08f,press))
                                     :ImVec4(.90f,.95f,1.0f,Lerpf(.14f,.07f,press));
    thumb.hasInnerShadow=press>0.001f;
    thumb.innerShadow=InnerShadow(8.0f*press,0.0f,2.0f*press,(int)0x26000000u,1.0f);
    thumb.ihProgress=press*pressHighlightIntensity;
    thumb.ihX=interactive.GetPointerX();thumb.ihY=interactive.GetPointerY();
    thumb.ihBaseAlpha=interactive.baseAlpha_;thumb.ihSpotAlpha=interactive.spotAlpha_;
    thumb.ihRadiusMultiplier=interactive.radiusMultiplier_;
    DrawGlass(indicator,thumb);
"""
        return replace_once(s, old, new, "bottom tabs glass-over-glass block")
    edit("jni/liquid_glass/ytbl_widgets.cpp", patch_widgets)

    def patch_surface(s: str) -> str:
        s = replace_once(s, "int materialIndex = 0;", "int materialIndex = 3;", "default material")
        s = replace_once(s,
            '            "材质", &materialIndex, "Clear\\0Regular\\0Reading\\0"\n',
            '            "材质", &materialIndex, "Clear\\0Regular\\0Reading\\0KernelSU\\0"\n',
            "material combo")
        s = replace_once(s, "float lens = 15.5f;", "float lens = 24.0f;", "default lens")
        s = replace_once(s, "float blur = 2.8f;", "float blur = 4.0f;", "default blur")
        s = replace_once(s, "float chroma = 0.085f;", "float chroma = 0.12f;", "default chroma")
        return s
    edit("jni/src/Android_draw/SurfaceGlass.cpp", patch_surface)

    (project / "README_KERNELSU_V34.md").write_text(
"""# v3.4 KernelSU-style Liquid Glass port

Independent C++/GLES implementation inspired by public visual behavior and
parameters. No KernelSU GPL source code is copied or line-by-line translated.

Changes:
- Material::KernelSU
- 4dp blur, 24/24 lens, 1.5x saturation
- glass-over-glass selected bottom-tab capsule
- press scale toward 78/56
- press-dependent lens, chromatic aberration and inner shadow
- retains v3.3 real-screen backdrop, excludeLayers, touch policy and iOS26 tuning
""", encoding="utf-8")
    changed.append("README_KERNELSU_V34.md")
    return changed

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("-o","--output",type=Path,default=Path("Surface_RealBackdrop_v3_4_KernelSUGlass.zip"))
    args=ap.parse_args()
    src=args.source.resolve(strict=True); out=args.output.resolve()
    if out.exists(): raise RuntimeError(f"refusing to overwrite {out}")
    with tempfile.TemporaryDirectory(prefix="kernelsu-v34-") as td:
        td=Path(td); safe_extract(src,td/"input"); project=locate(td/"input")
        staged=td/"Surface_RealBackdrop_v3_4_KernelSUGlass"
        shutil.copytree(project,staged)
        changed=patch(staged)
        manifest={
          "patch":"KernelSU-style liquid glass v3.4",
          "source":src.name,
          "source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
          "changed_files":changed,
          "ndk_build":"not_run_by_patch_tool",
          "android_runtime":"not_run_by_patch_tool"
        }
        (staged/"KERNELSU_V34_PATCH.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for p in sorted(staged.rglob("*")):
                if p.is_file(): z.write(p,staged.name+"/"+str(p.relative_to(staged)))
    with zipfile.ZipFile(out) as z:
        bad=z.testzip()
        if bad: raise RuntimeError("output ZIP failed at "+bad)
    print(out)
    print(hashlib.sha256(out.read_bytes()).hexdigest())

if __name__=="__main__":
    main()
