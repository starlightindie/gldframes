# GLDFrames Shorts Subtitle Studio

A lightweight native Linux desktop application blueprint for generating, editing, previewing, and burning subtitles into vertical videos for YouTube Shorts, TikTok, and Reels.

The project is designed for Debian-based Linux distributions, runs fully offline, and keeps the default workflow suitable for lower-end laptops with 8GB RAM.

## Goals

- Import a video and extract speech locally.
- Transcribe with efficient offline Whisper models through `faster-whisper`.
- Generate natural, timed subtitle chunks for short-form vertical video.
- Edit subtitles manually with a live preview and timeline-oriented workflow.
- Export burned-in MP4 files plus SRT, ASS, and VTT subtitle files.
- Package as a `.deb` with a desktop launcher and application icon.

## Platform

Supported targets are Debian-based distributions including Debian, Ubuntu, Linux Mint, Pop!_OS, KDE Neon, Tuxedo OS, and similar derivatives. The Qt6 interface is intended to work under Wayland and X11.

## Performance profile

The application defaults to the `tiny` transcription model and conservative preview settings. Larger models are opt-in from Settings. Model loading is isolated to the transcription module so the UI and editor can run without keeping unnecessary AI assets resident in memory.

Target hardware:

- 8GB RAM
- Dual-core or quad-core CPU
- No dedicated GPU required

## Project layout

```text
src/gldframes/
  audio/             audio extraction helpers
  transcription/     offline speech recognition adapters
  subtitle_editor/   subtitle model and editing operations
  timeline/          timeline data structures
  video/             video metadata and preview helpers
  export/            FFmpeg export pipeline
  styles/            built-in subtitle styles and animations
  settings/          app settings models
  ui/                Qt6 windows and widgets
packaging/debian/    Debian packaging metadata
assets/              desktop icon and launcher resources
```

## Quick start for development

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .
gldframes
```

Runtime tools expected on the host:

- FFmpeg / FFprobe
- Python 3.13+
- PySide6
- faster-whisper

## Packaging

Debian packaging metadata is included under `packaging/debian`. A package build can be wired to CI or run locally with standard Debian packaging tools once runtime dependencies are available.
