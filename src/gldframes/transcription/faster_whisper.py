"""Offline faster-whisper transcription adapter."""

from __future__ import annotations

from gldframes.settings.models import TranscriptionSettings
from gldframes.transcription.chunker import WordTiming, chunk_words


class FasterWhisperTranscriber:
    """Lazy-loading transcriber that keeps AI memory use optional."""

    def __init__(self, settings: TranscriptionSettings) -> None:
        self.settings = settings
        self._model = None

    def unload(self) -> None:
        """Release the loaded model so lower-end systems can reclaim memory."""
        self._model = None

    def transcribe(self, media_path: str):
        """Transcribe media and return editable subtitle cues."""
        if self._model is None:
            from faster_whisper import WhisperModel

            self._model = WhisperModel(
                self.settings.model_size,
                device="cpu",
                compute_type=self.settings.compute_type,
                cpu_threads=self.settings.cpu_threads,
            )
        segments, _info = self._model.transcribe(media_path, language=self.settings.language, word_timestamps=True)
        words: list[WordTiming] = []
        for segment in segments:
            for word in segment.words or []:
                words.append(WordTiming(word.word.strip(), word.start, word.end))
        cues = chunk_words(words)
        if not getattr(self.settings, "keep_model_loaded", False):
            self.unload()
        return cues
