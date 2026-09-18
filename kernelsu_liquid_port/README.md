# KernelSU-style Liquid Glass port kit

This kit targets the **generated Surface_RealBackdrop_v3_3_iOS26Style_Source.zip** from this conversation.

It does not copy KernelSU Kotlin source into the C++ project. KernelSU is GPL-3.0, while its ui/component/liquid files explicitly credit Kyant0/AndroidLiquidGlass and the compose-miuix-ui example. Those upstream libraries are Apache-2.0. The patch independently reimplements the visual recipe in the existing Ytbl C++/GLES renderer.

## What is ported

KernelSU's current FloatingBottomBar.kt uses approximately:

- base bar: vibrancy / saturation 1.5x
- blur: 4 dp
- lens edge band: 24 dp
- refraction amount: 24 dp
- pill: spring pressed scale 78/56
- pill while pressed: lens 10×progress, refraction 14×progress, depth effect
- pill chromatic aberration: 0.5×progress
- pill inner shadow: radius 8×progress, black ~0.15
- specular highlight bound to press progress
- glass-over-glass composition via a combined backdrop

The C++ adaptation adds a KernelSU material preset and a per-job backdrop override so the selected pill can sample the already rendered base glass from the current framebuffer. This is the closest equivalent to KernelSU's combined layer backdrop within the existing Ytbl renderer.

Device-tilt-driven dual-peak highlights are not copied in this patch; the existing Ytbl single-direction highlight is used as a stable approximation. A future native-sensor pass can add accelerometer-driven highlight rotation without changing the material API.

## Apply

Put this kit next to your v3.3 source ZIP and run:

    python3 apply.py Surface_RealBackdrop_v3_3_iOS26Style_Source.zip -o Surface_RealBackdrop_v3_4_KernelSUGlass.zip

Then extract the generated project and build it with your usual NDK command.

The patcher is fail-closed: if the expected v3.3 source blocks do not match, it stops instead of silently applying a partial port.

## License note

- KernelSU repository: GPL-3.0
- Kyant0/AndroidLiquidGlass: Apache-2.0
- compose-miuix-ui/miuix: Apache-2.0

If you later directly copy source code from KernelSU rather than independently reimplementing the effect or using the Apache-2.0 upstreams, review GPL-3.0 obligations for the combined work.
