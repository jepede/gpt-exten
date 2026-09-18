#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, stat, tempfile, zipfile
from pathlib import Path, PurePosixPath

def safe_extract(src: Path, dst: Path):
    with zipfile.ZipFile(src) as z:
        total=0
        for i in z.infolist():
            p=PurePosixPath(i.filename); total+=i.file_size
            if p.is_absolute() or ".." in p.parts or "\\" in i.filename or stat.S_ISLNK(i.external_attr>>16):
                raise ValueError("unsafe ZIP member: "+i.filename)
            if total>512*1024*1024: raise ValueError("archive too large")
        z.extractall(dst)

def locate(root: Path)->Path:
    matches=[p.parent.parent for p in root.rglob("jni/Android.mk")]
    if len(matches)!=1: raise ValueError(f"expected one project, found {len(matches)}")
    return matches[0]

def replace_once(text, old, new, label):
    n=text.count(old)
    if n!=1: raise ValueError(f"{label}: expected one anchor, found {n}")
    return text.replace(old,new,1)

def span(text: str, signature: str):
    starts=[m.start() for m in re.finditer(re.escape(signature),text)]
    if len(starts)!=1: raise ValueError("missing/ambiguous "+signature)
    start=starts[0]; brace=text.index("{",start); level=0; quote=None; line=False; block=False; i=brace
    while i<len(text):
        c=text[i]; two=text[i:i+2]
        if line:
            if c=="\n": line=False
        elif block:
            if two=="*/": block=False; i+=1
        elif quote:
            if c=="\\": i+=1
            elif c==quote: quote=None
        elif two=="//": line=True; i+=1
        elif two=="/*": block=True; i+=1
        elif c in ("'",'"'): quote=c
        elif c=="{": level+=1
        elif c=="}":
            level-=1
            if level==0:return start,i+1
        i+=1
    raise ValueError("unterminated "+signature)

def patch(root: Path):
    changed=[]
    def edit(rel, fn):
        p=root/rel; old=p.read_text(encoding="utf-8-sig"); new=fn(old)
        if new==old: raise ValueError("no change for "+rel)
        p.write_text(new,encoding="utf-8"); changed.append(rel)

    def h(text):
        text=replace_once(text,
            "enum class Material { Clear, Regular, Reading };",
            "enum class Material { Clear, Regular, Reading, KernelSU };",
            "Material enum")
        text=replace_once(text,
            "bool useBackdrop=true, opaqueBackdrop=false;\n",
            "bool useBackdrop=true, opaqueBackdrop=false;\n"
            "    // Per-job source selection: used by the selected liquid pill to sample the\n"
            "    // already-rendered glass container, approximating KernelSU's CombinedBackdrop.\n"
            "    bool hasBackdropModeOverride=false;\n"
            "    BackdropMode backdropModeOverride=BackdropMode::CurrentFramebuffer;\n",
            "per-job backdrop override")
        text=replace_once(text,
            "DampedDragAnimation animation{0,0,3,0.001f,1,1.06f};",
            "DampedDragAnimation animation{0,0,3,0.001f,1,78.0f/56.0f};",
            "KernelSU pressed indicator scale")
        return text
    edit("jni/liquid_glass/ytbl.h",h)

    def cpp(text):
        anchor="Job job;job.count=count;job.material=material;job.options=s.options;job.density=s.density;job.light=s.light;"
        text=replace_once(text,anchor,anchor+"\n    if(material.hasBackdropModeOverride)job.options.backdrop=material.backdropModeOverride;","job override")
        a,b=span(text,"GlassParams MakeMaterial(Material kind)")
        body=r'''GlassParams MakeMaterial(Material kind){
    GlassParams p;
    p.shape=GlassShape(Dp(24));
    p.effects.SetVibrancyEnabled(true);
    if(kind==Material::KernelSU){
        // Reimplementation of the visual recipe used by KernelSU's floating bar.
        // The implementation is written against this C++ renderer; no KernelSU GPL
        // source is copied here. See KERNELSU_LIQUID_PORT_NOTICE.md.
        p.effects
            .SetBlurRadiusPx(Dp(4.0f))
            .SetLens(Dp(24.0f),Dp(24.0f),false,false)
            .SetChromaticAberration(0.0f)
            .SetColorControls(0.0f,1.0f,1.5f);
        p.surfaceColor=s.light?ImVec4(0.96f,0.97f,0.99f,0.40f):ImVec4(0.10f,0.11f,0.14f,0.40f);
        p.tintMode=2;
        p.backdropFallback=FrostedBackdrop();
        p.hasShadow=true;
        p.shadow=Shadow(10.0f,0.0f,3.0f,s.light?(int)0x19000000u:(int)0x33000000u);
        p.highlight=Highlight(1.0f,2.0f,0.75f,
            HighlightStyle::Default((int)0x1FFFFFFFu,GlassBlendMode::PLUS,72.0f,1.2f));
        p.readability=0.0f;
        p.grain=0.00025f;
        return p;
    }
    float blur=kind==Material::Clear?2.2f:kind==Material::Regular?4.6f:10.0f;
    float lens=kind==Material::Reading?8.0f:(kind==Material::Regular?15.0f:13.5f);
    float chroma=kind==Material::Reading?0.05f:0.09f;
    p.effects
        .SetBlurRadiusPx(Dp(blur))
        .SetLens(Dp(16),Dp(lens),true,true)
        .SetChromaticAberration(chroma)
        .SetColorControls(0.008f,1.025f,1.08f);
    p.surfaceColor=s.light
        ? ImVec4(1.0f,1.0f,1.0f,kind==Material::Clear?0.045f:(kind==Material::Regular?0.072f:0.115f))
        : ImVec4(0.10f,0.13f,0.19f,kind==Material::Clear?0.055f:(kind==Material::Regular?0.095f:0.16f));
    p.tintMode=2;
    p.backdropFallback=FrostedBackdrop();
    p.backdropScaleX=1.015f;
    p.backdropScaleY=1.015f;
    p.backdropMix=0.12f;
    p.hasShadow=true;
    p.shadow=Shadow(18,0,4,(int)0x18000000u);
    p.highlight=Highlight(1.0f,0.3f,1.0f,HighlightStyle::Default((int)0x68FFFFFFu,GlassBlendMode::PLUS,72.0f,1.2f));
    p.readability=kind==Material::Reading?0.18f:0;
    p.grain=0.0004f;
    return p;
}'''
        return text[:a]+body+text[b:]
    edit("jni/liquid_glass/ytbl.cpp",cpp)

    def widgets(text):
        text=replace_once(text,
            "auto container=MakeMaterial(Material::Clear);container.shape=GlassShape();container.surfaceColor=ImVec4(",
            "auto container=MakeMaterial(Material::KernelSU);container.shape=GlassShape();container.surfaceColor=ImVec4(",
            "bottom-tabs container")
        old="auto thumb=Thumb(animation.GetPressProgress());thumb.hasShadow=false;thumb.surfaceColor=IsLightTheme()?ImVec4(1,1,1,.34f):ImVec4(.92f,.95f,1.0f,.18f);DrawGlass(indicator,thumb);"
        new=r'''float ksuPress=animation.GetPressProgress();
    auto thumb=MakeMaterial(Material::Clear);
    thumb.shape=GlassShape();
    // KernelSU combines the original backdrop with a layer backdrop. In this renderer,
    // CurrentFramebuffer at this point already contains the base glass, so the pill
    // optically samples "glass over glass" without a second persistent scene texture.
    thumb.hasBackdropModeOverride=true;
    thumb.backdropModeOverride=BackdropMode::CurrentFramebuffer;
    thumb.effects.SetBlurRadiusPx(0.0f);
    thumb.effects.SetLens(Dp(10.0f)*ksuPress,Dp(14.0f)*ksuPress,true,ksuPress>0.001f);
    thumb.effects.SetChromaticAberration(0.5f*ksuPress);
    thumb.hasShadow=false;
    thumb.hasHighlight=ksuPress>0.001f;
    thumb.highlight=Highlight(1.0f,2.0f,ksuPress,
        HighlightStyle::Default((int)0x1FFFFFFFu,GlassBlendMode::PLUS,162.0f,1.2f));
    thumb.hasInnerShadow=ksuPress>0.001f;
    thumb.innerShadow=InnerShadow(8.0f*ksuPress,0.0f,0.0f,(int)0x26000000u,ksuPress);
    if(IsLightTheme()){
        float a=Lerpf(0.10f,0.03f,ksuPress);
        thumb.surfaceColor=ImVec4(0,0,0,a);
    }else{
        thumb.surfaceColor=ImVec4(1,1,1,0.10f*(1.0f-ksuPress));
    }
    thumb.grain=0.0f;
    DrawGlass(indicator,thumb);'''
        text=replace_once(text,old,new,"selected liquid pill")
        return text
    edit("jni/liquid_glass/ytbl_widgets.cpp",widgets)

    def surface(text):
        text=replace_once(text,"int materialIndex = 0;","int materialIndex = 3;","default KernelSU preset")
        text=replace_once(text,
            '"材质", &materialIndex, "Clear\\0Regular\\0Reading\\0"',
            '"材质", &materialIndex, "Clear\\0Regular\\0Reading\\0KernelSU Glass\\0"',
            "preset combo")
        # Keep the v3.3 custom sliders for the first three presets; KernelSU gets its own recipe.
        old=r'''    material.shape = ytbl::GlassShape(28.0f);
    material.effects
        .SetLens(20.0f, lens, true, chroma > 0.001f)
        .SetBlurRadiusPx(blur)
        .SetChromaticAberration(chroma)
        .SetColorControls(0.008f, 1.03f, 1.08f);
    material.readability = windowReadability;
    material.grain = 0.00045f;
    material.backdropScaleX = 1.018f;
    material.backdropScaleY = 1.018f;
    material.backdropMix = 0.14f;
    material.surfaceColor = ytbl::IsLightTheme()
        ? ImVec4(1.0f, 1.0f, 1.0f, windowTint)
        : ImVec4(0.12f, 0.16f, 0.24f, std::min(windowTint + 0.01f, 0.06f));
    material.highlight = ytbl::Highlight(1.15f, 0.35f, 1.0f,
        ytbl::HighlightStyle::Default((int)0x6EFFFFFFu, ytbl::GlassBlendMode::PLUS, 72.0f, 1.2f));
    material.hasShadow = true;
    material.shadow = ytbl::Shadow(18.0f, 0.0f, 5.0f, (int)0x18000000u);
    material.backdropFallback.w = 0.06f; // avoid a thick opaque plate if live capture is unavailable'''
        new=r'''    material.shape = ytbl::GlassShape(28.0f);
    if(materialIndex==3){
        // Generic KernelSU floating-glass preset. The bottom-tab component has a
        // more exact pressed-pill recipe below in ytbl_widgets.cpp.
        material.effects
            .SetLens(24.0f,24.0f,false,false)
            .SetBlurRadiusPx(4.0f)
            .SetChromaticAberration(0.0f)
            .SetColorControls(0.0f,1.0f,1.5f);
        material.readability=0.0f;
        material.grain=0.00025f;
        material.surfaceColor=ytbl::IsLightTheme()
            ? ImVec4(0.96f,0.97f,0.99f,0.28f)
            : ImVec4(0.10f,0.11f,0.14f,0.34f);
        material.highlight=ytbl::Highlight(1.0f,2.0f,0.75f,
            ytbl::HighlightStyle::Default((int)0x1FFFFFFFu,ytbl::GlassBlendMode::PLUS,72.0f,1.2f));
        material.hasShadow=true;
        material.shadow=ytbl::Shadow(10.0f,0.0f,3.0f,
            ytbl::IsLightTheme()?(int)0x19000000u:(int)0x33000000u);
        material.backdropFallback.w=0.06f;
    }else{
        material.effects
            .SetLens(20.0f, lens, true, chroma > 0.001f)
            .SetBlurRadiusPx(blur)
            .SetChromaticAberration(chroma)
            .SetColorControls(0.008f, 1.03f, 1.08f);
        material.readability = windowReadability;
        material.grain = 0.00045f;
        material.backdropScaleX = 1.018f;
        material.backdropScaleY = 1.018f;
        material.backdropMix = 0.14f;
        material.surfaceColor = ytbl::IsLightTheme()
            ? ImVec4(1.0f, 1.0f, 1.0f, windowTint)
            : ImVec4(0.12f, 0.16f, 0.24f, std::min(windowTint + 0.01f, 0.06f));
        material.highlight = ytbl::Highlight(1.15f, 0.35f, 1.0f,
            ytbl::HighlightStyle::Default((int)0x6EFFFFFFu, ytbl::GlassBlendMode::PLUS, 72.0f, 1.2f));
        material.hasShadow = true;
        material.shadow = ytbl::Shadow(18.0f, 0.0f, 5.0f, (int)0x18000000u);
        material.backdropFallback.w = 0.06f;
    }'''
        text=replace_once(text,old,new,"main material block")
        note='''        if(materialIndex==3)
            ImGui::TextWrapped("KernelSU Glass：4dp 模糊 + 24/24 边缘透镜 + 1.5x vibrancy；底栏选中胶囊使用 glass-over-glass 与按压色散。");
'''
        marker='''        ImGui::SliderFloat("文字可读性遮罩", &windowReadability, 0.0f, 0.5f);
'''
        text=replace_once(text,marker,marker+note,"settings note")
        return text
    edit("jni/src/Android_draw/SurfaceGlass.cpp",surface)

    notice=root/"KERNELSU_LIQUID_PORT_NOTICE.md"
    notice.write_text("""# KernelSU-style Liquid Glass port notice

This patch uses KernelSU's current manager UI as a visual/behavior reference only.

KernelSU's repository is GPL-3.0. To avoid copying GPL-covered manager source into
this C++ project, the C++ implementation in this patch was written against the
project's existing renderer and the underlying permissive references named by
KernelSU's own source comments:

- Kyant0/AndroidLiquidGlass — Apache-2.0
- compose-miuix-ui/miuix — Apache-2.0

Visual recipe mirrored independently:
- base glass: saturation/vibrancy, light blur, rounded-edge lens
- selected pill: press-dependent lens, depth effect, chromatic dispersion
- spring scale / velocity deformation
- inner shadow and specular highlight
- glass-over-glass backdrop sampling

KernelSU-specific Kotlin source is not copied verbatim. Preserve the licenses and
notices of any upstream Apache-2.0 code you directly incorporate later.
""",encoding="utf-8")
    changed.append("KERNELSU_LIQUID_PORT_NOTICE.md")
    return changed

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source",type=Path)
    ap.add_argument("-o","--output",type=Path,default=Path("Surface_RealBackdrop_v3_4_KernelSUGlass.zip"))
    args=ap.parse_args()
    src=args.source.resolve(strict=True); out=args.output.resolve()
    if out.exists(): raise ValueError("refusing to overwrite output")
    with tempfile.TemporaryDirectory(prefix="ksu-liquid-port-",dir=out.parent) as td:
        td=Path(td); safe_extract(src,td/"input"); project=locate(td/"input")
        staged=td/"Surface_RealBackdrop_v3_4_KernelSUGlass"
        shutil.copytree(project,staged,ignore=shutil.ignore_patterns("obj","libs","dist","__pycache__"))
        changed=patch(staged)
        manifest={"version":"v3.4-kernelsu-glass-port","base":src.name,
                  "base_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
                  "changed":changed,"full_ndk_build":"not_run","android_runtime":"not_run"}
        (staged/"KERNELSU_LIQUID_PORT.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for p in sorted(staged.rglob("*")):
                if p.is_file(): z.write(p,Path(staged.name)/p.relative_to(staged))
    with zipfile.ZipFile(out) as z:
        bad=z.testzip()
        if bad: raise ValueError("output ZIP failed at "+bad)
    print(out)
    print(hashlib.sha256(out.read_bytes()).hexdigest())

if __name__=="__main__":
    try: main()
    except (ValueError,OSError,zipfile.BadZipFile) as e:
        raise SystemExit("ERROR: "+str(e))
