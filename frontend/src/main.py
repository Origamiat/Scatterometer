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
    app = QApplication(sys.argv)
    loader = QUiLoader()

    window = loader.load("frontend\\ui\\dashboard.ui")
    page_home = loader.load("frontend\\ui\\pages\\page_home.ui")
    page_control = loader.load("frontend\\ui\\pages\\page_control.ui")
    page_results = loader.load("frontend\\ui\\pages\\page_results.ui")
    page_calibration = loader.load("frontend\\ui\\pages\\page_calibration.ui")
    page_settings = loader.load("frontend\\ui\\pages\\page_settings.ui")

    window.Content.addWidget(page_home)
    window.Content.addWidget(page_control)
    window.Content.addWidget(page_results)
    window.Content.addWidget(page_calibration)
    window.Content.addWidget(page_settings)

    window.Content.setCurrentWidget(page_home)

    window.btn_nav_home.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_home)
    )
    window.btn_nav_dashboard.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_home)
    )
    window.btn_nav_control.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_control)
    )
    window.btn_nav_results.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_results)
    )
    window.btn_nav_calibration.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_calibration)
    )
    window.btn_nav_settings.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_settings)
    )

    page_home.btn_quick_start_scan.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_control)
    )
    page_home.btn_open_selected_scan.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_results)
    )
    page_home.btn_run_cal_check.clicked.connect(
        lambda: window.Content.setCurrentWidget(page_calibration)
    )

    apply_stylesheet(app, theme="dark_blue.xml")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()