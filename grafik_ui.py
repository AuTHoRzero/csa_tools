# Form implementation generated from reading ui file '/home/author/Bar_bot/Ignore/grafik.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import telebot
import datetime
import sqlite3
import configparser
import os, time
import hashlib

from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
import sys
from PyQt6 import QtCore, QtGui, QtWidgets




############
##Database##
############

users_db = sqlite3.connect('users.db')
conn = sqlite3.connect('CIS_admin_helper.db')
usr = users_db.cursor()
cur = conn.cursor()
usr.execute('CREATE TABLE IF NOT EXISTS users(login TEXT, password TEXT, name TEXT, surname TEXT, post TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS inventory(date TEXT, admin TEXT, itog TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS admin_bar(date TEXT, admin TEXT, position TEXT, value FLOAT, cost FLOAT)')
cur.execute('CREATE TABLE IF NOT EXISTS admins(name TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS positions (name TEXT, price FLOAT)')
cur.execute('CREATE TABLE IF NOT EXISTS config (parameter TEXT, value TEXT)')

with open('style.css', 'r') as r:
    style = r.read()

with open ("style.qss", 'r') as st:
            qstyle = st.read()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 672)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 951, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(21)
        usr.execute('SELECT * FROM users')
        users = usr.fetchall()
        i = 0
        for user in users:
             i += 1
        self.tableWidget.setRowCount(i)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Смен')
        self.tableWidget.setHorizontalHeaderItem(17,item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        item = QtWidgets.QTableWidgetItem()
        item.setText('За смены')
        self.tableWidget.setHorizontalHeaderItem(18,item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Штрафы')
        self.tableWidget.setHorizontalHeaderItem(19,item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Премии')
        self.tableWidget.setHorizontalHeaderItem(20,item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Итог')
        self.tableWidget.setHorizontalHeaderItem(21,item)

        i = 0
        day = 26
        for i in range(16):
            object = QtWidgets.QTableWidgetItem()
            object.setText(str(day))
            if day == 31:
                day = 0
            day += 1
            self.tableWidget.setHorizontalHeaderItem(i,object)
        i = 0
        for user in users:
             object = QtWidgets.QTableWidgetItem()
             object.setText(f'{user[2]} {user[3]}')
             self.tableWidget.setVerticalHeaderItem(i, object)
             i += 1
        self.tableWidget.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(21)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        



if __name__ == "__main__":
    import sys
    path = 'settings.ini'
    app = QtWidgets.QApplication(sys.argv)
    

    #################
    ##Основное окно##
    #################
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec())