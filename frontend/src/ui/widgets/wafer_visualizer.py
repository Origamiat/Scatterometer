from pathlib import Path
import numpy as np
import pyqtgraph as pg
from pyqtgraph.exporters import ImageExporter
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
)


class WaferVisualizer(QWidget):
    def __init__(self, wafer_radius_mm: float = 300.0, show_export_button: bool = True, parent=None):
        super().__init__(parent)

        self._plot = pg.PlotWidget()
        self._plot.setAspectLocked(True)
        self._plot.setLabel("bottom", "X (mm)")
        self._plot.setLabel("left", "Y (mm)")
        self._plot.showGrid(x=True, y=True, alpha=0.2)

        self._outline = self._plot.plot([], [], pen=pg.mkPen("#90a4ae", width=2))
        self._scatter = pg.ScatterPlotItem(pxMode=True, pen=None)
        self._plot.addItem(self._scatter)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._plot)

        if show_export_button:
            bar = QHBoxLayout()
            bar.setContentsMargins(0, 0, 0, 0)
            bar.addStretch()
            self._btn_export = QPushButton("Export PNG")
            self._btn_export.setFixedHeight(28)
            self._btn_export.clicked.connect(self._on_export_clicked)
            bar.addWidget(self._btn_export)
            layout.addLayout(bar)

        self.set_wafer_radius(wafer_radius_mm)

    def set_wafer_radius(self, radius_mm: float) -> None:
        theta = np.linspace(0, 2 * np.pi, 256)  # not really a circle, but good enough for visualization (dihectapentacontahexagon)
        self._outline.setData(radius_mm * np.cos(theta), radius_mm * np.sin(theta))
        self._plot.setXRange(-radius_mm, radius_mm)
        self._plot.setYRange(-radius_mm, radius_mm)

    def set_particles(
        self,
        x: np.ndarray,
        y: np.ndarray,
        sizes: np.ndarray | float = 7,
        colors: list | str = "#ff5252",
    ) -> None:
        brushes = [pg.mkBrush(c) for c in colors] if isinstance(colors, (list, tuple)) else pg.mkBrush(colors)
        self._scatter.setData(x=x, y=y, size=sizes, brush=brushes)

    def add_particles(
        self,
        x: np.ndarray,
        y: np.ndarray,
        sizes: np.ndarray | float = 7,
        colors: list | str = "#ff5252",
    ) -> None:
        brushes = [pg.mkBrush(c) for c in colors] if isinstance(colors, (list, tuple)) else pg.mkBrush(colors)
        self._scatter.addPoints(x=x, y=y, size=sizes, brush=brushes)

    def clear(self) -> None:
        self._scatter.clear()

    def export_png(self, filepath: str | Path, width: int = 1000) -> None:
        exporter = ImageExporter(self._plot.plotItem)
        exporter.parameters()["width"] = width
        exporter.export(str(filepath))

    def _on_export_clicked(self) -> None:
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            "Export Wafer Map as PNG",
            "wafer_map.png",
            "PNG Images (*.png)",
        )
        if not filepath: 
            return
        if not filepath.lower().endswith(".png"):
            filepath += ".png"
        self.export_png(filepath)