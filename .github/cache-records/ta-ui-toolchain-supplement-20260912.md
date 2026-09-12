## Android Build Tools 34.0.0

- Artifact Name: `android-build-tools-34.0.0-linux-x86_64`
- Artifact ID: `10298993889`
- Run ID: `34698130020`
- Workflow: `.github/workflows/cache-android-build-tools-34.yml`
- File: `android-build-tools-34.0.0-linux-x86_64.tar.zst`
- Size: `46918112` bytes
- SHA256: `b7e90503116a794e9c2a7a4076510f77d05745545a6c7d45e0cc10686b634be9` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T14:03:42Z`
- Expires At: `2026-12-11T14:02:53Z`
- Storage Mode: `SINGLE`
- Original File: `android-build-tools-34.0.0-linux-x86_64.tar.zst`
- Original Size: `46917333` bytes
- Original SHA256: `a87fb4da3df6d95eaa9f21b34fffb640ff7bbc5fdedb8dbc5e4ea9f749fcca2a`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android SDK Build-Tools | 34.0.0 | Linux | x86_64 | `build-tools/34.0.0` | `176da6c5eb438ebc9dcbfe078f4a02d352e39c37e43d3f65f0b29c67b15747e8` |

Directory entry SHA256 is a deterministic hash over sorted relative file hashes. The outer archive and original `.tar.zst` hashes are the authoritative restore checks.

### Restore

Download Artifact `10298993889`, verify the Artifact ZIP SHA256 `b7e90503116a794e9c2a7a4076510f77d05745545a6c7d45e0cc10686b634be9`, verify original SHA256 `a87fb4da3df6d95eaa9f21b34fffb640ff7bbc5fdedb8dbc5e4ea9f749fcca2a`, then extract into the same `ANDROID_SDK_ROOT` used by the API 35 bundle.

## TrustAttestor UI Kotlin compile dependency cache v2

- Artifact Name: `gradle-modules2-ta-ui-kotlincompile-linux-x86_64`
- Artifact ID: `10299541605`
- Run ID: `34698303924`
- Workflow: `.github/workflows/cache-ta-ui-kotlin-deps.yml`
- File: `gradle-modules2-ta-ui-kotlincompile-linux-x86_64.tar.zst`
- Size: `175412705` bytes
- SHA256: `8f93454a0b7ea4bad9993ff46aca7b91bd86deb8cbe141df631b310ea69e9b6b` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T14:07:27Z`
- Expires At: `2026-12-11T14:06:23Z`
- Storage Mode: `SINGLE`
- Original File: `gradle-modules2-ta-ui-kotlincompile-linux-x86_64.tar.zst`
- Original Size: `175412114` bytes
- Original SHA256: `05ad98f032233604c106b0d8dec061160d09a9ab212b8831abc9377728bd563c`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| TrustAttestor UI Gradle modules cache | AGP 8.7.2 + Kotlin 2.0.21 + exact UI dependencies + real Kotlin compile | Linux | x86_64 | `caches/modules-2` | `05ad98f032233604c106b0d8dec061160d09a9ab212b8831abc9377728bd563c` |
| Kotlin Build Tools implementation | 2.0.21 | Any | JVM | `org.jetbrains.kotlin/kotlin-build-tools-impl/2.0.21` | included in archive `05ad98f032233604c106b0d8dec061160d09a9ab212b8831abc9377728bd563c` |

This supersedes the v1 dependency cache for Kotlin source compilation. It was warmed by compiling an actual `.kt` source file with Kotlin 2.0.21, and contains `kotlin-build-tools-impl-2.0.21.jar`.
