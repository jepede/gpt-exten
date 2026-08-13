# Artifact Cache

GitHub Actions 可复用 Artifact 索引。下载资源前优先按 `Name + Version + Platform + Architecture` 查询；是否仍可用以 GitHub 实际返回的 `expires_at` 为准。

## Index

| Name | Version | Platform | Architecture | Run ID | Storage | Expires At |
|---|---|---|---|---:|---|---|
| Android NDK | r28c | Linux | x86_64 | `31684150811` | SPLIT × 2 | `2026-11-11T08:54:22Z` |
| USDA FoodData Central Foundation Foods CSV | 2026-04-30 | Any | Any | `31695314247` | SINGLE | `2026-11-11T11:23:52Z` |
| USDA FoodData Central SR Legacy CSV | 2018-04 | Any | Any | `31695560856` | SINGLE | `2026-11-11T11:27:10Z` |
| CulinaryDB CSV bundle | 2018-03-15 | Any | Any | `31723890750` | SINGLE | `2026-11-11T17:04:36Z` |

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
