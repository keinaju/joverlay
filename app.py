import ctypes
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

def enable_click_through(self):
    hwnd = int(self.winId())

    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x00080000
    WS_EX_TRANSPARENT = 0x00000020

    user32 = ctypes.windll.user32

    style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    user32.SetWindowLongW(
        hwnd,
        GWL_EXSTYLE,
        style | WS_EX_LAYERED | WS_EX_TRANSPARENT
    )

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
        self.label.setWordWrap(True)
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 128);
                font-family: 'Consolas';
                font-size: 20px;
                font-weight: bold;
            }
        """)

        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # Position and size
        self.setGeometry(2000, 200, 560, 100)

        self.show()
        enable_click_through(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())