#!/usr/bin/env bash
# Recover the official Delta Force CN Android APK from the four verified
# and SHA256-pinned GitHub Actions artifacts in jepede/gpt-exten.
# Run: bash scripts/restore-deltaforce-cn-apk.sh [destination-directory]
set -euo pipefail

REPO="jepede/gpt-exten"
RUN_ID="38596903200"
BASE="DeltaForce-CN-Android-v1.201.37117.67.apk"
EXPECTED_SHA256="af03179c62ac57f05e4e6d425b2471bdf651b46c2f5a636f5a9e3fa94c78337d"
EXPECTED_MD5="546f3d60b114ddd80e45a708d2d6e130"
TARGET_DIR="${1:-.}"
mkdir -p "$TARGET_DIR"
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"
TARGET="$TARGET_DIR/$BASE"

if ! command -v gh >/dev/null 2>&1; then
    echo "error: GitHub CLI (gh) is required; install gh and authenticate." >&2
    exit 1
fi

if [ -f "$TARGET" ] && printf '%s  %s\n' "$EXPECTED_SHA256" "$TARGET" | sha256sum -c - >/dev/null; then
    echo "CACHED: existing APK already verified: $TARGET"
    exit 0
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Using cached GitHub Actions run $RUN_ID (no Tencent CDN re-download)"
gh run download "$RUN_ID" -R "$REPO" -D "$TMP/artifacts"

EXPECTED_PART_SHA256=(
    ff89045d63daf2101f83357729c6fd501c2623d6db87fb3dd973c6e48fdb03be
    727fc9db85ce8e9df1d612d536b2c2919f05f94ae93f44141716d1f1a52655ef
    1be7e7ef8ca01bdd6677095fb6e5c20b297d0c2386a9269e58a9f3cc59773639
    ac3582fae315b8cc283df13dd1216df3f07245791f50cb90feecfc2ff74cb169
)
EXPECTED_PART_SIZE=(419430400 419430400 419430400 260924738)
PARTS=()
for i in 0 1 2 3; do
    printf -v suffix '%02d' "$i"
    filename="$BASE.part.$suffix"
    path="$(find "$TMP/artifacts" -type f -name "$filename" -print -quit)"
    if [ -z "$path" ]; then
        echo "error: missing cached part $filename" >&2
        exit 1
    fi
    if [ "$(stat -c '%s' "$path")" != "${EXPECTED_PART_SIZE[i]}" ]; then
        echo "error: invalid byte count for $filename" >&2
        exit 1
    fi
    printf '%s  %s\n' "${EXPECTED_PART_SHA256[i]}" "$path" | sha256sum -c -
    PARTS+=("$path")
done

PARTIAL="$TMP/$BASE"
cat "${PARTS[@]}" > "$PARTIAL"
printf '%s  %s\n' "$EXPECTED_SHA256" "$PARTIAL" | sha256sum -c -
printf '%s  %s\n' "$EXPECTED_MD5" "$PARTIAL" | md5sum -c -
mv -f -- "$PARTIAL" "$TARGET"

echo "RESTORE PASS: $TARGET"
echo "SHA256: $EXPECTED_SHA256"
echo "Size: $(stat -c '%s' "$TARGET") bytes"
