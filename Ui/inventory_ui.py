
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainterPath

with open('style.css', 'r') as file:
    style = file.read()
with open('style.qss', 'r') as file:
    qstyle = file.read()


class Inventory(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon("icon/colizeum_logo.ico"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(950, 797)
        MainWindow.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True )
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = MainWindow.frameGeometry()
        qr.moveCenter(center)
        MainWindow.move(qr.topLeft())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{background-image: url(background.png);\nbackground-position: absolute;}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet(style)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(qstyle)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 720, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(style)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 720, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(style)
        self.in_prog_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.in_prog_label.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.in_prog_label.setStyleSheet('color:white')
        font = QtGui.QFont()
        font.setPointSize(18)
        self.in_prog_label.setFont(font)
        self.in_prog_label.setObjectName("in_prog_label")
        self.at_club_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.at_club_label.setGeometry(QtCore.QRect(340, 20, 131, 41))
        self.at_club_label.setStyleSheet('color:white')

        ########################
        ##Текст в холодильнике##
        ########################
        self.at_fridge_label = QtWidgets.QLabel(self.centralwidget)
        self.at_fridge_label.setGeometry(QtCore.QRect(660, 20, 190, 40))
        self.at_fridge_label.setText('В холодильнике:')
        self.at_fridge_label.setFont(font)
        
        #############################
        ##Заполнение в холодильнике##
        #############################
        self.at_fridge_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.at_fridge_scroll.setGeometry(QtCore.QRect(660,70,250,540))
        self.at_fridge_scroll.setWidgetResizable(True)
        self.at_fridge_widget = QtWidgets.QWidget()
        self.at_fridge_widget.setGeometry(QtCore.QRect(0, 0, 248, 538))
        self.at_fridge_widget.setStyleSheet("background-color: rgb(45,45,45);\ncolor: white;\nborder-color: rgb(245, 232, 50);")
        self.grid_fridge = QtWidgets.QGridLayout(self.at_fridge_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.at_club_label.setFont(font)
        self.at_club_label.setObjectName("at_club_label")
        self.at_club_label.setStyleSheet('color:white')
        self.label_name_admin = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name_admin.setGeometry(QtCore.QRect(20, 650, 181, 31))
        self.label_name_admin.setObjectName("label_name_admin")
        self.label_name_admin.setStyleSheet('color: white')
        font_admin = QtGui.QFont()
        font_admin.setBold(True)
        font_admin.setPointSize(12)
        self.label_name_admin.setFont(font_admin)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 250, 540))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.content_widget = QtWidgets.QWidget()
        self.content_widget.setGeometry(QtCore.QRect(0, 0, 248, 538))
        self.content_widget.setObjectName("content_widget")
        self.content_widget.setStyleSheet("background-color: rgb(45,45,45);\ncolor: white;\nborder-color: rgb(245, 232, 50);")
        self.grid = QtWidgets.QGridLayout(self.content_widget)
        self.label_1 = QtWidgets.QLabel('Label')
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(340, 70, 250, 540))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.content_widget_1 = QtWidgets.QWidget()
        self.content_widget_1.setGeometry(QtCore.QRect(0, 0, 248, 538))
        self.content_widget_1.setObjectName("content_widget_1")
        self.content_widget_1.setStyleSheet("background-color: rgb(45,45,45);\ncolor: white;")
        self.grid_1 = QtWidgets.QGridLayout(self.content_widget_1)
        self.send_label = QtWidgets.QLabel(self.centralwidget)
        self.send_label.setGeometry(QtCore.QRect(840,695,90,20))
        self.send_label.setStyleSheet('color: green;')
        self.send_label.setObjectName('send_label')
        self.send_label.setVisible(False)
        self.current_admin = QtWidgets.QLabel(parent=self.centralwidget)
        self.current_admin.setGeometry(QtCore.QRect(210, 650, 201, 31))
        self.current_admin.setObjectName("current_admin")
        font_admin.setUnderline(True)
        self.current_admin.setFont(font_admin)
        self.current_admin.setStyleSheet('color: rgb(245, 232, 50);')
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Инвентаризация"))
        self.send_label.setText(_translate('MainWindow', "Отправлено"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
        self.pushButton_2.setText(_translate("MainWindow", "Отправить"))
        self.in_prog_label.setText(_translate("MainWindow", "В проге:"))
        self.at_club_label.setText(_translate("MainWindow", "На складе:"))
        self.label_name_admin.setText(_translate("MainWindow", "Имя администратора:"))