
import sys
import time
import queue
import numpy as np
import serial
import serial.tools.list_ports
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLabel
)
from PySide6.QtCore import QThread, QTimer, Signal, Slot
from PySide6.QtUiTools import QUiLoader
import pyqtgraph as pg
from qt_material import apply_stylesheet


def main():
    # 1. Create the application
    app = QApplication(sys.argv)
    loader = QUiLoader()
    window = loader.load("frontend\\ui\\dashboard.ui")
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()