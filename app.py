import sys
from PySide6.QtWidgets import QApplication, QTextEdit, QWidget
from PySide6.QtCore import Qt
from configuration import Configuration
from instructions import instructions
from styles import get_styles

class DraggableTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self._drag_offset = None

    def mousePressEvent(self, event):
        if (event.button() == Qt.MouseButton.LeftButton
                and event.modifiers() & Qt.KeyboardModifier.AltModifier):
            self._drag_offset = event.globalPosition().toPoint() - self.window().pos()
            event.accept()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._drag_offset is not None:
            self.window().move(event.globalPosition().toPoint() - self._drag_offset)
            event.accept()
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if (event.button() == Qt.MouseButton.LeftButton
                and self._drag_offset is not None):
            self._drag_offset = None
            event.accept()
            return
        super().mouseReleaseEvent(event)

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
        self.text_area = DraggableTextEdit()

        self.text_area.setLineWrapMode(
            QTextEdit.LineWrapMode.WidgetWidth
        )

        self.text_area.setPlainText(instructions)

        self.text_area.setStyleSheet(get_styles())

        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_area)

        # Position and size
        self.setGeometry(
            Configuration.get("x", 50),
            Configuration.get("y", 50),
            Configuration.get("width", 400),
            Configuration.get("height", 400)
        )

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())