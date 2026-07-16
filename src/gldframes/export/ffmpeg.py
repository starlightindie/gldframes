"""FFmpeg-based export pipeline."""

from __future__ import annotations

import subprocess
from pathlib import Path

from gldframes.settings.models import VideoSettings


def burn_subtitles(input_video: Path, ass_file: Path, output_mp4: Path, settings: VideoSettings) -> None:
    """Burn an ASS subtitle file into an MP4 using FFmpeg."""
    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_video),
        "-vf",
        f"ass={ass_file}",
        "-c:v",
        settings.codec,
        "-b:v",
        settings.video_bitrate,
        "-r",
        str(settings.fps),
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        str(output_mp4),
    ]
    subprocess.run(command, check=True)
