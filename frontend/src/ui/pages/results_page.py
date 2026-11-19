from PySide6.QtWidgets import QWidget
from ..ui_generated.ui_results_page import Ui_ResultsPage 
from ..widgets.utils import embed_widget
from ..widgets.graph_visualizer import GraphVisualizer
from ..widgets.wafer_visualizer import WaferVisualizer

class ResultsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ResultsPage()
        self.ui.setupUi(self)

        self.wafer = WaferVisualizer(wafer_radius_mm=300.0, show_export_button=True)
        self.graph = GraphVisualizer(x_label="Time (s)", y_label="Intensity (mV)")
        embed_widget(self.ui.wafer_placeholder, self.wafer)
        # embed_widget(self.ui.graph_placeholder, self.graph)