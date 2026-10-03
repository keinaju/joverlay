import sys
from PySide6.QtWidgets import QApplication, QTextEdit, QWidget
from PySide6.QtCore import Qt

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        # Transparent background
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        # Create a scrollable text area
        self.text_area = QTextEdit()
        self.text_area.setLineWrapMode(
            QTextEdit.LineWrapMode.WidgetWidth
        )

        self.text_area.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 200);
                border: none;
                color: white;
                font-family: 'Consolas';
                font-size: 20px;
            }

            QScrollBar:vertical {
                background: rgba(255, 255, 255, 30);
                width: 8px;
            }

            QScrollBar::handle:vertical {
                background: rgba(255, 255, 255, 150);
                min-height: 20px;
            }
        """)

        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_area)

        # Position and size
        self.setGeometry(2000, 200, 560, 400)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())