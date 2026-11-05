#!/usr/bin/env bash
set -euo pipefail

echo "Checking local prerequisites..."
missing=0
for cmd in node npm python3 ffmpeg; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "  %-10s %s\n" "$cmd" "$(command -v "$cmd")"
  else
    printf "  %-10s MISSING\n" "$cmd"
    missing=1
  fi
done

if command -v node >/dev/null 2>&1; then
  node_major="$(node -p 'Number(process.versions.node.split(".")[0])')"
  if [ "$node_major" -lt 22 ]; then
    echo "Node.js 22+ is required (found $(node --version))."
    missing=1
  fi
fi

if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY'
import sys
print("  Python    ", sys.version.split()[0])
if sys.version_info < (3, 10):
    raise SystemExit("Python 3.10+ is required.")
PY
fi

if [ "$missing" -ne 0 ]; then
  echo "Install the missing prerequisites, then run this script again."
  exit 1
fi

python3 -m venv .venv
if [ -f ".venv/Scripts/activate" ]; then
  # Git Bash on Windows
  source .venv/Scripts/activate
else
  source .venv/bin/activate
fi

python -m pip install --upgrade pip
python -m pip install numpy scipy pillow soundfile faster-whisper kokoro-onnx

if [ ! -d "node_modules" ]; then
  npm init -y >/dev/null
fi
npm install --save-dev playwright
npx playwright install chromium

echo
echo "All set. Local model files are downloaded on first voice/transcription use."
echo "Run: bash scripts/selftest.sh"
