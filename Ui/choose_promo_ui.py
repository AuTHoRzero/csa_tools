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


class Ui_Choose_promo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(350, 242)
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = MainWindow.frameGeometry()
        qr.moveCenter(center)
        MainWindow.move(qr.topLeft())
        MainWindow.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(qstyle)
        self.bonus_night = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bonus_night.setGeometry(QtCore.QRect(40, 30, 270, 30))
        self.bonus_night.setStyleSheet("border-radius: 15px;\n"
"border: 1.5px solid black;\n"
"color: black;\n"
"background-color: rgb(245,232,50)")
        self.bonus_night.setObjectName("bonus_night")
        self.five_new_users = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five_new_users.setGeometry(QtCore.QRect(40, 80, 270, 30))
        self.five_new_users.setStyleSheet("border-radius: 15px;\n"
"border: 1.5px solid black;\n"
"color: black;\n"
"background-color: rgb(245,232,50)")
        self.five_new_users.setObjectName("five_new_users")
        self.abonements = QtWidgets.QPushButton(parent=self.centralwidget)
        self.abonements.setGeometry(QtCore.QRect(40, 130, 270, 30))
        self.abonements.setStyleSheet("border-radius: 15px;\n"
"border: 1.5px solid black;\n"
"color: black;\n"
"background-color: rgb(245,232,50)")
        self.abonements.setObjectName("abonements")
        self.back_to_menu_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_to_menu_btn.setGeometry(QtCore.QRect(40, 180, 270, 30))
        self.back_to_menu_btn.setStyleSheet("border-radius: 15px;\n"
"border: 1.5px solid black;\n"
"color: black;\n"
"background-color: rgb(245,232,50)")
        self.back_to_menu_btn.setObjectName("back_to_menu_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bonus_night.setText(_translate("MainWindow", "6-я ночь в подарок"))
        self.five_new_users.setText(_translate("MainWindow", "5 новых пользователей"))
        self.abonements.setText(_translate("MainWindow", "Абонементы"))
        self.back_to_menu_btn.setText(_translate("MainWindow", "В меню"))
