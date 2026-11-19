# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ControlPage(object):
    def setupUi(self, ControlPage):
        if not ControlPage.objectName():
            ControlPage.setObjectName(u"ControlPage")
        ControlPage.resize(920, 700)
        self.verticalLayout_main = QVBoxLayout(ControlPage)
        self.verticalLayout_main.setSpacing(12)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(16, 16, 16, 16)
        self.group_control_ribbon = QGroupBox(ControlPage)
        self.group_control_ribbon.setObjectName(u"group_control_ribbon")
        self.horizontalLayout_ribbon = QHBoxLayout(self.group_control_ribbon)
        self.horizontalLayout_ribbon.setObjectName(u"horizontalLayout_ribbon")
        self.btn_start_scan = QPushButton(self.group_control_ribbon)
        self.btn_start_scan.setObjectName(u"btn_start_scan")
        self.btn_start_scan.setMinimumSize(QSize(120, 38))

        self.horizontalLayout_ribbon.addWidget(self.btn_start_scan)

        self.btn_pause_scan = QPushButton(self.group_control_ribbon)
        self.btn_pause_scan.setObjectName(u"btn_pause_scan")
        self.btn_pause_scan.setMinimumSize(QSize(100, 38))

        self.horizontalLayout_ribbon.addWidget(self.btn_pause_scan)

        self.btn_abort_scan = QPushButton(self.group_control_ribbon)
        self.btn_abort_scan.setObjectName(u"btn_abort_scan")
        self.btn_abort_scan.setMinimumSize(QSize(100, 38))

        self.horizontalLayout_ribbon.addWidget(self.btn_abort_scan)

        self.btn_return_home = QPushButton(self.group_control_ribbon)
        self.btn_return_home.setObjectName(u"btn_return_home")
        self.btn_return_home.setMinimumSize(QSize(120, 38))

        self.horizontalLayout_ribbon.addWidget(self.btn_return_home)

        self.progress_scan = QProgressBar(self.group_control_ribbon)
        self.progress_scan.setObjectName(u"progress_scan")
        self.progress_scan.setValue(0)

        self.horizontalLayout_ribbon.addWidget(self.progress_scan)

        self.lbl_scan_eta = QLabel(self.group_control_ribbon)
        self.lbl_scan_eta.setObjectName(u"lbl_scan_eta")
        self.lbl_scan_eta.setMinimumSize(QSize(110, 0))
        self.lbl_scan_eta.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_ribbon.addWidget(self.lbl_scan_eta)


        self.verticalLayout_main.addWidget(self.group_control_ribbon)

        self.layout_workspace = QHBoxLayout()
        self.layout_workspace.setSpacing(12)
        self.layout_workspace.setObjectName(u"layout_workspace")
        self.layout_graphs = QVBoxLayout()
        self.layout_graphs.setSpacing(12)
        self.layout_graphs.setObjectName(u"layout_graphs")
        self.group_oscilloscope = QGroupBox(ControlPage)
        self.group_oscilloscope.setObjectName(u"group_oscilloscope")
        self.verticalLayout_osc = QVBoxLayout(self.group_oscilloscope)
        self.verticalLayout_osc.setObjectName(u"verticalLayout_osc")
        self.graph_placeholder = QFrame(self.group_oscilloscope)
        self.graph_placeholder.setObjectName(u"graph_placeholder")
        self.graph_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_oscilloscope = QVBoxLayout(self.graph_placeholder)
        self.layout_oscilloscope.setObjectName(u"layout_oscilloscope")

        self.verticalLayout_osc.addWidget(self.graph_placeholder)


        self.layout_graphs.addWidget(self.group_oscilloscope)

        self.group_wafer_map = QGroupBox(ControlPage)
        self.group_wafer_map.setObjectName(u"group_wafer_map")
        self.verticalLayout_map = QVBoxLayout(self.group_wafer_map)
        self.verticalLayout_map.setObjectName(u"verticalLayout_map")
        self.wafer_placeholder = QFrame(self.group_wafer_map)
        self.wafer_placeholder.setObjectName(u"wafer_placeholder")
        self.wafer_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_live_wafer_map = QVBoxLayout(self.wafer_placeholder)
        self.layout_live_wafer_map.setObjectName(u"layout_live_wafer_map")

        self.verticalLayout_map.addWidget(self.wafer_placeholder)


        self.layout_graphs.addWidget(self.group_wafer_map)

        self.layout_graphs.setStretch(0, 2)
        self.layout_graphs.setStretch(1, 3)

        self.layout_workspace.addLayout(self.layout_graphs)

        self.layout_telemetry = QVBoxLayout()
        self.layout_telemetry.setSpacing(12)
        self.layout_telemetry.setObjectName(u"layout_telemetry")
        self.group_stage_telemetry = QGroupBox(ControlPage)
        self.group_stage_telemetry.setObjectName(u"group_stage_telemetry")
        self.formLayout_telemetry = QFormLayout(self.group_stage_telemetry)
        self.formLayout_telemetry.setObjectName(u"formLayout_telemetry")
        self.label_x = QLabel(self.group_stage_telemetry)
        self.label_x.setObjectName(u"label_x")

        self.formLayout_telemetry.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_x)

        self.lbl_live_x = QLabel(self.group_stage_telemetry)
        self.lbl_live_x.setObjectName(u"lbl_live_x")
        font = QFont()
        font.setBold(True)
        self.lbl_live_x.setFont(font)

        self.formLayout_telemetry.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lbl_live_x)

        self.label_y = QLabel(self.group_stage_telemetry)
        self.label_y.setObjectName(u"label_y")

        self.formLayout_telemetry.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_y)

        self.lbl_live_y = QLabel(self.group_stage_telemetry)
        self.lbl_live_y.setObjectName(u"lbl_live_y")
        self.lbl_live_y.setFont(font)

        self.formLayout_telemetry.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lbl_live_y)

        self.label_v = QLabel(self.group_stage_telemetry)
        self.label_v.setObjectName(u"label_v")

        self.formLayout_telemetry.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_v)

        self.lbl_live_speed = QLabel(self.group_stage_telemetry)
        self.lbl_live_speed.setObjectName(u"lbl_live_speed")

        self.formLayout_telemetry.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lbl_live_speed)

        self.label_p = QLabel(self.group_stage_telemetry)
        self.label_p.setObjectName(u"label_p")

        self.formLayout_telemetry.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_p)

        self.lbl_peak_intensity = QLabel(self.group_stage_telemetry)
        self.lbl_peak_intensity.setObjectName(u"lbl_peak_intensity")

        self.formLayout_telemetry.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lbl_peak_intensity)


        self.layout_telemetry.addWidget(self.group_stage_telemetry)

        self.group_defect_counters = QGroupBox(ControlPage)
        self.group_defect_counters.setObjectName(u"group_defect_counters")
        self.formLayout_counts = QFormLayout(self.group_defect_counters)
        self.formLayout_counts.setObjectName(u"formLayout_counts")
        self.label_total = QLabel(self.group_defect_counters)
        self.label_total.setObjectName(u"label_total")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_total.setFont(font1)

        self.formLayout_counts.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_total)

        self.lbl_count_total = QLabel(self.group_defect_counters)
        self.lbl_count_total.setObjectName(u"lbl_count_total")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lbl_count_total.setFont(font2)

        self.formLayout_counts.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lbl_count_total)

        self.label_small = QLabel(self.group_defect_counters)
        self.label_small.setObjectName(u"label_small")

        self.formLayout_counts.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_small)

        self.lbl_count_small = QLabel(self.group_defect_counters)
        self.lbl_count_small.setObjectName(u"lbl_count_small")

        self.formLayout_counts.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lbl_count_small)

        self.label_large = QLabel(self.group_defect_counters)
        self.label_large.setObjectName(u"label_large")

        self.formLayout_counts.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_large)

        self.lbl_count_large = QLabel(self.group_defect_counters)
        self.lbl_count_large.setObjectName(u"lbl_count_large")

        self.formLayout_counts.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lbl_count_large)


        self.layout_telemetry.addWidget(self.group_defect_counters)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_telemetry.addItem(self.verticalSpacer)


        self.layout_workspace.addLayout(self.layout_telemetry)

        self.layout_workspace.setStretch(0, 3)
        self.layout_workspace.setStretch(1, 1)

        self.verticalLayout_main.addLayout(self.layout_workspace)

        self.verticalLayout_main.setStretch(1, 1)

        self.retranslateUi(ControlPage)

        QMetaObject.connectSlotsByName(ControlPage)
    # setupUi

    def retranslateUi(self, ControlPage):
        self.group_control_ribbon.setTitle(QCoreApplication.translate("ControlPage", u"Wafer Scan ", None))
        self.btn_start_scan.setText(QCoreApplication.translate("ControlPage", u"Start Scan", None))
        self.btn_pause_scan.setText(QCoreApplication.translate("ControlPage", u"Pause", None))
        self.btn_abort_scan.setText(QCoreApplication.translate("ControlPage", u"Abort", None))
        self.btn_return_home.setText(QCoreApplication.translate("ControlPage", u"Home Stage", None))
        self.lbl_scan_eta.setText(QCoreApplication.translate("ControlPage", u"ETA: --:--:--", None))
        self.group_oscilloscope.setTitle(QCoreApplication.translate("ControlPage", u"Live Sensor Graph", None))
        self.group_wafer_map.setTitle(QCoreApplication.translate("ControlPage", u"Real-Time 2D Wafer Particle Map", None))
        self.group_stage_telemetry.setTitle(QCoreApplication.translate("ControlPage", u"Live Stage Position", None))
        self.label_x.setText(QCoreApplication.translate("ControlPage", u"X Position:", None))
        self.lbl_live_x.setText(QCoreApplication.translate("ControlPage", u"0.000 mm", None))
        self.label_y.setText(QCoreApplication.translate("ControlPage", u"Y Position", None))
        self.lbl_live_y.setText(QCoreApplication.translate("ControlPage", u"0.000 mm", None))
        self.label_v.setText(QCoreApplication.translate("ControlPage", u"Scan Speed:", None))
        self.lbl_live_speed.setText(QCoreApplication.translate("ControlPage", u"0.0 mm/s", None))
        self.label_p.setText(QCoreApplication.translate("ControlPage", u"Peak Intensity", None))
        self.lbl_peak_intensity.setText(QCoreApplication.translate("ControlPage", u"0.0 mV", None))
        self.group_defect_counters.setTitle(QCoreApplication.translate("ControlPage", u"Live Particle Tally", None))
        self.label_total.setText(QCoreApplication.translate("ControlPage", u"Total Particles:", None))
        self.lbl_count_total.setText(QCoreApplication.translate("ControlPage", u"0", None))
        self.label_small.setText(QCoreApplication.translate("ControlPage", u"Small", None))
        self.lbl_count_small.setText(QCoreApplication.translate("ControlPage", u"0", None))
        self.label_large.setText(QCoreApplication.translate("ControlPage", u"Large", None))
        self.lbl_count_large.setText(QCoreApplication.translate("ControlPage", u"0", None))
        pass
    # retranslateUi

