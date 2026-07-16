"""Main Qt6 window skeleton."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow, QSplitter, QTableWidget, QTableWidgetItem, QTextEdit, QToolBar, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """Desktop shell for the subtitle creation workflow."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("GLDFrames Shorts Subtitle Studio")
        self.resize(1200, 800)
        self._build_toolbar()
        self._build_layout()

    def _build_toolbar(self) -> None:
        toolbar = QToolBar("Workflow")
        toolbar.addAction("Import Video")
        toolbar.addAction("Transcribe")
        toolbar.addAction("Manual Mode")
        toolbar.addAction("Export MP4")
        self.addToolBar(toolbar)

    def _build_layout(self) -> None:
        splitter = QSplitter(Qt.Orientation.Horizontal)
        preview = QLabel("Video preview\nSubtitles update in real time")
        preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        preview.setMinimumWidth(420)

        editor_panel = QWidget()
        layout = QVBoxLayout(editor_panel)
        table = QTableWidget(0, 3)
        table.setHorizontalHeaderLabels(["Start", "End", "Text"])
        manual_text = QTextEdit()
        manual_text.setPlaceholderText("Manual subtitle mode: type captions here, then use automatic timing assistance.")
        layout.addWidget(QLabel("Subtitle Editor"))
        layout.addWidget(table)
        layout.addWidget(QLabel("Manual Subtitle Draft"))
        layout.addWidget(manual_text)

        splitter.addWidget(preview)
        splitter.addWidget(editor_panel)
        self.setCentralWidget(splitter)

    def load_demo_cue(self) -> None:
        """Populate a simple cue for smoke testing UI wiring."""
        table = self.findChild(QTableWidget)
        if table is None:
            return
        table.insertRow(0)
        for column, value in enumerate(("0.00", "2.10", "Today we're going\nto build an app")):
            table.setItem(0, column, QTableWidgetItem(value))
