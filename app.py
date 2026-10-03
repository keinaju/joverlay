
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt

class Content:
    FILENAME = "content.txt"

    try:
        with open(FILENAME, "r") as file:
            TEXT = file.read()
            if not TEXT:
                TEXT = f"File '{FILENAME}' was found but is empty."
    except FileNotFoundError:
        TEXT = f"No text file '{FILENAME}' found."

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
            | Qt.WindowType.WindowDoesNotAcceptFocus
        )

        # Transparent background
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        # Overlay text
        self.label = QLabel(Content.TEXT)
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 160);
                font-size: 28px;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
            }
        """)

        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # Position and size
        self.setGeometry(100, 100, 400, 70)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())