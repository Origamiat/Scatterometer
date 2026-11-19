from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_results_page import Ui_ResultsPage 

class ResultsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ResultsPage()
        self.ui.setupUi(self)