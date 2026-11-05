#!/usr/bin/env python3
"""Voice-generation adapter entry point.

Kokoro ONNX model and voice files are versioned separately from this skill.
Claude should inspect the installed kokoro-onnx API and the locally downloaded
model assets before wiring this adapter; do not guess model paths or signatures.
"""
import argparse
p = argparse.ArgumentParser(description="Generate narration WAV with local Kokoro ONNX.")
p.add_argument("script_json")
p.add_argument("--output", default="voice.wav")
p.parse_args()
raise SystemExit(
    "Voice adapter needs a local Kokoro ONNX model and voice file. "
    "Ask the skill to configure the installed kokoro-onnx version, then retry."
)
