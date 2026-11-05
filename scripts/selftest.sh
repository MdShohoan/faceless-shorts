#!/usr/bin/env bash
set -euo pipefail
fail=0

check() {
  if command -v "$1" >/dev/null 2>&1; then
    echo "PASS: $1"
  else
    echo "FAIL: $1 not found"
    fail=1
  fi
}

check node
check npm
check python3
check ffmpeg

if command -v node >/dev/null 2>&1; then
  node -e 'const major=+process.versions.node.split(".")[0]; if(major<22) process.exit(1)' \
    && echo "PASS: Node.js 22+" || { echo "FAIL: Node.js 22+ required"; fail=1; }
fi

if [ -x ".venv/bin/python" ]; then
  PY=".venv/bin/python"
elif [ -x ".venv/Scripts/python.exe" ]; then
  PY=".venv/Scripts/python.exe"
else
  PY="python3"
fi

"$PY" - <<'PY' || fail=1
import sys
if sys.version_info < (3, 10):
    raise SystemExit("FAIL: Python 3.10+ required")
for module in ("numpy", "scipy", "PIL", "faster_whisper", "kokoro_onnx"):
    try:
        __import__(module)
        print(f"PASS: {module}")
    except Exception as exc:
        print(f"FAIL: {module}: {exc}")
        raise SystemExit(1)
PY

if [ -d "node_modules/playwright" ]; then
  echo "PASS: Playwright package"
else
  echo "FAIL: Playwright package missing (run setup.sh)"
  fail=1
fi

if [ "$fail" -ne 0 ]; then
  echo "SELFTEST FAILED"
  exit 1
fi

echo "SELFTEST PASSED"
