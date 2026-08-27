# Artifact Cache

GitHub Actions 可复用 Artifact 索引。下载资源前优先按 `Name + Version + Platform + Architecture` 查询；是否仍可用以 GitHub 实际返回的 `expires_at` 为准。

## Index

| Name | Version | Platform | Architecture | Run ID | Storage | Expires At |
|---|---|---|---|---:|---|---|
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
| nlohmann/json single header | 3.12.0 | Any | Any | `32814216489` | SINGLE | `2026-11-23T05:47:17Z` |

| libUE4 GL | 4.5-v1.0.1 | Android | AArch64 | `33073762454` | SINGLE | `2026-11-25T12:50:04Z` |
| VaultPony VeraCrypt-compatible CLI | 0.1.0+fb4c460 | Android (API 24+) | AArch64 | `33089426736` | SINGLE | `2026-11-25T15:43:58Z` |

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
