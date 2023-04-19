from theme import setupTheme
from main__ import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    setupTheme()

    window = MainWindow()

    icon = QIcon('pokemmo/files/pokebola.png')

    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec_()
