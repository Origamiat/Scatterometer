import sys
import pyqtgraph as pg
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
from frontend.src.ui.main_window import MainWindow

def main() -> None:
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")
    pg.setConfigOptions(antialias=True, background="#232629", foreground="#e0e0e0")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()