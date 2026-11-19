# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 750)
        MainWindow.setMinimumSize(QSize(850, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Navbar = QFrame(self.centralwidget)
        self.Navbar.setObjectName(u"Navbar")
        self.Navbar.setMinimumSize(QSize(200, 500))
        self.Navbar.setMaximumSize(QSize(220, 16777215))
        self.Navbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.Navbar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Navbar)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Logo = QWidget(self.Navbar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(180, 80))
        self.Logo.setMaximumSize(QSize(220, 100))
        self.verticalLayout_3 = QVBoxLayout(self.Logo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_nav_home = QPushButton(self.Logo)
        self.btn_nav_home.setObjectName(u"btn_nav_home")
        self.btn_nav_home.setMinimumSize(QSize(160, 50))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.btn_nav_home.setFont(font)
        self.btn_nav_home.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_nav_home.setStyleSheet(u"background: transparent; border: none;")

        self.verticalLayout_3.addWidget(self.btn_nav_home)


        self.verticalLayout_2.addWidget(self.Logo)

        self.NavButtonsContainer = QWidget(self.Navbar)
        self.NavButtonsContainer.setObjectName(u"NavButtonsContainer")
        self.verticalLayout = QVBoxLayout(self.NavButtonsContainer)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_nav_dashboard = QPushButton(self.NavButtonsContainer)
        self.btn_nav_dashboard.setObjectName(u"btn_nav_dashboard")
        self.btn_nav_dashboard.setMinimumSize(QSize(160, 40))
        self.btn_nav_dashboard.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.verticalLayout.addWidget(self.btn_nav_dashboard)

        self.btn_nav_control = QPushButton(self.NavButtonsContainer)
        self.btn_nav_control.setObjectName(u"btn_nav_control")
        self.btn_nav_control.setMinimumSize(QSize(160, 40))

        self.verticalLayout.addWidget(self.btn_nav_control)

        self.btn_nav_results = QPushButton(self.NavButtonsContainer)
        self.btn_nav_results.setObjectName(u"btn_nav_results")
        self.btn_nav_results.setMinimumSize(QSize(160, 40))

        self.verticalLayout.addWidget(self.btn_nav_results)

        self.btn_nav_calibration = QPushButton(self.NavButtonsContainer)
        self.btn_nav_calibration.setObjectName(u"btn_nav_calibration")
        self.btn_nav_calibration.setMinimumSize(QSize(160, 40))

        self.verticalLayout.addWidget(self.btn_nav_calibration)

        self.btn_nav_settings = QPushButton(self.NavButtonsContainer)
        self.btn_nav_settings.setObjectName(u"btn_nav_settings")
        self.btn_nav_settings.setMinimumSize(QSize(160, 40))

        self.verticalLayout.addWidget(self.btn_nav_settings)


        self.verticalLayout_2.addWidget(self.NavButtonsContainer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.lbl_sidebar_status = QLabel(self.Navbar)
        self.lbl_sidebar_status.setObjectName(u"lbl_sidebar_status")
        self.lbl_sidebar_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_sidebar_status)


        self.horizontalLayout.addWidget(self.Navbar)

        self.Content = QStackedWidget(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setMinimumSize(QSize(600, 500))

        self.horizontalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1150, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wafer Scatterometry Control Suite", None))
        self.btn_nav_home.setText(QCoreApplication.translate("MainWindow", u"Scatterometer", None))
        self.btn_nav_dashboard.setText(QCoreApplication.translate("MainWindow", u"Home Dashboard", None))
        self.btn_nav_control.setText(QCoreApplication.translate("MainWindow", u"Live Scan", None))
        self.btn_nav_results.setText(QCoreApplication.translate("MainWindow", u"Analysis & Results", None))
        self.btn_nav_calibration.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.btn_nav_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lbl_sidebar_status.setText(QCoreApplication.translate("MainWindow", u"Teensy 4.1: Connected", None))
    # retranslateUi

