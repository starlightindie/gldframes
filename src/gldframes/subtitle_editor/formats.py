"""Subtitle file exporters."""

from __future__ import annotations

from gldframes.subtitle_editor.models import SubtitleCue


def to_srt(cues: list[SubtitleCue]) -> str:
    blocks = []
    for index, cue in enumerate(cues, start=1):
        blocks.append(f"{index}\n{_srt_time(cue.start)} --> {_srt_time(cue.end)}\n{cue.text}")
    return "\n\n".join(blocks) + "\n"


def to_vtt(cues: list[SubtitleCue]) -> str:
    body = []
    for cue in cues:
        body.append(f"{_vtt_time(cue.start)} --> {_vtt_time(cue.end)}\n{cue.text}")
    return "WEBVTT\n\n" + "\n\n".join(body) + "\n"


def _srt_time(seconds: float) -> str:
    millis = round(seconds * 1000)
    hours, remainder = divmod(millis, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, ms = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{ms:03}"


def _vtt_time(seconds: float) -> str:
    return _srt_time(seconds).replace(",", ".")
