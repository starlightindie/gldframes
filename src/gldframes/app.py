"""Application entry point."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from gldframes.ui.main_window import MainWindow


def main() -> int:
    """Start the Qt application."""
    app = QApplication(sys.argv)
    app.setApplicationName("GLDFrames")
    app.setOrganizationName("GLDFrames")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
