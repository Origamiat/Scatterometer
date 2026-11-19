from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_calibration_page import Ui_CalibrationPage 


class CalibrationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CalibrationPage()
        self.ui.setupUi(self)