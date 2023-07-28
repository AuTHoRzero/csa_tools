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



class Ui_settings(object):
    def setupUi(self, settings):
        settings.setWindowIcon(QtGui.QIcon("icon/colizeum_logo.ico"))
        settings.setObjectName("settings")
        settings.setFixedSize(850, 900)
        settings.setStyleSheet("QMainWindow{background-image: url(background.png);\nbackground-position: absolute;}")
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = settings.frameGeometry()
        qr.moveCenter(center)
        settings.move(qr.topLeft())
        self.centralwidget = QtWidgets.QWidget(parent=settings)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(style)

        self.telegram_menu_label_big = QtWidgets.QLabel(self.centralwidget)
        self.telegram_menu_label_big.setText('Меню настроек Telegram:')
        self.telegram_menu_label_big.setGeometry(QtCore.QRect(10,10,250,80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.telegram_menu_label_big.setFont(font)


        ########################
        ##Текст ошибка позиция##
        ########################
        self.error_position_label =QtWidgets.QLabel(parent=self.centralwidget)
        self.error_position_label.setVisible(False)
        self.error_position_label.setGeometry(670,450,61,21)
        self.error_position_label.setText('Ошибка')
        self.error_position_label.setStyleSheet("color: rgb(192, 28, 40);")

        self.item_list = QtWidgets.QLabel(parent=self.centralwidget)
        self.item_list.setGeometry(QtCore.QRect(20, 330, 251, 17))
        self.item_list.setObjectName("item_list")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 360, 491, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        ###########################
        ##Список с позициями бара##
        ###########################
        self.list_item_widget = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        self.list_item_widget.setObjectName("list_item_widget")
        self.verticalLayout_2.addWidget(self.list_item_widget)


        ##################################
        ##Наименование выбранной позиции##
        ##################################
        self.name_item_label = QtWidgets.QLabel(self.centralwidget)
        self.name_item_label.setVisible(False)
        self.name_item_label.setObjectName("name_item_label")
        self.name_item_label.setGeometry(QtCore.QRect(520, 480, 220, 40))
        ###########################
        ##Кнопка удаления позиции##
        ###########################
        self.delete_item_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_item_btn.setVisible(False)
        self.delete_item_btn.setStyleSheet("QPushButton{background-color: rgb(35, 35, 35);\n"
"color: rgb(192, 28, 40);}\
    QPushButton::hover{\
    background-color: rgb(63,63,63)\
    }")
        self.delete_item_btn.setGeometry(QtCore.QRect(740, 490, 80, 25))
        self.delete_item_btn.setObjectName("delete_item_btn")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(530, 360, 291, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.item_name_label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.item_name_label.setObjectName("item_name_label")
        self.gridLayout.addWidget(self.item_name_label, 0, 0, 1, 1)
        self.SpinBox = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.SpinBox.setMaximum(99999999.0)
        self.SpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.SpinBox, 1, 1, 1, 1)
        self.Item_name_field = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.Item_name_field.setObjectName("Item_name_field")
        self.gridLayout.addWidget(self.Item_name_field, 0, 1, 1, 1)

        ###Стоимость позиции
        self.item_cost_label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.item_cost_label.setObjectName("item_cost_label")
        self.gridLayout.addWidget(self.item_cost_label, 1, 0, 1, 1)

        ###Кнопка добавить позицию бара
        self.add_item_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_item_btn.setEnabled(False)
        self.add_item_btn.setGeometry(QtCore.QRect(740, 450, 80, 25))
        self.add_item_btn.setStyleSheet("QPushButton{background-color: rgb(35, 35, 35);\n"
"color: rgb(69, 186, 4);}\
    QPushButton::hover{\
    background-color: rgb(63,63,63)\
    }")
        self.add_item_btn.setObjectName("add_item_btn")

        ##Кнопка назад
        self.to_menu_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.to_menu_btn.setGeometry(QtCore.QRect(20, 840, 121, 25))
        self.to_menu_btn.setObjectName("to_menu_btn")
        self.to_menu_btn.setStyleSheet(style)


        self.api_label = QtWidgets.QLabel(self.centralwidget)
        self.api_label.setGeometry(QtCore.QRect(10, 80, 160,25))
        self.api_label.setText('Введите API ключ: ')

        self.api_label.setStyleSheet(style)
        self.api_field = QtWidgets.QLineEdit(self.centralwidget)
        self.api_field.setGeometry(QtCore.QRect(170,80, 480,30))
        self.api_field.setStyleSheet('font-size: 13px')
        
        ##########################
        ##Меню настроек телеграм##
        ##########################
        self.user_id_label = QtWidgets.QLabel(self.centralwidget)
        self.user_id_label.setText('Введите user_ID:')
        self.user_id_label.setGeometry(QtCore.QRect(10, 130, 160, 30))

        self.user_id_field = QtWidgets.QLineEdit(self.centralwidget)
        self.user_id_field.setGeometry(QtCore.QRect(170, 130, 480, 30))


        self.user_id_btn = QtWidgets.QPushButton(self.centralwidget)
        self.user_id_btn.setText('Сохранить')
        self.user_id_btn.setGeometry(QtCore.QRect(690, 130, 100, 25))

        self.saved_user_id_label = QtWidgets.QLabel(self.centralwidget)
        self.saved_user_id_label.setGeometry(QtCore.QRect(690,110,100,25))
        self.saved_user_id_label.setStyleSheet('color: green')
        self.saved_user_id_label.setText('Сохранено')
        self.saved_user_id_label.setVisible(False)

        self.api_btn = QtWidgets.QPushButton(self.centralwidget)
        self.api_btn.setGeometry(QtCore.QRect(690,80,100,25))
        self.api_btn.setText('Сохранить')

        self.saved_api_label = QtWidgets.QLabel(self.centralwidget)
        self.saved_api_label.setGeometry(QtCore.QRect(690,60,100,25))
        self.saved_api_label.setStyleSheet('color: green')
        self.saved_api_label.setText('Сохранено')
        self.saved_api_label.setVisible(False)

        self.next_setting_page = QtWidgets.QPushButton(self.centralwidget)
        self.next_setting_page.setGeometry(QtCore.QRect(720,840,100,25))
        self.next_setting_page.setText('Далее')


        settings.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=settings)
        self.statusbar.setObjectName("statusbar")
        settings.setStatusBar(self.statusbar)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Настройки"))
#        self.list_admins_label.setText(_translate("settings", "Выберите админа из списка"))
#        self.name_admin_label.setText(_translate("settings", "Имя"))
#        self.del_admin_btn.setText(_translate("settings", "Удалить"))
#        self.add_admin_label.setText(_translate("settings", "Добавить админа"))
#        self.Name_add_admin.setText(_translate("settings", "Имя:"))
#        self.add_admin_btn.setText(_translate("settings", "Добавить"))
        self.item_list.setText(_translate("settings", "Выберите товар из списка"))
        self.name_item_label.setText(_translate("settings", "Позиция"))
        self.delete_item_btn.setText(_translate("settings", "Удалить"))
        self.item_name_label.setText(_translate("settings", "Наименование"))
        self.item_cost_label.setText(_translate("settings", "Цена"))
        self.add_item_btn.setText(_translate("settings", "Добавить"))
        self.to_menu_btn.setText(_translate("settings", "Назад"))

