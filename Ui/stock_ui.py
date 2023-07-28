
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainterPath

with open('style.css', 'r') as r:
    style = r.read()

with open ("style.qss", 'r') as st:
            qstyle = st.read()









class Ui_Stock(object):
    def setupUi(self, Stock):
        Stock.setObjectName("Stock")
        Stock.setFixedSize(520, 820)
        Stock.setWindowTitle("Склад")
        Stock.setWindowOpacity(1)
        Stock.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True )
        Stock.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        Stock.setStyleSheet(style)
        qr = Stock.frameGeometry()
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(center)
        Stock.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(parent=Stock)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('#centralwidget{background-image: url(background_.png);\nbackground-position: center;\nborder-radius: 15px}')
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 491, 701))
        self.scrollArea.setObjectName("scroll_area_stock")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setStyleSheet('background-color: black;\ncolor: white;')
        self.grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.to_menu_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.to_menu_btn.setGeometry(QtCore.QRect(10, 770, 90, 30))
        self.to_menu_btn.setObjectName("to_menu_btn")
        self.confirm_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(410, 770, 90, 30))
        self.confirm_btn.setObjectName("confirm_btn")
        self.Stock_big_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Stock_big_label.setGeometry(QtCore.QRect(10, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Stock_big_label.setFont(font)
        self.Stock_big_label.setObjectName("Stock_big_label")
        Stock.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stock)
        QtCore.QMetaObject.connectSlotsByName(Stock)

    def retranslateUi(self, Stock):
        _translate = QtCore.QCoreApplication.translate
        self.to_menu_btn.setText(_translate("Stock", "Назад"))
        self.confirm_btn.setText(_translate("Stock", "Применить"))
        self.Stock_big_label.setText(_translate("Stock", "Склад:"))