
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

class Ui_Inv_history(object):
    def setupUi(self, Inv_history):
        Inv_history.setObjectName("Inv_history")
        Inv_history.setFixedSize(400, 800)
        Inv_history.setStyleSheet("QMainWindow{background-image: url(background.png);\nbackground-position: absolute;}")
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = Inv_history.frameGeometry()
        qr.moveCenter(center)
        Inv_history.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(parent=Inv_history)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 750, 111, 25))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.to_menu)
        self.back.setStyleSheet(style)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 350, 711))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: black;\ncolor: white;")
        Inv_history.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Inv_history)
        self.statusbar.setObjectName("statusbar")
        Inv_history.setStatusBar(self.statusbar)

        self.retranslateUi(Inv_history)
        QtCore.QMetaObject.connectSlotsByName(Inv_history)

    def retranslateUi(self, Inv_history):
        _translate = QtCore.QCoreApplication.translate
        Inv_history.setWindowTitle(_translate("Inv_history", "История инвентаризаций"))
        self.back.setText(_translate("Inv_history", "Назад"))