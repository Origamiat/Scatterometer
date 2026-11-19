# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CalibrationPage(object):
    def setupUi(self, CalibrationPage):
        if not CalibrationPage.objectName():
            CalibrationPage.setObjectName(u"CalibrationPage")
        CalibrationPage.resize(920, 700)
        self.horizontalLayout_main = QHBoxLayout(CalibrationPage)
        self.horizontalLayout_main.setSpacing(16)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.horizontalLayout_main.setContentsMargins(16, 16, 16, 16)
        self.layout_left_controls = QVBoxLayout()
        self.layout_left_controls.setSpacing(12)
        self.layout_left_controls.setObjectName(u"layout_left_controls")
        self.group_stage_jog = QGroupBox(CalibrationPage)
        self.group_stage_jog.setObjectName(u"group_stage_jog")
        self.verticalLayout_jog = QVBoxLayout(self.group_stage_jog)
        self.verticalLayout_jog.setObjectName(u"verticalLayout_jog")
        self.horizontalLayout_step = QHBoxLayout()
        self.horizontalLayout_step.setObjectName(u"horizontalLayout_step")
        self.label_step = QLabel(self.group_stage_jog)
        self.label_step.setObjectName(u"label_step")

        self.horizontalLayout_step.addWidget(self.label_step)

        self.combo_jog_step = QComboBox(self.group_stage_jog)
        self.combo_jog_step.addItem("")
        self.combo_jog_step.addItem("")
        self.combo_jog_step.addItem("")
        self.combo_jog_step.addItem("")
        self.combo_jog_step.setObjectName(u"combo_jog_step")

        self.horizontalLayout_step.addWidget(self.combo_jog_step)


        self.verticalLayout_jog.addLayout(self.horizontalLayout_step)

        self.gridLayout_jog = QGridLayout()
        self.gridLayout_jog.setObjectName(u"gridLayout_jog")
        self.btn_jog_y_pos = QPushButton(self.group_stage_jog)
        self.btn_jog_y_pos.setObjectName(u"btn_jog_y_pos")
        self.btn_jog_y_pos.setMinimumSize(QSize(75, 40))

        self.gridLayout_jog.addWidget(self.btn_jog_y_pos, 0, 1, 1, 1)

        self.btn_jog_x_neg = QPushButton(self.group_stage_jog)
        self.btn_jog_x_neg.setObjectName(u"btn_jog_x_neg")
        self.btn_jog_x_neg.setMinimumSize(QSize(75, 40))

        self.gridLayout_jog.addWidget(self.btn_jog_x_neg, 1, 0, 1, 1)

        self.btn_jog_home = QPushButton(self.group_stage_jog)
        self.btn_jog_home.setObjectName(u"btn_jog_home")
        self.btn_jog_home.setMinimumSize(QSize(75, 40))

        self.gridLayout_jog.addWidget(self.btn_jog_home, 1, 1, 1, 1)

        self.btn_jog_x_pos = QPushButton(self.group_stage_jog)
        self.btn_jog_x_pos.setObjectName(u"btn_jog_x_pos")
        self.btn_jog_x_pos.setMinimumSize(QSize(75, 40))

        self.gridLayout_jog.addWidget(self.btn_jog_x_pos, 1, 2, 1, 1)

        self.btn_jog_y_neg = QPushButton(self.group_stage_jog)
        self.btn_jog_y_neg.setObjectName(u"btn_jog_y_neg")
        self.btn_jog_y_neg.setMinimumSize(QSize(75, 40))

        self.gridLayout_jog.addWidget(self.btn_jog_y_neg, 2, 1, 1, 1)


        self.verticalLayout_jog.addLayout(self.gridLayout_jog)

        self.btn_set_origin = QPushButton(self.group_stage_jog)
        self.btn_set_origin.setObjectName(u"btn_set_origin")

        self.verticalLayout_jog.addWidget(self.btn_set_origin)


        self.layout_left_controls.addWidget(self.group_stage_jog)

        self.group_laser_override = QGroupBox(CalibrationPage)
        self.group_laser_override.setObjectName(u"group_laser_override")
        self.verticalLayout_lasers = QVBoxLayout(self.group_laser_override)
        self.verticalLayout_lasers.setObjectName(u"verticalLayout_lasers")
        self.btn_measure_noise_floor = QPushButton(self.group_laser_override)
        self.btn_measure_noise_floor.setObjectName(u"btn_measure_noise_floor")

        self.verticalLayout_lasers.addWidget(self.btn_measure_noise_floor)


        self.layout_left_controls.addWidget(self.group_laser_override)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_left_controls.addItem(self.verticalSpacer)


        self.horizontalLayout_main.addLayout(self.layout_left_controls)

        self.group_cal_scope = QGroupBox(CalibrationPage)
        self.group_cal_scope.setObjectName(u"group_cal_scope")
        self.verticalLayout_scope = QVBoxLayout(self.group_cal_scope)
        self.verticalLayout_scope.setObjectName(u"verticalLayout_scope")
        self.graph_placeholder = QFrame(self.group_cal_scope)
        self.graph_placeholder.setObjectName(u"graph_placeholder")
        self.graph_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_cal_scope = QVBoxLayout(self.graph_placeholder)
        self.layout_cal_scope.setObjectName(u"layout_cal_scope")

        self.verticalLayout_scope.addWidget(self.graph_placeholder)

        self.horizontalLayout_metrics = QHBoxLayout()
        self.horizontalLayout_metrics.setObjectName(u"horizontalLayout_metrics")
        self.lbl_cal_rms_noise = QLabel(self.group_cal_scope)
        self.lbl_cal_rms_noise.setObjectName(u"lbl_cal_rms_noise")

        self.horizontalLayout_metrics.addWidget(self.lbl_cal_rms_noise)

        self.lbl_cal_peak_v = QLabel(self.group_cal_scope)
        self.lbl_cal_peak_v.setObjectName(u"lbl_cal_peak_v")

        self.horizontalLayout_metrics.addWidget(self.lbl_cal_peak_v)

        self.lbl_cal_snr = QLabel(self.group_cal_scope)
        self.lbl_cal_snr.setObjectName(u"lbl_cal_snr")
        font = QFont()
        font.setBold(True)
        self.lbl_cal_snr.setFont(font)

        self.horizontalLayout_metrics.addWidget(self.lbl_cal_snr)


        self.verticalLayout_scope.addLayout(self.horizontalLayout_metrics)

        self.verticalLayout_scope.setStretch(0, 1)

        self.horizontalLayout_main.addWidget(self.group_cal_scope)

        self.horizontalLayout_main.setStretch(1, 2)

        self.retranslateUi(CalibrationPage)

        QMetaObject.connectSlotsByName(CalibrationPage)
    # setupUi

    def retranslateUi(self, CalibrationPage):
        self.group_stage_jog.setTitle(QCoreApplication.translate("CalibrationPage", u"Manual Stage Jogging", None))
        self.label_step.setText(QCoreApplication.translate("CalibrationPage", u"Step Size", None))
        self.combo_jog_step.setItemText(0, QCoreApplication.translate("CalibrationPage", u"0.01 mm (10 um)", None))
        self.combo_jog_step.setItemText(1, QCoreApplication.translate("CalibrationPage", u"0.10 mm (100 um)", None))
        self.combo_jog_step.setItemText(2, QCoreApplication.translate("CalibrationPage", u"1.00 mm", None))
        self.combo_jog_step.setItemText(3, QCoreApplication.translate("CalibrationPage", u"10.0 mm", None))

        self.btn_jog_y_pos.setText(QCoreApplication.translate("CalibrationPage", u"+Y (Up)", None))
        self.btn_jog_x_neg.setText(QCoreApplication.translate("CalibrationPage", u"-X (Left)", None))
        self.btn_jog_home.setText(QCoreApplication.translate("CalibrationPage", u"Home", None))
        self.btn_jog_x_pos.setText(QCoreApplication.translate("CalibrationPage", u"+X (Right)", None))
        self.btn_jog_y_neg.setText(QCoreApplication.translate("CalibrationPage", u"-Y (Down)", None))
        self.btn_set_origin.setText(QCoreApplication.translate("CalibrationPage", u"Set Current Position as Origin (0, 0)", None))
        self.group_laser_override.setTitle(QCoreApplication.translate("CalibrationPage", u"Diagnostics", None))
        self.btn_measure_noise_floor.setText(QCoreApplication.translate("CalibrationPage", u"Sample Dark Noise Floor", None))
        self.group_cal_scope.setTitle(QCoreApplication.translate("CalibrationPage", u"Graph", None))
        self.lbl_cal_rms_noise.setText(QCoreApplication.translate("CalibrationPage", u"Noise: 0.19 mV", None))
        self.lbl_cal_peak_v.setText(QCoreApplication.translate("CalibrationPage", u"Peak Amplitude: 0.00 mV", None))
        self.lbl_cal_snr.setText(QCoreApplication.translate("CalibrationPage", u"Live SNR: --", None))
        pass
    # retranslateUi

