from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_calibration_page import Ui_CalibrationPage 
from ..widgets.utils import embed_widget
from ..widgets.graph_visualizer import GraphVisualizer


class CalibrationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CalibrationPage()
        self.ui.setupUi(self)

        self.graph = GraphVisualizer(x_label="Time (s)", y_label="Intensity (mV)")
        embed_widget(self.ui.graph_placeholder, self.graph)