from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_control_page import Ui_ControlPage
from ..widgets.utils import embed_widget
from ..widgets.wafer_visualizer import WaferVisualizer
from ..widgets.graph_visualizer import GraphVisualizer

class ControlPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ControlPage()
        self.ui.setupUi(self)

        self.wafer = WaferVisualizer(wafer_radius_mm=300.0, show_export_button=False)
        self.graph = GraphVisualizer(x_label="Time (s)", y_label="Intensity (mV)")
        embed_widget(self.ui.wafer_placeholder, self.wafer)
        embed_widget(self.ui.graph_placeholder, self.graph)