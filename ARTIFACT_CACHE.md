# Artifact Cache

GitHub Actions 可复用 Artifact 索引。下载资源前优先按 `Name + Version + Platform + Architecture` 查询；是否仍可用以 GitHub 实际返回的 `expires_at` 为准。

## Index

| Name | Version | Platform | Architecture | Run ID | Storage | Expires At |
|---|---|---|---|---:|---|---|
| Android NDK | r28c | Linux | x86_64 | `31684150811` | SPLIT × 2 | `2026-11-11T08:54:22Z` |
| USDA FoodData Central Foundation Foods CSV | 2026-04-30 | Any | Any | `31695314247` | SINGLE | `2026-11-11T11:23:52Z` |

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
