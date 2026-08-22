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
