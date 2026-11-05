#!/usr/bin/env python3
"""Estimate spoken duration from a script or plain text."""
import argparse, json, re
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="Text file or script.json")
    p.add_argument("--wpm", type=int, default=145)
    a = p.parse_args()
    path = Path(a.input)
    raw = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(raw)
        text = " ".join(s.get("narration", "") for s in data.get("scenes", []))
    else:
        text = raw
    words = re.findall(r"\b[\w’'-]+\b", text)
    seconds = len(words) / max(a.wpm, 1) * 60
    print(f"Words: {len(words)}")
    print(f"Estimated narration: {seconds:.1f}s at {a.wpm} words/minute")
    print(f"Approximate range: {seconds*0.9:.1f}–{seconds*1.15:.1f}s")

if __name__ == "__main__":
    main()
