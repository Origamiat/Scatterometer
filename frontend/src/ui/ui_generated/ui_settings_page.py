# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_page.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(971, 700)
        self.verticalLayout_main = QVBoxLayout(SettingsPage)
        self.verticalLayout_main.setSpacing(16)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(20, 20, 20, 20)
        self.lbl_settings_title = QLabel(SettingsPage)
        self.lbl_settings_title.setObjectName(u"lbl_settings_title")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_settings_title.setFont(font)

        self.verticalLayout_main.addWidget(self.lbl_settings_title)

        self.layout_columns = QHBoxLayout()
        self.layout_columns.setSpacing(16)
        self.layout_columns.setObjectName(u"layout_columns")
        self.group_serial = QGroupBox(SettingsPage)
        self.group_serial.setObjectName(u"group_serial")
        self.formLayout_serial = QFormLayout(self.group_serial)
        self.formLayout_serial.setObjectName(u"formLayout_serial")
        self.label_port = QLabel(self.group_serial)
        self.label_port.setObjectName(u"label_port")

        self.formLayout_serial.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_port)

        self.combo_com_port = QComboBox(self.group_serial)
        self.combo_com_port.addItem("")
        self.combo_com_port.setObjectName(u"combo_com_port")

        self.formLayout_serial.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combo_com_port)

        self.label_rate = QLabel(self.group_serial)
        self.label_rate.setObjectName(u"label_rate")

        self.formLayout_serial.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_rate)

        self.spin_sample_rate = QSpinBox(self.group_serial)
        self.spin_sample_rate.setObjectName(u"spin_sample_rate")
        self.spin_sample_rate.setMinimum(10)
        self.spin_sample_rate.setMaximum(500)
        self.spin_sample_rate.setValue(100)

        self.formLayout_serial.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spin_sample_rate)

        self.btn_reconnect_teensy = QPushButton(self.group_serial)
        self.btn_reconnect_teensy.setObjectName(u"btn_reconnect_teensy")

        self.formLayout_serial.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.btn_reconnect_teensy)


        self.layout_columns.addWidget(self.group_serial)

        self.group_scan_params = QGroupBox(SettingsPage)
        self.group_scan_params.setObjectName(u"group_scan_params")
        self.formLayout_scan = QFormLayout(self.group_scan_params)
        self.formLayout_scan.setObjectName(u"formLayout_scan")
        self.label_diam = QLabel(self.group_scan_params)
        self.label_diam.setObjectName(u"label_diam")

        self.formLayout_scan.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_diam)

        self.combo_wafer_size = QComboBox(self.group_scan_params)
        self.combo_wafer_size.addItem("")
        self.combo_wafer_size.addItem("")
        self.combo_wafer_size.addItem("")
        self.combo_wafer_size.addItem("")
        self.combo_wafer_size.setObjectName(u"combo_wafer_size")

        self.formLayout_scan.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combo_wafer_size)

        self.label_speed = QLabel(self.group_scan_params)
        self.label_speed.setObjectName(u"label_speed")

        self.formLayout_scan.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_speed)

        self.spin_scan_speed = QDoubleSpinBox(self.group_scan_params)
        self.spin_scan_speed.setObjectName(u"spin_scan_speed")
        self.spin_scan_speed.setMinimum(1.000000000000000)
        self.spin_scan_speed.setMaximum(200.000000000000000)
        self.spin_scan_speed.setValue(69.689999999999998)

        self.formLayout_scan.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spin_scan_speed)

        self.label_pitch = QLabel(self.group_scan_params)
        self.label_pitch.setObjectName(u"label_pitch")

        self.formLayout_scan.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_pitch)

        self.spin_track_pitch = QDoubleSpinBox(self.group_scan_params)
        self.spin_track_pitch.setObjectName(u"spin_track_pitch")
        self.spin_track_pitch.setMinimum(2.000000000000000)
        self.spin_track_pitch.setMaximum(100.000000000000000)
        self.spin_track_pitch.setValue(11.000000000000000)

        self.formLayout_scan.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spin_track_pitch)

        self.label_edge = QLabel(self.group_scan_params)
        self.label_edge.setObjectName(u"label_edge")

        self.formLayout_scan.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_edge)

        self.spin_edge_exclusion = QDoubleSpinBox(self.group_scan_params)
        self.spin_edge_exclusion.setObjectName(u"spin_edge_exclusion")
        self.spin_edge_exclusion.setValue(3.000000000000000)

        self.formLayout_scan.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spin_edge_exclusion)


        self.layout_columns.addWidget(self.group_scan_params)

        self.group_detection = QGroupBox(SettingsPage)
        self.group_detection.setObjectName(u"group_detection")
        self.formLayout_detect = QFormLayout(self.group_detection)
        self.formLayout_detect.setObjectName(u"formLayout_detect")
        self.label_t = QLabel(self.group_detection)
        self.label_t.setObjectName(u"label_t")

        self.formLayout_detect.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_t)

        self.spin_thresh = QDoubleSpinBox(self.group_detection)
        self.spin_thresh.setObjectName(u"spin_thresh")
        self.spin_thresh.setValue(3.000000000000000)

        self.formLayout_detect.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spin_thresh)

        self.label_rf = QLabel(self.group_detection)
        self.label_rf.setObjectName(u"label_rf")

        self.formLayout_detect.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_rf)

        self.combo_feedback_r = QComboBox(self.group_detection)
        self.combo_feedback_r.addItem("")
        self.combo_feedback_r.addItem("")
        self.combo_feedback_r.addItem("")
        self.combo_feedback_r.setObjectName(u"combo_feedback_r")

        self.formLayout_detect.setWidget(1, QFormLayout.ItemRole.FieldRole, self.combo_feedback_r)


        self.layout_columns.addWidget(self.group_detection)


        self.verticalLayout_main.addLayout(self.layout_columns)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_main.addItem(self.verticalSpacer)

        self.layout_footer = QHBoxLayout()
        self.layout_footer.setObjectName(u"layout_footer")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_footer.addItem(self.horizontalSpacer)

        self.btn_load_json = QPushButton(SettingsPage)
        self.btn_load_json.setObjectName(u"btn_load_json")

        self.layout_footer.addWidget(self.btn_load_json)

        self.btn_save_json = QPushButton(SettingsPage)
        self.btn_save_json.setObjectName(u"btn_save_json")

        self.layout_footer.addWidget(self.btn_save_json)

        self.btn_apply_settings = QPushButton(SettingsPage)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        self.btn_apply_settings.setMinimumSize(QSize(140, 38))

        self.layout_footer.addWidget(self.btn_apply_settings)


        self.verticalLayout_main.addLayout(self.layout_footer)


        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        self.lbl_settings_title.setText(QCoreApplication.translate("SettingsPage", u"System Settings & Scan Parameters", None))
        self.group_serial.setTitle(QCoreApplication.translate("SettingsPage", u"Teensy 4.1 USB Communication", None))
        self.label_port.setText(QCoreApplication.translate("SettingsPage", u"Serial Port:", None))
        self.combo_com_port.setItemText(0, QCoreApplication.translate("SettingsPage", u"COM3 (Teensy USB Serial)", None))

        self.label_rate.setText(QCoreApplication.translate("SettingsPage", u"ADC Sample Rate:", None))
        self.spin_sample_rate.setSuffix(QCoreApplication.translate("SettingsPage", u" kHz", None))
        self.btn_reconnect_teensy.setText(QCoreApplication.translate("SettingsPage", u"Refresh Connection", None))
        self.group_scan_params.setTitle(QCoreApplication.translate("SettingsPage", u"Wafer & Motion Parameters", None))
        self.label_diam.setText(QCoreApplication.translate("SettingsPage", u"Wafer Diameter:", None))
        self.combo_wafer_size.setItemText(0, QCoreApplication.translate("SettingsPage", u"100 mm ", None))
        self.combo_wafer_size.setItemText(1, QCoreApplication.translate("SettingsPage", u"150 mm ", None))
        self.combo_wafer_size.setItemText(2, QCoreApplication.translate("SettingsPage", u"200 mm", None))
        self.combo_wafer_size.setItemText(3, QCoreApplication.translate("SettingsPage", u"300 mm", None))

        self.label_speed.setText(QCoreApplication.translate("SettingsPage", u"Linear Scan Speed:", None))
        self.spin_scan_speed.setSuffix(QCoreApplication.translate("SettingsPage", u" mm/s", None))
        self.label_pitch.setText(QCoreApplication.translate("SettingsPage", u"Track Step Pitch:", None))
        self.spin_track_pitch.setSuffix(QCoreApplication.translate("SettingsPage", u" um", None))
        self.label_edge.setText(QCoreApplication.translate("SettingsPage", u"Edge Exclusion:", None))
        self.spin_edge_exclusion.setSuffix(QCoreApplication.translate("SettingsPage", u" mm", None))
        self.group_detection.setTitle(QCoreApplication.translate("SettingsPage", u"Sensor & Detection Thresholds", None))
        self.label_t.setText(QCoreApplication.translate("SettingsPage", u"Trreshold", None))
        self.spin_thresh.setSuffix(QCoreApplication.translate("SettingsPage", u" mV", None))
        self.label_rf.setText(QCoreApplication.translate("SettingsPage", u"OPT101P Feedback R:", None))
        self.combo_feedback_r.setItemText(0, QCoreApplication.translate("SettingsPage", u"50 MOhm (+ 20x Stage 2)", None))
        self.combo_feedback_r.setItemText(1, QCoreApplication.translate("SettingsPage", u"100 MOhm (+ 10x Stage 2)", None))
        self.combo_feedback_r.setItemText(2, QCoreApplication.translate("SettingsPage", u"20 MOhm (+ 50x Stage 2)", None))

        self.btn_load_json.setText(QCoreApplication.translate("SettingsPage", u"Load Profile (.json)", None))
        self.btn_save_json.setText(QCoreApplication.translate("SettingsPage", u"Save Profile (.json)", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("SettingsPage", u"Apply Settings", None))
        pass
    # retranslateUi

