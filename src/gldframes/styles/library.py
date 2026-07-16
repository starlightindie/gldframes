"""Built-in subtitle styles for vertical social video."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SubtitleStyle:
    name: str
    font: str
    size: int
    bold: bool
    italic: bool
    text_color: str
    outline_color: str
    outline_width: int
    shadow: bool
    background_box: bool
    position: str
    animation: str


BUILT_IN_STYLES: tuple[SubtitleStyle, ...] = (
    SubtitleStyle("YouTube Shorts", "Inter", 64, True, False, "#FFFFFF", "#000000", 4, True, False, "bottom", "pop"),
    SubtitleStyle("TikTok", "Inter", 62, True, False, "#FFFFFF", "#111111", 5, True, False, "bottom", "bounce"),
    SubtitleStyle("Instagram Reels", "Inter", 58, True, False, "#FFFFFF", "#000000", 3, True, True, "bottom", "fade"),
    SubtitleStyle("Minimal", "Noto Sans", 48, False, False, "#FFFFFF", "#000000", 1, False, False, "bottom", "none"),
    SubtitleStyle("Cinematic", "Noto Serif", 44, False, True, "#F5F0E6", "#000000", 2, True, False, "lower-third", "fade"),
)
