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
