"""Subtitle data model and editing helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SubtitleCue:
    """A single editable subtitle cue."""

    start: float
    end: float
    text: str

    def shifted(self, seconds: float) -> "SubtitleCue":
        """Return a cue shifted by a number of seconds."""
        return SubtitleCue(max(0.0, self.start + seconds), max(0.0, self.end + seconds), self.text)


class SubtitleDocument:
    """In-memory subtitle document with common editor operations."""

    def __init__(self, cues: list[SubtitleCue] | None = None) -> None:
        self.cues: list[SubtitleCue] = cues or []

    def add(self, cue: SubtitleCue) -> None:
        self.cues.append(cue)
        self.cues.sort(key=lambda item: item.start)

    def delete(self, index: int) -> None:
        del self.cues[index]

    def shift_all(self, seconds: float) -> None:
        self.cues = [cue.shifted(seconds) for cue in self.cues]

    def merge(self, first_index: int, second_index: int) -> None:
        first = self.cues[first_index]
        second = self.cues[second_index]
        self.cues[first_index] = SubtitleCue(first.start, second.end, f"{first.text} {second.text}".strip())
        del self.cues[second_index]

    def split(self, index: int, split_time: float, first_text: str, second_text: str) -> None:
        cue = self.cues[index]
        if not cue.start < split_time < cue.end:
            raise ValueError("split_time must be inside the cue duration")
        self.cues[index:index + 1] = [
            SubtitleCue(cue.start, split_time, first_text),
            SubtitleCue(split_time, cue.end, second_text),
        ]
