---
name: faceless-shorts
description: Create narrated vertical short-form videos from scripts using local voice, word-level captions, code-drawn scenes, procedural audio, and MP4 rendering. Use when asked to make YouTube Shorts, TikToks, or Reels in one of the included visual styles.
---

# Faceless Shorts

Create original, narrated 9:16 short-form videos locally. Prefer deterministic code-generated visuals over AI video services. Do not require paid APIs, API keys, or hosted generation credits.

## Supported styles

Read the selected style's `STYLE.md` before creating a project:

- `deep-dive-3d` — colorful educational 3D-inspired explainer scenes.
- `night-file-3d` — atmospheric, fictionalized mystery / historical-case scenes.
- `inside-out` — clean flat 2D cutaway and x-ray-style explainers.
- `stick-story` — simple stick-figure survival and preparedness stories.
- `paper-atlas` — cut-paper history, maps, timelines, and architecture.
- `tall-tale-3d` — light, funny true stories with flat cartoon characters in stylized 3D environments.

Do not imitate a living creator's exact signature style. Translate references into broad visual traits (camera movement, color, pacing, depth, typography) and create original compositions. Do not use copyrighted characters, logos, music, or footage.

## Workflow

1. **Clarify the brief only when essential.** If the user gives a topic and style, proceed. Otherwise ask one concise question for the missing topic or style. Default target duration: 35–55 seconds; aspect ratio: 9:16; language: user's language.
2. **Research and fact-check.** Separate established facts from uncertainty. For real people, crimes, disasters, health, or history, use careful sourcing and avoid sensationalized claims. Never invent quotes or present speculation as fact. Avoid graphic descriptions.
3. **Write the narration.** Aim for 90–130 spoken words for a 45–55 second short. Start with a clear hook, build one idea per beat, and finish with a concise payoff. Keep sentences easy to narrate.
4. **Create `script.json`.** Use this schema:
   ```json
   {
     "title": "Short title",
     "style": "deep-dive-3d",
     "language": "en",
     "duration_target_seconds": 45,
     "voice": {"id": "af_heart", "speed": 1.0},
     "scenes": [
       {
         "id": "scene-01",
         "narration": "A complete spoken sentence.",
         "visual": "Original visual description for this beat.",
         "camera": "slow_push_in",
         "sfx": ["soft_whoosh"],
         "music_mood": "curious"
       }
     ]
   }
   ```
   Each scene should map to one narration beat. Use 5–9 scenes for a typical short. Never put visual instructions into the spoken narration.
5. **Generate local audio.** Use Kokoro ONNX locally when installed. If model files are missing, run `scripts/setup.sh` and explain the first-run model download and disk requirement before downloading. Do not use cloud TTS or request an API key. Save narration as WAV.
6. **Align words.** Run local faster-whisper to obtain word-level timestamps. Normalize the transcript against the approved script; flag substantial mismatches rather than silently rewriting the narration. Save `words.json`.
7. **Build scenes in code.** Use HTML/CSS/SVG/Canvas or Python drawing. Design at 1080×1920 (or render smaller for preview), 30 fps. Every visual element must be generated from code or user-provided assets. Keep captions within safe margins and readable on a phone.
8. **Synchronize captions.** Captions must follow word timestamps. Highlight the current word or phrase, use short readable chunks, and avoid covering important visual content. Include punctuation in the displayed text.
9. **Sound design.** Generate original procedural sound effects and a subtle music bed in code. Keep narration clearly audible. Avoid copyrighted songs or unlicensed samples. Make all audio optional and provide a silent render path.
10. **Render.** Use headless Chrome/Playwright to capture frames or a deterministic browser render, then FFmpeg to encode H.264 MP4 with AAC audio. Keep intermediate files in the project folder.
11. **Quality check.** Generate a contact sheet at regular intervals and inspect the entire sequence. Check spelling, safe margins, timing, visual continuity, audio clipping, factual accuracy, and the final frame. Fix issues and render again.
12. **Deliver.** Provide the MP4 path, project path, duration, resolution, and any known limitations. Never claim a video is complete unless the MP4 exists and has been checked.

## Project layout

Create each project under `output/<slug>/`:

- `script.json`
- `voice.wav`
- `words.json`
- `src/` — scene and animation source
- `frames/` — rendered frames
- `audio/` — narration, music, and effects
- `contact-sheet.jpg`
- `final.mp4`
- `NOTES.md` — sources, assumptions, render settings, and remaining issues

Use `scripts/new_video.py` to create a starter project. Use `scripts/estimate.py` to estimate narration duration.

## Local-first constraints

- No paid API, cloud generation service, or API key.
- Do not upload source files or audio unless the user explicitly asks.
- Do not silently install system-wide software. Explain what is missing and request permission when installation requires administrator privileges.
- Prefer existing Chrome/Chromium and FFmpeg installations.
- Keep model downloads limited to the selected local TTS and transcription models.
- Never put credentials or tokens in `script.json`, source files, or logs.

## YouTube publishing

Publishing is a separate, opt-in action. Do not upload automatically. If the user asks to publish, confirm the exact title, description, visibility, audience setting, and category before any upload. Use only an explicitly configured and authorized integration. If no integration is available, provide the finished MP4 and manual upload steps. Never claim an upload succeeded without confirmation from the publishing tool.

## Safety and editorial rules

- No graphic injury details or glorification of dangerous acts.
- For survival/preparedness topics, give conservative, non-hazardous advice and recommend trusted local authorities for emergencies.
- For health topics, avoid diagnosing or making guaranteed medical claims; use reputable sources and encourage professional advice for personal concerns.
- For true-crime and mystery topics, distinguish verified evidence from theories, avoid accusing uninvolved people, and respect victims and families.
- Use only original scripts, artwork, sound, and music or assets the user has rights to use.
