# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowSjjklI.ui'
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
        MainWindow.resize(770, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu = QFrame(self.centralwidget)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Menu.setFrameShape(QFrame.NoFrame)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Menu)
        self.horizontalLayout_3.setSpacing(0)
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
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget_2 = QStackedWidget(self.frame_pages_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.label_22 = QLabel(self.start_page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 20, 91, 31))
        self.label_23 = QLabel(self.start_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 60, 91, 31))
        self.label_24 = QLabel(self.start_page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 110, 161, 31))
        self.label_25 = QLabel(self.start_page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 160, 181, 31))
        self.textEdit_3 = QTextEdit(self.start_page)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(90, 60, 181, 31))
        self.textEdit_4 = QTextEdit(self.start_page)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(190, 110, 81, 31))
        self.textEdit_5 = QTextEdit(self.start_page)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(210, 160, 61, 31))
        self.stackedWidget_2.addWidget(self.start_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_26 = QLabel(self.settings_page)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 20, 111, 20))
        self.textEdit_6 = QTextEdit(self.settings_page)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(150, 20, 41, 31))
        self.label_27 = QLabel(self.settings_page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 70, 131, 31))
        self.textEdit_7 = QTextEdit(self.settings_page)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(150, 70, 41, 31))
        self.label_28 = QLabel(self.settings_page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 160, 81, 21))
        self.label_29 = QLabel(self.settings_page)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(60, 200, 61, 21))
        self.label_30 = QLabel(self.settings_page)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(60, 240, 61, 21))
        self.textEdit_8 = QTextEdit(self.settings_page)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(130, 190, 41, 31))
        self.textEdit_9 = QTextEdit(self.settings_page)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(130, 230, 41, 31))
        self.label_31 = QLabel(self.settings_page)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(180, 200, 21, 16))
        self.label_32 = QLabel(self.settings_page)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(180, 240, 21, 16))
        self.label_33 = QLabel(self.settings_page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(200, 80, 16, 16))
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 710, 326))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)


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

        self.verticalLayout_12.addWidget(self.stackedWidget_2)


        self.horizontalLayout_4.addWidget(self.frame_pages_2)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.control_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0430", None))
        self.calibration_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IP \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u043a\u0430\u0434\u0440\u0430\u043c\u0438", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0433\u043d\u0430\u043b \u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u043e \u0441\u044a\u0451\u043c\u043a\u0438, \u043f\u0438\u043d \u2116", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0440\u0435\u0437\u043e\u0432", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u043a\u0438", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440  \u00b1", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0432\u0438\u0437\u043d\u0430 \u00b1", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"%", None))
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

