#!/usr/bin/env bash
# 将指定目录下所有 SVG 卡片批量转换为 2x PNG（360x480 -> 720x960）
# 用法: svg2png.sh <卡片所在目录>
set -euo pipefail

DIR="${1:?用法: svg2png.sh <卡片所在目录>}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SCALE=2

for svg in "$DIR"/*.svg; do
  [ -e "$svg" ] || continue
  png="${svg%.svg}.png"
  "$CHROME" --headless --disable-gpu \
    --force-device-scale-factor="$SCALE" \
    --window-size=360,480 \
    --hide-scrollbars \
    --screenshot="$png" \
    "$svg" >/dev/null 2>&1
  echo "已生成: $(basename "$png")"
done
