from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_control_page import Ui_ControlPage

class ControlPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ControlPage()
        self.ui.setupUi(self)