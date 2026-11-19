from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_settings_page import Ui_SettingsPage 

class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsPage()
        self.ui.setupUi(self)