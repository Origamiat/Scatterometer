from PySide6.QtWidgets import QMainWindow
from .ui_generated.ui_dashboard import Ui_MainWindow  
from .pages.home_page import HomePage
from .pages.control_page import ControlPage
from .pages.results_page import ResultsPage
from .pages.calibration_page import CalibrationPage
from .pages.settings_page import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._setup_pages()
        self._setup_navigation()

    def _setup_pages(self) -> None:
        self.home_page = HomePage()
        self.control_page = ControlPage()
        self.results_page = ResultsPage()
        self.calibration_page = CalibrationPage()
        self.settings_page = SettingsPage()

        for page in (
            self.home_page,
            self.control_page,
            self.results_page,
            self.calibration_page,
            self.settings_page,
        ):
            self.ui.Content.addWidget(page)

        self.ui.Content.setCurrentWidget(self.home_page)

    def _setup_navigation(self) -> None:
        nav_routes = [
            (self.ui.btn_nav_home, self.home_page),
            (self.ui.btn_nav_dashboard, self.home_page),
            (self.ui.btn_nav_control, self.control_page),
            (self.ui.btn_nav_results, self.results_page),
            (self.ui.btn_nav_calibration, self.calibration_page),
            (self.ui.btn_nav_settings, self.settings_page),
            (self.home_page.ui.btn_quick_start_scan, self.control_page),
            (self.home_page.ui.btn_open_selected_scan, self.results_page),
            (self.home_page.ui.btn_run_cal_check, self.calibration_page),
        ]
        for button, target_page in nav_routes:
            button.clicked.connect(
                lambda checked=False, page=target_page: self.ui.Content.setCurrentWidget(page)
            )

    def closeEvent(self, event) -> None:
        if self.controller is not None:
            self.controller.emergency_stop()
            self.controller.disconnect()
        super().closeEvent(event)