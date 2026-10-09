# Artifact Cache

GitHub Actions 可复用 Artifact 索引。下载资源前优先按 `Name + Version + Platform + Architecture` 查询；是否仍可用以 GitHub 实际返回的 `expires_at` 为准。

## Index
| Mozilla NSS TLS Root Store | release-b9bd270cfa3e-20261005 | Any | Any | `37253767754` | SINGLE | `2027-01-03T02:02:10Z` |

| Name | Version | Platform | Architecture | Run ID | Storage | Expires At |
|---|---|---|---|---:|---|---|
| TinyHTTPS OpenSSL + curl reference sources | OpenSSL 4.0.3 + curl 8.22.0 | Any | Any | `37458536791` | SINGLE | `2027-01-04T11:45:33Z` |
| PUBG MOBILE Global Base APK | 4.6.0 (21525) | Android | arm64-v8a | `37217716536` | SINGLE | `2027-01-02T16:41:47Z` |
| radare2 | 6.2.2 | Linux / Debian | x86_64 | `36873712969` | SINGLE | `2026-12-30T14:06:12Z` |
| TrustAttestor UI Gradle dependency cache | agp8.7.2-kotlin2.0.21-ui-releasecomplete-v3 | Linux | x86_64 | `34698530131` | SINGLE | `2026-12-11T14:10:58Z` |
| Android SDK Build-Tools | 34.0.0 | Linux | x86_64 | `34698130020` | SINGLE | `2026-12-11T14:02:53Z` |
| TrustAttestor UI Gradle dependency cache | agp8.7.2-kotlin2.0.21-ui-kotlincompile-v2 | Linux | x86_64 | `34698303924` | SINGLE | `2026-12-11T14:06:23Z` |
| Android SDK compile bundle | api35-bt35.0.0-clt12.0-pt37.0.1-v1 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| Temurin JDK | 17.0.20.1+1 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| Gradle | 8.10.2 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| TrustAttestor UI Gradle dependency cache | agp8.7.2-kotlin2.0.21-ui-deps-v1 | Linux | x86_64 | `34697680626` | SINGLE | `2026-12-11T13:53:27Z` |
| Android NDK | r28c | Linux | x86_64 | `31684150811` | SPLIT × 2 | `2026-11-11T08:54:22Z` |
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

## Android NDK r28c

- Workflow: `.github/workflows/download-ndk-r28c.yml`
- Run ID: `31684150811`
- Source: `https://dl.google.com/android/repository/android-ndk-r28c-linux.zip`
- Repository Visibility: `Public`
- Requested Retention: `400 days`
- Effective Retention: `90 days` (GitHub public-repository cap)
- Storage Mode: `SPLIT`
- Original File: `android-ndk-r28c-linux.zip`
- Original Size: `722261334` bytes
- Original SHA-1: `a7b54a5de87fecd125a17d54f73c446199e72a64`
- Original SHA256: `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f`
- Part Count: `2`
- Expires At: `2026-11-11T08:54:22Z`

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android NDK | r28c | Linux | x86_64 | `android-ndk-r28c-linux.zip` | `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f` |

### Artifacts

| Part | Artifact ID | Artifact Name | Raw Size | Raw SHA256 | Artifact Size | Artifact Digest | Created At | Expires At |
|---:|---:|---|---:|---|---:|---|---|---|
| 1/2 | `9174697344` | `ndk-r28c-part-00` | `398458880` | `6e87d3bb98c2bfcdb9a703affd174b85ef00fff69b9aa0056372f79046308fa1` | `398459026` | `sha256:07ce7d79e2c15bfa567e2c97e961b812eb879e96fcdfe13761889fff492adf97` | `2026-08-13T08:54:33Z` | `2026-11-11T08:54:22Z` |
| 2/2 | `9174699121` | `ndk-r28c-part-01` | `323802454` | `bf9baef30047e4a7e1040034619728cce0b291d76e4d67b44a0d5d0554c0197c` | `323802600` | `sha256:40693e9180b35cdbcb23ac27e1d274d783d93af3667ca126e4fd4b98febda894` | `2026-08-13T08:54:37Z` | `2026-11-11T08:54:22Z` |

### Restore

下载两个 Artifact，分别解压出 `ndk-r28c.part.00` 和 `ndk-r28c.part.01`，按顺序拼接为 `android-ndk-r28c-linux.zip`，最后校验完整文件 SHA256。

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
