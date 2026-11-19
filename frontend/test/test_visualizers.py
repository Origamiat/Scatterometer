import sys
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QFrame, QPushButton, QTableWidget, QTableWidgetItem
)
from qt_material import apply_stylesheet

from frontend.src.ui.widgets.graph_visualizer import GraphVisualizer
from frontend.src.ui.widgets.wafer_visualizer import WaferVisualizer


class VisualizerTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizer Test")
        self.resize(1200, 650)

        root = QWidget()
        self.setCentralWidget(root)
        main_layout = QHBoxLayout(root)

        # --- Left side: QFrame holding GraphVisualizer ---
        left_col = QVBoxLayout()
        graph_frame = QFrame()
        graph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph = GraphVisualizer(x_label="Sample", y_label="Intensity (mV)")
        self._embed(graph_frame, self.graph)


        btn_export = QPushButton("Export Both to PNG")
        btn_export.clicked.connect(self._export_both)

        left_col.addWidget(graph_frame, stretch=1)
        left_col.addWidget(btn_export)

        # --- Right side: QFrame holding WaferVisualizer + real QTableWidget ---
        right_col = QVBoxLayout()
        wafer_frame = QFrame()
        wafer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.wafer = WaferVisualizer(wafer_radius_mm=50.0)
        self._embed(wafer_frame, self.wafer)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["X (mm)", "Y (mm)", "Intensity (mV)", "Confidence"])
        self._populate_sample_table()
        self._sync_table_to_wafer()
        # Editing any cell in the table immediately updates the wafer map
        self.table.itemChanged.connect(lambda *_: self._sync_table_to_wafer())

        right_col.addWidget(wafer_frame, stretch=2)
        right_col.addWidget(self.table, stretch=1)

        main_layout.addLayout(left_col, stretch=3)
        main_layout.addLayout(right_col, stretch=2)

        # --- Rolling buffer & 30 FPS timer for live random graph data ---
        self._buf_len = 5000
        self._x = np.arange(self._buf_len, dtype=np.float32)
        self._y = np.random.normal(0.0, 0.4, self._buf_len).astype(np.float32)
        self._sample_cursor = self._buf_len

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_live_graph)
        self._timer.start(33)  # ~30 FPS

    @staticmethod
    def _embed(frame: QFrame, widget: QWidget) -> None:
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(widget)

    def _update_live_graph(self) -> None:
        chunk = 100
        new_y = np.random.normal(0.0, 0.4, chunk).astype(np.float32)

        # Inject a random particle spike ~25% of frames
        if np.random.rand() < 0.25:
            pos = np.random.randint(10, chunk - 10)
            t = np.arange(-8, 9)
            spike_height = np.random.uniform(6.0, 45.0)
            new_y[pos - 8 : pos + 9] += spike_height * np.exp(-0.5 * (t / 2.2) ** 2)

        # Shift rolling window left and append new chunk
        self._y[:-chunk] = self._y[chunk:]
        self._y[-chunk:] = new_y
        self._x += chunk
        self.graph.set_data(self._x, self._y)

    def _populate_sample_table(self) -> None:
        # Realistic particle detections: (x_mm, y_mm, intensity_mV, confidence)
        sample_rows = [
            (-18.5,  12.2,  8.4, 0.86),
            (  5.1, -24.7, 32.0, 0.99),
            ( 31.4,   8.0, 14.2, 0.93),
            (-35.0, -15.3, 44.8, 0.99),
            (  0.4,   2.1,  6.5, 0.78),
            ( 19.8,  29.6, 21.5, 0.96),
        ]
        self.table.setRowCount(len(sample_rows))
        for r, row in enumerate(sample_rows):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(f"{val}"))

    def _sync_table_to_wafer(self) -> None:
        xs, ys, sizes, colors = [], [], [], []
        for r in range(self.table.rowCount()):
            try:
                x = float(self.table.item(r, 0).text())
                y = float(self.table.item(r, 1).text())
                intensity = float(self.table.item(r, 2).text())
            except (AttributeError, ValueError):
                continue

            xs.append(x)
            ys.append(y)
            sizes.append(float(np.clip(6 + intensity * 0.25, 6, 18)))
            colors.append("#ff5252" if intensity >= 20.0 else "#ffb74d")

        self.wafer.set_particles(
            np.array(xs), np.array(ys), sizes=np.array(sizes), colors=colors
        )

    def _export_both(self) -> None:
        self.graph.export_png("test_graph.png")
        self.wafer.export_png("test_wafer.png")
        print("Saved test_graph.png and test_wafer.png")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")
    pg.setConfigOptions(antialias=True, background="#232629", foreground="#e0e0e0")

    win = VisualizerTestWindow()
    win.show()
    sys.exit(app.exec())