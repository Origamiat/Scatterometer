# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ResultsPage(object):
    def setupUi(self, ResultsPage):
        if not ResultsPage.objectName():
            ResultsPage.setObjectName(u"ResultsPage")
        ResultsPage.resize(920, 700)
        self.verticalLayout_main = QVBoxLayout(ResultsPage)
        self.verticalLayout_main.setSpacing(12)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(16, 16, 16, 16)
        self.layout_toolbar = QHBoxLayout()
        self.layout_toolbar.setObjectName(u"layout_toolbar")
        self.label_select = QLabel(ResultsPage)
        self.label_select.setObjectName(u"label_select")

        self.layout_toolbar.addWidget(self.label_select)

        self.combo_dataset = QComboBox(ResultsPage)
        self.combo_dataset.addItem("")
        self.combo_dataset.setObjectName(u"combo_dataset")
        self.combo_dataset.setMinimumSize(QSize(220, 0))

        self.layout_toolbar.addWidget(self.combo_dataset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_toolbar.addItem(self.horizontalSpacer)

        self.btn_import_csv = QPushButton(ResultsPage)
        self.btn_import_csv.setObjectName(u"btn_import_csv")

        self.layout_toolbar.addWidget(self.btn_import_csv)

        self.btn_export_csv = QPushButton(ResultsPage)
        self.btn_export_csv.setObjectName(u"btn_export_csv")

        self.layout_toolbar.addWidget(self.btn_export_csv)

        self.btn_export_map_png = QPushButton(ResultsPage)
        self.btn_export_map_png.setObjectName(u"btn_export_map_png")

        self.layout_toolbar.addWidget(self.btn_export_map_png)


        self.verticalLayout_main.addLayout(self.layout_toolbar)

        self.layout_results_body = QHBoxLayout()
        self.layout_results_body.setSpacing(12)
        self.layout_results_body.setObjectName(u"layout_results_body")
        self.group_results_map = QGroupBox(ResultsPage)
        self.group_results_map.setObjectName(u"group_results_map")
        self.verticalLayout_1 = QVBoxLayout(self.group_results_map)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.wafer_placeholder = QFrame(self.group_results_map)
        self.wafer_placeholder.setObjectName(u"wafer_placeholder")
        self.wafer_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_results_wafer_map = QVBoxLayout(self.wafer_placeholder)
        self.layout_results_wafer_map.setObjectName(u"layout_results_wafer_map")

        self.verticalLayout_1.addWidget(self.wafer_placeholder)


        self.layout_results_body.addWidget(self.group_results_map)

        self.layout_right_panes = QVBoxLayout()
        self.layout_right_panes.setSpacing(12)
        self.layout_right_panes.setObjectName(u"layout_right_panes")
        self.group_histogram = QGroupBox(ResultsPage)
        self.group_histogram.setObjectName(u"group_histogram")
        self.verticalLayout_2 = QVBoxLayout(self.group_histogram)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.histogram_placeholder = QFrame(self.group_histogram)
        self.histogram_placeholder.setObjectName(u"histogram_placeholder")
        self.histogram_placeholder.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_histogram = QVBoxLayout(self.histogram_placeholder)
        self.layout_histogram.setObjectName(u"layout_histogram")
        self.lbl_hist_placeholder = QLabel(self.histogram_placeholder)
        self.lbl_hist_placeholder.setObjectName(u"lbl_hist_placeholder")
        self.lbl_hist_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_histogram.addWidget(self.lbl_hist_placeholder)


        self.verticalLayout_2.addWidget(self.histogram_placeholder)


        self.layout_right_panes.addWidget(self.group_histogram)

        self.group_defect_table = QGroupBox(ResultsPage)
        self.group_defect_table.setObjectName(u"group_defect_table")
        self.verticalLayout_3 = QVBoxLayout(self.group_defect_table)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_defects = QTableWidget(self.group_defect_table)
        if (self.table_defects.columnCount() < 4):
            self.table_defects.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_defects.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_defects.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_defects.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_defects.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_defects.setObjectName(u"table_defects")
        self.table_defects.setAlternatingRowColors(True)
        self.table_defects.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_defects.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.table_defects)


        self.layout_right_panes.addWidget(self.group_defect_table)

        self.layout_right_panes.setStretch(0, 2)
        self.layout_right_panes.setStretch(1, 3)

        self.layout_results_body.addLayout(self.layout_right_panes)

        self.layout_results_body.setStretch(0, 1)
        self.layout_results_body.setStretch(1, 1)

        self.verticalLayout_main.addLayout(self.layout_results_body)

        self.verticalLayout_main.setStretch(1, 1)

        self.retranslateUi(ResultsPage)

        QMetaObject.connectSlotsByName(ResultsPage)
    # setupUi

    def retranslateUi(self, ResultsPage):
        self.label_select.setText(QCoreApplication.translate("ResultsPage", u"Dataset:", None))
        self.combo_dataset.setItemText(0, QCoreApplication.translate("ResultsPage", u"Current / Latest Wafer Scan", None))

        self.btn_import_csv.setText(QCoreApplication.translate("ResultsPage", u"Import CSV", None))
        self.btn_export_csv.setText(QCoreApplication.translate("ResultsPage", u"Export CSV", None))
        self.btn_export_map_png.setText(QCoreApplication.translate("ResultsPage", u"Save ", None))
        self.group_results_map.setTitle(QCoreApplication.translate("ResultsPage", u" Wafer Particle Map (Click to Inspect)", None))
        self.group_histogram.setTitle(QCoreApplication.translate("ResultsPage", u"Particle Estimated Size Distribution (nm)", None))
        self.lbl_hist_placeholder.setText(QCoreApplication.translate("ResultsPage", u"Histogram", None))
        self.group_defect_table.setTitle(QCoreApplication.translate("ResultsPage", u"Detected Particle Coordinates", None))
        ___qtablewidgetitem = self.table_defects.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ResultsPage", u"ID", None))
        ___qtablewidgetitem1 = self.table_defects.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ResultsPage", u"X (mm)", None))
        ___qtablewidgetitem2 = self.table_defects.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ResultsPage", u"Y (mm)", None))
        ___qtablewidgetitem3 = self.table_defects.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ResultsPage", u"Estimated Size (nm)", None))
        pass
    # retranslateUi

