# KernelSU Liquid Glass PortKit v3.4

目标输入：

`Surface_RealBackdrop_v3_3_iOS26Style_Source.zip`

使用：

```sh
python3 apply.py Surface_RealBackdrop_v3_3_iOS26Style_Source.zip \
  -o Surface_RealBackdrop_v3_4_KernelSUGlass.zip
```

该补丁是针对现有 C++/ImGui/Ytbl 渲染器的 clean-room 重实现，不复制 KernelSU 的 Kotlin/Compose 源码。

主要改动：

- 新增 `Material::KernelSU`
- 约 4dp 模糊、24px 级透镜、1.5x 饱和度
- 底栏选中胶囊使用 glass-over-glass：底栏先采真实背景，胶囊再采当前 framebuffer
- 按压缩放约 `78/56`
- 按压动态 `10/14` lens、最高 0.5 色散、内阴影
- 在材质下拉框中加入 KernelSU 预设

注意：补丁本身只负责合并源码和生成新 ZIP，不会自动执行 NDK 编译或手机实测。
