# KernelSU Liquid Glass Port Kit v3.4

用于 Surface_RealBackdrop_v3_3_iOS26Style_Source.zip。

执行：

python3 apply.py Surface_RealBackdrop_v3_3_iOS26Style_Source.zip -o Surface_RealBackdrop_v3_4_KernelSUGlass.zip

生成的是已合并补丁的完整源码 ZIP。之后解压并运行工程原有 build_real_backdrop.sh。

移植内容：新增 KernelSU 材质、4dp blur、24/24 lens、1.5x saturation、底栏选中胶囊 glass-over-glass 二次折射、78/56 按压缩放、动态色散与内阴影；保留 v3.3 的真实屏幕背景、excludeLayers、触摸策略与 iOS26 调参。
