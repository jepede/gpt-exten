#!/usr/bin/env bash
set -euo pipefail
cd target
OUT=../evidence/vanilla-audit.md
mkdir -p ../evidence

{
  echo '# Vanilla full-source static audit'
  echo
  echo "Repository: reddxae/Vanilla"
  echo "Branch: vanilla"
  echo "Commit: $(git rev-parse HEAD)"
  echo "Last commit: $(git log -1 --date=iso-strict --format='%H | %ad | %an | %s')"

  echo
  echo '## Build / secret inputs'
  grep -RInE --include='*.yml' --include='*.yaml' --include='*.gradle' --include='*.properties' \
    'secrets\.|TELEGRAM_|HELPER_|SENTRY|FIREBASE|google-services|MAPS_API|REMOTE|BOT_TOKEN' \
    .github TMessagesProj build.gradle settings.gradle 2>/dev/null | head -n 400 || true

  echo
  echo '## Nekogram private-backend indicators'
  for p in nekonotificationbot HELPER_BOT BaseRemoteHelper CloudStorageHelper check_for_updates get_config CHANNEL_METADATA_ID RemoteConfig SENTRY_DSN FirebaseAnalytics FirebaseCrashlytics Crashlytics; do
    echo
    echo "### $p"
    git grep -n -i -e "$p" -- ':!TMessagesProj/jni/voip/webrtc/**' ':!README*' 2>/dev/null | head -n 120 || true
  done

  echo
  echo '## Bot-like usernames'
  grep -RhoE --include='*.java' --include='*.kt' --include='*.xml' --include='*.gradle' \
    '["@][A-Za-z0-9_]{4,}[Bb]ot\b' TMessagesProj 2>/dev/null | sed -E 's/^["@]//' | sort -fu || true

  echo
  echo '## Hard-coded HTTP(S) URLs (first 500 unique)'
  grep -RhoE --include='*.java' --include='*.kt' --include='*.xml' --include='*.gradle' --include='*.properties' \
    'https?://[^"[:space:]<>]+' TMessagesProj 2>/dev/null | \
    grep -v '/jni/voip/webrtc/' | sed -E 's/[),;]+$//' | sort -u | head -n 500 || true

  echo
  echo '## Download / upload acceleration'
  git grep -n -i -E \
    'download.{0,30}(speed|boost|parallel|thread|concurrent)|(?:speed|boost|parallel|thread|concurrent).{0,30}download|upload.{0,30}(speed|boost|parallel|thread|concurrent)|(?:speed|boost|parallel|thread|concurrent).{0,30}upload|maxConcurrent|currentMaxDownload|downloadQueue|ConnectionTypeDownload|FileLoadOperation' \
    -- TMessagesProj 2>/dev/null | head -n 800 || true

  echo
  echo '## Sponsored messages / ad-removal'
  git grep -n -i -E \
    'sponsor(ed)?|SponsoredMessage|getSponsored|TL_messages_getSponsored|hide.{0,20}ad(s)?|disable.{0,20}ad(s)?|remove.{0,20}ad(s)?|adblock' \
    -- TMessagesProj 2>/dev/null | head -n 800 || true

  echo
  echo '## Privacy / local enhancement'
  git grep -n -i -E \
    'dont.?send.?typing|send.?typing|anti.?recall|deleted.?message|edit.?history|no.?forwards|restrict.?saving|FLAG_SECURE|screenshot|read.?receipt|ghost.?mode|hide.?phone|hide.?premium|hide.?gift|hide.?star|translator|opencc|chat.?swipe|monet' \
    -- TMessagesProj 2>/dev/null | head -n 1200 || true

  echo
  echo '## Dynamic code loading / shell execution'
  git grep -n -i -E \
    'DexClassLoader|PathClassLoader|System\.load\(|System\.loadLibrary|Runtime\.getRuntime\(\)\.exec|ProcessBuilder|su -c|download.*dex|loadDex|Class\.forName' \
    -- TMessagesProj 2>/dev/null | head -n 600 || true

  echo
  echo '## Google / Firebase dependencies'
  grep -RInE --include='*.gradle' --include='*.toml' --include='*.properties' \
    'firebase|google-services|play-services|crashlytics|analytics' . 2>/dev/null | head -n 700 || true

  echo
  echo '## Feature resource names'
  grep -RInE --include='*.xml' \
    'name="[^"]*(Download|Upload|Speed|Boost|Sponsor|Ad|Typing|Deleted|History|Screenshot|Forward|Premium|Gift|Star|Monet|Proxy|Translate|OpenCC)[^"]*"' \
    TMessagesProj 2>/dev/null | head -n 1200 || true
} > "$OUT"

cat "$OUT"
