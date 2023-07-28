
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








class Ui_Settings_second(object):
    def setupUi(self, Settings_second):
        Settings_second.setWindowIcon(QtGui.QIcon("icon/colizeum_logo.ico"))
        Settings_second.setObjectName("Settings_second")
        Settings_second.setFixedSize(742, 780)
        Settings_second.setStyleSheet("QMainWindow{background-image: url(background.png);\nbackground-position: absolute;}")
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = Settings_second.frameGeometry()
        qr.moveCenter(center)
        Settings_second.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(parent=Settings_second)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(style)

        self.Bar_admin_big_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Bar_admin_big_label.setGeometry(QtCore.QRect(10, 60, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Bar_admin_big_label.setFont(font)
        self.Bar_admin_big_label.setObjectName("Bar_admin_big_label")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(10,22,151,21))
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setGeometry(QtCore.QRect(170,20,81,26))
        self.set_discount_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.set_discount_btn.setObjectName("pushButton_2")
        self.set_discount_btn.setGeometry(QtCore.QRect(260,20,190,25))
        self.position_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.position_label.setGeometry(QtCore.QRect(10, 120, 131, 21))
        self.position_label.setObjectName("position_label")

        self.all_position_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.all_position_list.setGeometry(QtCore.QRect(10, 150, 511, 201))
        self.all_position_list.setObjectName("all_position_list")

        self.search_admin_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.search_admin_label.setGeometry(QtCore.QRect(10, 370, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.search_admin_label.setFont(font)
        self.search_admin_label.setObjectName("search_admin_label")
        self.admin_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.admin_name_label.setGeometry(QtCore.QRect(15, 410, 101, 21))
        self.admin_name_label.setObjectName("admin_name_label")
        self.admin_name_combo_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.admin_name_combo_box.setGeometry(QtCore.QRect(110, 410, 220, 25))
        self.admin_name_combo_box.setObjectName("admin_name_combo_box")

#        self.confirm_admin_btn = QtWidgets.QPushButton(self.centralwidget)
#        self.confirm_admin_btn.setStyleSheet(style)
#        self.confirm_admin_btn.setGeometry(QtCore.QRect(240, 410, 100, 25))
#        self.confirm_admin_btn.setText('Подтвердить')

        ###################################
        ##Лист с поизициями одного админа##
        ###################################
        self.admin_positions_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.admin_positions_list.setGeometry(QtCore.QRect(10, 440, 341, 251))
        self.admin_positions_list.setObjectName("admin_positions_list")

        self.summ_bar_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.summ_bar_label.setGeometry(QtCore.QRect(360, 450, 151, 17))
        self.summ_bar_label.setObjectName("summ_bar_label")
        self.label_bar_admin = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bar_admin.setGeometry(QtCore.QRect(640, 450, 71, 16))
        self.label_bar_admin.setObjectName("label_bar_admin")
        self.summ_with_sale_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.summ_with_sale_label.setGeometry(QtCore.QRect(360, 480, 151, 17))
        self.summ_with_sale_label.setObjectName("summ_with_sale_label")
        self.label_bar_sale = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bar_sale.setGeometry(QtCore.QRect(640, 480, 81, 17))
        self.label_bar_sale.setObjectName("label_bar_sale")

        self.delete_all_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_all_btn.setGeometry(QtCore.QRect(530, 160, 191, 41))
        self.delete_all_btn.setObjectName("delete_all_btn")
        self.delete_all_btn.setStyleSheet(style)

        ##############################################
        ##Удаление одной позиции из списка по админу##
        ##############################################
        self.delete_tovar_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_tovar_btn.setGeometry(QtCore.QRect(550, 560, 121, 31))
        self.delete_tovar_btn.setObjectName("delete_tovar_btn")
        self.delete_tovar_btn.setStyleSheet("QPushButton{background-color: rgb(35, 35, 35);\n"
"color: rgb(192, 28, 40);}\
    QPushButton::hover{\
    background-color: rgb(63,63,63)\
    }")
        self.delete_tovar_btn.setVisible(False)


        ##############################################
        ##Выбранная позиция по списку администратора##
        ##############################################
        self.tovar_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.tovar_name_label.setGeometry(QtCore.QRect(360, 530, 181, 81))
        self.tovar_name_label.setObjectName("tovar_name_label")
        self.tovar_name_label.setVisible(False)

        self.delete_all_from_admin_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_all_from_admin_btn.setGeometry(QtCore.QRect(370, 654, 311, 31))
        self.delete_all_from_admin_btn.setObjectName("delete_all_from_admin_btn")

        
        ################################################
        ##Название выделенной позиции из общего списка##
        ################################################
        self.position_from_all_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.position_from_all_label.setGeometry(QtCore.QRect(530, 206, 141, 100))
        self.position_from_all_label.setObjectName("position_from_all_label")
        self.position_from_all_label.setVisible(False)

        ############################################
        ##Кнопка удаления позиции из общего списка##
        ############################################
        self.delete_from_all_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_from_all_btn.setGeometry(QtCore.QRect(530, 320, 200, 25))
        self.delete_from_all_btn.setObjectName("delete_from_all_btn")
        self.delete_from_all_btn.setStyleSheet("QPushButton{background-color: rgb(35, 35, 35);\n"
"color: rgb(192, 28, 40);}\
    QPushButton::hover{\
    background-color: rgb(63,63,63)\
    }")
        self.delete_from_all_btn.setVisible(False)


        ################
        ##Кнопка назад##
        ################
        self.back_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(10, 720, 101, 31))
        self.back_btn.setObjectName("back_btn")
        Settings_second.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(parent=Settings_second)
        self.statusbar.setObjectName("statusbar")
        Settings_second.setStatusBar(self.statusbar)

        self.retranslateUi(Settings_second)
        QtCore.QMetaObject.connectSlotsByName(Settings_second)

    def retranslateUi(self, Settings_second):
        _translate = QtCore.QCoreApplication.translate
        Settings_second.setWindowTitle(_translate("Settings_second", "Настройки"))
        self.Bar_admin_big_label.setText(_translate("Settings_second", "Бар администратор:"))
        self.label_4.setText(_translate("Settings_second", "Размер скидки ( в %):"))
        self.set_discount_btn.setText(_translate("Settings_second", "Применить"))
        self.position_label.setText(_translate("Settings_second", "Взятые позиции:"))
        self.search_admin_label.setText(_translate("Settings_second", "Поиск по админу:"))
        self.admin_name_label.setText(_translate("Settings_second", "Имя админа:"))
        self.summ_bar_label.setText(_translate("Settings_second", "Сумма взятого бара:"))
        self.label_bar_admin.setText(_translate("Settings_second", "0 ₽"))
        self.summ_with_sale_label.setText(_translate("Settings_second", "Сумма со скидкой:"))
        self.label_bar_sale.setText(_translate("Settings_second", "0 ₽"))
        self.delete_all_btn.setText(_translate("Settings_second", "Стереть все записи"))
        self.delete_tovar_btn.setText(_translate("Settings_second", "Стереть запись"))
        self.tovar_name_label.setText(_translate("Settings_second", "Товар"))
        self.delete_all_from_admin_btn.setText(_translate("Settings_second", "Стереть все записи по админу"))
        self.position_from_all_label.setText(_translate("Settings_second", "Запись"))
        self.delete_from_all_btn.setText(_translate("Settings_second", "Стереть"))
        self.back_btn.setText(_translate("Settings_second", "Назад"))