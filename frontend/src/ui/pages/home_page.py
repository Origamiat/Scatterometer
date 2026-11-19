from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_home_page import Ui_HomePage 
from ..widgets.utils import embed_widget
from ..widgets.wafer_visualizer import WaferVisualizer

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)

        self.wafer = WaferVisualizer(wafer_radius_mm=300.0, show_export_button=False)
        embed_widget(self.ui.wafer_placeholder, self.wafer)