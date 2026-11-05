#!/usr/bin/env python3
"""Create a new Faceless Shorts project scaffold."""
import argparse, json, re
from pathlib import Path

STYLES = {"deep-dive-3d", "night-file-3d", "inside-out", "stick-story", "paper-atlas", "tall-tale-3d"}

def slugify(value):
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or "new-short"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--style", choices=sorted(STYLES), default="deep-dive-3d")
    parser.add_argument("--out", default="output")
    args = parser.parse_args()

    project = Path(args.out) / slugify(args.title)
    for folder in ("src", "frames", "audio"):
        (project / folder).mkdir(parents=True, exist_ok=True)

    data = {
        "title": args.title,
        "style": args.style,
        "language": "en",
        "duration_target_seconds": 45,
        "voice": {"id": "af_heart", "speed": 1.0},
        "scenes": [
            {
                "id": "scene-01",
                "narration": "Replace this sentence with the opening hook.",
                "visual": "Describe an original, code-generated opening shot.",
                "camera": "slow_push_in",
                "sfx": ["soft_whoosh"],
                "music_mood": "curious"
            }
        ]
    }
    (project / "script.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    (project / "NOTES.md").write_text(
        f"# {args.title}\\n\\nStyle: `{args.style}`\\n\\n"
        "Add sources, factual notes, render settings, and known limitations here.\\n",
        encoding="utf-8"
    )
    print(f"Created project: {project.resolve()}")
    print("Next: edit script.json, then follow the workflow in SKILL.md.")

if __name__ == "__main__":
    main()
