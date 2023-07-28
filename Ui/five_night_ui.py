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

class Ui_six_night(object):
    def setupUi(self, six_night):
        six_night.setObjectName("six_night")
        six_night.resize(569, 222)
        six_night.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        six_night.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        six_night.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True )
        six_night.setStyleSheet(style)
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = six_night.frameGeometry()
        qr.moveCenter(center)
        six_night.move(qr.topLeft())
        
        self.centralwidget = QtWidgets.QWidget(parent=six_night)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(qstyle)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 40, 371, 25))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setCurrentText('')
       
        
        self.enter_num_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.enter_num_label.setGeometry(QtCore.QRect(20, 40, 111, 21))
        self.enter_num_label.setObjectName("enter_num_label")
        self.nights_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.nights_label.setGeometry(QtCore.QRect(20, 90, 120, 20))
        self.nights_label.setObjectName("nights_label")
        self.nights_value_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.nights_value_label.setGeometry(QtCore.QRect(170, 90, 60, 20))
        self.nights_value_label.setObjectName("nights_value_label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 90, 115, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        six_night.setCentralWidget(self.centralwidget)

        self.retranslateUi(six_night)
        QtCore.QMetaObject.connectSlotsByName(six_night)

    def retranslateUi(self, six_night):
        _translate = QtCore.QCoreApplication.translate
        six_night.setWindowTitle(_translate("six_night", "6-я ночь в подарок"))
        self.enter_num_label.setText(_translate("six_night", "Введите номер:"))
        self.nights_label.setText(_translate("six_night", "Кол-во ночей:"))
        self.nights_value_label.setText(_translate("six_night", "0"))
        self.pushButton.setText(_translate("six_night", "Добавить"))
        self.pushButton_2.setText(_translate("six_night", "Назад"))