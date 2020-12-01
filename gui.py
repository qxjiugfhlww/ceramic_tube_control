# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowXQwdAa.ui'
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
        MainWindow.resize(1826, 821)
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
        self.horizontalLayout_21 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_21.setSpacing(1)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_21.addWidget(self.score_btn)

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

        self.horizontalLayout_21.addWidget(self.connection_btn)


        self.verticalLayout_17.addWidget(self.frame_29)

        self.stackedWidget = QStackedWidget(self.frame_14)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.connection_page = QWidget()
        self.connection_page.setObjectName(u"connection_page")
        self.verticalLayout_19 = QVBoxLayout(self.connection_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_22 = QLabel(self.connection_page)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_19.addWidget(self.label_22)

        self.frame_36 = QFrame(self.connection_page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_23 = QLabel(self.frame_36)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(100, 50))

        self.horizontalLayout_26.addWidget(self.label_23)

        self.textEdit_3 = QTextEdit(self.frame_36)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_26.addWidget(self.textEdit_3)


        self.verticalLayout_19.addWidget(self.frame_36)

        self.frame_38 = QFrame(self.connection_page)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_24 = QLabel(self.frame_38)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_28.addWidget(self.label_24)

        self.textEdit_4 = QTextEdit(self.frame_38)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_28.addWidget(self.textEdit_4)


        self.verticalLayout_19.addWidget(self.frame_38)

        self.frame_37 = QFrame(self.connection_page)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_25 = QLabel(self.frame_37)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_27.addWidget(self.label_25)

        self.textEdit_5 = QTextEdit(self.frame_37)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_27.addWidget(self.textEdit_5)


        self.verticalLayout_19.addWidget(self.frame_37)

        self.stackedWidget.addWidget(self.connection_page)
        self.score_page = QWidget()
        self.score_page.setObjectName(u"score_page")
        self.verticalLayout_18 = QVBoxLayout(self.score_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_15 = QFrame(self.score_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(300, 150))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_31 = QFrame(self.frame_15)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(300, 150))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_31)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(300, 50))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_43 = QLabel(self.frame_32)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(150, 50))

        self.horizontalLayout_22.addWidget(self.label_43)

        self.diametr_inp_3 = QTextEdit(self.frame_32)
        self.diametr_inp_3.setObjectName(u"diametr_inp_3")
        self.diametr_inp_3.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_22.addWidget(self.diametr_inp_3)

        self.label_44 = QLabel(self.frame_32)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_22.addWidget(self.label_44)


        self.verticalLayout_15.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(300, 50))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_45 = QLabel(self.frame_33)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(100, 50))

        self.horizontalLayout_23.addWidget(self.label_45)

        self.curvature_inp_3 = QTextEdit(self.frame_33)
        self.curvature_inp_3.setObjectName(u"curvature_inp_3")
        self.curvature_inp_3.setMaximumSize(QSize(50, 30))
        self.curvature_inp_3.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_23.addWidget(self.curvature_inp_3)

        self.label_46 = QLabel(self.frame_33)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_23.addWidget(self.label_46)


        self.verticalLayout_15.addWidget(self.frame_33)


        self.verticalLayout_11.addWidget(self.frame_31)


        self.verticalLayout_18.addWidget(self.frame_15)

        self.frame_30 = QFrame(self.score_page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(100, 50))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_42 = QLabel(self.frame_30)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(100, 50))

        self.horizontalLayout_20.addWidget(self.label_42)


        self.verticalLayout_18.addWidget(self.frame_30)

        self.frame_16 = QFrame(self.score_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(300, 150))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_34 = QFrame(self.frame_16)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(300, 50))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_47 = QLabel(self.frame_34)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_24.addWidget(self.label_47)

        self.slices_amount_inp_3 = QTextEdit(self.frame_34)
        self.slices_amount_inp_3.setObjectName(u"slices_amount_inp_3")
        self.slices_amount_inp_3.setEnabled(True)
        self.slices_amount_inp_3.setMinimumSize(QSize(0, 0))
        self.slices_amount_inp_3.setMaximumSize(QSize(100, 50))
        self.slices_amount_inp_3.setLayoutDirection(Qt.LeftToRight)
        self.slices_amount_inp_3.setAutoFillBackground(False)

        self.horizontalLayout_24.addWidget(self.slices_amount_inp_3)


        self.verticalLayout_16.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_16)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(300, 50))
        self.frame_35.setLayoutDirection(Qt.LeftToRight)
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_48 = QLabel(self.frame_35)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(100, 50))

        self.horizontalLayout_25.addWidget(self.label_48)

        self.min_quiality_inp_3 = QTextEdit(self.frame_35)
        self.min_quiality_inp_3.setObjectName(u"min_quiality_inp_3")
        self.min_quiality_inp_3.setMaximumSize(QSize(100, 50))

        self.horizontalLayout_25.addWidget(self.min_quiality_inp_3)

        self.label_49 = QLabel(self.frame_35)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_25.addWidget(self.label_49)


        self.verticalLayout_16.addWidget(self.frame_35)


        self.verticalLayout_18.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.score_page)

        self.verticalLayout_17.addWidget(self.stackedWidget, 0, Qt.AlignTop)


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
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1784, 298))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../baddots_Moment.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.widget)


        self.verticalLayout_13.addWidget(self.frame)

        self.frame_2 = QFrame(self.control_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFocusPolicy(Qt.NoFocus)
        self.frame_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_2.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-width: 2;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_20.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)


        self.verticalLayout_20.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_20.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_21.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_21.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_21.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_21.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_21.addWidget(self.label_17)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_13.addWidget(self.frame_2)

        self.stackedWidget_2.addWidget(self.control_page)
        self.calibration_page = QWidget()
        self.calibration_page.setObjectName(u"calibration_page")
        self.verticalLayout_14 = QVBoxLayout(self.calibration_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_11 = QFrame(self.calibration_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 70, 131, 81))
        self.graphicsView = QGraphicsView(self.frame_11)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(270, 30, 256, 192))

        self.verticalLayout_14.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.calibration_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_23.addWidget(self.label_4)


        self.verticalLayout_22.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 20, 49, 16))
        self.textEdit = QTextEdit(self.frame_13)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 10, 51, 31))
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(130, 20, 16, 16))
        self.textEdit_2 = QTextEdit(self.frame_13)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(70, 50, 51, 31))
        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 60, 49, 16))
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(130, 60, 16, 16))

        self.verticalLayout_22.addWidget(self.frame_13)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.stackedWidget_2.addWidget(self.calibration_page)

        self.verticalLayout_12.addWidget(self.stackedWidget_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_pages_2)


        self.verticalLayout.addWidget(self.Content, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.control_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430", None))
        self.calibration_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.score_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430", None))
        self.connection_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IP \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u043a\u0430\u0434\u0440\u0430\u043c\u0438", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0433\u043d\u0430\u043b \u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u043e \u0441\u044a\u0451\u043c\u043a\u0438, \u043f\u0438\u043d \u2116", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440  \u00b1", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0432\u0438\u0437\u043d\u0430 \u00b1", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u043a\u0438", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0440\u0435\u0437\u043e\u0432", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"41-43 \u043c\u043c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0432\u0438\u0437\u043d\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"R = 3 \u043c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0432\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"K = 0.8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0444\u0435\u043a\u0442\u044b", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"10 \u0448\u0442", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"90%", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"80%", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e: 90%", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u044b\u0441\u043e\u0442\u0443", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0442\u043e\u0447\u043a\u0435 A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043c", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0442\u043e\u0447\u043a\u0435 B", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u043c\u043c", None))
    # retranslateUi

