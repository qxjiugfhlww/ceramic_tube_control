# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowoZzDVa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 955)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu = QFrame(self.centralwidget)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setFrameShape(QFrame.NoFrame)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Menu)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.control_btn = QPushButton(self.Menu)
        self.control_btn.setObjectName(u"control_btn")
        self.control_btn.setMinimumSize(QSize(0, 40))
        self.control_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.control_btn)

        self.calibration_btn = QPushButton(self.Menu)
        self.calibration_btn.setObjectName(u"calibration_btn")
        self.calibration_btn.setMinimumSize(QSize(0, 40))
        self.calibration_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.calibration_btn)

        self.settings_btn = QPushButton(self.Menu)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 40))
        self.settings_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.settings_btn)


        self.verticalLayout.addWidget(self.Menu)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_pages_2 = QFrame(self.Content)
        self.frame_pages_2.setObjectName(u"frame_pages_2")
        self.frame_pages_2.setFrameShape(QFrame.StyledPanel)
        self.frame_pages_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_pages_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_pages_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.verticalLayout_2 = QVBoxLayout(self.start_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2.addWidget(self.start_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_3 = QVBoxLayout(self.settings_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.settings_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_14)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 40))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_29)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.connection_btn = QPushButton(self.frame_29)
        self.connection_btn.setObjectName(u"connection_btn")
        self.connection_btn.setMinimumSize(QSize(0, 40))
        self.connection_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.connection_btn)

        self.score_btn = QPushButton(self.frame_29)
        self.score_btn.setObjectName(u"score_btn")
        self.score_btn.setMinimumSize(QSize(0, 40))
        self.score_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.score_btn)

        self.debug_btn = QPushButton(self.frame_29)
        self.debug_btn.setObjectName(u"debug_btn")
        self.debug_btn.setMinimumSize(QSize(0, 40))
        self.debug_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.debug_btn)


        self.verticalLayout_17.addWidget(self.frame_29)

        self.stackedWidget = QStackedWidget(self.frame_14)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.connection_page = QWidget()
        self.connection_page.setObjectName(u"connection_page")
        self.horizontalLayout_2 = QHBoxLayout(self.connection_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_36 = QFrame(self.connection_page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_36)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_23 = QLabel(self.frame_36)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_36)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_36)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label_24 = QLabel(self.frame_36)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(200, 50))

        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_36)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_25 = QLabel(self.frame_36)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(200, 50))

        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_22 = QLabel(self.frame_36)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(214, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_36)

        self.stackedWidget.addWidget(self.connection_page)
        self.score_page = QWidget()
        self.score_page.setObjectName(u"score_page")
        self.verticalLayout_18 = QVBoxLayout(self.score_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_15 = QFrame(self.score_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(755, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_28 = QLabel(self.frame_15)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 0, 0, 1, 2)

        self.ellipses_amount = QLineEdit(self.frame_15)
        self.ellipses_amount.setObjectName(u"ellipses_amount")

        self.gridLayout.addWidget(self.ellipses_amount, 0, 2, 1, 1)

        self.label_29 = QLabel(self.frame_15)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 1, 0, 1, 2)

        self.lineEdit_5 = QLineEdit(self.frame_15)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 2, 1, 1)

        self.label_30 = QLabel(self.frame_15)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_31 = QLabel(self.frame_15)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 3, 0, 1, 2)

        self.lineEdit_6 = QLineEdit(self.frame_15)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 4, 0, 1, 2)

        self.lineEdit_7 = QLineEdit(self.frame_15)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 4, 2, 1, 1)

        self.label_2 = QLabel(self.frame_15)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.radius_inp = QLineEdit(self.frame_15)
        self.radius_inp.setObjectName(u"radius_inp")

        self.gridLayout.addWidget(self.radius_inp, 5, 1, 1, 2)

        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.reddot1_inp = QLineEdit(self.frame_15)
        self.reddot1_inp.setObjectName(u"reddot1_inp")

        self.gridLayout.addWidget(self.reddot1_inp, 6, 1, 1, 2)

        self.label_26 = QLabel(self.frame_15)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 7, 0, 1, 1)

        self.reddot2_inp = QLineEdit(self.frame_15)
        self.reddot2_inp.setObjectName(u"reddot2_inp")

        self.gridLayout.addWidget(self.reddot2_inp, 7, 1, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(755, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.score_page)
        self.debug_page = QWidget()
        self.debug_page.setObjectName(u"debug_page")
        self.verticalLayout_4 = QVBoxLayout(self.debug_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.debug_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.debug_page)

        self.verticalLayout_17.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.settings_page)
        self.control_page = QWidget()
        self.control_page.setObjectName(u"control_page")
        self.verticalLayout_13 = QVBoxLayout(self.control_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame = QFrame(self.control_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(279, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 2, 3, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 3, 1, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 3, 3, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 4, 3, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 4, 1, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(279, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 793, 348))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Box)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame)

        self.stackedWidget_2.addWidget(self.control_page)
        self.calibration_page = QWidget()
        self.calibration_page.setObjectName(u"calibration_page")
        self.verticalLayout_14 = QVBoxLayout(self.calibration_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_11 = QFrame(self.calibration_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.camera_frames = QLabel(self.frame_11)
        self.camera_frames.setObjectName(u"camera_frames")
        self.camera_frames.setMinimumSize(QSize(0, 0))
        self.camera_frames.setPixmap(QPixmap(u"../stapi/curve.jpg"))
        self.camera_frames.setScaledContents(False)
        self.camera_frames.setAlignment(Qt.AlignCenter)
        self.camera_frames.setWordWrap(False)
        self.camera_frames.setIndent(-1)
        self.camera_frames.setOpenExternalLinks(False)
        self.camera_frames.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_8.addWidget(self.camera_frames, 0, 0, 1, 3)

        self.verticalSpacer_7 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 1, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_8, 3, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(792, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(792, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_18 = QLabel(self.frame_11)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_11)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_7.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_7.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_7.addWidget(self.pushButton, 3, 0, 1, 2)


        self.gridLayout_8.addLayout(self.gridLayout_7, 2, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.stackedWidget_2.addWidget(self.calibration_page)

        self.verticalLayout_12.addWidget(self.stackedWidget_2)


        self.horizontalLayout_4.addWidget(self.frame_pages_2)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.control_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430", None))
        self.calibration_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.connection_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.score_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0446\u0435\u043d\u043a\u0430", None))
        self.debug_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IP \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u043a\u0430\u0434\u0440\u0430\u043c\u0438", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0433\u043d\u0430\u043b \u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u043e \u0441\u044a\u0451\u043c\u043a\u0438, \u043f\u0438\u043d \u2116", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0440\u0435\u0437\u043e\u0432", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u043a\u0438", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0432\u0438\u0437\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 1", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 2", None))
        self.label_19.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"80%", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0432\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"41-43 \u043c\u043c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0444\u0435\u043a\u0442\u044b", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"K = 0.8", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"90%", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0432\u0438\u0437\u043d\u0430", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e: 90%", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"10 \u0448\u0442", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"R = 3 \u043c", None))
        self.label_27.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><div>\u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u043f\u043e\u043b\u0438\u0433\u043e\u043d: \u043f\u0440\u0438\u043c\u0435\u0440\u043d\u044b\u0439 \u043f\u043e\u043b\u0438\u0433\u043e\u043d \u0438\u0437 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u0434\u0438\u0443\u0441\u043e\u0432</div><div>\u041e\u0440\u0430\u043d\u0436\u0435\u0432\u044b\u0439 \u044d\u043b\u043b\u0438\u043f\u0441: \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f \u043a\u0440\u0430\u0441\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u0433\u043e\u043d\u0430</div><div>\u0421\u0438\u043d\u0438\u0439 \u044d\u043b\u043b\u0438\u043f\u0441: \u0438\u0434\u0435\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0440\u0435\u0437 \u0442\u0440\u0443\u0431\u043a\u0438</div><div>\u0417\u0435\u043b\u0451\u043d\u044b\u0439 \u043a\u0440\u0443\u0433: \u0432\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u043e\u0440\u043e\u0433\u0430</div></body></h"
                        "tml>", None))
        self.camera_frames.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u044b\u0441\u043e\u0442\u0443", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0442\u043e\u0447\u043a\u0435 A(\u043c\u043c)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0442\u043e\u0447\u043a\u0435 B(\u043c\u043c)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0444\u043e\u0442\u043e", None))
    # retranslateUi

