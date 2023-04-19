from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = QFont('Arial Black', 12, QFont.Bold)
        self.setFont(font)
        self.setMinimumSize(50, 50)
        self.setProperty('cssClass', 'specialButton')
