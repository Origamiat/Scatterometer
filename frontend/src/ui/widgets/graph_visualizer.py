from pathlib import Path
import numpy as np
import pyqtgraph as pg
from pyqtgraph.exporters import ImageExporter
from PySide6.QtWidgets import QWidget, QVBoxLayout


class GraphVisualizer(QWidget):
    def __init__(self, x_label: str = "Time / Position", y_label: str = "Intensity", parent=None):
        super().__init__(parent)

        self._plot = pg.PlotWidget()
        self._plot.setLabel("bottom", x_label)
        self._plot.setLabel("left", y_label)
        self._plot.showGrid(x=True, y=True, alpha=0.25)

        self._plot.setClipToView(True)
        self._plot.setDownsampling(auto=True, mode="peak")

        self._curve = self._plot.plot([], [], pen=pg.mkPen("#29b6f6", width=1.5))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._plot)

    def set_data(self, x: np.ndarray, y: np.ndarray) -> None:
        self._curve.setData(x, y)

    def clear(self) -> None:
        self._curve.setData([], [])

    def export_png(self, filepath: str | Path, width: int = 1200) -> None:
        exporter = ImageExporter(self._plot.plotItem)
        exporter.parameters()["width"] = width
        exporter.export(str(filepath))