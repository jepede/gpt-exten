# Artifact Cache

GitHub Actions 可复用 Artifact 索引。下载资源前优先按 `Name + Version + Platform + Architecture` 查询；是否仍可用以 GitHub 实际返回的 `expires_at` 为准。

## Index
| Honor of Kings IL2CPP coordinate native kit | 12.1.1.1 | Android | arm64-v8a | `40311637215` | SINGLE × 4 | `2027-01-24T10:59:21Z` |
| OSS NDK r28c pinned source snapshot | cJSON 1.7.19 + zlib 1.3.1 + xxHash 0.8.3 | GitHub source / Any | Portable C source | `40162823267` | SINGLE | `2027-01-23T04:41:50Z` |
| OSS Android ARM64 NDK r28c cJSON+zlib+xxHash | cJSON 1.7.19 + zlib 1.3.1 + xxHash 0.8.3 | Android API35 / Linux | arm64-v8a target, x86_64 host | `40162461240` | SINGLE | `2027-01-23T04:35:49Z` |
| Android NDK minimal Clang/LLD | r28c-minimal-v1 | Linux | x86_64 host + AArch64 target | 39121838147 | SPLIT × 2 (95 MB) | 2027-01-16T11:05:31Z |
| Mozilla NSS TLS Root Store | release-b9bd270cfa3e-20261005 | Any | Any | `37253767754` | SINGLE | `2027-01-03T02:02:10Z` |

| Name | Version | Platform | Architecture | Run ID | Storage | Expires At |
|---|---|---|---|---:|---|---|
| Android 36 ARM64 graphics/framework sysroot | android36-r02-graphics-20261017 | Android API36 | AArch64 | 39007458676 | SINGLE | 2027-01-15T05:45:59Z |
| Android 36 ARM64 i18n ICU APEX | android36-r02-i18n-20261017 | Android API36 APEX | AArch64 | 39007941479 | SINGLE | 2027-01-15T05:54:10Z |
| QEMU TCG Plugins: execlog/hotblocks/vmptrace | v10.0.13-plugin-api4-20261017 | Ubuntu 24.04 / Linux (QEMU Debian 13) | x86_64 host, AArch64 guest | `39003891690` | SINGLE | `2027-01-15T04:47:37Z` |
| Android Emulator (Ranchu/GLES) | 37.2.12.0 | Linux | x86_64 | `39122587987` | SPLIT × 4 | 2027-01-16T11:16:44Z |
| Android Platform-Tools ADB cached subset | 37.0.1 | Linux | x86_64 | `39123346053` | SINGLE | 2027-01-16T11:28:02Z |
| AOSP API36 full ARM64 SDK image (~95 MB partitions) | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `39119724365` | SPLIT × 9 | 2027-01-16T10:33:28Z |
| AOSP API36 full ARM64 SDK image | 36_r02-full-v1 | Android 16 / API36 | AArch64 | `39003325276` | SPLIT × 3 | `2027-01-15T04:38:31Z` |
| AOSP API35 full ARM64 SDK image | 35_r02-full-v1 | Android 15 / API35 | AArch64 | `39002974865` | SPLIT × 2 | `2027-01-15T04:32:52Z` |
| QEMU AArch64 User Static | 1:10.0.13+ds-0+deb13u1 | Debian 13 / Linux | x86_64 host + AArch64 guest | `39001231108` | SINGLE | `2027-01-15T04:05:09Z` |
| PRoot runtime bundle | 5.1.0-1.3 | Debian 12 / Linux | x86_64 | `38999498688` | SINGLE | `2027-01-15T03:37:28Z` |
| ARM64 NDK C debugging validation | r28c-run38642113778 | Ubuntu 24.04 Linux / Android Bionic API 36 | x86_64 host + AArch64 guest | `38642113778` | SINGLE | `2027-01-12T21:40:57Z` |
| Delta Force CN Android APK | 1.201.37117.67 | Android | arm64-v8a | `38596903200` | SPLIT × 4 | `2027-01-12T16:18:07Z` |
| PUBG CTF GL APK | 4.6.0-v1.0.1 | Android | arm64-v8a | `38431125316` | SINGLE | `2027-01-11T16:30:53Z` |
| Google Android Key Attestation trust reference | 2026-10-13 | Any | Any | `38354591700` | SINGLE | `2027-01-11T06:03:07Z` |
| UPX KeyGuard Android ARM64 QEMU E2E build | v1.1-testonly-20261013 | Android/Bionic API28+ | arm64-v8a | `38335627167` | SINGLE | `2027-01-11T02:10:30Z` |
| UPX KeyGuard Android ARM64 | 5.2.1-keyguard-arm64-demo-20261013 | Android / Bionic API 28+ | arm64-v8a | `38334950099` | SINGLE | `2027-01-11T02:01:54Z` |
| UPX KeyGuard ARM64 Linux | v5.2.1-keyguard-v1-20261013 | Linux | AArch64 | `38333914943` | SINGLE | `2027-01-11T01:48:51Z` |
| UPX KeyGuard | v5.2.1-keyguard-v1-20261013 | Linux | x86_64 | `38333114942` | SINGLE | `2027-01-11T01:38:45Z` |
| TinyHTTPS OpenSSL + curl reference sources | OpenSSL 4.0.3 + curl 8.22.0 | Any | Any | `37458536791` | SINGLE | `2027-01-04T11:45:33Z` |
| PUBG MOBILE Global Base APK | 4.6.0 (21525) | Android | arm64-v8a | `37217716536` | SINGLE | `2027-01-02T16:41:47Z` |
| radare2 | 6.2.2 | Linux / Debian | x86_64 | `36873712969` | SINGLE | `2026-12-30T14:06:12Z` |
| r2ghidra | 6.2.2 | Debian / Linux | x86_64 | `38850726295` | SINGLE | `2027-01-14T04:27:37Z` |
| TrustAttestor UI Gradle dependency cache | agp8.7.2-kotlin2.0.21-ui-releasecomplete-v3 | Linux | x86_64 | `34698530131` | SINGLE | `2026-12-11T14:10:58Z` |
| Android SDK Build-Tools | 34.0.0 | Linux | x86_64 | `34698130020` | SINGLE | `2026-12-11T14:02:53Z` |
| TrustAttestor UI Gradle dependency cache | agp8.7.2-kotlin2.0.21-ui-kotlincompile-v2 | Linux | x86_64 | `34698303924` | SINGLE | `2026-12-11T14:06:23Z` |
| Android SDK compile bundle | api35-bt35.0.0-clt12.0-pt37.0.1-v1 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| Temurin JDK | 17.0.20.1+1 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| Gradle | 8.10.2 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| TrustAttestor UI Gradle dependency cache | agp8.7.2-kotlin2.0.21-ui-deps-v1 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| Android NDK | r28c | Linux | x86_64 | `39019800471` | SPLIT × 5 | `2027-01-15T09:05:25Z` |
| USDA FoodData Central Foundation Foods CSV | 2026-04-30 | Any | Any | `31695314247` | SINGLE | `2026-11-11T11:23:52Z` |
| USDA FoodData Central SR Legacy CSV | 2018-04 | Any | Any | `31695560856` | SINGLE | `2026-11-11T11:27:10Z` |
| CulinaryDB CSV bundle | 2018-03-15 | Any | Any | `31723890750` | SINGLE | `2026-11-11T17:04:36Z` |
| cquant Binance Spot 15m Klines | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `32575307131` | SINGLE | `2026-11-20T13:16:44Z` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `32617341667` | SINGLE | `2026-11-21T04:13:42Z` |
| cquant Binance Spot 15m Golden Holdout | 2025-01-01_2026-08-21-15m-golden-holdout-v1 | Any | Any | `32618059050` | SINGLE | `2026-11-21T04:30:49Z` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `32641331696` | SINGLE | `2026-11-21T13:06:16Z` |
| TShield 6.2 Live W response | 6.2-live-w-bridge-run11-v1 | Any | Any | `32483541702` | SINGLE | `2026-11-19T12:47:00Z` |
| QEMU user-static | 1:7.2+dfsg-7+deb12u18+b3 | Debian 12 / Linux | x86_64 | `32748029497` | SINGLE | `2026-11-22T15:57:40Z` |
| Debian 12 elfutils runtime | 0.188-2.1 | Debian 12 / Linux | x86_64 | `33241532212` | SINGLE | `2026-11-27T07:44:22Z` |
| Debian 13 binutils host repair | 2.44-3 | Debian 13 / Linux | x86_64 | `36876468018` | SINGLE | `2026-12-30T14:27:26Z` |
| nlohmann/json single header | 3.12.0 | Any | Any | `32814216489` | SINGLE | `2026-11-23T05:47:17Z` |

| libUE4 GL | 4.5-v1.0.1 | Android | AArch64 | `33073762454` | SINGLE | `2026-11-25T12:50:04Z` |
| libUE4 GL | 4.6-v1.0.1 | Android | AArch64 | `37218608943` | SINGLE | `2027-01-02T16:56:20Z` |
| VaultPony VeraCrypt-compatible CLI | 0.1.0+fb4c460 | Android (API 24+) | AArch64 | `33089426736` | SINGLE | `2026-11-25T15:43:58Z` |
| Wine portable | 11.16 | Linux | x86_64 | `34743014984` | SINGLE | `2026-12-12T06:32:52Z` |
| 逃跑吧！少年 4399 channel APK | 8.41.0 | Android | Multi-ABI APK | `36716019163` | SPLIT × 5 | `2026-12-29T12:38:04Z` |
| ARM64 system lab | debian13-v1-qemu10.0.13-linux6.12.111 | Linux / Debian 13 | x86_64 host + AArch64 guest | `36566866696` | SINGLE | `2026-12-28T12:15:02Z` |

## TShield 6.2 Live W response

- Workflow: `.github/workflows/tshield-fetch-6-2.yml` (temporary PR #1 only; do not merge)
- Workflow Name: `TShield 6.2 Live W Bridge`
- Run ID: `32483541702`
- Run Number: `11`
- Run Conclusion: `success`
- Source: exact raw HTTP response captured by the temporary TShield 6.2 bridge workflow
- Repository Visibility: `Public`
- Requested Retention: `90 days`
- Storage Mode: `SINGLE`
- Artifact Name: `tshield-live-w-response`
- Artifact ID: `9446959149`
- File: `response.raw`
- Artifact Archive Size: `757` bytes
- Artifact Archive SHA256 / Digest: `6e3d247db11f6a0169d7577cc2643d2d5809804cde84869d3b9430b9acc06a93`
- Original Size: `810` bytes
- Original SHA256: `0b90973c5938d418345f1d0845ee2480b037fecc38950c38b94b21e8d9f62152`
- Part Count: `1`
- Created At: `2026-08-21T12:47:08Z`
- Expires At: `2026-11-19T12:47:00Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| TShield 6.2 Live W response | 6.2-live-w-bridge-run11-v1 | Any | Any | `response.raw` | `0b90973c5938d418345f1d0845ee2480b037fecc38950c38b94b21e8d9f62152` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9446959149` | `tshield-live-w-response` | `810` | `0b90973c5938d418345f1d0845ee2480b037fecc38950c38b94b21e8d9f62152` | `757` | `sha256:6e3d247db11f6a0169d7577cc2643d2d5809804cde84869d3b9430b9acc06a93` | `2026-08-21T12:47:08Z` | `2026-11-19T12:47:00Z` |

### Restore

下载 Artifact `9446959149`，校验 Artifact ZIP SHA256 `6e3d247d...`；解压得到 `response.raw`，再校验其 SHA256 `0b90973c...`。该 Artifact 来自临时 PR #1；缓存复用不依赖合并该 PR。

## Android NDK r28c — preferred five-part cache

- Workflow: `.github/workflows/repack-ndk-r28c-five-parts.yml`
- Workflow Run ID: `39019800471`
- Run URL: https://github.com/jepede/gpt-exten/actions/runs/39019800471
- Run Conclusion: `success` (all 5 data artifacts and manifest uploaded successfully)
- Source: existing verified three-part cache, Run `38921184228` (no re-download from Google)
- Source Artifact IDs: `12053444812`, `12054800876`, `12055205324`
- Storage Mode: `SPLIT`
- Original File: `android-ndk-r28c-linux.zip`
- Original Size: `722261334` bytes
- Original SHA256: `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f`
- Original SHA1: `a7b54a5de87fecd125a17d54f73c446199e72a64`
- Part Count: `5`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (GitHub actual expiration)
- Created At: `2026-10-17T09:05:40Z` to `2026-10-17T09:05:46Z`
- Expires At: `2027-01-15T09:05:25Z` (all five data artifacts and manifest)
- Integrity: each old part SHA256 verified, whole file SHA1/SHA256 and size verified, all five new parts reconstructed on Actions and matching whole-file SHA256, individual part SHA256 logged.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android NDK | r28c | Linux | x86_64 | `android-ndk-r28c-linux.zip` | `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw File | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---|---:|---|---:|---|---|---|
| 1/5 | `12096092994` | `ndk-r28c-five-part-00` | `ndk-r28c.part.00` | `144452267` | `5171e5cc785cc062e090c3edecf594ce355fa83143c6fb2e62aafdba9c70a621` | `144452413` | `sha256:a0e4865e6e3c8bf0f6f3b2e3f5f2a67122ce04c43849a0ae64b8a5fcd8638594` | `2026-10-17T09:05:40Z` | `2027-01-15T09:05:25Z` |
| 2/5 | `12096038185` | `ndk-r28c-five-part-01` | `ndk-r28c.part.01` | `144452267` | `56983eda293816841e9c87bb90adc2a41e80f216fdb0fce3a927083c677fded7` | `144452413` | `sha256:2a6ddad52bbf7bb907df85af39de6e036b73997ac2ccb7c2320ebb4d63fda381` | `2026-10-17T09:05:41Z` | `2027-01-15T09:05:25Z` |
| 3/5 | `12095993665` | `ndk-r28c-five-part-02` | `ndk-r28c.part.02` | `144452267` | `342c5394c75929a11ce8538997ae16a8a1213728440efcded5560c07c794faf5` | `144452413` | `sha256:3bdcf73aa23f420146f729d3ded007fff81bcb1b1235662ea4ba60d6c2fe7082` | `2026-10-17T09:05:43Z` | `2027-01-15T09:05:25Z` |
| 4/5 | `12095869374` | `ndk-r28c-five-part-03` | `ndk-r28c.part.03` | `144452267` | `fe4905960f15b33defa09a871d5f44c18076b02f5334d6bdf6eef94ae6da7394` | `144452413` | `sha256:61a3f4a5ab88d76bb738399d096162efe348a9e83317b91f0270fd4396fe9e6e` | `2026-10-17T09:05:44Z` | `2027-01-15T09:05:25Z` |
| 5/5 | `12096053090` | `ndk-r28c-five-part-04` | `ndk-r28c.part.04` | `144452266` | `f853ef4464dab98c084336ea80b8da9986770803e2718a01f4f0fea66e70d1d1` | `144452412` | `sha256:547ecef346b37c2c1ec204f7b841e0aa3aea4319561209261c5f8869ee4c76be` | `2026-10-17T09:05:46Z` | `2027-01-15T09:05:25Z` |

- Manifest Artifact ID: `12096182768`; Name: `ndk-r28c-five-part-manifest`; File: `five-part-manifest.txt`; Artifact ZIP Size: `580` bytes; Artifact Digest: `sha256:9ca5faf7d127833a5cfd9e078b7db80f77eff5514e635d695888926e57acd6e3`; Created At: `2026-10-17T09:05:46Z`; Expires At: `2027-01-15T09:05:25Z`.

### Restore

First verify all five artifacts exist and are unexpired via GitHub API. Download each with GitHub connector `download_workflow_artifact` using the corresponding `Artifact ID`. Every individual artifact archive is below 512MB. Verify each downloaded outer artifact ZIP against `Artifact Digest`, extract the single raw file `ndk-r28c.part.00` through `ndk-r28c.part.04`, verify each raw part against `Raw SHA256`, then concatenate in numeric order. Verify reconstructed file size `722261334` and SHA256 `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f` before extracting NDK. Prefer this five-part cache over the older three-part backup below; no new upstream Google download is needed.

## Android NDK r28c (older three-part fallback)

- Workflow: `.github/workflows/download-ndk-r28c.yml`
- Run ID: `38921184228`
- Run Number: `8`
- Run Conclusion: `success`
- Run URL: https://github.com/jepede/gpt-exten/actions/runs/38921184228
- Source: `https://dl.google.com/android/repository/android-ndk-r28c-linux.zip` (re-downloaded 2026-10-16)
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual GitHub `expires_at` is authoritative)
- Storage Mode: `SPLIT`
- Original File: `android-ndk-r28c-linux.zip`
- Original Size: `722261334` bytes
- Original SHA-1: `a7b54a5de87fecd125a17d54f73c446199e72a64` (verified by the workflow)
- Original SHA256: `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f` (verified by the workflow)
- Part Count: `3`
- Created At: `2026-10-16T15:06:28Z` to `2026-10-16T15:06:36Z`
- Expires At: `2027-01-14T15:06:12Z` (all three artifacts, verified by GitHub API)
- Previous artifact IDs deleted and verified absent before refresh: `12053422732`, `12053417838`
- Split verification: exactly three equally sized raw chunks; concatenated SHA256 matched the original in Actions.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android NDK | r28c | Linux | x86_64 | `android-ndk-r28c-linux.zip` | `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/3 | `12053444812` | `ndk-r28c-part-00` | `240753778` | `e487b472b81d478714bb9550575e75ddf13d7159fa6dd960e98e7ce9e0c0340d` | `240753924` | `sha256:006a5c80f627bb631d5ea71b6ffb36c4afb528b5c6bb34bd682e7846a0fffae7` | `2026-10-16T15:06:28Z` | `2027-01-14T15:06:12Z` |
| 2/3 | `12054800876` | `ndk-r28c-part-01` | `240753778` | `02cc5d048dc3560f705c614e1782a7f1664f286f7091da8c5e419f7cf419223c` | `240753924` | `sha256:e2325d8e5b8e04424e66adc28ce0806fa6585f5cac1e09cb1ab4e291e94f9474` | `2026-10-16T15:06:32Z` | `2027-01-14T15:06:12Z` |
| 3/3 | `12055205324` | `ndk-r28c-part-02` | `240753778` | `09aab1b4fba172ff21ee44a6ec5b6c7740ae5b52b060c4ca24f7188ce72d90c6` | `240753924` | `sha256:5b07da1d08399f30a9c1e0a511cbca150fa8ee5e7b7d8e8ecf0e3e98cdddd99c` | `2026-10-16T15:06:36Z` | `2027-01-14T15:06:12Z` |

### Restore

Use GitHub connector `download_workflow_artifact` for each Artifact ID (`12053444812`, `12054800876`, `12055205324`) from `jepede/gpt-exten`. Every individual artifact is less than the 512MB download limit. Verify each downloaded outer artifact ZIP SHA256 against its `Artifact Digest` in this index; extract respectively `ndk-r28c.part.00`, `ndk-r28c.part.01`, and `ndk-r28c.part.02`. Verify each raw part's `Raw SHA256` and concatenate in numerical order into `android-ndk-r28c-linux.zip`. Verify the reconstructed file size is `722261334` bytes and SHA256 is `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f`. The CI workflow has already verified that concatenating the three parts reproduces this checksum.

## USDA FoodData Central Foundation Foods CSV 2026-04-30

- Workflow: `.github/workflows/fetch-fdc-foundation-2026-04.yml`
- Run ID: `31695314247`
- Source: `https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_csv_2026-04-30.zip`
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (GitHub public-repository cap)
- Storage Mode: `SINGLE`
- Artifact Name: `fdc-foundation-foods-2026-04-csv`
- Artifact ID: `9179050974`
- File: `FoodData_Central_foundation_food_csv_2026-04-30.zip`
- Artifact Archive Size: `3825971` bytes
- Artifact Archive SHA256: `e8b10363483702a565a896acda1ad521becf7be476313a6c4aafaf7affed9cb3`
- Original File: `FoodData_Central_foundation_food_csv_2026-04-30.zip`
- Original Size: `3825517` bytes
- Original SHA256: `d6d4f41dcd19a46abcdd67775379cb6f0292ff08daa7e0680fdd0982830bf57b`
- Part Count: `1`
- Created At: `2026-08-13T11:23:58Z`
- Expires At: `2026-11-11T11:23:52Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| USDA FoodData Central Foundation Foods CSV | 2026-04-30 | Any | Any | `FoodData_Central_foundation_food_csv_2026-04-30.zip` | `d6d4f41dcd19a46abcdd67775379cb6f0292ff08daa7e0680fdd0982830bf57b` |

### Artifact

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9179050974` | `fdc-foundation-foods-2026-04-csv` | `3825517` | `d6d4f41dcd19a46abcdd67775379cb6f0292ff08daa7e0680fdd0982830bf57b` | `3825971` | `sha256:e8b10363483702a565a896acda1ad521becf7be476313a6c4aafaf7affed9cb3` | `2026-08-13T11:23:58Z` | `2026-11-11T11:23:52Z` |

### Restore

下载 Artifact `9179050974`，解压得到原始 USDA ZIP 与 `SHA256SUMS.txt`，校验原始文件 SHA256 后再解压 Foundation Foods CSV 数据集。

## USDA FoodData Central SR Legacy CSV 2018-04

- Workflow: `.github/workflows/fetch-fdc-sr-legacy-2018-04.yml`
- Run ID: `31695560856`
- Source: `https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip`
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (GitHub public-repository cap)
- Storage Mode: `SINGLE`
- Artifact Name: `fdc-sr-legacy-2018-04-csv`
- Artifact ID: `9179147903`
- File: `FoodData_Central_sr_legacy_food_csv_2018-04.zip`
- Artifact Archive Size: `6075034` bytes
- Artifact Archive SHA256: `10588dc4e136782a6575356fd9a08327d8bbfa686836aea831a137a7704c6419`
- Original File: `FoodData_Central_sr_legacy_food_csv_2018-04.zip`
- Original Size: `6074592` bytes
- Original SHA256: `b80817294b8850530aaedf2e515c02593b1824f763a0ff356e5c2081643e6fd0`
- Part Count: `1`
- Created At: `2026-08-13T11:27:15Z`
- Expires At: `2026-11-11T11:27:10Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| USDA FoodData Central SR Legacy CSV | 2018-04 | Any | Any | `FoodData_Central_sr_legacy_food_csv_2018-04.zip` | `b80817294b8850530aaedf2e515c02593b1824f763a0ff356e5c2081643e6fd0` |

### Artifact

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9179147903` | `fdc-sr-legacy-2018-04-csv` | `6074592` | `b80817294b8850530aaedf2e515c02593b1824f763a0ff356e5c2081643e6fd0` | `6075034` | `sha256:10588dc4e136782a6575356fd9a08327d8bbfa686836aea831a137a7704c6419` | `2026-08-13T11:27:15Z` | `2026-11-11T11:27:10Z` |

### Restore

下载 Artifact `9179147903`，解压得到原始 USDA ZIP 与 `SHA256SUMS.txt`，校验原始文件 SHA256 后再解压 SR Legacy CSV 数据集。

## CulinaryDB CSV bundle 2018-03-15

- Workflow: `.github/workflows/fetch-culinarydb.yml`
- Run ID: `31723890750`
- Source: `https://cosylab.iiitd.edu.in/culinarydb/static/data/CulinaryDB.zip`
- Repository Visibility: `Public`
- Dataset License: `CC BY-NC-SA 3.0` (non-commercial/share-alike; keep derived evidence optional)
- Requested Retention: `400 days`
- Effective Retention: `90 days` (GitHub public-repository cap)
- Storage Mode: `SINGLE`
- Artifact Name: `culinarydb-2017-csv`
- Artifact ID: `9190437874`
- File: `CulinaryDB.zip`
- Artifact Archive Size: `5310899` bytes
- Artifact Digest: `sha256:c0bf58f37048f26f9cedea382f54164e111f808715ae329fcacf611bdaa732ba`
- Original File: `CulinaryDB.zip`
- Original Size: `5310046` bytes
- Original SHA256: `ca8bd2e94e31990f7c5c0989ee9409a7959b05bc3daf9acabba93f2f8ef52b4e`
- Part Count: `1`
- Created At: `2026-08-13T17:04:53Z`
- Expires At: `2026-11-11T17:04:36Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| CulinaryDB CSV bundle | 2018-03-15 | Any | Any | `CulinaryDB.zip` | `ca8bd2e94e31990f7c5c0989ee9409a7959b05bc3daf9acabba93f2f8ef52b4e` |

### Artifact

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9190437874` | `culinarydb-2017-csv` | `5310046` | `ca8bd2e94e31990f7c5c0989ee9409a7959b05bc3daf9acabba93f2f8ef52b4e` | `5310899` | `sha256:c0bf58f37048f26f9cedea382f54164e111f808715ae329fcacf611bdaa732ba` | `2026-08-13T17:04:53Z` | `2026-11-11T17:04:36Z` |

### Restore

下载 Artifact `9190437874`，解压得到原始 `CulinaryDB.zip`、`SHA256SUMS.txt` 与 `CONTENTS.txt`；校验原始 ZIP SHA256 后再解压 CSV。由于数据许可为 CC BY-NC-SA 3.0，项目中的 CulinaryDB 派生先验应保持可选并明确标注非商业许可边界。

## cquant Binance Spot 15m Klines 2025-01-01 to 2026-08-21

- Workflow: `.github/workflows/fetch-cquant-binance-spot-15m-20250101-20260821.yml`
- Run ID: `32575307131`
- Source: `https://data.binance.vision/data/spot/{monthly,daily}/klines/...`
- Repository Visibility: `Public`
- Dataset: Binance Public Data, Spot USDT pairs, 15m Klines
- Symbols: `BTCUSDT ETHUSDT BNBUSDT SOLUSDT XRPUSDT DOGEUSDT ADAUSDT LINKUSDT SUIUSDT AVAXUSDT`
- Range: `2025-01-01T00:00:00Z` through `2026-08-21T23:45:00Z`
- Requested Retention: `400 days`
- Effective Retention: actual GitHub expiry below
- Storage Mode: `SINGLE`
- Artifact Name: `cquant-binance-spot-15m-20250101-20260821`
- Artifact ID: `9476457085`
- Artifact ZIP Size: `27277451` bytes
- Artifact ZIP SHA256 / Digest: `06c0d11a87c9c85119d473d80643f7f23d7c2f95c09387470bf9f8e8e368cda0`
- Original File: `cquant-binance-spot-15m-20250101-20260821.tar.gz`
- Original Size: `27195970` bytes
- Original SHA256: `a433ff6bebc4b715d3a1c53fa36cf11442bf3eae779a3d46eb42a792e7d14923`
- Part Count: `1`
- Created At: `2026-08-22T13:23:00Z`
- Expires At: `2026-11-20T13:16:44Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| cquant Binance Spot 15m ADAUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/ADAUSDT.csv` | `4056e6ab1f34261498b0584ad286ed37643ce758fed1ec89ca207612a14ef396` |
| cquant Binance Spot 15m AVAXUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/AVAXUSDT.csv` | `89f6b7a5e9081c78e8426ea8553aac90a7e68d02bd3e0bb6e27398497670bdc5` |
| cquant Binance Spot 15m BNBUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/BNBUSDT.csv` | `14f7dea250de074fd94d3b50c0fc21a3f91408c57707edeb6f0a624c52a5ad43` |
| cquant Binance Spot 15m BTCUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/BTCUSDT.csv` | `c9d9133452e87d2a02ed7fd05f8665387029db34832f9afa53d108d026dca550` |
| cquant Binance Spot 15m DOGEUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/DOGEUSDT.csv` | `92e8638b6fe338389a1deb043a646667b5c9b537995d2ffa5dfbeff831a3b344` |
| cquant Binance Spot 15m ETHUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/ETHUSDT.csv` | `1bb434dfdda8a6463354de64b153dcd87479466cafc2d012837a2144e658cf8f` |
| cquant Binance Spot 15m LINKUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/LINKUSDT.csv` | `a9da7c76da811d733bc382db25907beb926a499ec1b79d0c574e432315ea1afb` |
| cquant Binance Spot 15m SOLUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/SOLUSDT.csv` | `0380d49c61cc1578a46d9024a43ef0b910b15ae06b94bf0fd1a6e3a0f4684692` |
| cquant Binance Spot 15m SUIUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/SUIUSDT.csv` | `f99e6f6f37f9191b0459c610b58175b58acd013dd02ba9e443712dfd97a901dc` |
| cquant Binance Spot 15m XRPUSDT | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `raw/XRPUSDT.csv` | `744b9e8c7ac785aab69e6fa7e2536c454adc5446f60ed1e8064db3d65bfde0ba` |
| cquant Binance Spot 15m source manifest | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `SOURCE_MANIFEST.tsv` | `a83d32d77a39c3a57ff0c545a0d22133bac5c995d5c45438769c48bdcd9e0f7d` |
| cquant Binance Spot 15m metadata | 2025-01-01_2026-08-21-15m-v1 | Any | Any | `DATASET_METADATA.json` | `a417ba1d53e49eb024b7b878aa89498183cda6f738a2cc0f57b2dc5583a5991d` |

### Artifact

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9476457085` | `cquant-binance-spot-15m-20250101-20260821` | `27195970` | `a433ff6bebc4b715d3a1c53fa36cf11442bf3eae779a3d46eb42a792e7d14923` | `27277451` | `sha256:06c0d11a87c9c85119d473d80643f7f23d7c2f95c09387470bf9f8e8e368cda0` | `2026-08-22T13:23:00Z` | `2026-11-20T13:16:44Z` |

### Restore

下载 Artifact `9476457085`，校验 Artifact ZIP SHA256 `06c0d11a...`；解压后校验 `cquant-binance-spot-15m-20250101-20260821.tar.gz` SHA256 `a433ff6b...`，再解压数据集并执行 `sha256sum -c DATASET_MANIFEST.sha256`。10 个 CSV 均应为 57,408 根 15m Kline，且本版本连续性检查为 0 gap。

## cquant Binance USD-M Derivatives 2025-01-01 to 2026-08-21

- Workflow: `.github/workflows/fetch-cquant-binance-um-derivatives-20250101-20260821.yml`
- Run ID: `32617341667`
- Source: `https://data.binance.vision/data/futures/um/...`
- Dataset: Binance Public Data, USD-M perpetual 15m Klines + daily metrics + monthly funding rate
- Symbols: `BTCUSDT ETHUSDT BNBUSDT SOLUSDT XRPUSDT`
- Range: `2025-01-01` through `2026-08-21` (funding monthly through latest archived month)
- Requested Retention: `400 days`
- Storage Mode: `SINGLE`
- Artifact Name: `cquant-binance-um-derivatives-20250101-20260821`
- Artifact ID: `9487402324`
- Artifact Size: `46865584` bytes
- Artifact Digest: `sha256:68711a092b32066e445f45fa4cd3913a3bebacc28de7cadbaebf81e83622adc0`
- Original File: `cquant-binance-um-derivatives-20250101-20260821.tar.gz`
- Original Size: `46192615` bytes
- Original SHA256: `91773a0f5804bb511d348b3ebf8323a3d8e7c27fcd3e979ed4456c8080adb87a`
- Part Count: `1`
- Created At: `2026-08-23T04:19:17Z`
- Expires At: `2026-11-21T04:13:42Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/klines/BNBUSDT.csv` | `5f39c0617ecc4f8a4d90b231c67b4d931a7da4c3148c4fc821a3550da63a53c5` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/klines/BTCUSDT.csv` | `65a35cf24e1cc9d51c0cf069b7c4a1e5d5f916942b7ac0ad916cf98adde52f7c` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/klines/ETHUSDT.csv` | `9ce0a2a00d0d5030b4f58567990f06a6f481975259da5ebd47946641b4110699` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/klines/SOLUSDT.csv` | `f4b8e9bbf697efd1a3b3b9fc1ced81d4c63b0e8462618171ba23115eee901514` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/klines/XRPUSDT.csv` | `b8a5fd04a028a095b3dc855bd891db65823390cf1255c52fa30ad7e22d831faf` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/metrics/BNBUSDT.csv` | `3fd6902028f7baae49724ec872d6939aca76ac9797dbdc98edd2c7e1baf7f03c` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/metrics/BTCUSDT.csv` | `4cb4312b7ed53b371cee5f9e9211b72ce582345f21c9e50f9b09362c7f57fb9c` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/metrics/ETHUSDT.csv` | `656f423fe5939c7301fefcc034c2cd9aa974fd3255da9531e1d8796e42ebd619` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/metrics/SOLUSDT.csv` | `d8974f4dc5f678371e1b97227b9ead7c017ba0ad051bb1c95103fbe91dd86199` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/metrics/XRPUSDT.csv` | `a14d6cc7be4be66bc9fea21c79f6b85576496feee974d6ec147b2f1e8afbd093` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/funding/BNBUSDT.csv` | `de94959771503bc884dd5705dd7443273659877847308f836027dfed5435777a` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/funding/BTCUSDT.csv` | `7cb5d75e6bb5bf5d17287d18e6c11c1666fe5574b8e82fddad6c49b235084d63` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/funding/ETHUSDT.csv` | `d19765bc1123ba2af065e4c02825ea31ca1f3ea7d7839f569d2f4404c8472f30` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/funding/SOLUSDT.csv` | `75334aad4b3eec1e01286770e3fd29012197438553911fd49ee64c33bff25d45` |
| cquant Binance USD-M Derivatives | 2025-01-01_2026-08-21-15m-um-derivatives-v1 | Any | Any | `raw/funding/XRPUSDT.csv` | `b8b39bd52911e7becdc3312fb7b8a7488bf8ba4182e33bb97f7b540ddc54c8fe` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9487402324` | `cquant-binance-um-derivatives-20250101-20260821` | `46192615` | `91773a0f5804bb511d348b3ebf8323a3d8e7c27fcd3e979ed4456c8080adb87a` | `46865584` | `sha256:68711a092b32066e445f45fa4cd3913a3bebacc28de7cadbaebf81e83622adc0` | `2026-08-23T04:19:17Z` | `2026-11-21T04:13:42Z` |

### Restore

Download the single Artifact, verify the inner tar.gz SHA256, extract it, then run `sha256sum -c DATASET_MANIFEST.sha256`.

## cquant Binance Spot 15m Golden Holdout 2025-01-01 to 2026-08-21

- Workflow: `.github/workflows/fetch-cquant-binance-spot-15m-golden-holdout-20250101-20260821.yml`
- Run ID: `32618059050`
- Source: `https://data.binance.vision/data/spot/{monthly,daily}/klines/...`
- Symbols: `AAVEUSDT ATOMUSDT ETCUSDT FILUSDT UNIUSDT`
- Role: pristine symbol holdout for the frozen Regime Rotation v1 protocol
- Storage Mode: `SINGLE`
- Artifact Name: `cquant-binance-spot-15m-golden-holdout-20250101-20260821`
- Artifact ID: `9487571958`
- Artifact Size: `12256350` bytes
- Artifact Digest: `sha256:d94b8041f7cfa1caac744b9e66ad85c283210c9c47724b7b5535195d889a3fea`
- Original File: `cquant-binance-spot-15m-golden-holdout-20250101-20260821.tar.gz`
- Original Size: `12214339` bytes
- Original SHA256: `01f00b9c63644e594f9d28482bc56e292309628adfd6baffb6967a9deeff6161`
- Part Count: `1`
- Created At: `2026-08-23T04:33:38Z`
- Expires At: `2026-11-21T04:30:49Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| cquant Binance Spot 15m Golden Holdout | 2025-01-01_2026-08-21-15m-golden-holdout-v1 | Any | Any | `raw/AAVEUSDT.csv` | `76b418f8629f930eb1b8b8f7d649e6bc192a98927a821191e780121dbc8fea7e` |
| cquant Binance Spot 15m Golden Holdout | 2025-01-01_2026-08-21-15m-golden-holdout-v1 | Any | Any | `raw/ATOMUSDT.csv` | `4d590d1a1e48caa3d4656d13969aefabfa7e31a7e7fd4920b2c373030e2fe83e` |
| cquant Binance Spot 15m Golden Holdout | 2025-01-01_2026-08-21-15m-golden-holdout-v1 | Any | Any | `raw/ETCUSDT.csv` | `12d6cc349dfb50bc7417558ec83cf6d94c94242832de6c65765f21c175e49e79` |
| cquant Binance Spot 15m Golden Holdout | 2025-01-01_2026-08-21-15m-golden-holdout-v1 | Any | Any | `raw/FILUSDT.csv` | `8f0ab12a650fa7a3049ae6ab15f0ee0c67c2f1e5cc3686f8b2217008bd406a4a` |
| cquant Binance Spot 15m Golden Holdout | 2025-01-01_2026-08-21-15m-golden-holdout-v1 | Any | Any | `raw/UNIUSDT.csv` | `97d9765483b8b453dda783c11e18e714772b9c22edbb4b6d87ff76c732d0fd5d` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9487571958` | `cquant-binance-spot-15m-golden-holdout-20250101-20260821` | `12214339` | `01f00b9c63644e594f9d28482bc56e292309628adfd6baffb6967a9deeff6161` | `12256350` | `sha256:d94b8041f7cfa1caac744b9e66ad85c283210c9c47724b7b5535195d889a3fea` | `2026-08-23T04:33:38Z` | `2026-11-21T04:30:49Z` |

### Restore

Download the single Artifact, verify the inner tar.gz SHA256, extract, then run `sha256sum -c DATASET_MANIFEST.sha256`.

## cquant Binance USD-M Golden Derivatives 2025-01-01 to 2026-07-31

- Workflow: `.github/workflows/fetch-cquant-binance-um-golden-derivatives-20250101-20260731.yml`
- Run ID: `32641331696`
- Source: `https://data.binance.vision/data/futures/um/...`
- Dataset: Binance Public Data, USD-M perpetual 15m Klines + daily metrics + monthly funding rate
- Symbols: `AAVEUSDT ATOMUSDT ETCUSDT FILUSDT UNIUSDT`
- Range: `2025-01-01` through `2026-07-31`
- Frozen use: external Golden universe for protocol `short-only-ridge40-wf-v1`
- Requested Retention: `400 days`
- Storage Mode: `SINGLE`
- Artifact Name: `cquant-binance-um-golden-derivatives-20250101-20260731`
- Artifact ID: `9493764398`
- Artifact Size: `42554715` bytes
- Artifact Digest: `sha256:c6de2bdbfae2d1dada59630e6614f89b0434864a993f2adb2bfeb7e19545910d`
- Original File: `cquant-binance-um-golden-derivatives-20250101-20260731.tar.gz`
- Original Size: `41919490` bytes
- Original SHA256: `e1c335dd5da02b522573a24010f6f4370024460ba0ccaaadecf80520bf8b0bd3`
- Part Count: `1`
- Created At: `2026-08-23T13:13:37Z`
- Expires At: `2026-11-21T13:06:16Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/klines/AAVEUSDT.csv` | `66bab9dbbfd08d560b82b219ab37ee204de87dd9769afc87b9cd0fb2484afaec` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/klines/ATOMUSDT.csv` | `31cbc826944113ef8ff22df89e839635ff67c8879df141991cab5c2e53ee00f3` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/klines/ETCUSDT.csv` | `d08ef10fdfca388c76f50ad1abcb97f12cea098900bf726cbb7574d30524fc0d` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/klines/FILUSDT.csv` | `4ee598a0c92c82a97dc72d9a91d3d5b57dc4db65061b5d9ddffcd15402e13928` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/klines/UNIUSDT.csv` | `47dde92a199d7d8274a47c3dbdbab849dcd02e6d597583bee95bd6d8021f7bf6` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/metrics/AAVEUSDT.csv` | `907df6a8a40fa48f0ed2682addeb5d9c2bef8fdd8bc2977e97da33a1d2d3de7d` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/metrics/ATOMUSDT.csv` | `44981a58d5a9b910450494ca2ed01e26201baf90e37aabf88e9194a9c03f969a` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/metrics/ETCUSDT.csv` | `9fee054438d45951e0a99f164327f210823558a5c8d20ed3fd054024e8c8421a` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/metrics/FILUSDT.csv` | `d1c5c87c8032de6c71fac162ba8a22672437d1d512489021ac942098850e31ea` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/metrics/UNIUSDT.csv` | `1ff1b16a797ac2f99ef221822a7006127bc852f1a363c3ac4b57914b205cb086` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/funding/AAVEUSDT.csv` | `0d4afb45106897686ae4de3f8e5befbd45674a16c5630ffe0da9c3ac06440f2c` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/funding/ATOMUSDT.csv` | `9985cbecfc46cdaf13a2cd458eeee4afff73e0ddb0c627eda96e4f310ab5b890` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/funding/ETCUSDT.csv` | `7c63137756c398151307cae740b355ecbc8397fabf49a324be60a69ac4ec361a` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/funding/FILUSDT.csv` | `a37365bd529686863f8315c7dab2d8258fee4d075087c8081727a35a4095092b` |
| cquant Binance USD-M Golden Derivatives | 2025-01-01_2026-07-31-15m-um-golden-derivatives-v1 | Any | Any | `raw/funding/UNIUSDT.csv` | `f5ac7b4c549df42c054c920e86e82303259cb642d149411a49146a1cacb3d9ae` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9493764398` | `cquant-binance-um-golden-derivatives-20250101-20260731` | `41919490` | `e1c335dd5da02b522573a24010f6f4370024460ba0ccaaadecf80520bf8b0bd3` | `42554715` | `sha256:c6de2bdbfae2d1dada59630e6614f89b0434864a993f2adb2bfeb7e19545910d` | `2026-08-23T13:13:37Z` | `2026-11-21T13:06:16Z` |

### Restore

Download the single Artifact, verify the inner tar.gz SHA256, extract it, then run `sha256sum -c DATASET_MANIFEST.sha256`.


## QEMU user-static 1:7.2+dfsg-7+deb12u18+b3

- Workflow: `.github/workflows/fetch-qemu-user-static-bookworm.yml`
- Run ID: `32748029497`
- Source: `https://deb.debian.org/debian/pool/main/q/qemu/qemu-user-static_7.2+dfsg-7+deb12u18+b3_amd64.deb`
- Repository Visibility: `Public`
- Requested Retention: `90 days`
- Storage Mode: `SINGLE`
- Artifact Name: `qemu-user-static-7.2-deb12u18-amd64`
- Artifact ID: `9527836019`
- File: `qemu-user-static_7.2+dfsg-7+deb12u18+b3_amd64.deb`
- Artifact Archive Size: `62604562` bytes
- Artifact Archive SHA256 / Digest: `33fc072150ca5eb586aca5506b4a8c31226706f6b1f60cf68f94dc5ec6d89297`
- Original Size: `62603724` bytes
- Original SHA256: `c3e3ba2bd87f8c5b9a5da5ef21b5a3b82d7c63b89dd448d9ddaa4eabc5b6e402`
- Part Count: `1`
- Created At: `2026-08-24T15:57:46Z`
- Expires At: `2026-11-22T15:57:40Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| QEMU user-static Debian package | 1:7.2+dfsg-7+deb12u18+b3 | Debian 12 / Linux | x86_64 | `qemu-user-static_7.2+dfsg-7+deb12u18+b3_amd64.deb` | `c3e3ba2bd87f8c5b9a5da5ef21b5a3b82d7c63b89dd448d9ddaa4eabc5b6e402` |

The package contains the statically linked user-mode emulators, including `qemu-aarch64-static`, for running AArch64 Linux/Android user-space ELF binaries on an x86_64 host.

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9527836019` | `qemu-user-static-7.2-deb12u18-amd64` | `62603724` | `c3e3ba2bd87f8c5b9a5da5ef21b5a3b82d7c63b89dd448d9ddaa4eabc5b6e402` | `62604562` | `sha256:33fc072150ca5eb586aca5506b4a8c31226706f6b1f60cf68f94dc5ec6d89297` | `2026-08-24T15:57:46Z` | `2026-11-22T15:57:40Z` |

### Restore

Download Artifact `9527836019`, verify the Artifact ZIP SHA256 `33fc072150ca5eb586aca5506b4a8c31226706f6b1f60cf68f94dc5ec6d89297`, extract the Debian package, verify its SHA256 `c3e3ba2bd87f8c5b9a5da5ef21b5a3b82d7c63b89dd448d9ddaa4eabc5b6e402`, then extract it with `dpkg-deb -x`. The installed binary used for AArch64 testing is `usr/bin/qemu-aarch64-static`.


## nlohmann/json single header 3.12.0

- Workflow: `.github/workflows/fetch-nlohmann-json-3.12.0.yml`
- Workflow Name: `Fetch nlohmann json 3.12.0`
- Run ID: `32814216489`
- Run Number: `1`
- Run Conclusion: `success`
- Source: `https://raw.githubusercontent.com/nlohmann/json/v3.12.0/single_include/nlohmann/json.hpp`
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual GitHub `expires_at` governs validity)
- Storage Mode: `SINGLE`
- Artifact Name: `nlohmann-json-3.12.0-header`
- Artifact ID: `9550829984`
- File: `json.hpp`
- Artifact Archive Size: `141823` bytes
- Artifact Archive SHA256 / Digest: `06e8d874db0ab47a2915e097a000945ce6ed26c41e55e328bb5882800486ee7a`
- Original File: `json.hpp`
- Original Size: `953436` bytes
- Original SHA256: `aaf127c04cb31c406e5b04a63f1ae89369fccde6d8fa7cdda1ed4f32dfc5de63`
- Part Count: `1`
- Created At: `2026-08-25T05:47:22Z`
- Expires At: `2026-11-23T05:47:17Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| nlohmann/json single header | 3.12.0 | Any | Any | `json.hpp` | `aaf127c04cb31c406e5b04a63f1ae89369fccde6d8fa7cdda1ed4f32dfc5de63` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9550829984` | `nlohmann-json-3.12.0-header` | `953436` | `aaf127c04cb31c406e5b04a63f1ae89369fccde6d8fa7cdda1ed4f32dfc5de63` | `141823` | `sha256:06e8d874db0ab47a2915e097a000945ce6ed26c41e55e328bb5882800486ee7a` | `2026-08-25T05:47:22Z` | `2026-11-23T05:47:17Z` |

### Restore

Download Artifact `9550829984`, verify the Artifact ZIP SHA256 `06e8d874db0ab47a2915e097a000945ce6ed26c41e55e328bb5882800486ee7a`, extract `json.hpp` and `SHA256SUMS.txt`, then verify `json.hpp` SHA256 `aaf127c04cb31c406e5b04a63f1ae89369fccde6d8fa7cdda1ed4f32dfc5de63`.

## libUE4 GL 4.5 v1.0.1

- Workflow: `.github/workflows/tmp-fetch-libue4-gl45-20260827.yml` (temporary branch only; do not merge)
- Workflow Name: `Temporary libUE4 GL 4.5 Fetch`
- Run ID: `33073762454`
- Run Number: `1`
- Run Conclusion: `success`
- Source: `https://github.com/jepede/gpt-exten/releases/download/v1.0.1/libUE4-GL-4.5.so`
- Release: `v1.0.1`
- Release Asset ID: `473330078`
- Repository Visibility: `Public`
- Requested Retention: `90 days`
- Storage Mode: `SINGLE`
- Artifact Name: `libue4-gl-4.5-v1.0.1`
- Artifact ID: `9646923730`
- File: `libUE4-GL-4.5.so`
- Original Size: `247976280` bytes
- Original SHA256: `b5e68be0e06e52a81713c4241169ec493772bdcbca9b54b0845e89d08d2f8fdc`
- Artifact Archive Size: `247976629` bytes
- Artifact Digest: `sha256:42afa71f4ff1b1e20a161999c5ddde447352893109edb36fc9b7daea9e94b749`
- Created At: `2026-08-27T12:50:13Z`
- Expires At: `2026-11-25T12:50:04Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| libUE4 GL | 4.5-v1.0.1 | Android | AArch64 | `libUE4-GL-4.5.so` | `b5e68be0e06e52a81713c4241169ec493772bdcbca9b54b0845e89d08d2f8fdc` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9646923730` | `libue4-gl-4.5-v1.0.1` | `247976280` | `b5e68be0e06e52a81713c4241169ec493772bdcbca9b54b0845e89d08d2f8fdc` | `247976629` | `sha256:42afa71f4ff1b1e20a161999c5ddde447352893109edb36fc9b7daea9e94b749` | `2026-08-27T12:50:13Z` | `2026-11-25T12:50:04Z` |

### Restore

下载 Artifact `9646923730`，校验 Artifact ZIP SHA256 `42afa71f4ff1b1e20a161999c5ddde447352893109edb36fc9b7daea9e94b749`；解压得到 `libUE4-GL-4.5.so`，再校验 SHA256 `b5e68be0e06e52a81713c4241169ec493772bdcbca9b54b0845e89d08d2f8fdc`。

## VaultPony VeraCrypt-compatible CLI 0.1.0+fb4c460

- Workflow: `.github/workflows/build-vaultpony-android-arm64.yml`
- Workflow Name: `Build VaultPony Android ARM64`
- Run ID: `33089426736`
- Run Conclusion: `success`
- Source: `https://github.com/norsehorse-dev/VaultPonyCore.git`
- Source Commit: `fb4c460b84577543d4e90b9ede51dcdbd0b674e7`
- Build Target: `aarch64-linux-android`
- Minimum Android API: `24`
- Android NDK: `r28c` (`28.2.13676358`)
- Rust: `1.95.0`
- Storage Mode: `SINGLE`
- Artifact Name: `vaultpony-android-arm64`
- Artifact ID: `9653685980`
- File: `vaultpony-android-arm64`
- Original Size: `2022752` bytes
- Original SHA256: `4d72916de3be08e1485488f7b1ef246ee022488f64568e26be17fc1311f9834d`
- Artifact Archive Size: `1039037` bytes
- Artifact Archive SHA256 / Digest: `724b40575a8ba2a470aacd95cb77195d2a4f0ccd2c04017d2ba93bf33c896f0b`
- Created At: `2026-08-27T15:45:07Z`
- Expires At: `2026-11-25T15:43:58Z`
- Runtime ELF: `ELF64`, `AArch64`, `PIE`, interpreter `/system/bin/linker64`
- Runtime Shared Libraries: `libdl.so`, `libc.so`
- CLI License Declaration: `GPL-3.0-only`
- Core Workspace License Declaration: `Apache-2.0`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| VaultPony VeraCrypt-compatible CLI | 0.1.0+fb4c460 | Android (API 24+) | AArch64 | `vaultpony-android-arm64` | `4d72916de3be08e1485488f7b1ef246ee022488f64568e26be17fc1311f9834d` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9653685980` | `vaultpony-android-arm64` | `2022752` | `4d72916de3be08e1485488f7b1ef246ee022488f64568e26be17fc1311f9834d` | `1039037` | `sha256:724b40575a8ba2a470aacd95cb77195d2a4f0ccd2c04017d2ba93bf33c896f0b` | `2026-08-27T15:45:07Z` | `2026-11-25T15:43:58Z` |

### Restore

下载 Artifact `9653685980`，校验 Artifact ZIP SHA256 `724b40575a8ba2a470aacd95cb77195d2a4f0ccd2c04017d2ba93bf33c896f0b`；解压得到 `vaultpony-android-arm64`，再校验其 SHA256 `4d72916de3be08e1485488f7b1ef246ee022488f64568e26be17fc1311f9834d`。该文件是 Android/Bionic 原生 AArch64 PIE，可直接推送到 Android 设备执行。


## Debian 12 elfutils runtime 0.188-2.1

- Workflow: `.github/workflows/tmp-fetch-debian12-elfutils-0.188.yml` (temporary branch only; do not merge)
- Workflow Name: `Temporary fetch Debian 12 elfutils runtime`
- Run ID: `33241532212`
- Run Conclusion: `success`
- Source: `https://deb.debian.org/debian/pool/main/e/elfutils/`
- Repository Visibility: `Public`
- Requested Retention: `90 days`
- Storage Mode: `SINGLE`
- Artifact Name: `debian12-elfutils-runtime-0.188-amd64`
- Artifact ID: `9711497447`
- Artifact Archive Size: `409543` bytes
- Artifact Archive SHA256 / Digest: `12ca8957b89c7f684c21a1373279d267b7f9d8d17843e1dce086573c7da1d51e`
- Part Count: `1`
- Created At: `2026-08-29T07:44:30Z`
- Expires At: `2026-11-27T07:44:22Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | Size | SHA256 |
|---|---|---|---|---|---:|---|
| Debian libdw1 | 0.188-2.1 | Debian 12 / Linux | x86_64 | `libdw1_0.188-2.1_amd64.deb` | `234760` | `ffd7b1bad982ad1afd9c2b75ab2edd18e229508df731a8f4d8443f093a91442f` |
| Debian libelf1 | 0.188-2.1 | Debian 12 / Linux | x86_64 | `libelf1_0.188-2.1_amd64.deb` | `173796` | `619add379c606b3ac6c1a175853b918e6939598a83d8ebadf3bdfd50d10b3c8c` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `9711497447` | `debian12-elfutils-runtime-0.188-amd64` | `408556` (two DEBs combined) | see Contents | `409543` | `sha256:12ca8957b89c7f684c21a1373279d267b7f9d8d17843e1dce086573c7da1d51e` | `2026-08-29T07:44:30Z` | `2026-11-27T07:44:22Z` |

### Restore

下载 Artifact `9711497447`，校验 Artifact ZIP SHA256 `12ca8957b89c7f684c21a1373279d267b7f9d8d17843e1dce086573c7da1d51e`；解压后分别校验两个 DEB 的 SHA256，再用 `dpkg-deb -x` 解包到隔离的 GDB 根目录。该 Artifact 用于补齐 Debian 12 GDB 13.1 所需 `libdw.so.1` 与匹配的 `libelf.so.1`，不应覆盖宿主发行版库。

## Android SDK compile bundle API 35 / Build Tools 35.0.0

- Artifact Name: `android-sdk-api35-bt35.0.0-linux-x86_64`
- Artifact ID: `10299605918`
- Run ID: `34697680626`
- Workflow: `.github/workflows/cache-trustattestor-ui-toolchain.yml`
- File: `android-sdk-api35-bt35.0.0-linux-x86_64.tar.zst`
- Size: `236499853` bytes
- SHA256: `7ee54463a9abebf335d22e04533098ac4da3ec35e876108a6c81940675f3ca7c` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T13:57:08Z`
- Expires At: `2026-12-11T13:53:27Z`
- Storage Mode: `SINGLE`
- Original File: `android-sdk-api35-bt35.0.0-linux-x86_64.tar.zst`
- Original Size: `236498357` bytes
- Original SHA256: `d1625f8dde5ce737b376ee56e89089846056605aa3a0eb59ddf3b87c3ee24fcc`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android SDK Build-Tools | 35.0.0 | Linux | x86_64 | `build-tools/35.0.0` | `b6fde1805eea925b97994f39425996e5dffe78043f09d6005d6906c417ced802` |
| Android SDK Platform | API 35 rev 2 | Linux | x86_64 | `platforms/android-35` | `9de2ae1e84ee7cdf6867c6336ffde39136f267980b905192b1173a91ee34c1ee` |
| Android SDK Platform-Tools | 37.0.1 | Linux | x86_64 | `platform-tools` | `7d9bcebbc4547a7029e2a8637bab9d42d61d3f42042de097e3ed57561889f464` |
| Android SDK Command-line Tools | 12.0 | Linux | x86_64 | `cmdline-tools/latest` | `e6ac9ef5eb83365d84ff0a78a8af355811211935bf4c79e3a01230b32d1e0461` |
| Android SDK licenses snapshot | 2026-09-12 | Linux | x86_64 | `licenses` | `f401b51ef2920f7c8a4bae7e3141481b194236dbe7ed49627e44a604a0e17762` |

Directory entries use a deterministic SHA256 over sorted relative file hashes. The outer archive is the authoritative integrity check for restore.

### Restore

Download Artifact `10299605918`, verify the Artifact ZIP digest `7ee54463a9abebf335d22e04533098ac4da3ec35e876108a6c81940675f3ca7c`, extract the `.tar.zst`, verify original SHA256 `d1625f8dde5ce737b376ee56e89089846056605aa3a0eb59ddf3b87c3ee24fcc`, then extract it as `ANDROID_SDK_ROOT`.

## Temurin JDK 17.0.20.1+1

- Artifact Name: `temurin-jdk17-linux-x86_64`
- Artifact ID: `10298958603`
- Run ID: `34697680626`
- Workflow: `.github/workflows/cache-trustattestor-ui-toolchain.yml`
- File: `temurin-jdk17-linux-x86_64.tar.zst`
- Size: `170785749` bytes
- SHA256: `a408b6f11628fad2838cc1f29dbc00d4e81c2424208e537dd47a2f1c3eca4a7e` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T13:57:10Z`
- Expires At: `2026-12-11T13:53:27Z`
- Storage Mode: `SINGLE`
- Original File: `temurin-jdk17-linux-x86_64.tar.zst`
- Original Size: `170785268` bytes
- Original SHA256: `e1c2997df8e831452fe8cbec9b85c15565c9ad8ac1656966b2683b4c623b2b8e`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Eclipse Temurin JDK | 17.0.20.1+1 | Linux | x86_64 | `temurin-jdk17-linux-x86_64.tar.zst` | `e1c2997df8e831452fe8cbec9b85c15565c9ad8ac1656966b2683b4c623b2b8e` |

## Gradle 8.10.2

- Artifact Name: `gradle-8.10.2-bin`
- Artifact ID: `10299023549`
- Run ID: `34697680626`
- Workflow: `.github/workflows/cache-trustattestor-ui-toolchain.yml`
- File: `gradle-8.10.2-bin.zip`
- Size: `136715822` bytes
- SHA256: `cc0af2368404f92cd2f6363118b582aae86c8abe800040d7adee00c13dcc0a9e` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T13:57:13Z`
- Expires At: `2026-12-11T13:53:27Z`
- Storage Mode: `SINGLE`
- Original File: `gradle-8.10.2-bin.zip`
- Original Size: `136715430` bytes
- Original SHA256: `31c55713e40233a8303827ceb42ca48a47267a0ad4bab9177123121e71524c26`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Gradle binary distribution | 8.10.2 | Linux | x86_64 | `gradle-8.10.2-bin.zip` | `31c55713e40233a8303827ceb42ca48a47267a0ad4bab9177123121e71524c26` |

## TrustAttestor UI Gradle dependency cache

- Artifact Name: `gradle-modules2-ta-ui-linux-x86_64`
- Artifact ID: `10299307665`
- Run ID: `34697680626`
- Workflow: `.github/workflows/cache-trustattestor-ui-toolchain.yml`
- File: `gradle-modules2-ta-ui-linux-x86_64.tar.zst`
- Size: `171488247` bytes
- SHA256: `3e1d902f9206f04dbb084993aa0bc88203589c47b095d74cf05c12542773796f` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T13:57:15Z`
- Expires At: `2026-12-11T13:53:27Z`
- Storage Mode: `SINGLE`
- Original File: `gradle-modules2-ta-ui-linux-x86_64.tar.zst`
- Original Size: `171487726` bytes
- Original SHA256: `a1c95b74489951f93bc93a3e8a6f83f3eae0aba2fe1afbc434c9729de49263d7`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| TrustAttestor UI Gradle modules cache | AGP 8.7.2 + Kotlin 2.0.21 + exact UI dependencies | Linux | x86_64 | `caches/modules-2` | `a1c95b74489951f93bc93a3e8a6f83f3eae0aba2fe1afbc434c9729de49263d7` |

The cache was warmed by successfully assembling a minimal Android application with compileSdk 35 and the exact TrustAttestor UI dependency versions. Restore it under `GRADLE_USER_HOME`, then build with `--offline`.

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

## TrustAttestor UI release-complete Gradle dependency cache v3

- Artifact Name: `gradle-modules2-ta-ui-releasecomplete-linux-x86_64`
- Artifact ID: `10299263954`
- Run ID: `34698530131`
- Workflow: `.github/workflows/cache-ta-ui-lint-deps.yml`
- File: `gradle-modules2-ta-ui-releasecomplete-linux-x86_64.tar.zst`
- Size: `269477263` bytes
- SHA256: `ab02f8ec568e6aa8985eb1d7afe770642a26ba2ed20d76d342fa51fea2c89434` (GitHub Artifact ZIP digest)
- Created At: `2026-09-12T14:12:08Z`
- Expires At: `2026-12-11T14:10:58Z`
- Storage Mode: `SINGLE`
- Original File: `gradle-modules2-ta-ui-releasecomplete-linux-x86_64.tar.zst`
- Original Size: `269476662` bytes
- Original SHA256: `b561966039c37b7bc2368a5895a1752523c150d3dd2c673c2162f8fb83fcd3b4`
- Part Count: `1`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual `expires_at` from GitHub)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| TrustAttestor UI Gradle modules cache | AGP 8.7.2 + Kotlin 2.0.21 + exact UI deps + Kotlin compile + Release Lint | Linux | x86_64 | `caches/modules-2` | `b561966039c37b7bc2368a5895a1752523c150d3dd2c673c2162f8fb83fcd3b4` |
| Android Lint Gradle integration | 31.7.2 | Any | JVM | `com.android.tools.lint/lint-gradle/31.7.2` | included in archive `b561966039c37b7bc2368a5895a1752523c150d3dd2c673c2162f8fb83fcd3b4` |

This supersedes the v2 dependency cache for full offline Debug/Release builds. It contains the Android Lint 31.7.2 transitive dependency graph required by AGP 8.7.2 `lintVitalRelease`, and was verified locally by a successful `--offline :app:assembleRelease` of TrustAttestor-UI.

### Restore

Download Artifact `10299263954`, verify the Artifact ZIP SHA256 `ab02f8ec568e6aa8985eb1d7afe770642a26ba2ed20d76d342fa51fea2c89434`, extract the `.tar.zst`, verify original SHA256 `b561966039c37b7bc2368a5895a1752523c150d3dd2c673c2162f8fb83fcd3b4`, then restore `caches/modules-2` beneath `GRADLE_USER_HOME`.

## Wine portable 11.16 amd64

- Workflow: `.github/workflows/fetch-wine-11.16-amd64.yml` (temporary branch `tmp/fetch-wine-11.16-amd64-20260913`)
- Workflow Name: `Fetch Wine 11.16 amd64`
- Run ID: `34743014984`
- Run Number: `1`
- Run Conclusion: `success`
- Source: `https://github.com/Kron4ek/Wine-Builds/releases/download/11.16/wine-11.16-amd64.tar.xz`
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (GitHub public-repository cap)
- Storage Mode: `SINGLE`
- Artifact Name: `wine-11.16-amd64-linux-x86_64`
- Artifact ID: `10313207613`
- File: `wine-11.16-amd64.tar.xz`
- Artifact Archive Size: `103741066` bytes
- Artifact Archive SHA256 / Digest: `7a6a123f3e5d0d286bd8687fa53c2fa6f06f33f500adff7d249a9cf47c096b65`
- Original File: `wine-11.16-amd64.tar.xz`
- Original Size: `103740540` bytes
- Original SHA256: `bb4d0eba24fb4ca8636b06f3d7786aa7fc50cb853f9255a0a376adf1f50bca53`
- Part Count: `1`
- Created At: `2026-09-13T06:32:58Z`
- Expires At: `2026-12-12T06:32:52Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Wine portable | 11.16 | Linux | x86_64 | `wine-11.16-amd64.tar.xz` | `bb4d0eba24fb4ca8636b06f3d7786aa7fc50cb853f9255a0a376adf1f50bca53` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `10313207613` | `wine-11.16-amd64-linux-x86_64` | `103740540` | `bb4d0eba24fb4ca8636b06f3d7786aa7fc50cb853f9255a0a376adf1f50bca53` | `103741066` | `sha256:7a6a123f3e5d0d286bd8687fa53c2fa6f06f33f500adff7d249a9cf47c096b65` | `2026-09-13T06:32:58Z` | `2026-12-12T06:32:52Z` |

### Restore

下载 Artifact `10313207613`，校验 Artifact ZIP SHA256 `7a6a123f3e5d0d286bd8687fa53c2fa6f06f33f500adff7d249a9cf47c096b65`；解压得到 `wine-11.16-amd64.tar.xz` 后校验 SHA256 `bb4d0eba24fb4ca8636b06f3d7786aa7fc50cb853f9255a0a376adf1f50bca53`。


## Ytbl build dependencies v1

- Name: Ytbl build dependencies
- Version: imgui1.91.9b+1.92.5-khronos-20260917-v1
- Platform: Any
- Architecture: Any
- Workflow: `.github/workflows/ytbl-deps-20260917.yml`
- Run ID: `35180975425`
- Artifact Name: `ytbl-build-deps-v1`
- Artifact ID: `10480406146`
- File: `ytbl-build-deps-v1.tar.gz`
- Size: `3966031` bytes (artifact ZIP)
- SHA256: `6443e75fcf2cf6f0a92309933be4df28d018815548d305cebcc7423c9268d5ad` (artifact digest)
- Created At: `2026-09-17T04:11:37Z`
- Expires At: `2026-12-16T04:11:29Z`
- Storage Mode: `SINGLE`
- Original File: `ytbl-build-deps-v1.tar.gz`
- Original Size: `3969507` bytes
- Original SHA256: `abe81599d03de3f37a1215bba236b824d7c733477a1ac68f5530be195d85e66e`
- Part Count: `1`

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Ytbl build dependencies | imgui1.91.9b+1.92.5-khronos-20260917-v1 | Any | Any | `ytbl-build-deps-v1.tar.gz` | `abe81599d03de3f37a1215bba236b824d7c733477a1ac68f5530be195d85e66e` |

Contains official ImGui sources with their MIT license and official Khronos API headers. Individual file hashes are in CONTENT_SHA256SUMS.txt.
## Fortune AI skills bundle 2026-09-19

- Workflow: `.github/workflows/fetch-fortune-skills-20260919.yml` (temporary fetch branch; artifact retained, workflow branch not intended as permanent source)
- Run ID: `35427966584`
- Run Number: `1`
- Run Conclusion: `success`
- Source repositories: `xuemian168/bazi-skill`, `mingze21/bazi-ziwei-skill`, `weizeW/mingli-skills`, `ShousenZHANG/chinese-fortune`, `ai-freer/fortune-skill`
- Storage Mode: `SINGLE`
- Artifact Name: `fortune-skills-20260919-v1`
- Artifact ID: `10579343266`
- Artifact ZIP Size: `9749419` bytes
- Artifact Digest: `sha256:2c389cfacf7675ff50cf3f2f424898f1bf7d75f7df4a2ac1af48c9b35ace0c97`
- Created At: `2026-09-19T06:56:35Z`
- Expires At: `2026-12-18T06:56:23Z`

### Restore

Download Artifact `10579343266`, verify the ZIP digest above, then extract the five upstream repositories. The delivered integrated package is `fortune-skills-integrated-20260919-v1.tar.gz` and is a derived local integration artifact, not the upstream source archive.


## 逃跑吧！少年 4399 channel APK 8.41.0

- Name: 逃跑吧！少年 4399 channel APK
- Version: 8.41.0
- Package: `com.bairimeng.dmmdzz.m4399`
- Version Code: `84100000`
- Game ID: `120610`
- Platform: Android
- Architecture: Multi-ABI APK
- Workflow: `.github/workflows/fetch-tpbsn-4399-latest.yml`
- Run ID: `36448082222`
- Run Conclusion: `success`
- Source Metadata API: `https://cdn.yxhapi.com/android/box/game/v6.3/apk.html?id=120610`
- Source Transport: official 4399 GameBox Zstandard APK transport, resolved dynamically from metadata API
- Required Download UA: `4399GameCenter/9.6.0.47 (Android 16)`
- Storage Mode: `SPLIT`
- Original File: `tpbsn-4399-latest.apk`
- Original Size: `1883026337` bytes
- Original MD5: `ff7d47d04ab5a95351fc433b19752447`
- Original SHA256: `258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6`
- Part Count: `3`
- Split Size: `700 MiB` for parts 00/01
- Recombined SHA256: `258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6`
- Created At: `2026-09-28T16:03:39Z` (metadata artifact; APK parts completed by 16:04:01Z)
- Expires At: `2026-12-27T16:02:11Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| 逃跑吧！少年 4399 channel APK | 8.41.0 | Android | Multi-ABI APK | `tpbsn-4399-latest.apk` (recombine parts 00+01+02) | `258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Size | Artifact Size | Artifact Digest | Expires At |
|---:|---:|---|---:|---:|---|---|
| metadata | `10982240821` | `tpbsn-4399-latest-metadata` | small metadata set | `3041` | `sha256:971ee74b09ccf67053324626cf69432a4549d71d2b4c6da8556284fe0024ee6b` | `2026-12-27T16:02:11Z` |
| 1/3 | `10981791088` | `tpbsn-4399-latest-apk-part-00` | `734003200` | `734003372` | `sha256:d91ef4cf86675259ae079e85dac564c07d57aa2c11738df1f332c53b216c0707` | `2026-12-27T16:02:11Z` |
| 2/3 | `10981791119` | `tpbsn-4399-latest-apk-part-01` | `734003200` | `734003372` | `sha256:f4a947742574e49143ee91860b12150eee1167a6ba90344a2db30d988b2590c8` | `2026-12-27T16:02:11Z` |
| 3/3 | `10982205832` | `tpbsn-4399-latest-apk-part-02` | `415019937` | `415020109` | `sha256:197e2441fb16306c4769e55304e71b24a5cb85e4ab46532a825c3bb69dd0406b` | `2026-12-27T16:02:11Z` |

### Restore

下载并解压三个 APK part Artifact，得到 `tpbsn-4399-latest.apk.part.00`、`.01`、`.02`，然后：

```bash
cat tpbsn-4399-latest.apk.part.00 \
    tpbsn-4399-latest.apk.part.01 \
    tpbsn-4399-latest.apk.part.02 > tpbsn-4399-8.41.0.apk

echo '258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6  tpbsn-4399-8.41.0.apk' | sha256sum -c -
echo 'ff7d47d04ab5a95351fc433b19752447  tpbsn-4399-8.41.0.apk' | md5sum -c -
```

AAPT verification from the successful fetch run: package `com.bairimeng.dmmdzz.m4399`, versionName `8.41.0`, versionCode `84100000`, minSdk `24`, targetSdk `31`.


## ARM64 system lab Debian 13 v1

- Name: `ARM64 system lab`
- Version: `debian13-v1-qemu10.0.13-linux6.12.111`
- Platform: `Linux / Debian 13`
- Architecture: `x86_64 host + AArch64 guest`
- Workflow: `.github/workflows/fetch-arm64-system-lab-debian13.yml`
- Run ID: `36566866696`
- Artifact ID: `11032351529`
- Artifact Name: `arm64-system-lab-debian13-v1`
- File: `arm64-system-lab-debian13-v1.zip`
- Size: `122163597 bytes`
- SHA256: `64fdcf5d1843bedfe0012cb19667f4b2865f81b835033d6f296a01e3dce7599a`
- Created At: `2026-09-29T12:15:26Z`
- Expires At: `2026-12-28T12:15:02Z`
- Storage: `SINGLE`
- Original File: `arm64-system-lab-debian13-v1.tar`
- Original Size: `122163200 bytes`
- Original SHA256: `1819458934fb118d7b11bf9564aa8fb4c6882a932d6fada0dc76ac58dcf44ca1`
- Part Count: `1`

Public Debian packages only: QEMU system 10.0.13, Linux 6.12.111+deb13-arm64, ARM64 BusyBox, GDB server, strace, runtime libraries, and package hashes. Contains no user sample, Android rootfs, memory dump, or private research files.

Restore: download artifact 11032351529; verify ZIP, inner TAR, and meta/SHA256SUMS.txt hashes before use.
## 逃跑吧！少年 4399 channel APK 8.41.0 - 400MiB rechunk

- Workflow: `.github/workflows/rechunk-tpbsn-4399-apk-400m.yml`
- Workflow Name: `Rechunk TPBSN 4399 APK 400M`
- Run ID: `36716019163`
- Source Cache Run ID: `36448082222`
- Source Cache Storage: previous `SPLIT × 3` artifacts were valid on GitHub but `part-00/01` artifact archives exceeded the 512MB connector download ceiling, so this rechunk cache is the container-restorable record.
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Storage Mode: `SPLIT`
- Original File: `tpbsn-4399-8.41.0.apk`
- Original Size: `1883026337` bytes
- Original MD5: `ff7d47d04ab5a95351fc433b19752447`
- Original SHA256: `258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6`
- Part Count: `5`
- Split Size: `400MiB`
- Created At: `2026-09-30T12:38:45Z`
- Expires At: `2026-12-29T12:38:04Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| 逃跑吧！少年 4399 channel APK | 8.41.0 | Android | Multi-ABI APK | `tpbsn-4399-8.41.0.apk` | `258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| metadata | `11096017872` | `tpbsn-4399-8.41.0-rechunk-metadata` | small metadata set | n/a | `2712` | `sha256:352209b0e8fdf6d0e346f6ddae8a56d563c1ccead8456d840f1fe1fa7941c68b` | `2026-09-30T12:38:45Z` | `2026-12-29T12:38:04Z` |
| 1/5 | `11096586223` | `tpbsn-4399-8.41.0-apk-400m-part-00` | `419430400` | `82512e9997881652ce652ee9f0ea6505111c611c9b7d01120aead4299edc4dbd` | `419430572` | `sha256:de590ee2d1304e054541b63e292f005b3d246f4b4bdccd194c4f427ab914f6fc` | `2026-09-30T12:38:48Z` | `2026-12-29T12:38:04Z` |
| 2/5 | `11096481096` | `tpbsn-4399-8.41.0-apk-400m-part-01` | `419430400` | `233a257114372ea9716a65c6871e05947695fcf08845f6ac10f0c3751402e7b8` | `419430572` | `sha256:2a4269fa9440e6472956ad35f805023df8fd3bf1218792bb24a1ddfd6900f926` | `2026-09-30T12:38:50Z` | `2026-12-29T12:38:04Z` |
| 3/5 | `11096206959` | `tpbsn-4399-8.41.0-apk-400m-part-02` | `419430400` | `5121514a4018c0e7de8f3d5bc87e002a9b0a04a4292b7074d3357865861faf09` | `419430572` | `sha256:2bf1c63532e15e9aad3cc2cd0d2a407841ed10cfb4ae496986eb30af766260b0` | `2026-09-30T12:38:53Z` | `2026-12-29T12:38:04Z` |
| 4/5 | `11095434842` | `tpbsn-4399-8.41.0-apk-400m-part-03` | `419430400` | `6eab1859974f759e0578243894a7056d66cedb5542ec4fae140e17258c908ddf` | `419430572` | `sha256:a2a72d4665777d623556f5bc97f0e0e9574b3a80149903cd8db28f6edaafba1a` | `2026-09-30T12:38:56Z` | `2026-12-29T12:38:04Z` |
| 5/5 | `11096875511` | `tpbsn-4399-8.41.0-apk-400m-part-04` | `205304737` | `c25154e13cb978b4936027fe99d8c5ab0343e2e0b1ed5be446ceb33b94c7dab6` | `205304909` | `sha256:eebc471a1fedc7a63d9f6c6fdfe43208a6037db9e136f5d1a24c19a358a638bd` | `2026-09-30T12:38:57Z` | `2026-12-29T12:38:04Z` |

### Restore

下载 metadata Artifact `11096017872` 与 5 个 part Artifact `11096586223`, `11096481096`, `11096206959`, `11095434842`, `11096875511`；分别解压得到 `tpbsn-4399-8.41.0.apk.part-00` 到 `part-04`，按序拼接为 `tpbsn-4399-8.41.0.apk`，最后校验完整文件 SHA256 `258ac3675fc71fbc0b90d0d59d93658d844610e46964017a97dbfae3ec16a1a6`。


## 火影忍者 Tencent official APK 1.79.79.9 - verified 200MiB split

- Name: 火影忍者 Tencent official APK
- Version: 1.79.79.9
- Package: `com.tencent.KiHan`
- Version Code: `1079079009`
- Platform: Android
- Architecture: Multi-ABI APK (`arm64-v8a`, `armeabi-v7a`)
- Workflow: `.github/workflows/rechunk-naruto-200m.yml` (temporary branch `tmp/fetch-naruto-20261001`)
- Workflow Name: `Rechunk Verified Naruto APK 200MiB`
- Run ID: `36817118721`
- Source Fetch Run ID: `36815808636`
- Run Conclusion: `success`
- Source: Tencent 应用宝 official distribution for `com.tencent.KiHan`
- Source URL: `http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/1CE28CDBBE7AE3EA5CDC9A083DFB9857.apk?fsname=com.tencent.KiHan_1.79.79.9.apk`
- Storage Mode: `SPLIT`
- Original File: `naruto-1.79.79.9.apk`
- Original Size: `1735650312` bytes
- Original MD5: `1ce28cdbbe7ae3ea5cdc9a083dfb9857`
- Original SHA256: `5582bd1394f1438537829cb65bb486688ca2addc305c7a9717a7cf20b7eaa1b9`
- Recombined SHA256: `5582bd1394f1438537829cb65bb486688ca2addc305c7a9717a7cf20b7eaa1b9`
- Part Count: `9`
- Split Size: `200 MiB` for parts 00-07
- Created At: `2026-10-01T04:53:03Z` (metadata artifact; part artifacts completed by `2026-10-01T04:53:31Z`)
- Expires At: `2026-12-30T04:52:19Z`
- Requested Retention: `90 days` (repository is public; existing cache records establish an effective 90-day cap)
- Effective Retention: `90 days` (actual GitHub `expires_at`)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| 火影忍者 Tencent official APK | 1.79.79.9 | Android | arm64-v8a + armeabi-v7a | `naruto-1.79.79.9.apk` (recombine parts 00-08) | `5582bd1394f1438537829cb65bb486688ca2addc305c7a9717a7cf20b7eaa1b9` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| metadata | `11141359547` | `naruto-1.79.79.9-verified-metadata` | small metadata set | n/a | `4506` | `sha256:7cb9adaa65eb47808fd62013520d5e16c7e0add76e1e8e02a7ea3f9a0d1a95b7` | `2026-10-01T04:53:03Z` | `2026-12-30T04:52:19Z` |
| 1/9 | `11141309461` | `naruto-1.79.79.9-apk-200m-part-00` | `209715200` | `7402956f782b944df43412e04ec71fac49814889e3fb65a9e09a227b710e0b59` | `209715370` | `sha256:75578e684a4b272f3caef7c0b3c6968c309886f4bb4d6953769a913460b4f8db` | `2026-10-01T04:53:06Z` | `2026-12-30T04:52:19Z` |
| 2/9 | `11142255606` | `naruto-1.79.79.9-apk-200m-part-01` | `209715200` | `64c2848decf3b6ba34332afbb183e2d94010d02d8e277dfda7688c259bb137e7` | `209715370` | `sha256:b96edbec2b96ab4f171f5c0d5bab63a58cefca7ededce959469dce3059e99a0c` | `2026-10-01T04:53:09Z` | `2026-12-30T04:52:19Z` |
| 3/9 | `11141194843` | `naruto-1.79.79.9-apk-200m-part-02` | `209715200` | `37dc4782e2b849e5be00dd1d7d3bf444fc29592dfc8ffb6dc3bf3ec875bb2cd8` | `209715370` | `sha256:b2aab5dc4a597de3563b4e71f79b230dc7b7e4df4a0e6c1d084ab944dda4faf0` | `2026-10-01T04:53:13Z` | `2026-12-30T04:52:19Z` |
| 4/9 | `11141184990` | `naruto-1.79.79.9-apk-200m-part-03` | `209715200` | `bdc87d7b20bebcbe882d3d70ce13ee24b75e2df27bb4a9380b9a2186a1e5221c` | `209715370` | `sha256:d608d4a270eec97be7a755d2fb25b8ec8605ac3e7520988f9c721dde4952f2a3` | `2026-10-01T04:53:16Z` | `2026-12-30T04:52:19Z` |
| 5/9 | `11142245673` | `naruto-1.79.79.9-apk-200m-part-04` | `209715200` | `74bbd33c47b748b98d7d403d9c010cf5a85fb1a6a8a6bdbaaec05a267efb321f` | `209715370` | `sha256:52c00baa944d2fc7f86c435c83e335e9b684a49382726f906aba4854152c69df` | `2026-10-01T04:53:19Z` | `2026-12-30T04:52:19Z` |
| 6/9 | `11142240675` | `naruto-1.79.79.9-apk-200m-part-05` | `209715200` | `9721dc39f50c3db2189b8971c37e309d442ad9ce699836ee287e5a09ef6b79eb` | `209715370` | `sha256:efedb270ad04a8358f1241c1d3fc87cb487acdadd1149a8fa45e3ea05f4f4ea5` | `2026-10-01T04:53:23Z` | `2026-12-30T04:52:19Z` |
| 7/9 | `11142250687` | `naruto-1.79.79.9-apk-200m-part-06` | `209715200` | `354ad70526613bda0e60395c6fb50533e91a719f9a0d31537368ad346e34a280` | `209715370` | `sha256:aacbf58beb6cf19e86c11a2005288c5f13167349ce463a773162d65056bf12bd` | `2026-10-01T04:53:26Z` | `2026-12-30T04:52:19Z` |
| 8/9 | `11142305362` | `naruto-1.79.79.9-apk-200m-part-07` | `209715200` | `3a38a4533b382a3aceee7f323e713811055f088c6a5bd2d2261b6bd4fb78e238` | `209715370` | `sha256:8c3ad5a3411dab2e7b4d1c59e94b0874b61180b2794b6feac58f7e52cbd3e017` | `2026-10-01T04:53:29Z` | `2026-12-30T04:52:19Z` |
| 9/9 | `11142430023` | `naruto-1.79.79.9-apk-200m-part-08` | `57928712` | `2ef071f55491d919c8072ef68373b28c10b8116745ac66891c5981e6ca3b1b60` | `57928882` | `sha256:e673ac258915ba5289d219c27abb676fde73e206bbee74e273c42816b7c6675b` | `2026-10-01T04:53:31Z` | `2026-12-30T04:52:19Z` |

### Restore

下载 metadata Artifact `11141359547` 与 9 个 APK part Artifact `11141309461`, `11142255606`, `11141194843`, `11141184990`, `11142245673`, `11142240675`, `11142250687`, `11142305362`, `11142430023`。解压 part Artifact 后按 `part-00` 到 `part-08` 顺序拼接为 `naruto-1.79.79.9.apk`，最终校验 SHA256 `5582bd1394f1438537829cb65bb486688ca2addc305c7a9717a7cf20b7eaa1b9` 与 MD5 `1ce28cdbbe7ae3ea5cdc9a083dfb9857`。AAPT 已验证 package `com.tencent.KiHan`、versionName `1.79.79.9`、versionCode `1079079009`，native-code 为 `arm64-v8a` 与 `armeabi-v7a`。


## radare2 6.2.2 Linux x86_64

- Name: `radare2`
- Version: `6.2.2`
- Platform: `Linux / Debian`
- Architecture: `x86_64`
- Workflow: `.github/workflows/fetch-radare2-6.2.2-amd64.yml`
- Run ID: `36873712969`
- Run Number: `1`
- Run Conclusion: `success`
- Source: official radareorg/radare2 GitHub release asset
- Source File: `radare2_6.2.2_amd64.deb`
- Storage Mode: `SINGLE`
- Artifact Name: `radare2-6.2.2-linux-x86_64`
- Artifact ID: `11168472545`
- Artifact ZIP Size: `8582514` bytes
- Artifact ZIP SHA256 / Digest: `a627196da624e8aa7f1764d6ddb99c796e28f0b59ed5fae20fe492bc2212e90f`
- Original File: `radare2_6.2.2_amd64.deb`
- Original Size: `8579612` bytes
- Original SHA256: `09234e4139bf8dfcbb7fc1fdb2519859ad516e63c19d3c27d92aaecdf463b1ad`
- Part Count: `1`
- Created At: `2026-10-01T14:06:19Z`
- Expires At: `2026-12-30T14:06:12Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| radare2 | 6.2.2 | Linux / Debian | x86_64 | `radare2_6.2.2_amd64.deb` | `09234e4139bf8dfcbb7fc1fdb2519859ad516e63c19d3c27d92aaecdf463b1ad` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `11168472545` | `radare2-6.2.2-linux-x86_64` | `8579612` | `09234e4139bf8dfcbb7fc1fdb2519859ad516e63c19d3c27d92aaecdf463b1ad` | `8582514` | `sha256:a627196da624e8aa7f1764d6ddb99c796e28f0b59ed5fae20fe492bc2212e90f` | `2026-10-01T14:06:19Z` | `2026-12-30T14:06:12Z` |

### Restore

Download Artifact `11168472545`, verify the Artifact ZIP SHA256 `a627196da624e8aa7f1764d6ddb99c796e28f0b59ed5fae20fe492bc2212e90f`, extract `radare2_6.2.2_amd64.deb`, then verify its SHA256 `09234e4139bf8dfcbb7fc1fdb2519859ad516e63c19d3c27d92aaecdf463b1ad` before installing.


## Debian 13 binutils host repair 2.44-3

- Workflow: `.github/workflows/tmp-fetch-debian13-binutils-2.44-20261001.yml` on temporary branch `tmp/repair-debian13-binutils-20261001`
- Workflow Name: `Temporary fetch Debian 13 binutils 2.44 repair`
- Run ID: `36876468018`
- Run Conclusion: `success`
- Source: Debian trixie official package pool at `https://deb.debian.org/debian/pool/main/b/binutils/`
- Repository Visibility: `Public`
- Requested Retention: `90 days`
- Storage Mode: `SINGLE`
- Artifact Name: `debian13-binutils-2.44-repair-amd64`
- Artifact ID: `11169466690`
- Artifact Archive Size: `3044472` bytes
- Artifact Archive SHA256 / Digest: `8596cfe7c823d64bc2df16b8bd8720bad8110b5e03b31f948952d8600526aa33`
- Part Count: `1`
- Created At: `2026-10-01T14:27:34Z`
- Expires At: `2026-12-30T14:27:26Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | Size | SHA256 |
|---|---|---|---|---|---:|---|
| Debian binutils-common | 2.44-3 | Debian 13 / Linux | x86_64 | `binutils-common_2.44-3_amd64.deb` | `2508768` | `002da5d23f8757dee97a2c0a40e0e1d4d85a43da094488ee2ee7068d4d3691f9` |
| Debian libbinutils | 2.44-3 | Debian 13 / Linux | x86_64 | `libbinutils_2.44-3_amd64.deb` | `534440` | `4f4664c8a8f0ad0c8631c39fab02e3d8d86ccc6f4436a1d59f059dbcb0492679` |

### Restore

Download Artifact `11169466690`, verify ZIP SHA256 `8596cfe7c823d64bc2df16b8bd8720bad8110b5e03b31f948952d8600526aa33`, extract the two Debian packages, verify the per-file SHA256 values above, then install both with `dpkg -i`. This cache is for restoring Debian 13 host binutils 2.44 shared libraries after testing the isolated Debian 12 GDB bundle; it must not be mixed into the isolated GDB root.


## PUBG MOBILE Global Base APK 4.6.0 (21525)

- Name: PUBG MOBILE Global Base APK
- Version: 4.6.0
- Version Code: `21525`
- Package: `com.tencent.ig`
- Platform: Android
- Architecture: `arm64-v8a`
- Region: Global
- Workflow: `.github/workflows/fetch-pubg-global-arm64-apk.yml`
- Workflow Name: `Fetch PUBG Global ARM64 Base APK`
- Run ID: `37217716536`
- Run Conclusion: `success`
- Source: APKMirror / Level Infinite, latest PUBG MOBILE arm64-v8a OBB-bundle release; workflow selects its separate Base APK download and does not download the OBB
- Source Page: `https://www.apkmirror.com/apk/level-infinite/playerunknowns-battlegrounds-pubg-mobile/pubg-mobile-4-6-0-release/pubg-mobile-4-6-0-2-android-apk-download/`
- Storage Mode: `SINGLE`
- Artifact Name: `pubg-mobile-global-4.6.0-21525-arm64-v8a`
- Artifact ID: `11308584380`
- Artifact ZIP Size: `107406885` bytes
- Artifact Digest: `sha256:677af3e93aa55b485613352eb58f9eec93ae4d79d0803a6431ba4c80d2b68e58`
- Original File: `PUBG-MOBILE-Global-4.6.0-21525-arm64-v8a.apk`
- Original Size: `107399819` bytes
- Original MD5: `ac9ba3006c7c1dcdddf320f8e821f9c7`
- Original SHA256: `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696`
- Part Count: `1`
- Created At: `2026-10-04T16:42:04Z`
- Expires At: `2027-01-02T16:41:47Z`
- OBB Downloaded: `no`
- Verification: AAPT confirmed `com.tencent.ig`, versionName `4.6.0`, versionCode `21525`; ZIP and AAPT both confirmed native ABI is only `arm64-v8a`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| PUBG MOBILE Global Base APK | 4.6.0 (21525) | Android | arm64-v8a | `PUBG-MOBILE-Global-4.6.0-21525-arm64-v8a.apk` | `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `11308584380` | `pubg-mobile-global-4.6.0-21525-arm64-v8a` | `107399819` | `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696` | `107406885` | `sha256:677af3e93aa55b485613352eb58f9eec93ae4d79d0803a6431ba4c80d2b68e58` | `2026-10-04T16:42:04Z` | `2027-01-02T16:41:47Z` |

### Restore

下载 Artifact `11308584380`，校验 Artifact ZIP digest `677af3e93aa55b485613352eb58f9eec93ae4d79d0803a6431ba4c80d2b68e58`；解压得到 `PUBG-MOBILE-Global-4.6.0-21525-arm64-v8a.apk`，再校验 APK SHA256 `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696`。该缓存只包含 Base APK 和校验元数据，不包含 `.obb`。


## libUE4 GL 4.6 v1.0.1

- Name: `libUE4 GL`
- Version: `4.6-v1.0.1`
- PUBG Version: `4.6.0`
- PUBG Version Code: `21525`
- PUBG Package: `com.tencent.ig`
- Platform: Android
- Architecture: AArch64 / `arm64-v8a`
- Workflow: `.github/workflows/fetch-pubg-global-arm64-apk.yml`
- Workflow Name: `Sync PUBG Global ARM64 libUE4`
- Run ID: `37218608943`
- Run Attempt 1: `success` — detected missing release asset, downloaded the ARM64 Base APK, extracted and uploaded libUE4
- Run Attempt 2: `success` — detected the asset already existed and skipped APK download, extraction, release upload, and verification Artifact upload
- Release Tag: `v1.0.1`
- Release Asset: `libUE4-GL-4.6.so`
- Release Asset ID: `610224470`
- Release Asset Size: `252290584` bytes
- Release Asset SHA256: `abb9343f69735378b6aea4db97a66e9789664075b0196b1b99378514052454ce`
- Release Asset URL: `https://github.com/jepede/gpt-exten/releases/download/v1.0.1/libUE4-GL-4.6.so`
- Source APK: `PUBG-MOBILE-Global-4.6.0-21525-arm64-v8a.apk`
- Source APK Size: `107399819` bytes
- Source APK SHA256: `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696`
- Extracted Path: `lib/arm64-v8a/libUE4.so`
- Verification: extracted file is ELF64, machine `AArch64`; APK package/version/ABI were verified before extraction
- Storage Mode: `SINGLE`
- Verification Artifact Name: `pubg-global-4.6.0-21525-libue4-sync`
- Verification Artifact ID: `11309845408`
- Verification Artifact ZIP Size: `359700188` bytes
- Verification Artifact Digest: `sha256:816ab7a7b41a2ae5c45a4d4c0373fde6eab42e561bd5c01eced4f8bd05a065ab`
- Created At: `2026-10-04T16:56:46Z`
- Expires At: `2027-01-02T16:56:20Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | Size | SHA256 |
|---|---|---|---|---|---:|---|
| libUE4 GL | 4.6-v1.0.1 | Android | AArch64 | `libUE4-GL-4.6.so` | `252290584` | `abb9343f69735378b6aea4db97a66e9789664075b0196b1b99378514052454ce` |
| PUBG MOBILE Global Base APK | 4.6.0 (21525) | Android | arm64-v8a | `PUBG-MOBILE-Global-4.6.0-21525-arm64-v8a.apk` | `107399819` | `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696` |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact Digest | Expires At |
|---:|---:|---|---:|---|---|
| 1/1 | `11309845408` | `pubg-global-4.6.0-21525-libue4-sync` | `359700188` | `sha256:816ab7a7b41a2ae5c45a4d4c0373fde6eab42e561bd5c01eced4f8bd05a065ab` | `2027-01-02T16:56:20Z` |

### Restore

优先直接使用 Release `v1.0.1` 的 `libUE4-GL-4.6.so`。若按联网缓存规则恢复，则下载 Artifact `11309845408`，校验 Artifact ZIP digest `816ab7a7b41a2ae5c45a4d4c0373fde6eab42e561bd5c01eced4f8bd05a065ab`，解压得到 `libUE4-GL-4.6.so` 后再校验 SHA256 `abb9343f69735378b6aea4db97a66e9789664075b0196b1b99378514052454ce`。


## Mozilla NSS TLS Root Store release-b9bd270cfa3e-20261005

- Name: Mozilla NSS TLS Root Store
- Version: release-b9bd270cfa3e-20261005
- Source: Mozilla Firefox release branch NSS `security/nss/lib/ckfw/builtins/certdata.txt`
- Firefox Release Commit: `b9bd270cfa3ea2f17871975ac8fa5a5afdf93842`
- certdata.txt SHA256: `beb7e6dfe6499926e52c075c27bcfbe4c957f8609c575b3860273ae2806f63eb`
- Selection: Mozilla NSS `SERVER_AUTH` + `TRUSTED_DELEGATOR`, cross-checked with curl 8.22.0 official `mk-ca-bundle.pl`
- TLS Server Trust Anchors: `121`
- Workflow: `.github/workflows/fetch-mozilla-nss-rootstore-20261005.yml`
- Run ID: `37253767754`
- Run Conclusion: `success`
- Requested Retention: `400 days`
- Storage Mode: `SINGLE`
- Artifact Name: `mozilla-nss-tls-rootstore-20261005`
- Artifact ID: `11321254343`
- Artifact ZIP Size: `514597` bytes
- Artifact ZIP SHA256 / Digest: `5a73a5d0fd3a57092367ddcdd8a0887f48b568ec21d111332232aa1a25a28145`
- Original File: `mozilla-nss-tls-rootstore-20261005.tar.gz`
- Original Size: `514175` bytes
- Original SHA256: `c0761aa6e48fd7c81852f0e7a1125bb4b89b212f32b4cf74742c834f8a754e97`
- Part Count: `1`
- Created At: `2026-10-05T02:02:16Z`
- Expires At: `2027-01-03T02:02:10Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Mozilla NSS certdata | Firefox release `b9bd270cfa3e` | Any | Any | `certdata.txt` | `beb7e6dfe6499926e52c075c27bcfbe4c957f8609c575b3860273ae2806f63eb` |
| Mozilla TLS Root Store DER pack | THCA2 / 121 roots | Any | Any | `mozilla-tls-roots.thca` | `ec2aeb1a6cbfcb9cad4a5842d8f24d9273c10596219d6559fb62910c433f486f` |
| Mozilla TLS Root Store PEM | 121 roots | Any | Any | `mozilla-tls-roots.pem` | `bc96d4f2521bed110477519f2c9695e120ca4ad3a2c9bf09fad947abc863517a` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `11321254343` | `mozilla-nss-tls-rootstore-20261005` | `514175` | `c0761aa6e48fd7c81852f0e7a1125bb4b89b212f32b4cf74742c834f8a754e97` | `514597` | `sha256:5a73a5d0fd3a57092367ddcdd8a0887f48b568ec21d111332232aa1a25a28145` | `2026-10-05T02:02:16Z` | `2027-01-03T02:02:10Z` |

### Restore

Download Artifact `11321254343`, verify Artifact ZIP SHA256 `5a73a5d0...`, extract `mozilla-nss-tls-rootstore-20261005.tar.gz`, verify SHA256 `c0761aa6...`, then verify `source.sha256` and `generated.sha256` inside the TAR before use.


## TinyHTTPS OpenSSL 4.0.3 + curl 8.22.0 reference sources

- Name: `TinyHTTPS OpenSSL + curl reference sources`
- Version: `OpenSSL 4.0.3 + curl 8.22.0`
- Platform: Any
- Architecture: Any
- Workflow: `.github/workflows/cache-tinyhttps-reference-sources.yml`
- Workflow Name: `Cache TinyHTTPS OpenSSL curl reference sources`
- Run ID: `37458536791`
- Run Conclusion: `success`
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: actual GitHub expiry below
- Storage Mode: `SINGLE`
- Artifact Name: `tinyhttps-openssl-4.0.3-curl-8.22.0-sources`
- Artifact ID: `11411116830`
- Artifact Archive Size: `59117818` bytes
- Artifact Archive SHA256 / Digest: `608684e7f70296d287fc33a3e673efb4c59588d9db72812f49af55e147ee172e`
- Original File: `openssl-4.0.3.tar.gz` + `curl-8.22.0.tar.gz`
- Original Size: `59116768` bytes combined
- Original SHA256: OpenSSL `29cbaaabad1f3b0e8f28274eb8445a1cb0c54af21a6f845882ee018763df7159`; curl `222c6b5c1f368ac63aed59bce2774eb5def9e8e67e46e800be182e684d2845a3`
- Source Manifest SHA256: `64ff386c25b282641db60c57e4ba19cec40becaf26deee322aacbbdbcc54deee`
- Part Count: `1`
- Created At: `2026-10-06T11:45:45Z`
- Expires At: `2027-01-04T11:45:33Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| OpenSSL source | 4.0.3 | Any | Any | `openssl-4.0.3.tar.gz` | `29cbaaabad1f3b0e8f28274eb8445a1cb0c54af21a6f845882ee018763df7159` |
| curl source | 8.22.0 | Any | Any | `curl-8.22.0.tar.gz` | `222c6b5c1f368ac63aed59bce2774eb5def9e8e67e46e800be182e684d2845a3` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `11411116830` | `tinyhttps-openssl-4.0.3-curl-8.22.0-sources` | `59116768` combined | per-file hashes above | `59117818` | `sha256:608684e7f70296d287fc33a3e673efb4c59588d9db72812f49af55e147ee172e` | `2026-10-06T11:45:45Z` | `2027-01-04T11:45:33Z` |

### Restore

Download Artifact `11411116830`, verify the Artifact ZIP SHA256 `608684e7f70296d287fc33a3e673efb4c59588d9db72812f49af55e147ee172e`, extract both source archives, then verify `SHA256SUMS.txt`. OpenSSL 4.0.3 must match `29cbaaabad1f3b0e8f28274eb8445a1cb0c54af21a6f845882ee018763df7159`; curl 8.22.0 must match `222c6b5c1f368ac63aed59bce2774eb5def9e8e67e46e800be182e684d2845a3`.


## Artifact Record: JNI Vulkan complete project vulkan1.1-imgui1.92.5-ndk28c-94b51d98a2f9

- Name: JNI Vulkan complete project
- Version: vulkan1.1-imgui1.92.5-ndk28c-94b51d98a2f9
- Platform: Android API 31+
- Architecture: arm64-v8a
- Artifact Name: `jni-vulkan-full`
- Artifact ID: `11636698531`
- Run ID: `37973436668`
- Workflow: `.github/workflows/jni-vulkan-20261010.yml`
- File: `jni_vulkan_full.zip` (downloaded Artifact ZIP, project at archive root)
- Size: `6810583`
- SHA256: `e6fe83cb7c5d44b3f8b113897b94f828f474ba41d50fe9cc2edbcd1e5ca76ebe`
- Created At: `2026-10-09T18:29:31Z`
- Expires At: `2027-01-07T18:27:46Z`
- Storage Mode: SINGLE
- Original File: `jni_vulkan_full.zip` (delivery archive itself)
- Original Size: `6810583`
- Original SHA256: `e6fe83cb7c5d44b3f8b113897b94f828f474ba41d50fe9cc2edbcd1e5ca76ebe`
- Part Count: 1
- Verification: Android release/debug builds, host input sanitizer tests, host real Vulkan rendering, delivered ZIP CRC and internal SHA256 hashes passed. Android device presentation not tested.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| JNI Vulkan complete project | vulkan1.1-imgui1.92.5-ndk28c-94b51d98a2f9 | Android API 31+ | arm64-v8a | Artifact ZIP root | `e6fe83cb7c5d44b3f8b113897b94f828f474ba41d50fe9cc2edbcd1e5ca76ebe` |
| libAndroid.so | vulkan1.1-imgui1.92.5-ndk28c-94b51d98a2f9 | Android API 31+ | arm64-v8a | `prebuilt/arm64-v8a/libAndroid.so` | `0dba79d501e6c56322ff4c384de020b2b04ca1e03e7855cb936f83eae637cb33` |
| libdobby.a | vulkan1.1-imgui1.92.5-ndk28c-94b51d98a2f9 | Android API 31+ | arm64-v8a | `jni/Library/dobby/arm64-v8a/libdobby.a` | `0a13c9ed67cfa8c384397d10e28f351ee1165ca74bf1b6422264cdc9d57dc66a` |


## Artifact Record: JNI1 Vulkan-only Complete v1.0 (2026-10-10)

- Name: JNI1 Vulkan-only Complete
- Version: Vulkan-only-v1.0-jni1-20261010
- Platform: Android API 31+
- Architecture: arm64-v8a
- Artifact Name: `jni1-vulkan-only-full-source-binaries`
- Artifact ID: `11652900609`
- Run ID: `38008777577`
- Workflow: `.github/workflows/jni-vulkan-direct-delivery.yml`
- File: `jni1-vulkan-only-full-arm64.zip`
- Size: `12687674` bytes
- SHA256: `cf6664b14254de267d26f8d4c991a793d527958823ec934348ce52b5d0774cda`
- Created At: `2026-10-10T00:22:45Z`
- Expires At: `2027-01-08T00:22:37Z`
- Storage Mode: SINGLE
- Original File: `jni1-vulkan-only-full-arm64.zip`
- Original Size: `12687674` bytes
- Original SHA256: `cf6664b14254de267d26f8d4c991a793d527958823ec934348ce52b5d0774cda`
- Part Count: 1
- Source: `jni1.zip` uploaded by the user; compiled ARM64 .so from GitHub Actions Run `37974144680`.
- Validation: original JNI ZIP CRC; migrated Android ARM64 compilation; ELF DT_NEEDED includes Vulkan but no EGL/GLES; flattened project content check; SHA256 manifest. Physical Android runtime not tested.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| JNI1 Vulkan-only Complete | Vulkan-only-v1.0-jni1-20261010 | Android API 31+ | arm64-v8a | `jni1-vulkan-only-full-arm64.zip` | `cf6664b14254de267d26f8d4c991a793d527958823ec934348ce52b5d0774cda` |


## Artifact Record: JNI1 Vulkan Surface Lifecycle Fix v2

- Name: JNI Vulkan Surface Lifecycle Fix
- Version: v2-supervisor-backpressure-20261010
- Platform: Android API 31+
- Architecture: arm64-v8a
- Artifact Name: `jni-vulkan-surface-lifecycle-fix-v1`
- Artifact ID: `11652034611`
- Run ID: `38010810572`
- Workflow: `.github/workflows/jni-vulkan-lifecycle-fix.yml`
- File: `jni-vulkan-surface-fix-v2-arm64.zip`
- Size: `12703450` bytes
- SHA256: `0b5621b3837e89324796362de8c8c89c566d9eff6afeaba5a5e8682a65260b49`
- Created At: `2026-10-10T00:52:01Z`
- Expires At: `2027-01-08T00:51:12Z`
- Storage Mode: SINGLE
- Original File: `jni-vulkan-surface-fix-v2-arm64.zip`
- Original Size: `12703450` bytes
- Original SHA256: `0b5621b3837e89324796362de8c8c89c566d9eff6afeaba5a5e8682a65260b49`
- Part Count: 1
- Source: cached complete project from Run `38008777577`, Artifact `11652900609`, originally derived from user `jni1.zip`.
- Verification: Android NDK r28c arm64 compilation success; Vulkan-only ELF dependencies; source SHA256SUMS pass; downloaded/uploaded Google Drive ZIP SHA256 independently verified with digest.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| JNI Vulkan Surface Lifecycle Fix | v2-supervisor-backpressure-20261010 | Android API 31+ | arm64-v8a | `jni-vulkan-surface-fix-v2-arm64.zip` | `0b5621b3837e89324796362de8c8c89c566d9eff6afeaba5a5e8682a65260b49` |



## Artifact Record: JNI Vulkan v3 Surface and Input Diagnostics

- Name: JNI Vulkan v3 Surface and Input Diagnostics
- Version: v3-rawtouch-suspendresume-compositor-20261010
- Platform: Android API 31+
- Architecture: arm64-v8a
- Artifact Name: `jni-vulkan-v3-surface-input-diagnostics`
- Artifact ID: `11655401892`
- Run ID: `38013414598`
- Workflow: `.github/workflows/jni-vulkan-v3-fix.yml`
- File: `JNI-Vulkan-v3-Surface-Input-Diagnostics.zip`
- Size: `12711556` bytes
- SHA256: `af80014eab64d25a88dc5798dd3f80eb83ea694ab9c4e5295acea4ec5425b66b`
- Created At: `2026-10-10T01:31:05Z`
- Expires At: `2027-01-08T01:30:09Z`
- Storage Mode: SINGLE
- Original File: `JNI-Vulkan-v3-Surface-Input-Diagnostics.zip`
- Original Size: `12711556` bytes
- Original SHA256: `af80014eab64d25a88dc5798dd3f80eb83ea694ab9c4e5295acea4ec5425b66b`
- Part Count: 1
- Source: cached Vulkan v2 project from Run `38010810572`, Artifact `11652034611`.
- Verification: NDK r28c ARM64 API31 compile success; readelf dynamic dependencies include libvulkan and exclude EGL/GLES; full file SHA256SUMS checked. Physical Android runtime not tested.
- Changes: indefinite geometry suspension/resume; sampled ASurfaceTransaction onComplete diagnostics; TAG YS; local/raw touch traces and raw coordinates default.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| JNI Vulkan v3 Surface and Input Diagnostics | v3-rawtouch-suspendresume-compositor-20261010 | Android API 31+ | arm64-v8a | `JNI-Vulkan-v3-Surface-Input-Diagnostics.zip` | `af80014eab64d25a88dc5798dd3f80eb83ea694ab9c4e5295acea4ec5425b66b` |



## Artifact Record: JNI Vulkan v4 Window and Touch Fix (2026-10-10)

- Name: JNI Vulkan v4 Window and Touch Fix
- Version: v4-enodev-dedup-calibration-20261010
- Platform: Android API 31+
- Architecture: arm64-v8a
- Artifact Name: `jni-vulkan-v4-input-layer-diagnostics`
- Artifact ID: `11655293904`
- Run ID: `38014372015`
- Workflow: `.github/workflows/jni-vulkan-v4-fix.yml`
- File: `JNI-Vulkan-v4-Window-Touch-Fix.zip`
- Size: `12722272` bytes
- SHA256: `112d319cb393fea7a9fd2d56d4df4f392535e725a2c10bccb1e76c77f7253756`
- Created At: `2026-10-10T01:45:45Z`
- Expires At: `2027-01-08T01:45:04Z`
- Storage Mode: SINGLE
- Original File: `JNI-Vulkan-v4-Window-Touch-Fix.zip`
- Original Size: `12722272` bytes
- Original SHA256: `112d319cb393fea7a9fd2d56d4df4f392535e725a2c10bccb1e76c77f7253756`
- Part Count: 1
- Build Inputs: cached Vulkan v3 Artifact ID `11655401892`, cached NDK r28c Artifact parts `9174697344` and `9174699121`.
- Verification: GitHub Actions ARM64 ndk-build success; libvulkan.so DT_NEEDED and no EGL/GLES; complete SHA256SUMS passed. Real game rendering / overlay visibility not verified.
- Changes: treats ANativeWindow negative width/height as fatal query errors (-19=-ENODEV); bounded zero-size wait; event timestamp+pointer dedup ring for MotionEvent::copyFrom; corrected pointerIndex logging; visual corner/crosshair calibration; YS logs.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| JNI Vulkan v4 Window and Touch Fix | v4-enodev-dedup-calibration-20261010 | Android API 31+ | arm64-v8a | `JNI-Vulkan-v4-Window-Touch-Fix.zip` | `112d319cb393fea7a9fd2d56d4df4f392535e725a2c10bccb1e76c77f7253756` |



## Artifact Record: JNI Vulkan v7.1 Clean Production ARM64 (2026-10-10)

- Name: JNI Vulkan v7.1 Clean Production ARM64
- Version: v7.1-clean-release-20261010
- Platform: Android API 31+ (tested baseline v7 on Android 16)
- Architecture: arm64-v8a
- Artifact Name: `jni-vulkan-v7-1-clean-production-arm64`
- Artifact ID: `11661779126`
- Run ID: `38031262676`
- Workflow: `.github/workflows/jni-vulkan-v7-clean-release.yml`
- File: `JNI-Vulkan-v7.1-Clean-Production-ARM64.zip`
- Size: `8024700` bytes
- SHA256: `664fa501312644af384a151f3e14e992ffbe5a2c3b659300da04805f8274169c`
- Created At: `2026-10-10T06:33:10Z`
- Expires At: `2027-01-08T06:31:58Z`
- Storage Mode: SINGLE
- Original File: `JNI-Vulkan-v7.1-Clean-Production-ARM64.zip`
- Original Size: `8024700` bytes
- Original SHA256: `664fa501312644af384a151f3e14e992ffbe5a2c3b659300da04805f8274169c`
- Part Count: 1
- Production `libAndroid.so` SHA256: `fa3de56692d6ebf45232b34a7e5a71cb74cf2b91aadbc486bc6802508aeecaf7`
- Build source: verified v7 package SHA256 `e18bd5e2fabe214b785e9d602ef2ae7c18dbc8773381c35936c5c29477722ab6`, restored from GitHub blobs, then `tools/jni-vulkan-only/clean_v7_release.py`.
- Reused cached NDK r28c artifact parts `9174697344` and `9174699121`, original NDK SHA256 `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f`.
- Verification: CLEAN_SOURCE_VERIFIED=PASS, PRODUCTION_VULKAN_ARM64_COMPILE=PASS, CLEAN_COMPLETE_PACKAGE=PASS; Vulkan DT_NEEDED present and EGL/GLES absent; 34 source/binary files hash-verified.
- Change: removes 5-second auto parent probing, calibration, debug properties, logs and present-receipts; retains user-tested v7 SurfaceView parent host, Vulkan and MotionEvent handling. Clean build **not yet user-device-tested**.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| JNI Vulkan v7.1 Clean Production ARM64 | v7.1-clean-release-20261010 | Android API31+ | arm64-v8a | `JNI-Vulkan-v7.1-Clean-Production-ARM64.zip` | `664fa501312644af384a151f3e14e992ffbe5a2c3b659300da04805f8274169c` |



## JNI Vulkan v7.2 Minimal Production — 2026-10-10

- Name: JNI Vulkan v7.2 Minimal Production
- Version: 7.2 clean production (v7 tested branch)
- Platform: Android API 31+
- Architecture: arm64-v8a
- Artifact Name: `jni-vulkan-v7-2-minimal-production-arm64`
- Artifact ID: `11662600874`
- Run ID: `38031782393`
- Workflow: `.github/workflows/jni-vulkan-v7-clean-release.yml`
- File: `JNI-Vulkan-v7.2-Minimal-Production-ARM64.zip`
- Size: `8023879` bytes
- SHA256: `f0e28cdf4907150a9c4bf1a3f8bcda692521867874c6abc9448533f6fdd7d38e`
- Created: `2026-10-10T06:42:09Z`
- Expires: `2027-01-08T06:41:01Z`
- Storage: SINGLE GitHub Actions Artifact, mirrored in ChatGPT Library at `/JNI-Vulkan-v7.2-Minimal-Production-ARM64.zip`
- Original File: `JNI-Vulkan-v7.2-Minimal-Production-ARM64.zip`
- Original Size: `8023879` bytes
- Original SHA256: `f0e28cdf4907150a9c4bf1a3f8bcda692521867874c6abc9448533f6fdd7d38e`
- Part Count: 1
- `libAndroid.so` SHA256: `fa3de56692d6ebf45232b34a7e5a71cb74cf2b91aadbc486bc6802508aeecaf7`.
- Cached Dependencies: Android NDK r28c Parts 00 & 01, Run `31684150811`, IDs `9174697344` and `9174699121`.
- Source: user-verified Vulkan v7 ZIP SHA256 `e18bd5e2fabe214b785e9d602ef2ae7c18dbc8773381c35936c5c29477722ab6`.
- Verification: `NO_DEBUG_HELPERS_REMAIN=PASS`, `CLEAN_SOURCE_VERIFIED=PASS`, `PRODUCTION_VULKAN_ARM64_COMPILE=PASS`, `CLEAN_COMPLETE_PACKAGE=PASS`; no EGL/GLES, Vulkan only. Output binary SHA256 equals v7.1 release, indicating more thorough dead-source removal produced the same ARM64 optimized binary. Original v7 real-device verified by user, v7.2 needs device regression test.

| Name | Version | Platform | Architecture | File | SHA256 |
|---|---|---|---|---|---|
| JNI Vulkan Minimal Production | v7.2 | Android API 31+ | arm64-v8a | `JNI-Vulkan-v7.2-Minimal-Production-ARM64.zip` | `f0e28cdf4907150a9c4bf1a3f8bcda692521867874c6abc9448533f6fdd7d38e` |



## Artifact Record: UPX KeyGuard v1 Linux x86_64 (2026-10-13)

- **Source:** official `upx/upx` tag `v5.2.1` (modified source and add-on runtime), branch `work/upx-keyguard-20261013`
- **Workflow:** `.github/workflows/upx-keyguard.yml`
- **Run ID:** `38333114942` (success)
- **Artifact Name:** `upx-keyguard-v1-linux-x86_64`
- **Artifact ID:** `11784260295`
- **Created At:** `2026-10-13T01:39:23Z`
- **Expires At:** `2027-01-11T01:38:45Z`
- **Storage Mode:** `SINGLE`
- **Original File:** `UPX_KeyGuard_Actions_Artifact.zip` (GitHub-generated ZIP packaging the `release/` directory)
- **Original Size:** `4626042` bytes
- **Original SHA256:** `bbe099a78444ca37fac1c4a15c1739dcb5f46c58be86681ab62b6c16d4cb4bcb`
- **Artifact Archive Size:** `4626042` bytes
- **Artifact Archive SHA256:** `bbe099a78444ca37fac1c4a15c1739dcb5f46c58be86681ab62b6c16d4cb4bcb`
- **Part Count:** `1` (well below 512MB)
- **Validation:** GitHub Actions passed correct/no/wrong key, ordinary UPX unpack rejection; local independent Linux re-run passed; authenticated decrypt recovered internal UPX compressed file and unpacking reproduced the original ELF byte-for-byte.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| UPX KeyGuard protected demo SO | v5.2.1-keyguard-v1-20261013 | Linux | x86_64 | `password_upx_keyguard_linux_x86_64.so` | `3ae60e1dc2806f389c76c73359ac1c5d9d5a06c91a0864def724a077fe8d41ac` |
| UPX KeyGuard modified UPX tool | v5.2.1-keyguard-v1-20261013 | Linux | x86_64 | `upx-keyguard-linux-x86_64` | `e18935fa16616eb655feda374195b8cc7cdb3f429dd8862ef0a0deaac5cb2a3e` |
| UPX KeyGuard outer ELF stub | v5.2.1-keyguard-v1-20261013 | Linux | x86_64 | `guard_stub_linux_x86_64.so` | `e0a7544fe2ebbaa272e679b10e652cd4c06bbd781c86067d23d1fdbdbcdc8269` |
| UPX KeyGuard original test ELF | v5.2.1-keyguard-v1-20261013 | Linux | x86_64 | `original_linux_x86_64` | `9acb77c83c3ee9b32e0ee31ea2a5478e057a65edd82f6b695a67aecdd1af918b` |
| UPX KeyGuard patched UPX source archive | v5.2.1-keyguard-v1-20261013 | Any | Any | `upx-keyguard-patched-upstream.tar.gz` | `56028854e1bdca97507338b7891c61032ebebeaae43cf5b7ff6ffc37ee446d45` |
| UPX KeyGuard add-on source archive | v5.2.1-keyguard-v1-20261013 | Any | Any | `upx-keyguard-src-addons.tar.gz` | `795f9b38ac1529247ff77426c87de307fad4009b8fd9fe3240722daacbcac75d` |
| UPX KeyGuard source patch | v5.2.1-keyguard-v1-20261013 | Any | Any | `upx-5.2.1-keyguard.patch` | `d36cac8297028d7addef8f9cbbd00f36954e18fa8b6c3dc52ee0c6e6841ad452` |

### Artifact

| Part | Artifact ID | Artifact Name | File/Path | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---|---:|---|---|---|
| 1/1 | `11784260295` | `upx-keyguard-v1-linux-x86_64` | `UPX_KeyGuard_Actions_Artifact.zip` | `4626042` | `bbe099a78444ca37fac1c4a15c1739dcb5f46c58be86681ab62b6c16d4cb4bcb` | `2026-10-13T01:39:23Z` | `2027-01-11T01:38:45Z` |

### Restore

Call `download_workflow_artifact` on artifact `11784260295` from run `38333114942`; verify ZIP SHA256 `bbe099a...`; unzip to get the nested ELF, packed UPX fork, source tarballs, patch and demo key; verify `SHA256SUMS` after removing the `release/` prefix, because GitHub upload-artifact flattens the source directory root. The 32-byte demo key is public testing material, **not a production secret and not Android hardware-backed**.


## Artifact Record: UPX KeyGuard ARM64 Linux (2026-10-13)

- **Name:** UPX KeyGuard ARM64 Linux
- **Version:** `v5.2.1-keyguard-v1-20261013`
- **Platform:** Linux
- **Architecture:** AArch64
- **Source:** cached UPX 5.2.1 modified source from artifact `11784260295` (no repeated source download), ARM-native modified build branch `work/upx-keyguard-arm64-20261013`
- **Workflow:** `.github/workflows/upx-keyguard-arm64.yml`
- **Run ID:** `38333914943` (success)
- **Artifact Name:** `upx-keyguard-native-linux-aarch64-v1`
- **Artifact ID:** `11784246824`
- **File:** `UPX_KeyGuard_ARM64_Actions_Artifact.zip`
- **Size:** `4594253` bytes
- **SHA256:** `8d0e705f28a290456005daaa50df89e199088acc9f083b377a3c928879ff7bd7`
- **Created At:** `2026-10-13T01:49:52Z`
- **Expires At:** `2027-01-11T01:48:51Z`
- **Storage Mode:** SINGLE
- **Original File:** `UPX_KeyGuard_ARM64_Actions_Artifact.zip`
- **Original Size:** `4594253` bytes
- **Original SHA256:** `8d0e705f28a290456005daaa50df89e199088acc9f083b377a3c928879ff7bd7`
- **Part Count:** 1
- **Validation:** Native GitHub Actions Linux AArch64 runner verified: correct key/password exit=0, wrong password exit=1, absent key exit=71, wrong key exit=73, ordinary UPX -d on encrypted outer exit=2. Independently authenticated AES-GCM recovered a 9748-byte UPX linux/arm64 inner ELF; UPX unpacked 70920-byte original with exact SHA256 match. **Not an Android/Bionic binary and not TEE bound.**

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| UPX KeyGuard ARM64 executable | v5.2.1-keyguard-v1 | Linux | AArch64 | `password_upx_keyguard_linux_arm64.so` | `fc1b8ee87f192517566b35d2a18a5ece886b260166b84c6aebe5b17805e2c56d` |
| UPX KeyGuard ARM64 modified packer | v5.2.1-keyguard-v1 | Linux | AArch64 | `upx-keyguard-linux-arm64` | `077425d284aa18c12e18edbeaa9d09150fb2e0df043b9fdeb37e7327adb24a12` |
| UPX KeyGuard ARM64 outer stub | v5.2.1-keyguard-v1 | Linux | AArch64 | `guard_stub_linux_arm64.so` | `492fa7844e2d179fb31661516a070465be9066311164a5ff696ceb8fe637adef` |
| UPX KeyGuard ARM64 original sample | v5.2.1-keyguard-v1 | Linux | AArch64 | `original_arm64` | `ca7a00971324b2971cfbebb57c77a3020d9de7999bcd36be2200db1845365df4` |

### Artifact

| Part | Artifact ID | Artifact Name | File/Path | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---|---:|---|---|---|
| 1/1 | `11784246824` | `upx-keyguard-native-linux-aarch64-v1` | `UPX_KeyGuard_ARM64_Actions_Artifact.zip` | `4594253` | `8d0e705f28a290456005daaa50df89e199088acc9f083b377a3c928879ff7bd7` | `2026-10-13T01:49:52Z` | `2027-01-11T01:48:51Z` |

### Restore

Use `mcp__GitHub__download_workflow_artifact` with repository `jepede/gpt-exten`, artifact `11784246824`, verify artifact ZIP SHA256 `8d0e705f28a290456005daaa50df89e199088acc9f083b377a3c928879ff7bd7`, then unzip and run SHA256SUMS verification. `demo.key` inside is a **public disposable test key**, not a production key; share the encrypted ELF separately from keys.


## Artifact Record: UPX KeyGuard Android ARM64 API28 (2026-10-13)

- Name: UPX KeyGuard Android ARM64
- Version: `5.2.1-keyguard-arm64-demo-20261013`
- Platform: Android/Bionic API 28+
- Architecture: ARM64 / arm64-v8a / AArch64
- Workflow: `.github/workflows/upx-keyguard-android-arm64.yml`
- Run ID: `38334950099` (success)
- Artifact Name: `upx-keyguard-android-arm64-bionic`
- Artifact ID: `11784720583`
- Artifact ZIP File: `UPX_KeyGuard_Android_ARM64_Actions_Artifact.zip`
- Artifact ZIP Size: `1287617` bytes
- Artifact ZIP SHA256: `25a033428a7618117d9c91d12c0dab4364efe58d7e7fda6ef376dc06eb6d3797`
- Created At: `2026-10-13T02:03:15Z`
- Expires At: `2027-01-11T02:01:54Z`
- Storage Mode: `SINGLE`
- Original File: `UPX_KeyGuard_Android_ARM64_Actions_Artifact.zip`
- Original Size: `1287617` bytes
- Original SHA256: `25a033428a7618117d9c91d12c0dab4364efe58d7e7fda6ef376dc06eb6d3797`
- Part Count: `1`
- Important: The `demo.key` in this artifact is a test software key, not hardware-backed. A physical Android phone has not been available for device-side verification.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| UPX KeyGuard encrypted outer executable SO | 5.2.1-keyguard-arm64-demo-20261013 | Android/Bionic API 28+ | arm64-v8a | `NGuard_UPX_Android_ARM64.so` | `31f60bbc41313c238d5784d2f915cfd0338e0edec2f95689eb8289f03940dda3` |
| UPX KeyGuard original inner ELF | 5.2.1-keyguard-arm64-demo-20261013 | Android/Bionic API 28+ | arm64-v8a | `original_android_arm64` | `b3c1302f183b1200783ff4b47fc494f9d7bc6d40a35126d2df7cf229d671e904` |

### Artifact

| Part | Artifact ID | Artifact Name | File/Path | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---|---:|---|---|---|
| 1/1 | `11784720583` | `upx-keyguard-android-arm64-bionic` | `UPX_KeyGuard_Android_ARM64_Actions_Artifact.zip` | `1287617` | `25a033428a7618117d9c91d12c0dab4364efe58d7e7fda6ef376dc06eb6d3797` | `2026-10-13T02:03:15Z` | `2027-01-11T02:01:54Z` |

### Restore

Use GitHub `download_workflow_artifact` on artifact `11784720583` (run `38334950099`); validate ZIP SHA256 `25a033428a7618117d9c91d12c0dab4364efe58d7e7fda6ef376dc06eb6d3797`, extract files, and check the enclosed `SHA256SUMS` manifest after removing any `release/` prefix. Verified independently: decrypt AES-256-GCM ciphertext with demo key and zlib decompress to byte-identical ARM64 ELF; invalid key and tampering rejected; under Android 16 Bionic rootfs and qemu-aarch64-static 7.2.22 outer no-key / wrong-key exited 71/73 with zero stdout. Correct-key QEMU execution reached second execve but QEMU linux-user did not re-execute the nested ELF; original inner ELF ran successfully on the same emulator. Real phone full-path execution remains unverified.

## Artifact Record: UPX KeyGuard ARM64 QEMU runtime verification v1.1

- Name: UPX KeyGuard Android ARM64 QEMU E2E build
- Version: `v1.1-testonly-20261013`
- Platform: Android/Bionic API28+ (emulated Android 16 rootfs)
- Architecture: arm64-v8a (loader), x86_64 (build tool)
- Workflow: `.github/workflows/upx-keyguard-android-arm64.yml`
- Run ID: `38335627167` (**workflow conclusion failure**: Python regression assertion used an incorrect escaped footer string; build binaries were produced; **independent local QEMU/Bionic 8/8 tests passed**)
- Artifact Name: `upx-keyguard-android-arm64-bionic`
- Artifact ID: `11785120751`
- Artifact ZIP File: `UPX_ARM64_QEMU_test_intermediate.zip`
- Artifact ZIP Size: `1353384` bytes
- Artifact ZIP SHA256: `1c17ff9b14802a321e3f8dcbece8f797e6a65e547174024fef63014f70d59543`
- Created At: `2026-10-13T02:11:52Z`
- Expires At: `2027-01-11T02:10:30Z`
- Storage Mode: `SINGLE`
- Original File: `UPX_ARM64_QEMU_test_intermediate.zip`
- Original Size: `1353384` bytes
- Original SHA256: `1c17ff9b14802a321e3f8dcbece8f797e6a65e547174024fef63014f70d59543`
- Part Count: `1`
- Validation: Real QEMU 7.2.22 with user-provided Android 16 Bionic rootfs; production no-key and wrong-key were silent on stdout (71/73); separately compiled **QEMU_TEST_ONLY** ARM64 variant with correct key and user password printed real login-success (exit 0) or wrong-password (exit 1); no key/wrong key/tampered data/strict-no-disk checked; 8/8 succeeded, no leaked temp files. No physical Android device execution or TEE/KeyMint tested.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| UPX KeyGuard production encrypted ELF | v1.1-testonly-20261013 | Android/Bionic API28+ | ARM64 | `NGuard_UPX_Android_ARM64.so` | `e1c91fee09cd8bf86eb8606813d7d9a6ae9d79d5728b66d231676b7a4271ee69` |
| UPX KeyGuard QEMU-only encrypted ELF | v1.1-testonly-20261013 | Android/Bionic API28+ | ARM64 | `NGuard_UPX_Android_ARM64_QEMU_TEST_ONLY.so` | `9c8c6e060a300a145b5300d0b214384e23283d7f2e9210b1e79a62df095c68ca` |
| UPX KeyGuard Android ARM64 QEMU loader | v1.1-testonly-20261013 | Android/Bionic API28+ | ARM64 | `guard_outer_android_arm64_QEMU_TEST_ONLY` | `65fd11e11c0c664b1706637256d6f9fd3de5f1a1bec2547c328b5ca714383c42` |
| UPX KeyGuard original ARM64 ELF (test only) | v1.1-testonly-20261013 | Android/Bionic API28+ | ARM64 | `original_android_arm64` | `b3c1302f183b1200783ff4b47fc494f9d7bc6d40a35126d2df7cf229d671e904` |
| UPX KeyGuard x86_64 packer | v1.1-testonly-20261013 | Linux | x86_64 | `upx-keyguard-5.2.1-host-x86_64` | `3cafb52fcad6e8b0f94e3d9a90b68ef0483378abaff8a278095ada4d1ded4158` |

### Artifact

| Part | Artifact ID | Artifact Name | File/Path | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---|---:|---|---|---|
| 1/1 | `11785120751` | `upx-keyguard-android-arm64-bionic` | `UPX_ARM64_QEMU_test_intermediate.zip` | `1353384` | `1c17ff9b14802a321e3f8dcbece8f797e6a65e547174024fef63014f70d59543` | `2026-10-13T02:11:52Z` | `2027-01-11T02:10:30Z` |

### Restore

Call GitHub `download_workflow_artifact` for artifact `11785120751` from run `38335627167`. Validate artifact ZIP SHA256 `1c17ff9b14802a321e3f8dcbece8f797e6a65e547174024fef63014f70d59543`. Extraction includes normal ARM64 ELF and separate QEMU-only variant. Do not ship `NGuard_UPX_Android_ARM64_QEMU_TEST_ONLY.so` as the production version. The public `demo.key` is for unit testing and is **not** a TEE hardware key.

## Artifact Record: Google Android Key Attestation trust reference 2026-10-13

- Name: Google Android Key Attestation trust reference
- Version: `2026-10-13`
- Platform: Any
- Architecture: Any
- Workflow: `.github/workflows/keyguard-v7-attestation-trust.yml`
- Run ID: `38354591700` (success)
- Artifact Name: `keyguard-v7-attestation-reference-20261013`
- Artifact ID: `11792870161`
- Created At: `2026-10-13T06:03:12Z`
- Expires At: `2027-01-11T06:03:07Z`
- Storage Mode: `SINGLE`
- File: `KeyGuard_V7_Google_Attestation_Reference.zip`
- Size: `29751` bytes
- SHA256: `47a3bb109fd6506200795de805a340c689a26c9f329a0e76d80b53d13ec8bc15`
- Original File: `KeyGuard_V7_Google_Attestation_Reference.zip`
- Original Size: `29751` bytes
- Original SHA256: `47a3bb109fd6506200795de805a340c689a26c9f329a0e76d80b53d13ec8bc15`
- Part Count: `1`
- Note: ZIP includes two pinned Google attestation root certificates, current revocation entries and retrieval timestamps. Revocation data is considered **fresh for only 24 hours** by the V7 issuer; a live issuer MUST refresh status after that regardless of Artifact lifetime.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Google attestation trust roots | 2026-10-13 | Any | Any | `root.json` | `7ff10488836c6c270bb09d48fc4d43c17ae35434a42e113fed1f22f7fc4ca2ff` |
| Google attestation revocation status | 2026-10-13 | Any | Any | `status.json` | `13e803c2dbef970961ca427951300274401813344326cbacde0a9ededfdc5433` |
| Trust snapshot metadata | 2026-10-13 | Any | Any | `metadata.json` | `eee68536f6efae11b5f5ba582ed619401b3b7e0c1f1c8d79f5fe207a39426876` |

### Artifact

| Part | Artifact ID | Artifact Name | File/Path | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---|---:|---|---|---|
| 1/1 | `11792870161` | `keyguard-v7-attestation-reference-20261013` | `KeyGuard_V7_Google_Attestation_Reference.zip` | `29751` | `47a3bb109fd6506200795de805a340c689a26c9f329a0e76d80b53d13ec8bc15` | `2026-10-13T06:03:12Z` | `2027-01-11T06:03:07Z` |

### Restore

Use GitHub `download_workflow_artifact` artifact `11792870161` from run `38354591700`. Verify outer ZIP SHA256 then verify each JSON SHA256. Google root pins also verified inside the V7 issuer code. This is **not** a permanent revocation-status cache; refresh the online status within 24 hours before approving a device.


## Artifact Record: Official AOSP Bionic Linker Android 15 + Android 16 (2026-10-13)

- **Name:** Official AOSP Bionic linker sources
- **Version:** `android-15.0.0_r36+android-16.0.0_r2`
- **Platform:** Android Bionic source / Any host
- **Architecture:** ARM64 / AArch64 (source includes cross-ABI code)
- **Source:** `https://android.googlesource.com/platform/bionic` (official Google AOSP); tag checkout, not arbitrary branch
- **AOSP Android 15 commit:** `8d67ca893c1523eb926b9080dbe4e2ffd2a27ba1`
- **AOSP Android 16 commit:** `09a271af557444c9a6b3f3146d6d474156fd6cdb`
- **Workflow:** `.github/workflows/aosp-linker-compat-snapshot.yml` (on `work/aosp-linker-analysis-20261013` branch)
- **Run ID:** `38422855360` (success)
- **Artifact Name:** `aosp-bionic-linker-15r36-16r2`
- **Artifact ID:** `11827525995`
- **Artifact ZIP:** `aosp-bionic-linker-15r36-16r2.zip`
- **Artifact ZIP Size:** `760791` bytes
- **Artifact ZIP SHA256:** `e1852fc5e8f1795a6187d2621a9ba7a54643328081cbd42c542fb8b2a851d2f6`
- **Created At:** `2026-10-13T15:32:09Z`
- **Expires At:** `2027-01-11T15:31:50Z` (actual returned GitHub value)
- **Storage Mode:** `SINGLE`
- **Original File:** `aosp-bionic-linker-15r36-16r2.tar.gz`
- **Original Size:** `762423` bytes
- **Original SHA256:** `849e05db5ec47e68a3ab7f1ec23edb860f635a2e38a499c8bca388b0f2f6c1c9`
- **Part Count:** `1`
- **Retention Requested:** `400 days`, actual GitHub expiry governs validity
- **Validation:** GitHub Actions checkout official tags, `sha256sum` of original tarball; cached artifact ZIP downloaded and independently SHA256 checked. Includes source `linker/`, `libc/include/`, `libc/private/` and `tests/dlfcn_test.cpp` for both Android versions.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Official AOSP Bionic linker sources | android-15.0.0_r36+android-16.0.0_r2 | Android Bionic source | ARM64 / All | `aosp-bionic-linker-15r36-16r2.tar.gz` | `849e05db5ec47e68a3ab7f1ec23edb860f635a2e38a499c8bca388b0f2f6c1c9` |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|---|
| 1/1 | `11827525995` | `aosp-bionic-linker-15r36-16r2` | 760791 | `e1852fc5e8f1795a6187d2621a9ba7a54643328081cbd42c542fb8b2a851d2f6` | 2026-10-13T15:32:09Z | 2027-01-11T15:31:50Z |

### Restore

Use `download_workflow_artifact` with repo `jepede/gpt-exten` and artifact `11827525995`, confirm artifact ZIP SHA256; unpack `aosp-bionic-linker-15r36-16r2.tar.gz`, verify original SHA256 and use pinned `COMMIT.txt` per release. Reuse this artifact while GitHub reports it present and unexpired.


## PUBG CTF GL APK 4.6.0 v1.0.1

- Name: `PUBG CTF GL APK`
- Version: `4.6.0-v1.0.1`
- PUBG Version: `4.6.0`
- PUBG Version Code: `21525`
- Package: `com.tencent.ig`
- Platform: Android
- Architecture: `arm64-v8a`
- Region: Global
- Workflow: `.github/workflows/fetch-pubg-global-arm64-apk.yml`
- Workflow Name: `Sync PUBG Global ARM64 libUE4`
- Run ID: `38431125316`
- Run Attempt 1: `success` — APKMirror live resolution returned 403, workflow fell back to `ARTIFACT_CACHE.md`, reused the existing valid Base APK Artifact, and uploaded the APK Release asset without re-downloading from APKMirror
- Run Attempt 2: `success` — both `libUE4-GL-4.6.so` and `PUBG-CTF-GL-4.6.0.apk` already existed, so all download/extract/upload work was skipped
- Release Tag: `v1.0.1`
- Release Asset: `PUBG-CTF-GL-4.6.0.apk`
- Release Asset ID: `637604009`
- Release Asset Size: `107399819` bytes
- Release Asset SHA256: `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696`
- Release Asset URL: `https://github.com/jepede/gpt-exten/releases/download/v1.0.1/PUBG-CTF-GL-4.6.0.apk`
- Source Cache Artifact: `pubg-mobile-global-4.6.0-21525-arm64-v8a`
- Source Cache Artifact ID: `11308584380`
- Storage Mode: `SINGLE`
- Verification Artifact Name: `pubg-global-4.6.0-21525-libue4-sync`
- Verification Artifact ID: `11830109931`
- Verification Artifact ZIP Size: `107407879` bytes
- Verification Artifact Digest: `sha256:0baa17bb45dcebc39f719590725037ceef32e33403ec12bafa059a9f0ae6d18f`
- Original File: `PUBG-CTF-GL-4.6.0.apk`
- Original Size: `107399819` bytes
- Original SHA256: `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696`
- Part Count: `1`
- Created At: `2026-10-13T16:31:19Z`
- Expires At: `2027-01-11T16:30:53Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | Size | SHA256 |
|---|---|---|---|---|---:|---|
| PUBG CTF GL APK | 4.6.0-v1.0.1 | Android | arm64-v8a | `PUBG-CTF-GL-4.6.0.apk` | `107399819` | `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696` |

### Artifact

| Part | Artifact ID | Artifact Name | Original Size | Original SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | `11830109931` | `pubg-global-4.6.0-21525-libue4-sync` | `107399819` | `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696` | `107407879` | `sha256:0baa17bb45dcebc39f719590725037ceef32e33403ec12bafa059a9f0ae6d18f` | `2026-10-13T16:31:19Z` | `2027-01-11T16:30:53Z` |

### Restore

优先直接使用 Release `v1.0.1` 中的 `PUBG-CTF-GL-4.6.0.apk`。若通过缓存恢复，则下载 Artifact `11830109931`，校验 Artifact ZIP digest `0baa17bb45dcebc39f719590725037ceef32e33403ec12bafa059a9f0ae6d18f`；解压后校验 APK SHA256 `9e28aa526caa748fc650a2f7b86f1ef545acf94f09811a5fa41414ca818e8696`。


## Artifact Record: Android ARM64 LLD APS2 real-ELF smoke 2026-10-13

- Name: Android ARM64 LLD APS2 real-ELF smoke evidence
- Version: ndk-r28c-api28-aps2-v1-20261013
- Platform: Android/Bionic API 28+ target, Linux x86_64 host
- Architecture: AArch64 / arm64-v8a
- Workflow: .github/workflows/android-arm64-compat-smoke.yml
- Run ID: 38435474384 (success)
- Artifact Name: android-arm64-ndk-real-aps2-evidence
- Artifact ID: 11833330555
- File: android-arm64-ndk-real-aps2-evidence.zip
- Size: 19393 bytes
- SHA256: 4207c689719b43ad1612bcf16bfbdcea556238cc511a0ecf28b11d62aab1b895
- Created At: 2026-10-13T17:03:41Z
- Expires At: 2027-01-11T17:02:52Z (actual GitHub value)
- Storage Mode: SINGLE
- Original File: android-arm64-ndk-real-aps2-evidence.zip
- Original Size: 19393 bytes
- Original SHA256: 4207c689719b43ad1612bcf16bfbdcea556238cc511a0ecf28b11d62aab1b895
- Part Count: 1
- Source toolchain: reused cached Android NDK r28c artifacts 9174697344 and 9174699121, split-part SHA256 and reassembled NDK zip SHA256 dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f verified. No new external NDK download.
- Results: Android NDK API28 cross-compiled APS2 / GNU version / ELF map-plan unit tests. Real NDK LLD --pack-dyn-relocs=android generated SO with DT_ANDROID_RELA = 0x450, DT_ANDROID_RELASZ = 147; APS2 decode validated 100 real AArch64 relocations.
- Scope: isolated compatibility evidence, not end-to-end Android/Bionic shell-loader runtime test.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android ARM64 LLD APS2 real-ELF smoke evidence | ndk-r28c-api28-aps2-v1-20261013 | Android API28+ target / Linux x86_64 host | ARM64 | android-arm64-ndk-real-aps2-evidence.zip | 4207c689719b43ad1612bcf16bfbdcea556238cc511a0ecf28b11d62aab1b895 |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|---|
| 1/1 | 11833330555 | android-arm64-ndk-real-aps2-evidence | 19393 | 4207c689719b43ad1612bcf16bfbdcea556238cc511a0ecf28b11d62aab1b895 | 2026-10-13T17:03:41Z | 2027-01-11T17:02:52Z |

### Restore

Call download_workflow_artifact for repo jepede/gpt-exten with artifact_id=11833330555; verify SHA256. The archive contains libaps2_real.so, dynamic.txt, result.txt, compiled ARM64 object files, host inspector, and SHA256SUMS.txt.


## Artifact Record: Custom linker ARM64 compatibility kit v2

- Name: Custom linker ARM64 compatibility kit v2
- Version: v2-20261013-android16-comparison
- Platform: Android/Bionic source compatibility, Linux host
- Architecture: AArch64 / arm64-v8a
- Workflow: .github/workflows/package-android-linker-compat.yml
- Run ID: 38436179725 (success)
- Artifact Name: custom-linker-arm64-compat-kit-v2
- Artifact ID: 11833176641
- File: custom-linker-arm64-compat-kit-v2.zip
- Size: 13562 bytes
- SHA256: 6d3491f064ab42ccef49fa742722c6685ca2a1a3dfa00d6610924d3ae62f61cf
- Created At: 2026-10-13T17:08:11Z
- Expires At: 2027-01-11T17:08:05Z (actual GitHub value)
- Storage Mode: SINGLE
- Original File: custom-linker-arm64-compat-kit-v2.tar.gz
- Original Size: 13165 bytes (verified by cached-artifact inspection, run 38436696056)
- Original SHA256: 6ae344dbc23945b3aaedfc34925f7e90a30ce15cdc1fe693f7c6e4cd3c768d52
- Part Count: 1
- Validation: GCC C11 APS2 decoder, ELF GNU version reader and 4K/16K PT_LOAD planner tests pass. Real ARM64 NDK r28c API28 compile and LLD-generated APS2 decoding independently passed in run 38435474384 (100 relocations).
- Note: The kit is independent public C11 source + tests + integration guide. The uploaded private custom linker project is NOT included, and this is not a fully integrated production loader.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| ARM64 linker compat source bundle | v2-20261013-android16-comparison | Android/Bionic source | AArch64 | custom-linker-arm64-compat-kit-v2.tar.gz | 6ae344dbc23945b3aaedfc34925f7e90a30ce15cdc1fe693f7c6e4cd3c768d52 |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|
| 1/1 | 11833176641 | custom-linker-arm64-compat-kit-v2 | 13562 | 6d3491f064ab42ccef49fa742722c6685ca2a1a3dfa00d6610924d3ae62f61cf | 2026-10-13T17:08:11Z | 2027-01-11T17:08:05Z |

### Restore

Download workflow artifact 11833176641 from jepede/gpt-exten, verify artifact ZIP SHA256, extract custom-linker-arm64-compat-kit-v2.tar.gz and verify SHA256, then extract compatibility/ components.


## Artifact Record: GDB Multiarch 15.1 x86_64 for QEMU AArch64 debugging (2026-10-14)

- **Name:** GDB Multiarch debugger for Android ARM64 QEMU
- **Version:** 15.1-1ubuntu1~24.04.1-python3.12-v3-20261014
- **Platform:** Ubuntu 24.04 / Linux
- **Architecture:** x86_64 host, AArch64 target remote
- **Workflow:** `.github/workflows/fetch-gdb-multiarch-arm64-debug.yml` on branch `work/aosp-linker-analysis-20261013`
- **Run ID:** `38516782411` (success)
- **Artifact Name:** `gdb-multiarch-ubuntu2404-x86_64`
- **Artifact ID:** `11871824237`
- **Artifact ZIP File:** `gdb-multiarch-x86_64-portable-v3.zip` (local artifact download name)
- **Artifact ZIP Size:** `33974608` bytes
- **Artifact ZIP SHA256:** `0b6674bd5241f169eada855d657f79554fbba1d061bc9304d1e2d0526ae6a857`
- **Created At:** `2026-10-14T05:28:26Z`
- **Expires At:** `2027-01-12T05:28:01Z` (actual GitHub value)
- **Storage Mode:** `SINGLE`
- **Original File:** `gdb-multiarch-ubuntu2404-x86_64.tar.gz`
- **Original Size:** `34214965` bytes
- **Original SHA256:** `e4cf124f92272c12eaca6b38663f58c5983244987855544985a661458fae9d4d`
- **Part Count:** `1`
- **Requested Retention:** `400 days` (actual expiry governs)
- **Source:** Official Ubuntu 24.04 `gdb-multiarch` distribution package and Python3.12 dependencies.
- **Validation:** `--version` GDB 15.1; `set architecture aarch64`; GDB Python works; connected to QEMU `-g PORT` and read PC/SP + stack of actual Android ARM64 packed custom-linker executable, continued to normal exit. Portable wrapper may depend on x86_64 glibc compatibility.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| GDB Multiarch portable bundle | 15.1 Python3.12 v3 | Ubuntu24.04 Linux | x86_64 host, AArch64 target | `gdb-multiarch-ubuntu2404-x86_64.tar.gz` | `e4cf124f92272c12eaca6b38663f58c5983244987855544985a661458fae9d4d` |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|---|
| 1/1 | `11871824237` | `gdb-multiarch-ubuntu2404-x86_64` | `33974608` | `0b6674bd5241f169eada855d657f79554fbba1d061bc9304d1e2d0526ae6a857` | `2026-10-14T05:28:26Z` | `2027-01-12T05:28:01Z` |

### Restore

Download artifact ID `11871824237` from repo `jepede/gpt-exten`, check ZIP SHA256, extract `gdb-multiarch-ubuntu2404-x86_64.tar.gz`, check its SHA256, unpack; validate included per-file `SHA256SUMS.txt` inside the extracted portable root. Run `./gdb-multiarch.sh`.

## Artifact Record: Official Google Android 36 AArch64 Bionic runtime libraries (2026-10-14)

- **Name:** Official Android API36 ARM64 Bionic runtime sysroot
- **Version:** android-36-default-arm64-v8a-r02-20261014
- **Platform:** Android API 36 SDK system image runtime (extracted Bionic libraries and loader)
- **Architecture:** arm64-v8a / AArch64 (emulated using x86_64 host QEMU)
- **Source:** `https://dl.google.com/android/repository/sys-img/android/arm64-v8a-36_r02.zip`
- **Source Archive Size:** `810736863` bytes (original image not uploaded because it exceeds 512MB single-artifact limit)
- **Source Archive SHA256:** `c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1` (validated against official SDK XML SHA1)
- **Extraction:** official Google image ZIP -> GPT `system.img` -> dynamic `super` -> logical `system` ext4 -> `com.android.runtime.apex` and `com.android.art.apex` -> ELF files. Extraction workflow uses `lpunpack` rebuilt from public Apache-licensed upstream source. Outputs REAL runtime .so binaries, not NDK stubs.
- **Workflow:** `.github/workflows/fetch-aosp-arm64-bionic-runtime.yml` and `compatibility/tools/extract_aosp_runtime.py` on `work/aosp-linker-analysis-20261013`
- **Run ID:** `38517156477` (success)
- **Artifact Name:** `aosp-arm64-bionic-runtime`
- **Artifact ID:** `11872515999`
- **Artifact ZIP File:** `aosp-arm64-bionic-runtime-android36.zip` (local download name)
- **Artifact ZIP Size:** `13982231` bytes
- **Artifact ZIP SHA256:** `b2318392c4b67c242de6bf8f49b5a00466d9b7386a7b0f848048211fa94e2db3`
- **Created At:** `2026-10-14T05:33:01Z`
- **Expires At:** `2027-01-12T05:32:10Z` (actual GitHub value)
- **Storage Mode:** `SINGLE`
- **Original File:** `aosp-arm64-bionic-runtime.tar.gz`
- **Original Size:** `14020506` bytes
- **Original SHA256:** `0d0c5c925cbee0c461b42a6df104e9316b52ca822c73bdb42fcd4100eae9ee8e`
- **Part Count:** `1`
- **Requested Retention:** `400 days` (actual expiry governs)
- **Validation:** Extracted 54 ARM64 runtime files, verified native ARM64 linker64, libc, libdl and libm. NDK r28c API35 executable boots under cached QEMU AArch64 static 7.2.22 with this runtime. The user private custom-linker 45-case packed-vs-native matrix passed defined runtime assertions. QEMU guest `-p 16384` separate 12/12 simulated page-size checks. Minimal runtime sysroot lacks Android device `/linkerconfig/ld.config.txt`; tests are not a device certification. App `libc++_shared.so` was added separately from the NDK for C++ tests, NOT part of this AOSP runtime artifact.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Bionic linker64 | Android API36 default r02 | Android 36 runtime | AArch64 | `sysroot/system/bin/linker64` | `30ed9bea070250e0b080c8a84d8398baab1b4eb95a90bfced82a94d5f235144b` |
| Bionic libc | Android API36 default r02 | Android 36 runtime | AArch64 | `sysroot/apex/com.android.runtime/lib64/bionic/libc.so` | `d3f8599b8b3f00101a31f94ac170ceb5875ee8446c201cb18382b2e02df84301` |
| Bionic libdl | Android API36 default r02 | Android 36 runtime | AArch64 | `sysroot/apex/com.android.runtime/lib64/bionic/libdl.so` | `9f6447d910742a57b398a6a3f31746e02302ee9547da6d02757f001058a69df3` |
| Bionic libm | Android API36 default r02 | Android 36 runtime | AArch64 | `sysroot/apex/com.android.runtime/lib64/bionic/libm.so` | `44433149f62eeb8f09f38ecd3566683fac01a0f89de6ea6d15f6e4deca1ba4bc` |
| Android system libc++ | Android API36 default r02 | Android 36 runtime | AArch64 | `sysroot/system/lib64/libc++.so` | `2267f93b8b3c9d1967f1833d5f71c7312213c43bb291250cf772800763037fb9` |
| Android system liblog | Android API36 default r02 | Android 36 runtime | AArch64 | `sysroot/system/lib64/liblog.so` | `efcce90970ed85d61b9c05791ad76ff5f573035b1c0f7d2a3839063c7db5d1a0` |
| Minimal runtime archive | Android API36 default r02 | Linux host / Android 36 runtime | x86_64 extraction, AArch64 payload | `aosp-arm64-bionic-runtime.tar.gz` | `0d0c5c925cbee0c461b42a6df104e9316b52ca822c73bdb42fcd4100eae9ee8e` |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|---|
| 1/1 | `11872515999` | `aosp-arm64-bionic-runtime` | `13982231` | `b2318392c4b67c242de6bf8f49b5a00466d9b7386a7b0f848048211fa94e2db3` | `2026-10-14T05:33:01Z` | `2027-01-12T05:32:10Z` |

### Restore

Download artifact `11872515999` from repo `jepede/gpt-exten`; verify downloaded ZIP SHA256 `b2318392...`; unzip, check nested tar SHA256 via included `SHA256SUMS.txt`; extract to runtime root so `sysroot/system/bin/linker64` exists. For C++ tests separately add NDK r28c `libc++_shared.so`. Use `qemu-aarch64-static -L SYSROOT` with Android `LD_LIBRARY_PATH` and **remove host `LD_PRELOAD`**.


## Delta Force CN Android Official APK 1.201.37117.67 (2026-10-14)

- Name: **Delta Force CN Android APK**
- Version: `1.201.37117.67`
- Package: `com.tencent.tmgp.dfm`
- Platform: `Android`
- Architecture: `arm64-v8a` (inspected in APK `lib/` entries)
- Repository: `jepede/gpt-exten`
- Workflow: `.github/workflows/fetch-deltaforce-cn-android-apk.yml`
- Run ID: `38596903200`
- Run Conclusion: `success`
- Official Source Landing Page: `https://a.app.qq.com/o/simple.jsp?pkgname=com.tencent.tmgp.dfm`
- Source URL: `http://imtt.dd.qq.com/sjy.00022/sjy.00001/16891/apk/546F3D60B114DDD80E45A708D2D6E130.apk?fsname=com.tencent.tmgp.dfm_1.201.37117.67.apk`
- Source Notes: Tencent MyApp page published this HTTP APK URL; GitHub runner's HTTPS attempt timed out but HTTP Range requests succeeded. Published MD5 and Content-Length were checked.
- Requested Retention: `400 days`; **Effective Retention:** GitHub-reported expiration below (~90 days).
- Storage Mode: `SPLIT`
- Artifact Name Prefix: `deltaforce-cn-android-v1.201.37117.67-part-`
- Original File: `DeltaForce-CN-Android-v1.201.37117.67.apk`
- Original Size: `1519215938` bytes
- Original MD5 (Tencent and verified locally in Actions): `546f3d60b114ddd80e45a708d2d6e130`
- Original SHA256: `af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d`
- Part Count: `4`
- Max Raw Part Size: `419430400` bytes (400 MiB); **each artifact ZIP below 512 MB**
- Created At: `2026-10-14T16:24:45Z` (first uploaded artifact)
- Expires At: `2027-01-12T16:18:07Z`
- Manifest: `metadata/manifest.json` and `metadata/SHA256SUMS.txt` are included with part 00.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Delta Force CN Android APK part 00 | 1.201.37117.67 | Android | arm64-v8a | `DeltaForce-CN-Android-v1.201.37117.67.apk.part.00` | `ff89045d63daf2101f83357729c6fd501c2623d6db87fb3dd973c6e48fdb03be` |
| Delta Force CN Android APK part 01 | 1.201.37117.67 | Android | arm64-v8a | `DeltaForce-CN-Android-v1.201.37117.67.apk.part.01` | `727fc9db85ce8e9df1d612d536b2c2919f05f94ae93f44141716d1f1a52655ef` |
| Delta Force CN Android APK part 02 | 1.201.37117.67 | Android | arm64-v8a | `DeltaForce-CN-Android-v1.201.37117.67.apk.part.02` | `1be7e7ef8ca01bdd6677095fb6e5c20b297d0c2386a9269e58a9f3cc59773639` |
| Delta Force CN Android APK part 03 | 1.201.37117.67 | Android | arm64-v8a | `DeltaForce-CN-Android-v1.201.37117.67.apk.part.03` | `ac3582fae315b8cc283df13dd1216df3f07245791f50cb90feecfc2ff74cb169` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Part Size | Raw Part SHA256 | Artifact ZIP Size | Artifact ZIP Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/4 | `11912605268` | `deltaforce-cn-android-v1.201.37117.67-part-00` | `419430400` | `ff89045d63daf2101f83357729c6fd501c2623d6db87fb3dd973c6e48fdb03be` | `419433088` | `sha256:c6ffaca827e09cecf5a07f77724a28e3688998b61f00c271321257e76a5ab039` | `2026-10-14T16:24:45Z` | `2027-01-12T16:18:07Z` |
| 2/4 | `11912625263` | `deltaforce-cn-android-v1.201.37117.67-part-01` | `419430400` | `727fc9db85ce8e9df1d612d536b2c2919f05f94ae93f44141716d1f1a52655ef` | `419430612` | `sha256:97d7f9fbb177b4f4841c4752516a0aa99d39202656da9bb04e731ad2050f179f` | `2026-10-14T16:24:51Z` | `2027-01-12T16:18:07Z` |
| 3/4 | `11913085103` | `deltaforce-cn-android-v1.201.37117.67-part-02` | `419430400` | `1be7e7ef8ca01bdd6677095fb6e5c20b297d0c2386a9269e58a9f3cc59773639` | `419430612` | `sha256:80d92f97ebabc0f97cc6e69ee2fba6e27cac8b702b874626fff4035ebf4b6b17` | `2026-10-14T16:24:57Z` | `2027-01-12T16:18:07Z` |
| 4/4 | `11912650314` | `deltaforce-cn-android-v1.201.37117.67-part-03` | `260924738` | `ac3582fae315b8cc283df13dd1216df3f07245791f50cb90feecfc2ff74cb169` | `260924950` | `sha256:cb685ddaf4a10e0ca73a9503dae30b6143295f3cc2a9248952ba6738bd020db0` | `2026-10-14T16:25:01Z` | `2027-01-12T16:18:07Z` |

### Independent persisted-Artifact restore check (2026-10-14)

- Verification Workflow: `.github/workflows/verify-deltaforce-cn-android-apk.yml`
- Verification Run ID: `38639952423`
- Verification Conclusion: `success` / `PASS`
- Verification Method: **re-download all four stored ZIP Artifacts via GitHub API**; validate each Archive SHA256 against GitHub's recorded digest, extract and validate every raw part SHA256, concatenate in numeric order, validate original length `1519215938`, SHA256 `af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d`, MD5 `546f3d60b114ddd80e45a708d2d6e130`, and APK `AndroidManifest.xml` plus `arm64-v8a` entries.
- Log: `https://github.com/jepede/gpt-exten/actions/runs/38639952423`
- Report Artifact: `deltaforce-cn-apk-restoration-verification` (Artifact ID `11928879281`, verification metadata only, expires at `2026-10-15T21:24:43Z`; this temporary report is not a replacement for the APK split archives).

### Restore

Download all four Artifact ZIPs from run `38596903200` (IDs above), using `download_workflow_artifact` or the GitHub CLI. Verify each downloaded Artifact ZIP SHA256 against **Artifact ZIP Digest**; extract each ZIP, find `DeltaForce-CN-Android-v1.201.37117.67.apk.part.00` through `DeltaForce-CN-Android-v1.201.37117.67.apk.part.03`; then concatenate **in numeric order** (00, 01, 02, 03) into `DeltaForce-CN-Android-v1.201.37117.67.apk`. Check every raw part SHA256 against the Contents table, then the reconstructed file SHA256 `af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d` and MD5 `546f3d60b114ddd80e45a708d2d6e130`.

Direct CLI restore (requires authenticated `gh` and `sha256sum`):

```bash
gh run download 38596903200 -R jepede/gpt-exten -D ./deltaforce-cn-parts
prefix="DeltaForce-CN-Android-v1.201.37117.67.apk"
find_part() { find ./deltaforce-cn-parts -type f -name "${prefix}.part.$1" -print -quit; }
cat "$(find_part 00)" "$(find_part 01)" "$(find_part 02)" "$(find_part 03)" > "${prefix}"
echo 'af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d  DeltaForce-CN-Android-v1.201.37117.67.apk' | sha256sum -c -
echo '546f3d60b114ddd80e45a708d2d6e130  DeltaForce-CN-Android-v1.201.37117.67.apk' | md5sum -c -
```


## Artifact Record: ARM64 NDK r28c C debugging validation (2026-10-15)

- **Name:** ARM64 NDK C debugging validation
- **Version:** r28c-run38642113778
- **Platform:** Ubuntu 24.04 Linux / Android API 36 Bionic on QEMU User 7.2.22
- **Architecture:** x86_64 host, AArch64 Android test binary
- **Workflow:** `.github/workflows/ndk-arm64-debug-validation.yml`
- **Run ID:** `38642113778`
- **Workflow Conclusion:** success
- **Artifact Name:** `arm64-ndk-r28c-debug-validation`
- **Artifact ID:** `11931276591`
- **File:** `arm64-ndk-r28c-debug-evidence.zip` (GitHub artifact ZIP archive; contains tests, logs, binaries)
- **Size:** `48966` bytes
- **SHA256:** `9b0c29cc200a5ae2d9f1880d065238dd5508cbd1fdeb4bd033c0a51865164d1d`
- **Created At:** `2026-10-14T21:41:50Z`
- **Expires At:** `2027-01-12T21:40:57Z` (actual GitHub value, verified)
- **Storage Mode:** SINGLE
- **Original File:** `arm64-ndk-r28c-debug-evidence.zip`
- **Original Size:** `48966` bytes
- **Original SHA256:** `9b0c29cc200a5ae2d9f1880d065238dd5508cbd1fdeb4bd033c0a51865164d1d`
- **Part Count:** 1
- **Requested Retention:** 400 days (actual repository max 90 days)
- **Source NDK:** previously cached Android NDK r28c artifact pair, run `31684150811`; SHA256 checked against original `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f`.
- **Validation Summary:** 18 PASS, 3 UNSUPPORTED (User-mode hardware write, read, access watchpoints), 0 FAIL, across 21 tests, on GitHub Actions runner (NOT ChatGPT local container).
- **Sources:** `tooling/arm64-ndk-debug/probe.c`, `probe_plugin.c`, `runner.py`, `build.sh`, and `install_ndk_from_cache.sh`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android ARM64 C debug probe | NDK r28c build 38642113778 | Android API 28+ | AArch64 | `tooling/arm64-ndk-debug/build/probe` | `19f6263f1829adb9728654f9d2757ba8eaf625d8d5231ce259b298b5a6cbcf70` |
| Android ARM64 shared-library probe | NDK r28c build 38642113778 | Android API 28+ | AArch64 | `tooling/arm64-ndk-debug/build/libprobe_plugin.so` | `c21aba09005579b57f740bfd576266860ef6552a0c74a78ca67b3264f4d50789` |
| Raw debug tests and logs artifact ZIP | NDK r28c run 38642113778 | Linux/Android API 36 | x86_64/AArch64 | `arm64-ndk-r28c-debug-evidence.zip` | `9b0c29cc200a5ae2d9f1880d065238dd5508cbd1fdeb4bd033c0a51865164d1d` |

### Artifact

| Part | Artifact ID | Artifact Name | File Size | SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|---|
| 1/1 | `11931276591` | `arm64-ndk-r28c-debug-validation` | `48966` | `9b0c29cc200a5ae2d9f1880d065238dd5508cbd1fdeb4bd033c0a51865164d1d` | `2026-10-14T21:41:50Z` | `2027-01-12T21:40:57Z` |

### Restore

Call `download_workflow_artifact` with repo `jepede/gpt-exten`, Artifact ID `11931276591`. Verify the ZIP SHA256 above, unpack logs and binaries, and validate the compiled probe ELF and shared-library checksums before execution. No new NDK resource download was performed during this run; both existing NDK artifact parts were reused.

## r2ghidra 6.2.2 Linux x86_64 (radare2 6.2.2)

- Name: `r2ghidra`
- Version: `6.2.2`
- Platform: `Debian / Linux`
- Architecture: `x86_64`
- Workflow: `.github/workflows/tmp-fetch-r2ghidra-622.yml` (temporary branch `tmp/r2ghidra-622-20261016`)
- Run ID: `38850726295`
- Run Number: `1`
- Run Conclusion: `success`
- Sources: official `radareorg/r2ghidra` GitHub release/tag `6.2.2` (`.deb` and Sleigh archive)
- Requested Retention: `400 days`
- Effective Retention: `90 days` (actual GitHub expiration)
- Storage Mode: `SINGLE`
- Artifact Name: `r2ghidra-6.2.2-amd64-sleigh`
- Artifact ID: `12024094996`
- File: `r2ghidra-6.2.2-amd64-sleigh-artifact.zip` (ZIP emitted by upload-artifact)
- Size: `24255437 bytes` (artifact archive)
- SHA256: `2be8591084f0fd0507df31086551baa8eb7e65472322cd45495b55faa4e34776` (artifact archive)
- Created At: `2026-10-16T04:27:42Z`
- Expires At: `2027-01-14T04:27:37Z`
- Original File: `concat(r2ghidra_6.2.2_amd64.deb, r2ghidra_sleigh-6.2.2.zip)` (ordered, *not* an individual filename)
- Original Size: `24254838 bytes` (sum of both original asset sizes)
- Original SHA256: `90a82ffdf824e8f325b8c60fd3917c734b589009c6256a2196878967f96b891d` (SHA256 of ordered raw concatenation)
- Part Count: `1`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Native Ghidra radare2 plugin | 6.2.2 | Debian / Linux | x86_64 | `r2ghidra_6.2.2_amd64.deb` | `248f5f3f1a8ba67dac8209fa7ae0688c21d9c2802021bb77f1b9dcdf876c729f` |
| r2ghidra Sleigh language bundle | 6.2.2 | Any | Any | `r2ghidra_sleigh-6.2.2.zip` | `05ff67acce1f32e0d97aecb59f6f2a782cc9e37c4b40ede6b66386cd651086a0` |

### Artifact

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---:|---:|---|---:|---|---|---|
| 1/1 | `12024094996` | `r2ghidra-6.2.2-amd64-sleigh` | `24255437` | `2be8591084f0fd0507df31086551baa8eb7e65472322cd45495b55faa4e34776` | `2026-10-16T04:27:42Z` | `2027-01-14T04:27:37Z` |

### Restore

Check the actual artifact exists, is unexpired, and matches `Name+Version+Platform+Architecture`; download existing Artifact `12024094996` through `download_workflow_artifact`. Verify the outer ZIP SHA256, extract both files and `SHA256SUMS`, verify SHA256 for both assets, and optionally verify the original concatenated payload hash. The `.deb` contains `core_ghidra.so`, r2fidb, sleighc, and embedded Sleigh files. For isolated radare2 installation, extract with `dpkg-deb -x`, symlink the plugin and Sleigh directory under the radare2 library plugin prefix, and export `SLEIGHHOME` to that real Sleigh path. Current user-mode ARM64 sample passed `pdg` and `pdgj` under radare2 6.2.2.


## PRoot runtime bundle 5.1.0-1.3

- Artifact Name: `proot-debian12-amd64-bundle-20261017`
- Artifact ID: `12088830875`
- Run ID: `38999498688`
- Workflow: `.github/workflows/fetch-proot-deb12-amd64.yml`
- Artifact File: `proot-debian12-amd64-artifact.zip`
- Artifact Size: `169181` bytes
- Artifact SHA256: `60b7ea6d26348f8dedfcee81ff8afc53255ee68b0adbeaf8b151f86379f168ae`
- Original File: `proot-debian12-amd64.tar.gz`
- Original Size: `168882` bytes
- Original SHA256: `f6a7542a47d74a23954f066c3238a0c39685ef7bcc969e16e78f60b155303f92`
- Created At: `2026-10-17T03:37:37Z`
- Expires At: `2027-01-15T03:37:28Z` (actual GitHub response, requested retention-days=400)
- Storage Mode: `SINGLE`
- Part Count: `1`
- Download: `download_workflow_artifact` from `jepede/gpt-exten`, Artifact ID `12088830875`; verify ZIP SHA256, extract inner archive, then verify original SHA256.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| PRoot executable and local runtime libraries | 5.1.0-1.3 | Debian 12 / Linux | x86_64 | `proot-debian12-amd64.tar.gz` | `f6a7542a47d74a23954f066c3238a0c39685ef7bcc969e16e78f60b155303f92` |


## AOSP GKI ARM64 kernels 6.6 / 6.12, 4 KB / 16 KB v1

- Name: `AOSP GKI ARM64 kernels`
- Version: `6.6-6.12-4k-16k-v1`
- Platform: `Android / Linux`
- Architecture: `AArch64`
- Workflow: `.github/workflows/fetch-aosp-gki-arm64-kernels-v1.yml`
- Run ID: `39000440004`
- Artifact ID: `12088643253`
- Artifact Name: `aosp-gki-arm64-kernels-6.6-6.12-4k-16k-v1`
- File: `aosp-gki-kernels.zip`
- Size: `59660969 bytes`
- SHA256: `d376f7d45300e489c553f1018facb67c447d6b7a1a8e98804e2fa7d66ae9d19a`
- Created At: `2026-10-17T03:52:48Z`
- Expires At: `2027-01-15T03:52:30Z`
- Storage: `SINGLE`
- Original File: `aosp-gki-arm64-kernels-6.6-6.12-4k-16k-v1.tar.gz`
- Original Size: `59660524 bytes`
- Original SHA256: `dcfebd4ba27c221a743f5b879e5a65ad96ee6420ca67922cf926a8f215863a27`
- Part Count: `1`
- Source 6.6: `https://android.googlesource.com/kernel/prebuilts/6.6/arm64`, commit `6104d37087c872b8183f8483ba32e3bc165d3517`
- Source 6.12: `https://android.googlesource.com/kernel/prebuilts/6.12/arm64`, commit `ba5af8825f23428021efb670c0ad025d6b1e0966`

Public AOSP prebuilt kernels, embedded build configurations, source metadata and SHA256 checksums only. No user program or private target included. ZIP, original TAR.GZ and per-file hashes independently verified after restoration. Boot/runtime compatibility validation is separate from cache integrity.


## QEMU AArch64 User Static 10.0.13

- Name: QEMU AArch64 User Static
- Version: `1:10.0.13+ds-0+deb13u1`
- Platform: Debian 13 / Linux
- Architecture: x86_64 host + AArch64 guest
- Artifact Name: `qemu-aarch64-static-debian13-20261017`
- Artifact ID: `12089252099`
- Run ID: `39001231108`
- Workflow: `.github/workflows/fetch-qemu-trixie-aarch64-static.yml`
- File: `qemu10-debian13-aarch64-artifact.zip` (outer artifact archive)
- Size: `3706833` bytes (outer artifact archive)
- SHA256: `01c9b8fdd33d31473abc3caec9655ebaab093e31e505363aa8b8ff8550c1dfa4` (outer artifact archive)
- Created At: `2026-10-17T04:05:20Z`
- Expires At: `2027-01-15T04:05:09Z` (actual GitHub result; requested 400 days)
- Storage Mode: `SINGLE`
- Original File: `qemu-aarch64-static`
- Original Size: `16661520` bytes
- Original SHA256: `73cc2584f119f9e74c85c0a8549dbb6fd104ae3897a06a7500797f9e5b4d0943`
- Part Count: `1`
- Repository: `jepede/gpt-exten`
- GitHub Actions artifact status at creation: expired=false

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| QEMU AArch64 Static PIE | 1:10.0.13+ds-0+deb13u1 | Debian 13 / Linux | x86_64 | `qemu-aarch64-static` | `73cc2584f119f9e74c85c0a8549dbb6fd104ae3897a06a7500797f9e5b4d0943` |

### Restore

Use GitHub connector `download_workflow_artifact` with Artifact ID `12089252099` in `jepede/gpt-exten`. Verify outer ZIP SHA256, extract the included `qemu-aarch64-static` and verify original file SHA256 before installing or invoking. Do not re-download while artifact remains available and its `expires_at` is in the future.


## AOSP API35 ARM64 native runtime 35_r02 v1

- Name: `AOSP API35 ARM64 native runtime`
- Version: `35_r02-native-v1`
- Platform: `Android 15 / API 35`
- Architecture: `AArch64`
- Workflow: `.github/workflows/fetch-aosp-api35-arm64-runtime-v1.yml`
- Run ID: `39001884393`
- Artifact ID: `12088924872`
- Artifact Name: `aosp-api35-arm64-native-runtime-v1`
- File: `aosp-api35-native-runtime.zip`
- Size: `148807332 bytes`
- SHA256: `ba198b5de382ac74f787b0a470f8f73f91ac73536b8ed070ea7ca32a97e76b65`
- Created At: `2026-10-17T04:16:52Z`
- Expires At: `2027-01-15T04:15:30Z`
- Storage: `SINGLE`
- Original File: `aosp-api35-arm64-native-runtime-v1.tar.xz`
- Original Size: `148806908 bytes`
- Original SHA256: `d91c053b71f4776253d8402ecd88382e892aef907110bfa6e09f64df999f2e44`
- Part Count: `1`
- Source: `https://dl.google.com/android/repository/sys-img/android/arm64-v8a-35_r02.zip`
- Source Size: `769099654 bytes`
- Source SHA256: `1e6ae4fca6449c07278a333311f0ef29c5101d1e3e18ba48fbe9bd2dc5006926`
- Source SHA1 (official SDK repository metadata): `2026a06409db630b56711afdbffb457c1dbaed49`

Contains public AOSP native bin/lib64/etc trees, authentic build properties, and expanded APEX native runtime directories. APK/framework content and full boot images are excluded. No private user program is included. ZIP, original TAR.XZ and 2253 per-file SHA256 hashes were independently verified after restoration. Runtime validation is separate from cache integrity.


## AOSP API35 full ARM64 SDK image 35_r02 v1

- Name: `AOSP API35 full ARM64 SDK image`
- Version: `35_r02-full-v1`
- Platform: `Android 15 / API35`
- Architecture: `AArch64`
- Workflow: `.github/workflows/cache-aosp-api35-full-image-r02-v1.yml`
- Run ID: `39002974865` (success)
- Repository: `jepede/gpt-exten` (public)
- Source: `https://dl.google.com/android/repository/sys-img/android/arm64-v8a-35_r02.zip`
- Source File: `arm64-v8a-35_r02.zip`
- Source Size: `769099654` bytes
- Source SHA256: `1e6ae4fca6449c07278a333311f0ef29c5101d1e3e18ba48fbe9bd2dc5006926`
- Official SDK metadata SHA1: `2026a06409db630b56711afdbffb457c1dbaed49`
- Storage Mode: `SPLIT`
- Part Count: `2` equal raw chunks, each `384549827` bytes
- Part 00 SHA256: `6768eda6f66b296079146983e85d28f47d1efb9123e0653b2a60c7040fd6201d`
- Part 01 SHA256: `0fa1f44ae8c6f148657068051c693a8ce674ec07ecc94b5420a7a0a6081e2e1b`
- Metadata Artifact: `FULL_IMAGE_SOURCE.json`, `SHA256SUMS.txt`
- Requested Retention: `90 days`; actual GitHub expires_at governs.

| Part | Artifact ID | Artifact Name | Artifact ZIP Size | Artifact Digest | Created At | Expires At |
|---|---:|---|---:|---|---|---|
| metadata | `12090245193` | `aosp-api35-full-image-r02-metadata-v1` | `4841` | `sha256:8f937de317a736488e80e9d5f9e83a780417301050ef6e41dba085b2a913aeba` | `2026-10-17T04:33:09Z` | `2027-01-15T04:32:52Z` |
| 2/2 | `12090155626` | `aosp-api35-full-image-r02-part-01-v1` | `384549977` | `sha256:a952775e21cbfcdc484436fb1863a55a8fa82681e6998945671af78459c5af62` | `2026-10-17T04:33:16Z` | `2027-01-15T04:32:52Z` |
| 1/2 | `12090026892` | `aosp-api35-full-image-r02-part-00-v1` | `384549977` | `sha256:80ed7d62dd83de3bd9717de96219181995926f9557179667213bc49c454e117c` | `2026-10-17T04:33:13Z` | `2027-01-15T04:32:52Z` |

### Restore

Use the GitHub connector to download all three artifact ZIPs. Each archive is below 512 MB. Verify every outer ZIP against its Artifact Digest; extract metadata and the two raw chunks, verify each raw SHA256, concatenate `full-api35.part.00` then `full-api35.part.01`, and verify final size/SHA256 before extracting the SDK ZIP. CI verified the official SDK checksum, ZIP CRCs, equal chunk sizes and reconstructed SHA256; local restoration independently verified all outer archives, raw chunks and reconstructed image. Includes original public kernel, ramdisk, system/vendor images and SDK metadata. No private target program is included. Image integrity does not certify any user program execution result.


## AOSP API36 full ARM64 SDK image 36_r02 v1

- Name: `AOSP API36 full ARM64 SDK image`
- Version: `36_r02-full-v1`
- Platform: `Android 16 / API36`
- Architecture: `AArch64`
- Workflow: `.github/workflows/cache-aosp-api36-full-image-r02-v1.yml`
- Run ID: `39003325276`
- Repository: `jepede/gpt-exten` (public)
- Source: `https://dl.google.com/android/repository/sys-img/android/arm64-v8a-36_r02.zip`
- Source File: `arm64-v8a-36_r02.zip`
- Source Size: `810736863` bytes
- Source SHA256: `c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1`
- Official SDK metadata SHA1: `62ad6714df790f89c8a8ad32552ffe20bb16fe87`
- Storage Mode: `SPLIT`
- Part Count: `3` equal raw chunks, each `270245621` bytes
- Part 00 SHA256: `017b944a5e8182f4b502c94708ec933a6d280e98f428243a451ed4a870906776`
- Part 01 SHA256: `0385c38d8ddf768783ac4ff222bb1aae199492a44d4ab320ea2ffd20f58cde8a`
- Part 02 SHA256: `9ffbe1506140dd355d97a321d8b70cd7a49d95eef9d7f424e536e82d62b4c5a0`
- Metadata Artifact: `FULL_IMAGE_SOURCE.json`, `SHA256SUMS.txt`
- Requested Retention: `90 days`; actual GitHub expires_at governs.

| Part | Artifact ID | Artifact Name | Artifact ZIP Size | Artifact Digest | Created At | Expires At |
|---|---:|---|---:|---|---|---|
| NaN/3 | `12090325568` | `aosp-api36-full-image-r02-part-00-v1` | `270245771` | `sha256:745c47f39cd31d1385d21de0585a890b3974a88ff08f2682713cf49a389220de` | `2026-10-17T04:38:57Z` | `2027-01-15T04:38:31Z` |
| NaN/3 | `12090186116` | `aosp-api36-full-image-r02-part-01-v1` | `270245771` | `sha256:ef23f75cf7bd10f5f79043e4a83118778886686939d45563cde2c468297c9c32` | `2026-10-17T04:39:00Z` | `2027-01-15T04:38:31Z` |
| metadata | `12089942877` | `aosp-api36-full-image-r02-metadata-v1` | `4405` | `sha256:b51b9dc25f3c3408e39c012d6971879292979438de614dc80ed98368de76786c` | `2026-10-17T04:38:53Z` | `2027-01-15T04:38:31Z` |
| NaN/3 | `12089883391` | `aosp-api36-full-image-r02-part-02-v1` | `270245771` | `sha256:8f91cae29adacf9b0c6f6ffc513effddf4e422e0b3cc1b93075c413e78bb3422` | `2026-10-17T04:39:04Z` | `2027-01-15T04:38:31Z` |

### Restore

Use the GitHub connector to download all four artifact ZIPs. Every archive is below 512 MB. Verify outer ZIPs against Artifact Digest values, extract the metadata and raw chunks, verify individual raw SHA256 values, concatenate parts 00/01/02 in order, then verify the final size/SHA256 before extracting the original SDK ZIP. CI verified the official SDK checksum, ZIP CRCs, equal chunk sizes and reconstructed SHA256. All outer archives, raw chunks and reconstructed source image were independently verified locally. Contains only the original public SDK images, kernel, ramdisk and metadata; no private user program. Image integrity does not certify successful execution of any user program.


## QEMU 10.0.13 TCG plugin toolchain (2026-10-17)

- **Name:** QEMU TCG Plugins: execlog/hotblocks/vmptrace
- **Version:** v10.0.13-plugin-api4-20261017
- **Platform:** Ubuntu 24.04 Linux / Debian 13 QEMU
- **Architecture:** x86_64 host, AArch64 guest
- **Repository:** `jepede/gpt-exten`
- **Workflow:** `.github/workflows/build-qemu10-tcg-plugins-20261017.yml`
- **Run ID:** `39003891690`
- **Artifact ID:** `12089733087`
- **Artifact Name:** `qemu10-tcg-plugins-upstream-execlog-hotblocks`
- **File:** `qemu10-tcg-plugins-vmptrace.zip` (download name, archive includes plugins and source/header)
- **Size:** `61605` bytes
- **SHA256:** `698bcf2f2cb1c18ef1c99834c824acc8f5d32f3d4e80406c36e4007c9c4eacba`
- **Created At:** `2026-10-17T04:47:54Z`
- **Expires At:** `2027-01-15T04:47:37Z` (GitHub actual result, expired=false, retention-days requested 400)
- **Storage Mode:** `SINGLE`
- **Original File:** `qemu10-tcg-plugins-vmptrace.zip` (the original artifact ZIP payload, no extra nested TAR)
- **Original Size:** `61605` bytes
- **Original SHA256:** `698bcf2f2cb1c18ef1c99834c824acc8f5d32f3d4e80406c36e4007c9c4eacba`
- **Part Count:** `1`
- **Validation:** SHA256 of downloaded archive and inner `SHA256SUMS.txt` verified; QEMU 10.0.13 loads plugins; live ARM64 guest traced instruction execution and memory accesses without changing register state.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| QEMU libexeclog.so | 10.0.13 API4 | Linux | x86_64 | `libexeclog.so` | `87a167f4eb08a26d1b9136f6be07cdaf74977db545f13c7613a9ed528303a8e9` |
| QEMU libhotblocks.so | 10.0.13 API4 | Linux | x86_64 | `libhotblocks.so` | `696e30377b3af26c9c017c42bb1ceae640f332246d98ff93c790ad3479ca69d7` |
| QEMU passive VMP trace plugin | 10.0.13 API4 | Linux | x86_64 | `libvmptrace.so` | `7fb3b4eb9b7d22f9f1d6dd19b251b36254a4ab537dd6c99e4cb8bcb5080101df` |
| QEMU plugin SDK header | 10.0.13 API4 | Any | Any | `qemu-plugin.h` | `ceca12f3ba448340b38223617b1c66d7b92e0e0d78687d1e108c42287542836e` |
| Passive VMP plugin source | 20261017 | Any | Any | `vmptrace.c` | `6ca2778a11211f2753e7eebf2eeace469b43432ef3534bab70fde786e657f7f9` |

### Restore

Use `download_workflow_artifact` with repo `jepede/gpt-exten`, ID `12089733087`. Check outer ZIP SHA256 `698bcf2f...`; unpack files and run `sha256sum -c SHA256SUMS.txt`. The `vmptrace` source is located in repository path `tools/tcg_plugins/vmptrace.c`. This plugin is passive; any GDB register modification is a separate experiment and not a plugin feature.

## Artifact Record: Android 36 ARM64 graphics/framework sysroot (2026-10-17)

- Name: Android 36 ARM64 graphics/framework sysroot
- Version: android36-r02-graphics-20261017
- Platform: Android API36 SDK runtime
- Architecture: AArch64 / arm64-v8a (x86_64 host)
- Workflow: .github/workflows/tmp-android36-graphics.yml on branch tmp/android36-egl-20261017
- Run ID: 39007458676 (success)
- Source: https://dl.google.com/android/repository/sys-img/android/arm64-v8a-36_r02.zip
- Source SHA256: c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1
- Artifact Name: android36-graphics-00
- Artifact ID: 12090878722
- Metadata Artifact: android36-graphics-meta, ID 12091043204
- Storage Mode: SINGLE (one original file in part 00; separate metadata artifact)
- Original File: android36-arm64-graphics-sysroot.tar.gz
- Original Size: 80764977 bytes
- Original SHA256: 963b4123e91e5bad16463115b4ca201fa3b54907fa474feda0fb82a3fd070ee4
- Part Count: 1
- Artifact Size: 80765123 bytes
- Artifact ZIP SHA256: 0a1fb9f79e6049ac29090bfefee7ddfe16a40e4c342c3ca6cfdddd403c359a93
- Metadata Artifact Size: 10204 bytes
- Metadata ZIP SHA256: 0baed2a10a244737b573f834b2d078a65695d5d5d4623d76997409472b2b3714
- Created At: 2026-10-17T05:46:54Z
- Expires At: 2027-01-15T05:45:59Z (actual GitHub expires_at)
- Retention Requested: 400 days; actual expiry is authoritative
- Validation: Outer ZIP and inner archive SHA256 checked, extracted 737 runtime files.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Graphics/framework archive | android36-r02-graphics-20261017 | Android API36 | AArch64 | android36-arm64-graphics-sysroot.tar.gz | 963b4123e91e5bad16463115b4ca201fa3b54907fa474feda0fb82a3fd070ee4 |
| libEGL.so | Android 36 r02 | Android | AArch64 | sysroot/system/lib64/libEGL.so | c967542bdb196f84deecc6a65d754a6fd6e18aa18b5039fed1b6d5dbf9016de7 |
| libGLESv2.so | Android 36 r02 | Android | AArch64 | sysroot/system/lib64/libGLESv2.so | b81e8b3c754ad96e7495217e55dcd7c67d3e7ba6da99d503ea4e9e1a254e2200 |
| libGLESv3.so | Android 36 r02 | Android | AArch64 | sysroot/system/lib64/libGLESv3.so | 36de13cedc528931144a503f94b56d216b935cfcf05eebd87a29d6ee9a08c846 |
| libgui.so | Android 36 r02 | Android | AArch64 | sysroot/system/lib64/libgui.so | 3cccdaf945764512a7f896cc8407b8c4a500713a254cb71bfcac8915c393a445 |
| libui.so | Android 36 r02 | Android | AArch64 | sysroot/system/lib64/libui.so | c97cec2cce586bfe42c82a7a265533fe0d7e572e04e9f1074bcde38e723092c8 |
| libbinder.so | Android 36 r02 | Android | AArch64 | sysroot/system/lib64/libbinder.so | 9b5800819be6fe3f7b66c9507cc408b9d2a8daf5dc7af63baaea940d1a43c009 |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | 12090878722 | android36-graphics-00 | 80764977 | 963b4123e91e5bad16463115b4ca201fa3b54907fa474feda0fb82a3fd070ee4 | 80765123 | sha256:0a1fb9f79e6049ac29090bfefee7ddfe16a40e4c342c3ca6cfdddd403c359a93 | 2026-10-17T05:46:54Z | 2027-01-15T05:45:59Z |
| metadata | 12091043204 | android36-graphics-meta | 74025 | n/a | 10204 | sha256:0baed2a10a244737b573f834b2d078a65695d5d5d4623d76997409472b2b3714 | 2026-10-17T05:46:52Z | 2027-01-15T05:45:59Z |

Restore: download_workflow_artifact IDs 12090878722 and 12091043204, verify ZIP digests, extract graphics.part.00 as the full TAR.GZ, verify inner SHA256, extract to Android sysroot.

## Artifact Record: Android 36 ARM64 i18n ICU APEX (2026-10-17)

- Name: Android 36 ARM64 i18n ICU APEX
- Version: android36-r02-i18n-20261017
- Platform: Android API36 SDK APEX
- Architecture: AArch64 / arm64-v8a
- Workflow: .github/workflows/tmp-android36-i18n.yml on branch tmp/android36-egl-20261017
- Run ID: 39007941479 (success)
- Source: https://dl.google.com/android/repository/sys-img/android/arm64-v8a-36_r02.zip
- Source SHA256: c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1
- Artifact Name: android36-arm64-i18n-icu
- Artifact ID: 12091780944
- Storage Mode: SINGLE
- Original File: android36-arm64-i18n-icu.tar.gz
- Original Size: 12730942 bytes
- Original SHA256: ff8e006de1fabdb98cccfcffdb3393410245d9336190ca0821d86e78f089eb49
- Part Count: 1
- Artifact Size: 12608751 bytes
- Artifact ZIP SHA256: 7e3592f26e217b10325ce9c34c64998840226e32fc5f48d479f9989c41cc4900
- Created At: 2026-10-17T05:54:53Z
- Expires At: 2027-01-15T05:54:10Z (actual GitHub expires_at)
- Retention Requested: 400 days; actual expiry is authoritative
- Validation: Outer ZIP and inner archive SHA256 checked. Android ELF test static DT_NEEDED closure becomes zero-missing (243 resolved ELF files).

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| i18n ICU APEX archive | android36-r02-i18n-20261017 | Android API36 APEX | AArch64 | android36-arm64-i18n-icu.tar.gz | ff8e006de1fabdb98cccfcffdb3393410245d9336190ca0821d86e78f089eb49 |
| libicu.so | Android 36 r02 | Android APEX | AArch64 | sysroot/apex/com.android.i18n/lib64/libicu.so | 7a6a0e8f8e55dfae5a2c789c95eda01e05dfa6ad5ae599e567e40b9ffb0c50f9 |
| libandroidicu.so | Android 36 r02 | Android APEX | AArch64 | sysroot/apex/com.android.i18n/lib64/libandroidicu.so | 188794585b34624aead7db7e8a62859c7035108765ffef7d9e71ab28652654aa |
| ICU data | Android 36 r02 | Android APEX | AArch64 | sysroot/apex/com.android.i18n/etc/icu/icudt76l.dat | c5450087565eb20ca37d70af5ef53a99a4c8e2e3da17c9140582b685f06d980f |

### Artifact

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/1 | 12091780944 | android36-arm64-i18n-icu | 12730942 | ff8e006de1fabdb98cccfcffdb3393410245d9336190ca0821d86e78f089eb49 | 12608751 | sha256:7e3592f26e217b10325ce9c34c64998840226e32fc5f48d479f9989c41cc4900 | 2026-10-17T05:54:53Z | 2027-01-15T05:54:10Z |

Restore: download_workflow_artifact ID 12091780944, verify ZIP and inner archive SHA256, extract sysroot/apex/com.android.i18n. Add /apex/com.android.i18n/lib64 to the Guest LD_LIBRARY_PATH.


## Artifact Record: Android 36 ARM64 graphics and ICU runtime 2026-10-17

- Source: Official Google Android SDK default ARM64-v8a API 36 r02 system image; Source SHA256: c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1.
- Platform: Android 36; Architecture: ARM64/AArch64 guest; Version: android36-r02-20261017; Requested Retention: 400 days (GitHub actual expires_at is authoritative).
- Graphics Name: Android 36 ARM64 graphics Framework runtime. Workflow: .github/workflows/tmp-android36-graphics.yml; Run ID: 39007458676; Storage Mode: SPLIT (1 part + metadata); Original File: android36-arm64-graphics-sysroot.tar.gz; Original Size: 80764977 bytes; Original SHA256: 963b4123e91e5bad16463115b4ca201fa3b54907fa474feda0fb82a3fd070ee4; Part Count: 1; Created At: 2026-10-17T05:46:52Z to 2026-10-17T05:46:54Z; Expires At: 2027-01-15T05:45:59Z.
- ICU Name: Android 36 ARM64 i18n ICU APEX. Workflow: .github/workflows/tmp-android36-i18n.yml; Run ID: 39007941479; Storage Mode: SINGLE; Original File: android36-arm64-i18n-icu.tar.gz; Original Size: 12730942 bytes; Original SHA256: ff8e006de1fabdb98cccfcffdb3393410245d9336190ca0821d86e78f089eb49; Part Count: 1; Created At: 2026-10-17T05:54:53Z; Expires At: 2027-01-15T05:54:10Z.
- Graphics path manifest: graphics metadata artifact release/FILE_LIST.txt enumerates all 737 extracted files.
- The Android runtime libraries are real API36 ARM64 binaries, not stubs. Display rendering, Framework ABI compatibility and SurfaceFlinger require additional services and verified graphics backend.

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android 36 Graphics Sysroot archive | android36-r02-20261017 | Android 36 | ARM64 | android36-arm64-graphics-sysroot.tar.gz | 963b4123e91e5bad16463115b4ca201fa3b54907fa474feda0fb82a3fd070ee4 |
| Android 36 libEGL | android36-r02-20261017 | Android 36 | ARM64 | sysroot/system/lib64/libEGL.so | c967542bdb196f84deecc6a65d754a6fd6e18aa18b5039fed1b6d5dbf9016de7 |
| Android 36 libGLESv2 | android36-r02-20261017 | Android 36 | ARM64 | sysroot/system/lib64/libGLESv2.so | b81e8b3c754ad96e7495217e55dcd7c67d3e7ba6da99d503ea4e9e1a254e2200 |
| Android 36 libgui | android36-r02-20261017 | Android 36 | ARM64 | sysroot/system/lib64/libgui.so | 3cccdaf945764512a7f896cc8407b8c4a500713a254cb71bfcac8915c393a445 |
| Android 36 ANGLE EGL | android36-r02-20261017 | Android 36 | ARM64 | sysroot/system/lib64/libEGL_angle.so | b96e3e57c13008203c6785689568d5b43fcb9be901c59c343af1423e93a437d5 |
| Android 36 ANGLE GLESv2 | android36-r02-20261017 | Android 36 | ARM64 | sysroot/system/lib64/libGLESv2_angle.so | 5da7bb9ec6cf0b40d302d64559a96c4e4af5b8a9afd7d0484866d9b073bc08b6 |
| Android 36 i18n APEX archive | android36-r02-20261017 | Android 36 | ARM64 | android36-arm64-i18n-icu.tar.gz | ff8e006de1fabdb98cccfcffdb3393410245d9336190ca0821d86e78f089eb49 |
| Android 36 libicu | android36-r02-20261017 | Android 36 i18n | ARM64 | sysroot/apex/com.android.i18n/lib64/libicu.so | 7a6a0e8f8e55dfae5a2c789c95eda01e05dfa6ad5ae599e567e40b9ffb0c50f9 |
| Android 36 libandroidicu | android36-r02-20261017 | Android 36 i18n | ARM64 | sysroot/apex/com.android.i18n/lib64/libandroidicu.so | 188794585b34624aead7db7e8a62859c7035108765ffef7d9e71ab28652654aa |

### Artifacts

| Part | Artifact ID | Artifact Name | Artifact Size | Artifact SHA256 | Created At | Expires At |
|---|---|---|---|---|---|---|
| Graphics metadata | 12091043204 | android36-graphics-meta | 10204 | 0baed2a10a244737b573f834b2d078a65695d5d5d4623d76997409472b2b3714 | 2026-10-17T05:46:52Z | 2027-01-15T05:45:59Z |
| Graphics 1/1 | 12090878722 | android36-graphics-00 | 80765123 | 0a1fb9f79e6049ac29090bfefee7ddfe16a40e4c342c3ca6cfdddd403c359a93 | 2026-10-17T05:46:54Z | 2027-01-15T05:45:59Z |
| i18n 1/1 | 12091780944 | android36-arm64-i18n-icu | 12608751 | 7e3592f26e217b10325ce9c34c64998840226e32fc5f48d479f9989c41cc4900 | 2026-10-17T05:54:53Z | 2027-01-15T05:54:10Z |

### Restore

Download artifacts using GitHub download_workflow_artifact. Verify each outer ZIP against the Artifact SHA256 above. Extract graphics.part.00; size must be 80764977 bytes; SHA256 must be 963b4123e91e5bad16463115b4ca201fa3b54907fa474feda0fb82a3fd070ee4; rename it to android36-arm64-graphics-sysroot.tar.gz. Verify ICU inner tar.gz SHA256 ff8e006de1fabdb98cccfcffdb3393410245d9336190ca0821d86e78f089eb49. Unpack preserving sysroot/system and sysroot/apex paths. The graphics metadata Artifact provides the complete 737-file path manifest.

One-day temporary vendor probe: Workflow .github/workflows/tmp-android36-vendor.yml; Run ID 39010004799; Artifact ID 12092650991; name android36-vendor-graphics-temporary; Expires At 2026-10-18T06:28:41Z; SHA256 de4469d3889474e81a13650019b28ec531fb1df5d83dccf3134a904c54ba3038. Per temporary-download exception, it is not treated as a long-term cache.


## AOSP API36 95 MB split recovery (2026-10-18)

- Name: `AOSP API36 full ARM64 SDK image (~95 MB partitions)`
- Version: `36_r02-full-v1-95MB`
- Platform: Android 16 / API36 SDK Runtime
- Architecture: AArch64 (arm64-v8a), x86_64 transfer host
- Workflow: `.github/workflows/repack-aosp-api36-95mb-20261018.yml`
- Run ID: `39119724365` ([Actions run](https://github.com/jepede/gpt-exten/actions/runs/39119724365), conclusion success)
- Source workflow Run ID: `39003325276`, reuse of three unexpired original artifacts; **no re-download from Google**
- Artifact Name: `aosp-api36-r02-95mb-part-00` through `-08`, plus `aosp-api36-r02-95mb-manifest`
- Artifact ID: individual per-part IDs below; metadata ID `12133453926`
- File: `full-api36.chunk.00` through `full-api36.chunk.08`, `MANIFEST.json`, `SHA256SUMS.txt`
- Size: parts 00–07 = 95,000,000 raw bytes each; part 08 = 50,736,863 raw bytes
- SHA256: individual part hashes below; original file SHA256 `c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1`
- Created At: `2026-10-18T10:34:17Z` (first chunk); metadata `2026-10-18T10:34:36Z`
- Expires At: `2027-01-16T10:33:28Z` (checked against GitHub API; expires_at governs)
- Storage Mode: `SPLIT`
- Original File: `arm64-v8a-36_r02.zip`
- Original Size: `810736863` bytes
- Original SHA256: `c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1`
- Part Count: `9` (+ 1 manifest Artifact)
- Metadata Artifact: ID `12133453926`, size `4814` bytes, outer ZIP digest `sha256:88c84d2e020ef82b9ce7ce18eb0b7e8936c183f4a22aeb1116da80208c876424`
- Retention: requested `400` days; GitHub reported expires_at `2027-01-16T10:33:28Z` (effectively about 90 days; honor actual expiry)

| Part | Artifact ID | Artifact Name | Outer ZIP Size | Outer ZIP SHA256 | Created At | Expires At |
|---|---:|---|---:|---|---|---|
| 00 | `12133677845` | `aosp-api36-r02-95mb-part-00` | `95000152` | `sha256:6a3ebb139326920c86fa6ce670e62064e906ec41cc60889cbe9e8b7ffee8ff8f` | `2026-10-18T10:34:17Z` | `2027-01-16T10:33:28Z` |
| 01 | `12133677851` | `aosp-api36-r02-95mb-part-01` | `95000152` | `sha256:1f50a12a0ca8dc535a0a90acf6f283696ead22a23644f19fe7117bf51349e90e` | `2026-10-18T10:34:19Z` | `2027-01-16T10:33:28Z` |
| 02 | `12133533564` | `aosp-api36-r02-95mb-part-02` | `95000152` | `sha256:328c7f7b48bddcf437116804fce2e232b6d497bd6e76706ec464373fb7190b5b` | `2026-10-18T10:34:21Z` | `2027-01-16T10:33:28Z` |
| 03 | `12133608269` | `aosp-api36-r02-95mb-part-03` | `95000152` | `sha256:5287c5710d674b5197d35cd4104c55357b30b73da9c4905b67743d170fba20f7` | `2026-10-18T10:34:24Z` | `2027-01-16T10:33:28Z` |
| 04 | `12133309620` | `aosp-api36-r02-95mb-part-04` | `95000152` | `sha256:9a29901ba2a37f30490e56567f56d3d27721b28d43f8470070433ffddc32b1f8` | `2026-10-18T10:34:26Z` | `2027-01-16T10:33:28Z` |
| 05 | `12133657891` | `aosp-api36-r02-95mb-part-05` | `95000152` | `sha256:7202bb6cee628b768bbbbeaafde050f2ae2f67cd1068bb8a90042c4a3dd76405` | `2026-10-18T10:34:28Z` | `2027-01-16T10:33:28Z` |
| 06 | `12133623161` | `aosp-api36-r02-95mb-part-06` | `95000152` | `sha256:76e37042c01f22a330243ea02c4b11e69602c3f3c8cf3585116997b22d01168f` | `2026-10-18T10:34:31Z` | `2027-01-16T10:33:28Z` |
| 07 | `12133473855` | `aosp-api36-r02-95mb-part-07` | `95000152` | `sha256:7ddfdc89656f16b5ce135530ab30dd63eb2c945dece0d7bf8b7f2766cec3deb7` | `2026-10-18T10:34:33Z` | `2027-01-16T10:33:28Z` |
| 08 | `12133638131` | `aosp-api36-r02-95mb-part-08` | `50737015` | `sha256:8dcc55567a23d43de78e711ce2b9bf560d07c380b1b6ecb210460ebf5720d64a` | `2026-10-18T10:34:35Z` | `2027-01-16T10:33:28Z` |

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android 36 ARM64 AOSP source chunk 00 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.00` | `5d5a7dab507283f337db1960e717016cd3acd6dd663781d7d3d6b8e6c1b0d628` |
| Android 36 ARM64 AOSP source chunk 01 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.01` | `e99ac48ef8791d56577f7e0d1ac5119a843197c22c18a98e1b6e87273c82ab39` |
| Android 36 ARM64 AOSP source chunk 02 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.02` | `77ee411e03586659a8d00bf0e1720784a210994c828807de0dd0f4441e3eaaed` |
| Android 36 ARM64 AOSP source chunk 03 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.03` | `fe2695e340aae6237e8ba24a36fae9f320ede836c8848e8767aa17235ab4f272` |
| Android 36 ARM64 AOSP source chunk 04 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.04` | `820bef5417c4f0f6eee78c68ab77bd473a66f5399419e1baac648bb609d328d8` |
| Android 36 ARM64 AOSP source chunk 05 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.05` | `0df7f2fb170a55c63b711fe929b2a668d7fe37355b5b6278f9f96d2193301178` |
| Android 36 ARM64 AOSP source chunk 06 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.06` | `731491c097d20ff106a301e0cae64d866129dd4a38d6fc7f625de5e0fa4c56d1` |
| Android 36 ARM64 AOSP source chunk 07 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.07` | `30e0b86d488c778a43da0753757490ab28a57e4965bcff85e1c830e72ac174e0` |
| Android 36 ARM64 AOSP source chunk 08 | 36_r02-full-v1-95MB | Android 16 / API36 | AArch64 | `full-api36.chunk.08` | `319f861fc28fde186e6fda0c4ddd37bbb7999b3bccb4e5602837fd6b7ff9dfc7` |

### Restore & verified test

Check each Artifact ID against GitHub Actions `expires_at` before downloading. Download the manifest and parts `00` through `08` **individually** with `download_workflow_artifact` (each outer Artifact ≤95,000,152 bytes, final one 50,737,015 bytes). Verify each outer archive SHA256 against the table, extract each raw chunk and compare SHA256 with the raw-file table, concatenate in numerical order, and check reconstructed byte count `810736863` plus SHA256 `c6194eb8ace128b174ea86b5fbc0c78204147123b3b5ce6d0e3d615a06ad31d1`. Prefer internal directories such as `/opt/arm64-lab/sdk-cache` for the 811 MB assembled file, avoiding durable conversation attachment uploads over 512 MB. Locally tested on 2026-10-18: all 9 outer Artifact downloads returned successfully, all raw SHA256 checks passed, assembled source matched, all 20 ZIP internal entries passed CRC, Android 36 SDK image extracted; no `ClientError` or OOM. A different generated-attachment upload error occurred when placing the assembled 811 MB ZIP under `/mnt/data` and was resolved by using the internal `/opt` path. This does not imply the Android guest or `test_elf` can run on QEMU virt without Android Emulator/Ranchu devices.

## Artifact Record: Android NDK r28c minimal Clang/LLD (2026-10-18)

- Name: Android NDK minimal Clang/LLD
- Version: r28c-minimal-v1 (Clang 19.0.1; NDK r28c/r530567e)
- Platform: Linux
- Architecture: x86_64 host + AArch64 Android target
- Workflow: .github/workflows/arm64-lab-clang-r28c-minimal-20261018.yml
- Run ID: 39121838147
- Run URL: https://github.com/jepede/gpt-exten/actions/runs/39121838147
- Source: verified, unexpired five-part NDK r28c cache Run 39019800471; no upstream Google re-download
- Source SHA256: dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f
- Artifact Name: arm64-lab-clang-r28c-95mb-00, arm64-lab-clang-r28c-95mb-01
- Artifact ID: 12135105748, 12135080934
- File: ndk-clang-r28c.part.00, ndk-clang-r28c.part.01
- Size: raw parts 95000000 and 72910784 bytes; ZIP sizes 95000158 and 72910942 bytes
- SHA256: per-part raw and outer ZIP hashes in the table below
- Created At: 2026-10-18T11:10:12Z to 2026-10-18T11:10:16Z
- Expires At: 2027-01-16T11:05:31Z (actual GitHub expires_at; expired=false)
- Storage Mode: SPLIT
- Original File: ndk-clang-r28c.tar.xz
- Original Size: 167910784 bytes
- Original SHA256: b0d693a2b69a0bf218135e07abfed0350c3c5ab317b42fe40a16e8324ec6d81c
- Part Count: 2
- Requested Retention: 400 days; effective expiry is authoritative
- Metadata Artifact Name: arm64-lab-clang-r28c-meta
- Metadata Artifact ID: 12135105757
- Metadata ZIP Size: 17175 bytes
- Metadata ZIP SHA256: c6629148293e3014b2bd3f6793a82e2a3cc558a318124fb00a48014a7d5d2c2b
- Metadata File: MANIFEST.json
- Metadata File SHA256: e86218a7f9e1402a226114f9a5d67d3925628c894c62e653e5343f35fc3d8a37
- Scope: minimal compiler, LLD, shared compiler libraries and Clang resource headers/runtimes. This is not the complete NDK sysroot. It supports the ARM64 lab's supplied -nostdlib C/assembly example build recipes.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android NDK minimal compiler bundle | r28c-minimal-v1 | Linux | x86_64 host + AArch64 target | ndk-clang-r28c.tar.xz | b0d693a2b69a0bf218135e07abfed0350c3c5ab317b42fe40a16e8324ec6d81c |
| NDK Clang native executable | 19.0.1/r530567e | Linux | x86_64 | ndk-clang/bin/clang-19 | 6156dd4e5e466333197a00b8d20bca72c292186643b749dcaaa3aa9164afb1de |
| NDK LLD native executable | r28c/r530567e | Linux | x86_64 | ndk-clang/bin/lld | 0bb0398c038e4c8b5e01e61061f6d9349961fb495efb4cbf2552e36058acf0be |

| Part | Artifact ID | Artifact Name | Raw File | Raw Size | Raw SHA256 | Artifact Size | Artifact ZIP SHA256 | Created At | Expires At |
|---|---:|---|---|---:|---|---:|---|---|---|
| 00 | 12135105748 | arm64-lab-clang-r28c-95mb-00 | ndk-clang-r28c.part.00 | 95000000 | a3e7ccf417f6bbfef8e50096314c5523783ce0d725d14a9b8a2e4f1b41b9ca01 | 95000158 | 9413b8cb72e65dd57da165b636af9fc50dc550b79fdf7856cfd0f141d5476718 | 2026-10-18T11:10:12Z | 2027-01-16T11:05:31Z |
| 01 | 12135080934 | arm64-lab-clang-r28c-95mb-01 | ndk-clang-r28c.part.01 | 72910784 | 877f9733e726b49fc50d32a01ea8186ed94d7bde67ff4dceb02bb2e9fd7dac20 | 72910942 | d2c7bcdd6d7e08d153ec92653594f3eafe6683da8fe0733e84957e1999da1949 | 2026-10-18T11:10:15Z | 2027-01-16T11:05:31Z |

Restore: check actual existence and expires_at, download each artifact separately with download_workflow_artifact, verify outer ZIP and raw part SHA256, concatenate 00 then 01, verify original size/SHA256, and extract ndk-clang. Every outer ZIP is below 100 MB and 512 MB. MANIFEST.json records the full extracted path/hash list; hashes of symlink entries represent link target bytes.


## Android Emulator 37.2.12 ARM64 TCGraphics repair (2026-10-18)

- Name: Android Emulator (Ranchu/GLES)
- Version: 37.2.12.0 (build 16428233, stable)
- Platform: Linux
- Architecture: x86_64 host, ARM64-v8a guest (cross-ISA TCG)
- Workflow: `.github/workflows/cache-android-emulator-37_2_12-90mb-20261018.yml`
- Run ID: `39122587987` ([Actions run](https://github.com/jepede/gpt-exten/actions/runs/39122587987))
- Source: `https://dl.google.com/android/repository/emulator-linux_x64-16428233.zip`
- Artifact Name: `android-emulator-37_2_12-x64-part-00` through `-03`, metadata `android-emulator-37_2_12-x64-metadata`
- Artifact ID: listed below; metadata Artifact ID `12133754942`
- File: `emulator-37.2.12.part.00` through `-03`, `MANIFEST.json`, `SHA256SUMS.txt`
- Size: each of parts 00-02 = 90,000,000 bytes; part 03 = 79,654,171 bytes
- SHA256: per part listed below; original source SHA256 `b08fc43d8608d2955f607f1b287beb525041e730086bdca3af152accac3af9c1`
- Created At: `2026-10-18T11:16:56Z` (first part)
- Expires At: `2027-01-16T11:16:44Z` (actual GitHub API expiry, not requested retention)
- Storage Mode: SPLIT
- Original File: `emulator-linux_x64-16428233.zip`
- Original Size: 349654171 bytes
- Original SHA256: `b08fc43d8608d2955f607f1b287beb525041e730086bdca3af152accac3af9c1`
- Part Count: 4
- Metadata outer ZIP SHA256: `sha256:26cf288fbb2212a9a9714361efd8f3f2d89b633bfd61219dbc52ae8c1c040147`; expires `2027-01-16T11:16:44Z`

| Part | Artifact ID | Artifact Name | Artifact Size | Outer SHA256 | Expires At |
|---|---:|---|---:|---|---|
| 00 | `12135255704` | `android-emulator-37_2_12-x64-part-00` | 90000162 | `sha256:1fb562e6bd38ad1df6d9443150ccd4931495cf190e1699a26b172c87c223ff77` | `2027-01-16T11:16:44Z` |
| 01 | `12135071739` | `android-emulator-37_2_12-x64-part-01` | 90000162 | `sha256:2a004ef603759d06f51ef47a143ed56731ec1fa0ae2136690cb7ed8be957d860` | `2027-01-16T11:16:44Z` |
| 02 | `12135036812` | `android-emulator-37_2_12-x64-part-02` | 90000162 | `sha256:c0c4f10166fa9981e4495e8a668bb626b33652638ea7127cb94a12ecccaa0602` | `2027-01-16T11:16:44Z` |
| 03 | `12135146417` | `android-emulator-37_2_12-x64-part-03` | 79654333 | `sha256:bb8f904323ddb22c0ad1a79bdb536878bbb25c1d769c9dbcb4f2fa969194f963` | `2027-01-16T11:16:44Z` |

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android Emulator source chunk 00 | 37.2.12.0 | Linux | x86_64 | `emulator-37.2.12.part.00` | `c06b59081fb40c1ed3161612f6d63c870afca38f00441b828d6609d8d6bedb80` |
| Android Emulator source chunk 01 | 37.2.12.0 | Linux | x86_64 | `emulator-37.2.12.part.01` | `f1c50cde1af94cd91778fab6a0152bbc612cbd9513df49e89299afb79e8d1345` |
| Android Emulator source chunk 02 | 37.2.12.0 | Linux | x86_64 | `emulator-37.2.12.part.02` | `9cab730bd6d4f4eb7a69f72a7ab739d655e0d1433201c175df5897489f366489` |
| Android Emulator source chunk 03 | 37.2.12.0 | Linux | x86_64 | `emulator-37.2.12.part.03` | `d4d9e2fe5df31da0544f6b6b4df66aeeec5802524a87d6cc0816357678c98960` |

### Restore

Download four part Artifacts plus metadata from GitHub, check archive SHA256, extract in part order, verify raw-part SHA256, concatenate into emulator source ZIP, then verify exact original size and SHA256. ZIP CRC tested locally, extracted to `/opt/arm64-lab/android-sdk/emulator`, executable `emulator -version` verified. Standard emulator launcher blocks ARM64 API36 on x86_64. Direct engine `qemu/linux-x86_64/qemu-system-aarch64-headless` with `ANDROID_I_WANT_MY_TCG=yes`, `-feature -VirtioSndCard`, `-qemu -machine virt` booted official Android 16 init/service-manager on TCG. This is experimental, slow, and does not certify full Android boot or app execution.

## Android Platform-Tools ADB cached subset (2026-10-18)

- Name: Android Platform-Tools ADB cached subset
- Version: 37.0.1
- Platform: Linux
- Architecture: x86_64
- Workflow: `.github/workflows/repack-cached-adb-20261018.yml`
- Run ID: `39123346053`, source Run ID `34697680626` (cache reuse, no download from Google)
- Artifact ID: `12135192496`
- Artifact Name: `android-adb-37_0_1-cached-small`
- File: `platform-tools-37.0.1.tar.gz`
- Size: outer Artifact `8791019` bytes; extracted tarball `8790360` bytes
- SHA256: outer ZIP `sha256:c80d9a38e94fd642a019a5e93acdfd450790163f81145490cc5e425a3ac534d4`, inner tar.gz `3358695e1c060ae59cfd137651a7c0ba4d7685a9cc4465e473e1982ed99dc88d`
- Created At: `2026-10-18T11:28:20Z`
- Expires At: `2027-01-16T11:28:02Z`
- Storage Mode: SINGLE
- Original File: `platform-tools-37.0.1.tar.gz`
- Original Size: 8790360 bytes
- Original SHA256: `3358695e1c060ae59cfd137651a7c0ba4d7685e473e1982ed99dc88d`
- Part Count: 1

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android ADB / Platform-Tools | 37.0.1 | Linux | x86_64 | `platform-tools-37.0.1.tar.gz` | `3358695e1c060ae59cfd137651a7c0ba4d7685a9cc4465e473e1982ed99dc88d` |

### Restore

Download Artifact `12135192496` via GitHub connector, verify outer ZIP SHA256, unpack tar.gz and verify inner SHA256, then extract `platform-tools/` to SDK root. Cached bundle was repacked from still-active prior SDK artifact `10299605918` and its original compressed SHA256 independently checked. Installed ADB was tested with `adb version` and `adb devices`.

## Artifact Record: Lua recovery tools (2026-10-24)

- Artifact Name: `lua-recovery-tools-x86_64-v1`
- Artifact ID: `12550289662`
- Run ID: `40069691962`
- Workflow: `.github/workflows/lua-recovery-tools-20261024.yml`
- File: `lua-recovery-tools-v1.tar.gz` (plus SHA256SUMS.txt inside Artifact ZIP)
- Size: `17307390` bytes (Artifact ZIP)
- SHA256: `d2681339cd0cd6f1194c64e8d7404c8a1d0a468d5b147e58856d1317ca614849` (Artifact ZIP)
- Created At: `2026-10-24T06:19:00Z`
- Expires At: `2027-01-22T06:18:37Z` (actual GitHub expires_at)
- Storage Mode: `SINGLE`
- Original File: `lua-recovery-tools-v1.tar.gz`
- Original Size: `17307005` bytes
- Original SHA256: `9bebb43bee2e903b6837d008585b7470208b0d2b899db1191ac0cc0b44a2e459`
- Part Count: `1`
- Requested retention-days: `400`; actual expiry above governs.
- Verified locally: outer ZIP SHA256, inner TAR.GZ SHA256, and all 24 manifest file hashes.
- Version: `luajit-ubuntu24-stylua2.6.0-ruff0.14.3-v1`
- Platform: `Linux`; Architecture: `x86_64`

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| LuaJIT | 2.1.0+git20231223.c525bcb+dfsg-1ubuntu0.1 | Linux | x86_64 | bin/luajit | 0a700d653c9f38b8bfbc732707815b2833eb65b2c9af5d4f7eb706278f0859ed |
| StyLua | 2.6.0 | Linux | x86_64 | bin/stylua | 58f2f3056700c3a3c34b50da1c1e6316a24dc5713ecef436f01e77364e561270 |
| ruff | 0.14.3 | Linux | x86_64 | bin/ruff | fe1e096f493c1fc66f23914dd4c6ac79c580f5ebff959690efafa9184dfdd186 |

Restore: check Artifact existence and actual expires_at, download Artifact 12550289662, verify ZIP and inner archive SHA256, extract the TAR.GZ and validate MANIFEST.json. Set LD_LIBRARY_PATH to tools/lib and LUA_PATH to tools/share/?.lua when running the bundled LuaJIT. The Artifact is below 100 MB and the 512 MB single-download limit.


## Artifact Record: clang-format 19.1.7 Linux x86_64 (2026-10-24)

- Artifact Name: `clang-format-19_1_7-linux-x86_64`
- Artifact ID: `12553130239`
- Run ID: `40074754345`
- Workflow: `.github/workflows/cache-clang-format-20261024.yml`
- File: `clang-format-19.1.7-linux-x86_64.tar.gz`
- Size: `3454899` bytes (Artifact ZIP)
- SHA256: `475b18624be86b3ad47d30d4b62e78753cdee26b401595a730b6b99375abdefb` (Artifact ZIP)
- Created At: `2026-10-24T07:35:47Z`
- Expires At: `2027-01-22T07:35:41Z` (GitHub actual expiry)
- Storage Mode: `SINGLE`
- Original File: `clang-format-19.1.7-linux-x86_64.tar.gz`
- Original Size: `1727754` bytes
- Original SHA256: `0f0fcf5c623dd67fd0fbec294cd4b59321b0d473e54d055027778f07f83282d9`
- Part Count: `1`
- Requested retention-days: `400`; actual expiry above governs.
- Locally verified: outer ZIP SHA256/CRC, inner TAR.GZ SHA256, formatter version, executed to format C++17 sources.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| clang-format | 19.1.7 | Linux | x86_64 | tools/bin/clang-format | 70966c7d32d605aaccd043dd59bd3ee2173531043918a9714b78ebf8eb8e4028 |

Restore: verify Artifact 12553130239 still exists and is unexpired, download with download_workflow_artifact, check ZIP and inner TAR SHA256, extract tools/, and verify tools/bin/clang-format --version. Original pinned PyPI wheel is also included for provenance. Archive is below 100 MB.


## Artifact Record: ARM64 system lab 95 MB cache reuse (2026-10-25)

- Name: ARM64 system lab
- Version: debian13-v1-qemu10.0.13-linux6.12.111-95MB
- Platform: Linux / Debian 13
- Architecture: x86_64 host + AArch64 guest
- Workflow: `.github/workflows/reuse-arm64-system-lab-95mb-20261025.yml`
- Run ID: `40152956031`
- Source: verified, unexpired Artifact `11032351529`, Run `36566866696`; no upstream re-download
- Source Artifact ZIP SHA256: `64fdcf5d1843bedfe0012cb19667f4b2865f81b835033d6f296a01e3dce7599a`
- Artifact Name: `arm64-system-lab-reuse-95mb-00`, `arm64-system-lab-reuse-95mb-01`
- Artifact ID: `12582993616`, `12582729069`
- File: `arm64-system.part.00`, `arm64-system.part.01`
- Size: raw parts `95000000` and `27163200` bytes; outer ZIP sizes `95000154` and `27163354` bytes
- SHA256: per-part hashes below
- Created At: `2026-10-25T02:03:01Z` through `2026-10-25T02:03:04Z`
- Expires At: `2027-01-23T02:02:53Z` (actual GitHub expires_at, expired=false)
- Storage Mode: SPLIT
- Original File: `arm64-system-lab-debian13-v1.tar`
- Original Size: `122163200` bytes
- Original SHA256: `1819458934fb118d7b11bf9564aa8fb4c6882a932d6fada0dc76ac58dcf44ca1`
- Part Count: 2 (+ 1 manifest Artifact)
- Requested retention-days: 400; actual expiry above governs
- Metadata Artifact Name: `arm64-system-lab-reuse-95mb-manifest`
- Metadata Artifact ID: `12582978637`
- Metadata File: `MANIFEST.json`
- Metadata ZIP Size: `494` bytes
- Metadata ZIP SHA256: `48f77e90db0ca0d8bba7bc0493b987db8d271f6535f3629fa5f4f625f005cdc2`
- Verified locally: all three outer ZIP hashes, both raw part sizes/SHA256, reconstructed TAR size/SHA256, and every packaged DEB against meta/SHA256SUMS.txt.

| Part | Artifact ID | Artifact Name | Raw File | Raw Size | Raw SHA256 | ZIP Size | ZIP SHA256 | Created At | Expires At |
|---|---:|---|---|---:|---|---:|---|---|---|
| 00 | 12582993616 | arm64-system-lab-reuse-95mb-00 | arm64-system.part.00 | 95000000 | 415fa9a67382e5bcf029496d81d19e688d9e6a52423b0c003ce6c325f484383c | 95000154 | 950b75e67aacfce9f27e6d79f4a1a61f4c65002a0b3e426b2f4d0bf9d29fbe2e | 2026-10-25T02:03:01Z | 2027-01-23T02:02:53Z |
| 01 | 12582729069 | arm64-system-lab-reuse-95mb-01 | arm64-system.part.01 | 27163200 | 57d1039dd4c499c41348217464809e406ad9e9ee8dffb9d3a63717d84f306377 | 27163354 | 4cedb32efe7021d949e55dcdc6ea4743f4efec5131137d7d52cd26fc78b46cf8 | 2026-10-25T02:03:03Z | 2027-01-23T02:02:53Z |

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| e2fsprogs | 1.47.2-3+b12 | Linux / Debian 13 | amd64 | host/e2fsprogs_1.47.2-3+b12_amd64.deb | e9e638eb3e22b5f14d01ce0b28aa512a5a22fcc0e70d1c733444579b67ea236b |
| qemu-system-arm | 1:10.0.13+ds-0+deb13u1 | Linux / Debian 13 | amd64 | host/qemu-system-arm_1%3a10.0.13+ds-0+deb13u1_amd64.deb | babb8ab3c9f5f045184bd8c20604237d28c1b5e6a578d7f400566b9f257b59e7 |
| qemu-system-common | 1:10.0.13+ds-0+deb13u1 | Linux / Debian 13 | amd64 | host/qemu-system-common_1%3a10.0.13+ds-0+deb13u1_amd64.deb | 3a99dc23c42c66bb7e96dc1f2ba12b1797d154a472fbdb1cfcd822d9fb69e85b |
| qemu-system-data | 1:10.0.13+ds-0+deb13u1 | Linux / Debian 13 | all | host/qemu-system-data_1%3a10.0.13+ds-0+deb13u1_all.deb | a0e03c526cc09d4c2ab20aa19a8c12e916cdc49a170acb16a6563c28f70eafd3 |
| busybox-static | 1:1.37.0-6+b9 | Linux / Debian 13 | arm64 | guest/busybox-static_1%3a1.37.0-6+b9_arm64.deb | c833be48abfa16bc19c4966ec93e289ff1ce5d2f1476cad3a57bd105378cd15c |
| gdbserver | 16.3-1 | Linux / Debian 13 | arm64 | guest/gdbserver_16.3-1_arm64.deb | b749a29afca991a43f82b04b42f8dedc2ad3182a020cd776a327568a3660e1bb |
| linux-image-6.12.111+deb13-arm64 | 6.12.111-1 | Linux / Debian 13 | arm64 | guest/linux-image-6.12.111+deb13-arm64_6.12.111-1_arm64.deb | 981370389cb9f6241b41f66ea5c8a0e7bdd28b9e959cec4d3bac97b1eb1248bf |
| strace | 6.13+ds-1 | Linux / Debian 13 | arm64 | guest/strace_6.13+ds-1_arm64.deb | d793af70a104eb0bd5be466c3043b512f549e7cb27971320a7c9b8f4c6165e55 |

Restore: verify current existence and expires_at, download each Artifact separately with download_workflow_artifact, verify outer ZIP and raw-part hashes, concatenate part 00 then 01, verify the original TAR, and extract the DEBs. No individual Artifact exceeds 100 MB or the 512 MB tool limit. This is the same verified source bundle as the older SINGLE cache, repacked for safer transfers.


## Artifact Record: OSS NDK r28c AArch64 cJSON / zlib / xxHash (2026-10-25)

- Name: OSS Android ARM64 NDK r28c cJSON+zlib+xxHash
- Version: cJSON 1.7.19 + zlib 1.3.1 + xxHash 0.8.3
- Platform: Android API35 (Bionic) / Linux x86_64 Actions host
- Architecture: arm64-v8a
- Workflow: `.github/workflows/arm64-ndk-oss-github-actions-20261025.yml`
- Run ID: `40162461240`
- Run Conclusion: success
- Build NDK: r28c, Clang 19.0.1; reused valid verified NDK cache run `39019800471` (no new upstream NDK download)
- Artifact Name: `oss-ndk-r28c-arm64-api35-20261025`
- Artifact ID: `12587265634`
- File: `oss-ndk-r28c-arm64-api35-20261025-actions.zip`
- Size: `206346` bytes
- SHA256: `7362bb7209be4ee272d17a00cb4488b8121af3676ce837310fb7cfceab997a48` (actual downloaded Artifact ZIP digest)
- Created At: 2026-10-25T04:35:49Z
- Expires At: 2027-01-23T04:35:49Z (actual GitHub result, expired=false)
- Storage Mode: SINGLE
- Original File: `release/` (19 files; GitHub Actions artifact payload)
- Original Size: `612727` bytes (uncompressed entries)
- Original SHA256: `3c727b2567050a1fac5a3bf352c2c453c9872ca5dde9d9b6b6dfa40c8843be0d` (SHA256 of payload's `SHA256SUMS.txt` manifest; original is a directory, so this is **not** an overall directory hash)
- Part Count: 1
- Source revisions: cJSON `c859b25da02955fef659d658b8f324b5cde87be3`, zlib `51b7f2abdade71cd9bb0e7a373ef2610ec6f9daf`, xxHash `e626a72bc2321cd320e953a0ccf1584cad60f363`
- Verified in local QEMU System 10.0.13 TCG + ARM64 kernel 6.12.111 + Android 15 Bionic linker64: `smoke_link` real JSON parse, compression/decompression, XXH64/XXH3 checks; `smoke_dlopen` loads and executes exported functions from all three SO; both Guest target exit codes = 0, QEMU host RC = 0; `-nic none`.
- Upstream sources are obtained by Actions from their public repositories at the immutable release tags. Build task first failed on missing `unistd.h` declaration for zlib, then rebuilt successfully with `-include unistd.h`; no upstream source modification.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| cJSON | 1.7.19 | Android API35 | arm64-v8a | `lib/liboss_cjson.so` | `bd6adf9af21f3b717cbf9fd0548595b7525fe63c17734d5b85692d7f5b0ed75d` |
| zlib | 1.3.1 | Android API35 | arm64-v8a | `lib/liboss_zlib.so` | `779583a3584cf49fda8729b8526b8c8ab9f59a084ab9c610350d4c06060b4bf1` |
| xxHash | 0.8.3 | Android API35 | arm64-v8a | `lib/liboss_xxhash.so` | `c6233adf8c8abdcfc7ffb0b1168e6a5f9206200491bd2202358da63ad65341dc` |
| Linked ELF test | v1 | Android API35 | arm64-v8a | `bin/smoke_link` | `3833d58e367d3422f58dc8578f54ce4970b320ed6ecec17c8bc6ec09e8c4becb` |
| dlopen/dlsym ELF test | v1 | Android API35 | arm64-v8a | `bin/smoke_dlopen` | `5c2f751e3b55c96b5dc4523d56f67afc1031b5292778e6912ecc756a5da099a9` |



## Artifact Record: OSS ARM64 NDK build pinned upstream source snapshot (2026-10-25)

- Artifact Name: `oss-ndk-r28c-upstream-sources-20261025`
- Artifact ID: `12586738612`
- Run ID: `40162823267`
- Workflow: `.github/workflows/arm64-ndk-oss-full-source-20261025.yml`
- Name: OSS NDK r28c pinned source snapshot
- Version: cJSON 1.7.19 + zlib 1.3.1 + xxHash 0.8.3
- Platform: Portable C sources / GitHub Actions Linux
- Architecture: Any (used to build Android arm64-v8a)
- File: `oss-ndk-r28c-upstream-sources-complete-20261025.zip`
- Size: `3330692` bytes
- SHA256: `ed5edfd5dd622e0069db2b254591071e5474c3557b79911c4dfb147ba3d0996e` (GitHub artifact archive)
- Created At: `2026-10-25T04:41:50Z`
- Expires At: `2027-01-23T04:41:50Z` (actual GitHub result; expired=false)
- Storage Mode: SINGLE
- Original File: `release/upstream/` directory with `UPSTREAM_COMMITS.txt` + `SOURCES_SHA256SUMS.txt`
- Original Size: `11184297` bytes (uncompressed ZIP contents)
- Original SHA256: `a22401a39d6d89b56a760f678f5ac611712dc70bbf4c61264b4cd621927877de` (SHA256 of source manifest `SOURCES_SHA256SUMS.txt`, not a directory aggregate hash)
- Part Count: 1
- Source file count: 573 upstream files + two metadata files.
- Verification: downloaded GitHub artifact ZIP SHA256 matched, ZIP CRC passed, all 574 manifest entries passed `sha256sum -c`. The first source run `40162740958` omitted 30 hidden files because `actions/upload-artifact@v4` defaults; corrected with `include-hidden-files: true` in run `40162823267`. Use the corrected artifact.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| cJSON source snapshot | 1.7.19 | Portable source | Any | `upstream/cJSON/` | `a22401a39d6d89b56a760f678f5ac611712dc70bbf4c61264b4cd621927877de` (combined manifest hash, not individual directory hash) |
| zlib source snapshot | 1.3.1 | Portable source | Any | `upstream/zlib/` | `a22401a39d6d89b56a760f678f5ac611712dc70bbf4c61264b4cd621927877de` (combined manifest hash) |
| xxHash source snapshot | 0.8.3 | Portable source | Any | `upstream/xxHash/` | `a22401a39d6d89b56a760f678f5ac611712dc70bbf4c61264b4cd621927877de` (combined manifest hash) |


## Honor of Kings CN Unity IL2CPP coordinate kit v12.1.1.1 (2026-10-26)

- Original APK: Tencent MyApp remote ZIP, version 12.1.1.1, package `com.tencent.tmgp.sgame`, claimed source 1,748,020,376 bytes.
- Source checksum caveat: ZIP member CRC32 and extracted SO SHA256 verified; entire APK MD5/SHA256 **not** verified.
- Workflow: `.github/workflows/hok-coordinate-engine.yml`, GitHub Run ID `40311637215`.
- All per-member ZIPs individually below 100MB; `Storage Mode: SINGLE` for every Artifact.
- Requested retention: 400 days. Actual GitHub expires_at governs: `2027-01-24T10:59:21Z`.
- Part Count: 1 for each individually packaged file; each original binary is inside its own ZIP.

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| HoK IL2CPP native | 12.1.1.1 | Android | arm64-v8a | `lib/arm64-v8a/libil2cpp.so` | `6e00c3ac8ac129d7b6dd5bdd5c8c72777d70a91a317d193bf5f422505d9bafd5` |
| HoK GameCore native | 12.1.1.1 | Android | arm64-v8a | `lib/arm64-v8a/libGameCore.so` | `dc034883ea2fc5c6be42d2e3b068652a7e1829f73450bb732fceebbd8f75d4c8` |
| HoK Unity native | 12.1.1.1 | Android | arm64-v8a | `lib/arm64-v8a/libunity.so` | `6f862b245e048e8062b71c747d817bbb942276039bf6991adea60046b19b68a8` |
| HoK global-metadata | 12.1.1.1 | Android / Unity IL2CPP Metadata | arm64-v8a | `assets/bin/Data/Managed/Metadata/global-metadata.dat` | `5e66b7a0597679b6ef0383755eee4adb60a71f15a87a6fab91582eaa7f85a3a7` |

### Artifacts

| Artifact Name | Artifact ID | Run ID | File | Artifact Size | Artifact Digest | Created At | Expires At | Storage Mode | Original File | Original Size | Original SHA256 | Part Count |
|---|---:|---:|---|---:|---|---|---|---|---|---:|---|---:|
| `hok-coordinate-v12.1.1.1-il2cpp-arm64` | `12644338989` | `40311637215` | `hok-12.1.1.1-il2cpp.zip` | 77648291 | `sha256:7fb40761b492dd94d98687b42aa415b0a230dad9cc2d8bebb10dec854a0904fa` | `2026-10-26T11:00:17Z` | `2027-01-24T10:59:21Z` | SINGLE | `lib/arm64-v8a/libil2cpp.so` | 227661664 | `6e00c3ac8ac129d7b6dd5bdd5c8c72777d70a91a317d193bf5f422505d9bafd5` | 1 |
| `hok-coordinate-v12.1.1.1-gamecore-arm64` | `12644064463` | `40311637215` | `hok-12.1.1.1-gamecore.zip` | 21200618 | `sha256:867d29d1b57fb7b2fb2d670a1670dd89adc11a5a69592aee45779ec81590f708` | `2026-10-26T11:00:19Z` | `2027-01-24T10:59:21Z` | SINGLE | `lib/arm64-v8a/libGameCore.so` | 86426392 | `dc034883ea2fc5c6be42d2e3b068652a7e1829f73450bb732fceebbd8f75d4c8` | 1 |
| `hok-coordinate-v12.1.1.1-unity-arm64` | `12644788311` | `40311637215` | `hok-12.1.1.1-unity.zip` | 13956892 | `sha256:e3005dff66484e8f3aa591e19730345b94bae1e302f4050ff91a07a3c41fb3e5` | `2026-10-26T11:00:21Z` | `2027-01-24T10:59:21Z` | SINGLE | `lib/arm64-v8a/libunity.so` | 30220440 | `6f862b245e048e8062b71c747d817bbb942276039bf6991adea60046b19b68a8` | 1 |
| `hok-coordinate-v12.1.1.1-global-metadata` | `12644384544` | `40311637215` | `hok-12.1.1.1-metadata.zip` | 17343114 | `sha256:7d820c83f0715afe5e5a18b102c6f876b6ab86ea00cf6aa79301e7a081724b1a` | `2026-10-26T11:00:23Z` | `2027-01-24T10:59:21Z` | SINGLE | `assets/bin/Data/Managed/Metadata/global-metadata.dat` | 60322264 | `5e66b7a0597679b6ef0383755eee4adb60a71f15a87a6fab91582eaa7f85a3a7` | 1 |

### Restore

Use the four GitHub artifact IDs above; download each individually with `download_workflow_artifact`. Check its outer ZIP against `Artifact Digest`, extract its inner `hok-12.1.1.1-*.zip`, check against `portable_archive_sha256` in `reports/hok_20261026/portable_archive_manifest.json` of branch `work/hok-coordinate-study-20261026`, extract ELF/metadata, verify original SHA256 and ZIP CRC32. These are individual binary files; no 1.75GB whole APK is included.
