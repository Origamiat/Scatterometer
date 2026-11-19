# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(920, 700)
        self.verticalLayout_main = QVBoxLayout(HomePage)
        self.verticalLayout_main.setSpacing(16)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(20, 20, 20, 20)
        self.layout_header = QHBoxLayout()
        self.layout_header.setObjectName(u"layout_header")
        self.lbl_title = QLabel(HomePage)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_title.setFont(font)

        self.layout_header.addWidget(self.lbl_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_header.addItem(self.horizontalSpacer)

        self.btn_quick_start_scan = QPushButton(HomePage)
        self.btn_quick_start_scan.setObjectName(u"btn_quick_start_scan")
        self.btn_quick_start_scan.setMinimumSize(QSize(200, 42))

        self.layout_header.addWidget(self.btn_quick_start_scan)


        self.verticalLayout_main.addLayout(self.layout_header)

        self.layout_status_cards = QHBoxLayout()
        self.layout_status_cards.setSpacing(12)
        self.layout_status_cards.setObjectName(u"layout_status_cards")
        self.group_mcu_status = QGroupBox(HomePage)
        self.group_mcu_status.setObjectName(u"group_mcu_status")
        self.verticalLayout_1 = QVBoxLayout(self.group_mcu_status)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.lbl_teensy_status = QLabel(self.group_mcu_status)
        self.lbl_teensy_status.setObjectName(u"lbl_teensy_status")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_teensy_status.setFont(font1)

        self.verticalLayout_1.addWidget(self.lbl_teensy_status)


        self.layout_status_cards.addWidget(self.group_mcu_status)

        self.group_laser_status = QGroupBox(HomePage)
        self.group_laser_status.setObjectName(u"group_laser_status")
        self.horizontalLayout = QHBoxLayout(self.group_laser_status)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_laser_s = QLabel(self.group_laser_status)
        self.lbl_laser_s.setObjectName(u"lbl_laser_s")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.lbl_laser_s.setFont(font2)

        self.horizontalLayout.addWidget(self.lbl_laser_s)

        self.lbl_laser_status = QLabel(self.group_laser_status)
        self.lbl_laser_status.setObjectName(u"lbl_laser_status")
        self.lbl_laser_status.setFont(font2)

        self.horizontalLayout.addWidget(self.lbl_laser_status)


        self.layout_status_cards.addWidget(self.group_laser_status)

        self.group_sensor_status = QGroupBox(HomePage)
        self.group_sensor_status.setObjectName(u"group_sensor_status")
        self.verticalLayout_3 = QVBoxLayout(self.group_sensor_status)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_baseline_voltage = QLabel(self.group_sensor_status)
        self.lbl_baseline_voltage.setObjectName(u"lbl_baseline_voltage")
        self.lbl_baseline_voltage.setFont(font1)

        self.verticalLayout_3.addWidget(self.lbl_baseline_voltage)

        self.bar_ambient_leakage = QProgressBar(self.group_sensor_status)
        self.bar_ambient_leakage.setObjectName(u"bar_ambient_leakage")
        self.bar_ambient_leakage.setMaximum(3300)
        self.bar_ambient_leakage.setValue(8)

        self.verticalLayout_3.addWidget(self.bar_ambient_leakage)


        self.layout_status_cards.addWidget(self.group_sensor_status)

        self.group_stage_status = QGroupBox(HomePage)
        self.group_stage_status.setObjectName(u"group_stage_status")
        self.verticalLayout_4 = QVBoxLayout(self.group_stage_status)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_stage_status = QLabel(self.group_stage_status)
        self.lbl_stage_status.setObjectName(u"lbl_stage_status")
        self.lbl_stage_status.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbl_stage_status)

        self.lbl_stage_coords = QLabel(self.group_stage_status)
        self.lbl_stage_coords.setObjectName(u"lbl_stage_coords")

        self.verticalLayout_4.addWidget(self.lbl_stage_coords)


        self.layout_status_cards.addWidget(self.group_stage_status)


        self.verticalLayout_main.addLayout(self.layout_status_cards)

        self.layout_bottom_area = QHBoxLayout()
        self.layout_bottom_area.setSpacing(16)
        self.layout_bottom_area.setObjectName(u"layout_bottom_area")
        self.group_recent_scans = QGroupBox(HomePage)
        self.group_recent_scans.setObjectName(u"group_recent_scans")
        self.verticalLayout_5 = QVBoxLayout(self.group_recent_scans)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.table_recent_scans = QTableWidget(self.group_recent_scans)
        if (self.table_recent_scans.columnCount() < 4):
            self.table_recent_scans.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_recent_scans.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_recent_scans.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_recent_scans.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_recent_scans.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_recent_scans.setObjectName(u"table_recent_scans")
        self.table_recent_scans.setMinimumSize(QSize(400, 0))
        self.table_recent_scans.setAlternatingRowColors(True)
        self.table_recent_scans.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_recent_scans.horizontalHeader().setDefaultSectionSize(122)

        self.verticalLayout_5.addWidget(self.table_recent_scans)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_open_selected_scan = QPushButton(self.group_recent_scans)
        self.btn_open_selected_scan.setObjectName(u"btn_open_selected_scan")

        self.horizontalLayout_2.addWidget(self.btn_open_selected_scan)

        self.btn_run_cal_check = QPushButton(self.group_recent_scans)
        self.btn_run_cal_check.setObjectName(u"btn_run_cal_check")

        self.horizontalLayout_2.addWidget(self.btn_run_cal_check)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.layout_bottom_area.addWidget(self.group_recent_scans)

        self.group_last_preview = QGroupBox(HomePage)
        self.group_last_preview.setObjectName(u"group_last_preview")
        self.verticalLayout_6 = QVBoxLayout(self.group_last_preview)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.placeholder_home_wafer = QFrame(self.group_last_preview)
        self.placeholder_home_wafer.setObjectName(u"placeholder_home_wafer")
        self.placeholder_home_wafer.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_home_wafer_preview = QVBoxLayout(self.placeholder_home_wafer)
        self.layout_home_wafer_preview.setObjectName(u"layout_home_wafer_preview")
        self.lbl_home_plot_placeholder = QLabel(self.placeholder_home_wafer)
        self.lbl_home_plot_placeholder.setObjectName(u"lbl_home_plot_placeholder")
        self.lbl_home_plot_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_home_wafer_preview.addWidget(self.lbl_home_plot_placeholder)


        self.verticalLayout_6.addWidget(self.placeholder_home_wafer)


        self.layout_bottom_area.addWidget(self.group_last_preview)

        self.layout_bottom_area.setStretch(0, 3)
        self.layout_bottom_area.setStretch(1, 2)

        self.verticalLayout_main.addLayout(self.layout_bottom_area)

        self.verticalLayout_main.setStretch(2, 1)

        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        self.lbl_title.setText(QCoreApplication.translate("HomePage", u"Dashboard", None))
        self.btn_quick_start_scan.setText(QCoreApplication.translate("HomePage", u"New Wafer Scan", None))
        self.group_mcu_status.setTitle(QCoreApplication.translate("HomePage", u"Controller (Teensy 4.1)", None))
        self.lbl_teensy_status.setText(QCoreApplication.translate("HomePage", u"ONLINE ", None))
        self.group_laser_status.setTitle(QCoreApplication.translate("HomePage", u"Laser (405nm 1mW)", None))
        self.lbl_laser_s.setText(QCoreApplication.translate("HomePage", u"Laser Status:", None))
        self.lbl_laser_status.setText(QCoreApplication.translate("HomePage", u"Ready", None))
        self.group_sensor_status.setTitle(QCoreApplication.translate("HomePage", u"Sensor Baseline", None))
        self.lbl_baseline_voltage.setText(QCoreApplication.translate("HomePage", u"0.008 V (Dark OK)", None))
        self.bar_ambient_leakage.setFormat(QCoreApplication.translate("HomePage", u"%v mV", None))
        self.group_stage_status.setTitle(QCoreApplication.translate("HomePage", u"Motion Stage", None))
        self.lbl_stage_status.setText(QCoreApplication.translate("HomePage", u" READY", None))
        self.lbl_stage_coords.setText(QCoreApplication.translate("HomePage", u"X: 0.00 mm | Y: 0.00 mm", None))
        self.group_recent_scans.setTitle(QCoreApplication.translate("HomePage", u"Recent Inspection Results", None))
        ___qtablewidgetitem = self.table_recent_scans.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HomePage", u"Wafer ID", None))
        ___qtablewidgetitem1 = self.table_recent_scans.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HomePage", u"Date / Time", None))
        ___qtablewidgetitem2 = self.table_recent_scans.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HomePage", u"Particles", None))
        ___qtablewidgetitem3 = self.table_recent_scans.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HomePage", u"Status", None))
        self.btn_open_selected_scan.setText(QCoreApplication.translate("HomePage", u"Open", None))
        self.btn_run_cal_check.setText(QCoreApplication.translate("HomePage", u"Run  Calibration Check", None))
        self.group_last_preview.setTitle(QCoreApplication.translate("HomePage", u"Last Wafer Defect Map", None))
        self.lbl_home_plot_placeholder.setText(QCoreApplication.translate("HomePage", u"Wafer component", None))
        pass
    # retranslateUi

