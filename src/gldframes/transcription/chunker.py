"""Create readable short-form subtitle chunks from recognized words."""

from __future__ import annotations

from dataclasses import dataclass

from gldframes.subtitle_editor.models import SubtitleCue


@dataclass(slots=True)
class WordTiming:
    word: str
    start: float
    end: float


def chunk_words(
    words: list[WordTiming],
    max_words: int = 7,
    max_characters_per_line: int = 40,
    max_lines: int = 2,
    pause_threshold: float = 0.55,
) -> list[SubtitleCue]:
    """Split word timings into natural two-line subtitle cues."""
    if not words:
        return []

    cues: list[SubtitleCue] = []
    current: list[WordTiming] = []

    def flush() -> None:
        if not current:
            return
        lines = _wrap_words([item.word for item in current], max_characters_per_line, max_lines)
        cues.append(SubtitleCue(current[0].start, current[-1].end, "\n".join(lines)))
        current.clear()

    for word in words:
        if current:
            pause = word.start - current[-1].end
            projected = current + [word]
            projected_text = " ".join(item.word for item in projected)
            if pause >= pause_threshold or len(projected) > max_words or len(projected_text) > max_characters_per_line * max_lines:
                flush()
        current.append(word)
    flush()
    return cues


def _wrap_words(words: list[str], max_chars: int, max_lines: int) -> list[str]:
    lines: list[str] = []
    line: list[str] = []
    for word in words:
        candidate = " ".join([*line, word]).strip()
        if line and len(candidate) > max_chars and len(lines) < max_lines - 1:
            lines.append(" ".join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        lines.append(" ".join(line))
    if len(lines) > max_lines:
        lines = lines[:max_lines - 1] + [" ".join(lines[max_lines - 1:])]
    return lines
