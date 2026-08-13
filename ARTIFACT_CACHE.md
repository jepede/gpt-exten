# ARTIFACT_CACHE.md

## Android NDK r28c

- Name: Android NDK
- Version: r28c
- Platform: Linux
- Architecture: x86_64
- Workflow: `.github/workflows/download-ndk-r28c.yml`
- Run ID: `31481618204`
- Source: `https://dl.google.com/android/repository/android-ndk-r28c-linux.zip`
- Storage Mode: `SPLIT`
- Original File: `android-ndk-r28c-linux.zip`
- Original Size: `722261334` bytes
- Original SHA-1: `a7b54a5de87fecd125a17d54f73c446199e72a64`
- Original SHA256: `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f`
- Part Count: `2`
- Status: `AVAILABLE`
- Expires At: `2026-08-13T13:41:47Z` (earliest part expiry)

### Contents

| Name | Version | Platform | Architecture | File/Path | SHA256 |
|---|---|---|---|---|---|
| Android NDK | r28c | Linux | x86_64 | `android-ndk-r28c-linux.zip` | `dfb20d396df28ca02a8c708314b814a4d961dc9074f9a161932746f815aa552f` |

### Parts

| Part | Artifact ID | Artifact Name | Raw Size | Artifact Size | Artifact SHA256 Digest | Created At | Expires At | Status |
|---:|---:|---|---:|---:|---|---|---|---|
| 1/2 | `9143794514` | `ndk-r28c-part-00` | `398458880` | `398459026` | `ca2af1ac8367889d37e5e18f3400ecabf85559a9e15323f99df4621cadebcc52` | `2026-08-12T13:41:51Z` | `2026-08-13T13:41:47Z` | `AVAILABLE` |
| 2/2 | `9143797044` | `ndk-r28c-part-01` | `323802454` | `323802600` | `0ebecfa2c452d37bbe6f756a7dec7dd1b7419fb66c8534887f4d35502942661e` | `2026-08-12T13:41:56Z` | `2026-08-13T13:41:52Z` | `AVAILABLE` |

### Restore

Download both Artifacts, extract `ndk-r28c.part.00` and `ndk-r28c.part.01`, then concatenate them in order to restore `android-ndk-r28c-linux.zip`. Verify the final SHA256 against the value above.
