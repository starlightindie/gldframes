"""Settings models for performance-conscious local processing."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TranscriptionSettings:
    """Offline speech recognition settings."""

    model_size: str = "tiny"
    language: str | None = None
    cpu_threads: int = 2
    compute_type: str = "int8"


@dataclass(slots=True)
class SubtitleSettings:
    """Subtitle chunking and presentation defaults."""

    max_words: int = 7
    max_characters_per_line: int = 40
    max_lines: int = 2
    style_name: str = "YouTube Shorts"


@dataclass(slots=True)
class VideoSettings:
    """Export settings for Shorts-ready MP4 files."""

    output_width: int = 1080
    output_height: int = 1920
    fps: int = 30
    video_bitrate: str = "8M"
    codec: str = "libx264"


@dataclass(slots=True)
class PerformanceSettings:
    """Knobs for low-memory operation."""

    preview_scale: float = 0.5
    cache_size_mb: int = 256
    keep_model_loaded: bool = False
