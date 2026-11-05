#!/usr/bin/env python3
"""Word-alignment adapter entry point for local faster-whisper."""
import argparse
p = argparse.ArgumentParser(description="Create word-level timestamps with faster-whisper.")
p.add_argument("audio")
p.add_argument("--output", default="words.json")
p.parse_args()
raise SystemExit(
    "Word-alignment adapter needs the local Whisper model configuration. "
    "Ask the skill to configure faster-whisper for this machine, then retry."
)
