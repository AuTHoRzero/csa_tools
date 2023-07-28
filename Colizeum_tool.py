import typing
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
from PyQt6.QtGui import QPainterPath

from Ui.main_menu_ui import Ui_Main_Menu
from Ui.Authorize_ui import Ui_Authorization_window
from Ui.Admin_bar_ui import Ui_Bar
from Ui.inventory_ui import Inventory
from Ui.inv_history_ui import Ui_Inv_history
from Ui.settiing_first_ui import Ui_settings
from Ui.settings_second_ui import Ui_Settings_second
from Ui.manager_menu_ui import Ui_Manager_menu
from Ui.add_user_ui import Ui_AddUser
from Ui.stock_ui import Ui_Stock
from Ui.choose_promo_ui import Ui_Choose_promo
from Ui.five_night_ui import Ui_six_night


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
promo_db = sqlite3.connect('promotion.db')
cur_promo = promo_db.cursor()
cur_promo.execute('CREATE TABLE IF NOT EXISTS users (number TEXT, nights INTEGER, friends INTEGER)')
cur_promo.execute('CREATE TABLE IF NOT EXISTS abonement_one (number TEXT, abonement TEXT, packs INTEGER)')
cur_promo.execute('CREATE TABLE IF NOT EXISTS abonement_two (number TEXT, abonement TEXT, packs INTEGER)')

try:
    cur.execute('ALTER TABLE positions ADD at_stock INTEGER')
except:
    pass

with open('style.css', 'r') as r:
    style = r.read()

with open ("style.qss", 'r') as st:
            qstyle = st.read()
##########
##Config##
##########
def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.add_section("Active_user")
    with open (path, 'w') as config_file:
        config.write(config_file)

def config_add_user_id(path, user_id):
    if not os.path.exists(path):
        create_config(path)
    
    config = configparser.ConfigParser()
    config.read(path)
    config.set('Settings', 'USER_ID', user_id)
    with open(path, "w") as config_file:
        config.write(config_file)

def add_api(path, api):
    if not os.path.exists(path):
        create_config(path)
    
    config = configparser.ConfigParser()
    config.read(path)
    config.set('Settings', 'API', api)
    with open(path, "w") as config_file:
        config.write(config_file)

def add_password(path, password):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    passwrd = hashlib.md5(password.encode())
    passwrd = passwrd.hexdigest()
    config.set('Settings', 'MANAGER_PASSOWRD', passwrd)
    with open(path, "w") as config_file:
        config.write(config_file)

def config_set_discount(path, discount):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    config.set('Settings', 'DISCOUNT', discount)
    with open(path, "w") as config_file:
        config.write(config_file)
    
def config_get_value(path, header, setting):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    value = config.get(header, setting)
    return value

def config_is_first(path):
    if not os.path.exists(path):
        create_config(path)
    try:
        config_get_value(path, 'Settings', 'is_first')
    except:
        config = configparser.ConfigParser()
        config.read(path)
        config.set('Settings', 'is_first', 'False')
        with open(path, "w") as config_file:
            config.write(config_file)

def config_not_first(path):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    config.set('Settings', 'is_first', 'True')
    with open(path, "w") as config_file:
        config.write(config_file)

def config_active_user(path, user):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    config.set('Active_user', 'user', user)
    with open(path, "w") as config_file:
        config.write(config_file)






class Authorize(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Authorization_window()
        self.ui.setupUi(self)
        self.show()
        self.ui.close_btn.clicked.connect(self.exit)
        self.ui.password_field.returnPressed.connect(self.authorize)
        self.ui.etner_btn.clicked.connect(self.authorize)
    def exit(self):
        self.close()

    def authorize(self):
        login = self.ui.login_field.text()
        login = login.lower()
        password = self.ui.password_field.text()
        if password != '':
            password = hashlib.md5(password.encode())
            password = password.hexdigest()
        if login == '':
            self.ui.etner_btn.setObjectName('error_enter_btn')
            self.ui.etner_btn.setStyleSheet(qstyle)
            self.ui.etner_btn.setText("Введите логин")
            QTimer.singleShot(1200,self.btn_normal)
        elif password == '':
            try:
                usr.execute(f'SELECT * FROM users WHERE login = "{login}"')
                all_users = usr.fetchall()
                try:
                    if all_users[0][1] == password:
                        config_active_user(path, all_users[0][0])
                        self.close()
                        main_window.show()
                    else:
                        self.ui.etner_btn.setText("Неверный пароль")
                        self.ui.etner_btn.setObjectName('error_enter_btn')
                        self.ui.etner_btn.setStyleSheet(qstyle)
                        QTimer.singleShot(1200,self.btn_normal)
                except:
                    self.ui.etner_btn.setObjectName('error_enter_btn')
                    self.ui.etner_btn.setStyleSheet(qstyle)
                    self.ui.etner_btn.setGeometry(QtCore.QRect(205,250,200,30))
                    self.ui.etner_btn.setText("Пользователь не найден")
                    QTimer.singleShot(1200, self.btn_normal)
            except:
                self.ui.etner_btn.setObjectName('error_enter_btn')
                self.ui.etner_btn.setStyleSheet(qstyle)
                self.ui.etner_btn.setText("Введите пароль")
                QTimer.singleShot(1200,self.btn_normal)
        else:
            usr.execute(f'SELECT * FROM users WHERE login = "{login}"')
            all_users = usr.fetchall()
            try:
                if all_users[0][1] == password:
                    config_active_user(path, all_users[0][0])
                    self.close()
                    main_window.show()
                else:
                    self.ui.etner_btn.setText("Неверный пароль")
                    self.ui.etner_btn.setObjectName('error_enter_btn')
                    self.ui.etner_btn.setStyleSheet(qstyle)
                    QTimer.singleShot(1200,self.btn_normal)
            except:
                self.ui.etner_btn.setObjectName('error_enter_btn')
                self.ui.etner_btn.setStyleSheet(qstyle)
                self.ui.etner_btn.setGeometry(QtCore.QRect(205,250,200,30))
                self.ui.etner_btn.setText("Пользователь не найден")
                QTimer.singleShot(1200, self.btn_normal)

    def btn_normal(self):
        self.ui.etner_btn.setText('Вход')
        self.ui.etner_btn.setObjectName('enter_btn')
        self.ui.etner_btn.setStyleSheet(qstyle)
        self.ui.etner_btn.setGeometry(QtCore.QRect(230, 250, 151, 31))

    def centralize(self):
        center = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr = self.frameGeometry()
        qr.moveCenter(center)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()
    


class Main_Menu(QMainWindow, Ui_Main_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        username = config_get_value(path, 'Active_user', 'user')
        usr.execute(f'SELECT * FROM users WHERE login = "{username}"')
        user = usr.fetchone()
        self.current_account.setText(f'{user[2]} {user[3]}')
        self.change_acc_btn.clicked.connect(self.change_account)
        self.admin_bar_btn.clicked.connect(lambda: self.change_window(admin_bar_window))
        self.inventory_btn.clicked.connect(lambda: self.change_window(inventory_window))
        self.inv_history_btn.clicked.connect(lambda: self.change_window(inv_history_window))
        self.manager_menu.clicked.connect(lambda: self.change_window(manager_menu_window))
        self.stock_btn.clicked.connect(lambda: self.change_window(stock_window))
        self.promo_btn.clicked.connect(lambda: self.change_window(choose_promo_window))
    
    def change_account(self):
        self.close()
        authorize_window.show()

    def change_window(self, window):
        self.close()
        window.show()

class Admin_bar(QMainWindow, Ui_Bar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def refresh(self):
        self.setupUi(self)
        self.back.clicked.connect(self.to_menu)
        usr.execute('SELECT * FROM users')
        admins = usr.fetchall()
        for admin in admins:
            self.comboBox.addItem(f'{admin[2]} {admin[3]}')
        cur.execute('SELECT * FROM positions')
        result = cur.fetchall()
        self.send.clicked.connect(self.get_result)
        self.sended_label = QtWidgets.QLabel(self.centralwidget)
        self.sended_label.setGeometry(QtCore.QRect(290, 655, 90,20))
        self.sended_label.setText('Отправлено')
        self.sended_label.setStyleSheet('color: green')
        self.sended_label.setVisible(False)
        self.grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        s = 0
        for i in result:
            object_0 = QtWidgets.QLabel(f'{i[0]}')
            object_0.setStyleSheet('color: white;')
            object_1 = QtWidgets.QSpinBox()
            object_1.setMaximum(99999)
            object_1.setStyleSheet(style)
            self.grid.addWidget(object_0,s,0)
            self.grid.addWidget(object_1, s, 1)
            s = s + 1
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh()
        
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()

    def get_result(self):
        self.sended_label.setVisible(True)
        self.send.setDisabled(True)
        self.send.setStyleSheet('color: white;\nbackground: gray;')
        QTimer.singleShot(1500, self.end_send)
        admin_name = self.comboBox.currentText()
        i = 0
        while i < self.grid.rowCount():
            name = self.grid.itemAtPosition(i, 0)
            name = name.widget().text()
            count = self.grid.itemAtPosition(i, 1)
            count = count.widget().value()
            
            today = datetime.datetime.now().strftime('%d.%m.%Y %H:%M.%S')
            if count > 0:
                cur.execute(f'SELECT * FROM positions WHERE name = "{str(name)}"')
                res = cur.fetchall()
                cur.execute(f'INSERT INTO admin_bar VALUES("{today}", "{admin_name}", "{name}", "{count}", "{res[0][1]}")')
                conn.commit()
            self.grid.itemAtPosition(i,1).widget().clear()
            i = i +1


    def end_send(self):
        self.sended_label.setVisible(False)
        self.send.setStyleSheet(style)
        self.send.setDisabled(False)


    def to_menu(self):
        self.close()
        main_window.show()


class Invent(QMainWindow, Inventory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def refresh(self):
        self.setupUi(self)
        try:
            active_user = config_get_value(path, 'Active_user', 'user')
            usr.execute(f'SELECT * FROM users WHERE login = "{active_user}"')
            result = usr.fetchone()
            self.current_admin.setText(f'{result[2]} {result[3]}')
        except:
            pass
        
        self.pushButton.clicked.connect(self.to_menu)

        ##################
        ##В холодильнике##
        ##################
        cur.execute('SELECT * FROM positions')
        result = cur.fetchall()
        self.dic = {}
        s = 0
        for i in result:
            self.dic[str(i)] = QtWidgets.QLabel(f'{i[0]}')
            object_1 = QtWidgets.QSpinBox()
            object_1.setStyleSheet(style)
            object_1.setMaximum(99999)
            self.grid_fridge.addWidget(self.dic[str(i)], s, 0)
            self.grid_fridge.addWidget(object_1, s, 1)
            s = s+1

        self.at_fridge_scroll.setWidget(self.at_fridge_widget)

        ###########
        ##В проге##
        ###########
        cur.execute('SELECT * FROM positions')
        result = cur.fetchall()
        self.dic = {}
        s = 0
        for i in result:
            self.dic[str(i)] = QtWidgets.QLabel(f'{i[0]}')
            object_1 = QtWidgets.QSpinBox()
            object_1.setStyleSheet(style)
            object_1.setMaximum(99999)
            self.grid.addWidget(self.dic[str(i)], s, 0)
            self.grid.addWidget(object_1, s, 1)
            s = s+1
        self.scrollArea.setWidget(self.content_widget)
        #############
        ##На складе##
        #############
        s = 0
        for i in result:
            object_0 = QtWidgets.QLabel(f'{i[0]}')
            object_1 = QtWidgets.QSpinBox()
            object_0.setStyleSheet(style)
            try:
                object_1.setValue(i[2])
            except:
                pass
            object_1.setStyleSheet(style)
            object_1.setMaximum(99999)
            self.grid_1.addWidget(object_0, s, 0)
            self.grid_1.addWidget(object_1, s, 1)
            s = s+1
        self.scrollArea_2.setWidget(self.content_widget_1)

        self.pushButton_2.clicked.connect(self.get_result)


    def showEvent(self, event):
        super().showEvent(event)
        self.refresh()



    def get_result(self):
        admin_name = self.current_admin.text()


        i = 0
        today = datetime.datetime.now()
        date = f'{today.year}-{today.month}-{today.day}'
        self.to_insrt = f'{today.year}-{today.month}-{today.day}\n\n{admin_name}\n\n'
        to_bd = ''

        #############################
        ##Не считать взятое админом##
        #############################
        cur.execute('SELECT * FROM admin_bar')
        result = cur.fetchall()

        while i < self.grid.rowCount():
            name = self.grid.itemAtPosition(i,0)
            name = name.widget().text()
            in_program = self.grid.itemAtPosition(i,1)
            in_program = in_program.widget()

            at_stock = self.grid.itemAtPosition(i,1).widget().value()

            at_club = self.grid_1.itemAtPosition(i,1)
            at_club = at_club.widget()
            in_program_value = in_program.value()
            for item in result:
                if name == item[2]:
                    in_program_value = in_program_value - int(item[3])
            if in_program_value:
                itog = at_club.value() + at_stock - in_program_value
            else:
                itog = at_club.value() + at_stock - in_program.value()
            i = i +1

            self.to_insrt += f'{name}:   {itog}\n'
            to_bd += f'{name}:   {itog}\n'
        cur.execute(f'INSERT INTO inventory VALUES("{date}", "{admin_name}", "{to_bd}")')
        conn.commit()
        self.send_tg()

    def send_tg(self):          #Отправка в телегу
        bot = telebot.TeleBot(config_get_value(path,'Settings', 'api'))
        self.pushButton_2.setDisabled(True)
        self.send_label.setVisible(True)
        self.pushButton_2.setStyleSheet('background: gray;\ncolor: white;')
        QTimer.singleShot(1500, self.deactivate_btn)
        bot.send_message(config_get_value(path, 'Settings', 'USER_ID'), self.to_insrt)

    def deactivate_btn(self):
        self.pushButton_2.setStyleSheet('style')
        self.pushButton_2.setDisabled(False)

    def to_menu(self):
        self.close()
        main_window.show()



class History_inv(QMainWindow, Ui_Inv_history):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        cur.execute('SELECT * FROM inventory')
        result = cur.fetchall()
        l = 0
        for i in result:
            self.textBrowser.insertPlainText(f'{result[l][0]} - {result[l][1]}\n\n{result[l][2]}\n\n')
            l = l+1
        self.back.clicked.connect(self.to_menu)

    def to_menu(self):
        self.close()
        main_window.show()



class Manager_menu(QMainWindow, Ui_Manager_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(lambda: self.change_window(main_window))
        self.settings_btn.clicked.connect(lambda: self.change_window(settings_window))
        self.account_btn.clicked.connect(lambda: self.change_window(add_user_window))

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()





    def change_window(self, window):
        self.close()
        window.show()



class Settings(QMainWindow, Ui_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.to_menu_btn.clicked.connect(lambda: self.change_window(manager_menu_window))
        try:
            self.user_id_field.setText(config_get_value(path,'Settings', 'USER_ID'))
            self.api_field.setText(config_get_value(path,'Settings', 'api'))
        except:
            pass
        cur.execute('SELECT * FROM positions')
        self.items = cur.fetchall()
        for item in self.items:
            self.list_item_widget.addItem(f'{item[0]} | {item[1]}')
        self.list_item_widget.clicked.connect(self.item_clicked)
        self.delete_item_btn.clicked.connect(self.del_item)
        self.Item_name_field.textChanged.connect(self.activate_add_item)
        self.add_item_btn.clicked.connect(self.add_item)
        self.user_id_field.returnPressed.connect(self.add_user_id)
        self.user_id_btn.clicked.connect(self.add_user_id)
        self.api_field.returnPressed.connect(self.set_api)
        self.api_btn.clicked.connect(self.set_api)
        self.next_setting_page.clicked.connect(lambda: self.change_window(second_settings_window))





    def add_user_id(self):
        user_id = self.user_id_field.text()
        config_add_user_id(path, user_id)
        self.saved_user_id_label.setVisible(True)
        QTimer.singleShot(2000, self.hide_label_saved_user_id)
        
    def hide_label_saved_user_id(self):
        self.saved_user_id_label.setVisible(False)
    #####################
    ##Активаторы кнопок##
    #####################
    def activate_add_admin(self):
        self.add_admin_btn.setEnabled(True)

    def activate_add_item(self):
        self.add_item_btn.setEnabled(True)

    def activate_api(self):
        self.api_btn.setEnabled(True)
        self.api_btn.setStyleSheet(style)
        self.saved_api_label.setVisible(False)


    ######################################
    ##Добавление/удаление администратора##
    ######################################
    def add_admin(self):
        self.admin_name = self.add_admin_text_field.text()
        if self.admin_name == '':
            self.error_admin_label.setVisible(True)
        elif self.admin_name == ' ':
            self.error_admin_label.setVisible(True)     
        else:
            cur.execute(f'INSERT INTO admins VALUES("{self.admin_name}")')
            conn.commit()
            self.List_admins_widget.addItem(self.admin_name)
            self.error_admin_label.setVisible(False)
        self.add_admin_text_field.clear()



    def admin_name_clicked(self):
        self.name_admin_label.setVisible(True)
        self.del_admin_btn.setVisible(True)
        name = self.List_admins_widget.currentItem()
        self.name_admin_label.setText(str(name.text()))

    def admin_del(self):
        name = self.List_admins_widget.currentItem()                               #Получаем выбраннй элемент
        el = self.List_admins_widget.indexFromItem(name).row()                     #Получаем его номер
        cur.execute(f'DELETE FROM admins WHERE name LIKE "{str(name.text())}"')    #Закидываем имя в бд
        conn.commit()
        self.List_admins_widget.takeItem(el)                                       #Удаляем из списка
        self.del_admin_btn.setVisible(False)                                       #Офаем кнопку и имя
        self.name_admin_label.setVisible(False)



    def add_item(self):
        item_name = self.Item_name_field.text()
        item_cost = self.SpinBox.value()
        if item_cost == 0:
            self.error_position_label.setVisible(True)
        elif item_name == '' or item_name == ' ':
            self.error_position_label.setVisible(True)
        else:
            cur.execute(f'INSERT INTO positions VALUES("{item_name}", "{item_cost}", "0")')
            conn.commit()
            self.error_position_label.setVisible(False)
            self.list_item_widget.addItem(f'{item_name} | {item_cost}')
        self.Item_name_field.clear()
        self.SpinBox.setValue(0)


    def item_clicked(self):
        item = self.list_item_widget.currentItem()
        self.name_item_label.setText(str(item.text()))
        self.delete_item_btn.setVisible(True)
        self.name_item_label.setVisible(True)

    def del_item(self):
        item = self.list_item_widget.currentItem()
        item_position = self.list_item_widget.indexFromItem(item).row()
        name = str(item.text()).split(" |")[0]
        cur.execute(f'DELETE FROM positions WHERE name = "{name}"')
        conn.commit()
        self.list_item_widget.takeItem(item_position)
        self.delete_item_btn.setVisible(False)
        self.name_item_label.setVisible(False)

    def set_api(self):
        self.saved_api_label.setVisible(True)
        self.api_btn.setStyleSheet('background: gray;\ncolor: white')
        self.api_btn.setEnabled(False)
        QTimer.singleShot(1500, self.activate_api)
        key = self.api_field.text()
        add_api(path, key)

    def change_window(self, window):
        self.close()
        window.show()


class Settings_Second(QMainWindow, Ui_Settings_second):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(lambda: self.change_window(settings_window))
        try:
            discount = config_get_value(path, 'Settings',"discount")
            self.spinBox.setValue(int(discount))
        except:
            pass
        cur.execute('SELECT * FROM admin_bar')
        result = cur.fetchall()
        for item in result:
            self.all_position_list.addItem(f'{item[0]} | {item[1]} | {item[2]} - {int(item[3])}')
        self.all_position_list.clicked.connect(self.selected_from_all_list)
        usr.execute('SELECT * FROM users')
        admins = usr.fetchall()
        for admin in admins:
            self.admin_name_combo_box.addItem(f'{admin[2]} {admin[3]}')
        self.set_discount_btn.clicked.connect(self.set_discount)
#        self.confirm_admin_btn.clicked.connect(self.search_by_admin)
        self.admin_positions_list.clicked.connect(self.selected_by_admin_list)
        self.delete_all_btn.clicked.connect(self.delete_all)
        self.delete_tovar_btn.clicked.connect(self.delete_one_from_by_admin_list)
        self.delete_all_from_admin_btn.clicked.connect(self.delete_by_admin_all)
        self.delete_from_all_btn.clicked.connect(self.delete_one_from_all_list)
        self.admin_name_combo_box.currentTextChanged.connect(self.search_by_admin)



    def set_discount(self):
        value = self.spinBox.value()
        config_set_discount(path, str(value))

    def search_by_admin(self):
        try:
            self.admin_positions_list.clear()
        except:
            pass
        admin_name = self.admin_name_combo_box.currentText()
        cur.execute(f'SELECT * FROM admin_bar WHERE admin = "{admin_name}"')
        results = cur.fetchall()
        summ = 0
        for result in results:
            summ = summ + (result[4] * result[3])
            self.admin_positions_list.addItem(f'{result[0]} | {result[1]} | {int(result[3])} - {result[2]}')
        self.label_bar_admin.setText(f'{int(summ)} ₽')
        discount = int(config_get_value(path,'Settings', 'discount'))
        discount = summ / 100 * (100-discount)
        self.label_bar_sale.setText(f'{int(discount)} ₽')

    def selected_from_all_list(self):
        self.delete_from_all_btn.setVisible(True)
        item = self.all_position_list.currentItem()
        text = item.text().split(' | ')
        self.position_from_all_label.setVisible(True)
        self.position_from_all_label.setText(f'{text[0]}\n{text[1]}\n{text[2]} шт.')

    def delete_all(self):
        i = 0
        count = self.all_position_list.count()
        while i < count:
            self.all_position_list.takeItem(0)
            i = i + 1 
        cur.execute('DELETE FROM admin_bar')
        conn.commit()

    def delete_one_from_all_list(self):
        item = self.all_position_list.currentItem()
        index = self.all_position_list.currentIndex().row()
        item = item.text()
        data = item.split(' | ')
        date, admin = data[0], data[1]
        data = data[2].split(' - ')
        position, count = data[0], data[1]
        cur.execute(f'DELETE FROM admin_bar WHERE date = "{date}" AND admin = "{admin}" AND position = "{position}" AND value = "{count}"')
        conn.commit()
        self.all_position_list.takeItem(index)
        self.delete_from_all_btn.setVisible(False)
        self.position_from_all_label.setVisible(False)
        

    def selected_by_admin_list(self):
        item = self.admin_positions_list.currentItem()
        text = item.text().split(' | ')
        self.tovar_name_label.setVisible(True)
        self.delete_tovar_btn.setVisible(True)
        self.tovar_name_label.setText(f'{text[0]}\n{text[1]}\n{text[2]}')

    def delete_one_from_by_admin_list(self):
        admin = self.admin_name_combo_box.currentText()
        item = self.admin_positions_list.currentItem()
        index = self.admin_positions_list.currentIndex().row()
        data = item.text().split(' | ')
        data_1 = data[2].split(' - ')
        date, position, value = data[0], data_1[1], data_1[0]
        cur.execute(f'DELETE FROM admin_bar WHERE admin = "{admin}" AND date = "{date}" AND position = "{position}" AND value = "{value}"')
        conn.commit()
        self.tovar_name_label.setVisible(False)
        self.delete_tovar_btn.setVisible(False)
        self.admin_positions_list.takeItem(index)
        cur.execute(f'SELECT * FROM admin_bar WHERE admin = "{admin}"')
        results = cur.fetchall()
        summ = 0
        for result in results:
            summ = summ + result[4]
        self.label_bar_admin.setText(f'{int(summ)} ₽')
        discount = config_get_value(path, 'Settings' ,'discount')
        summ_with_discount = int(summ) /100 * (100 - int(discount))
        self.label_bar_sale.setText(f'{int(summ_with_discount)} ₽')

    def delete_by_admin_all(self):
        admin = self.admin_name_combo_box.currentText()
        cur.execute(f'DELETE FROM admin_bar WHERE admin = "{admin}"')
        conn.commit()
        self.admin_positions_list.clear()
        self.tovar_name_label.setVisible(False)
        self.delete_tovar_btn.setVisible(False)
        self.label_bar_sale.setText('0 ₽')
        self.label_bar_admin.setText('0 ₽')






    def change_window(self, window):
        self.close()
        window.show()




class Add_User(QMainWindow, Ui_AddUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_btn.clicked.connect(lambda: self.change_window(manager_menu_window))
        usr.execute('SELECT * FROM users')
        accs = usr.fetchall()
        for acc in accs:
             self.acc_list_widget.addItem(f'{acc[2]} {acc[3]} | {acc[0]} | {acc[4]}')
        self.acc_list_widget.clicked.connect(self.selected_user_from_list)
        self.change_post_btn.clicked.connect(self.change_post)
        self.change_password_btn.clicked.connect(self.change_password)
        self.change_login_btn.clicked.connect(self.change_login)
        self.delete_acc_btn.clicked.connect(self.delete_user)
        self.accept_add_admin_btn.clicked.connect(self.add_user)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()

    def add_user(self):
        login, password, name, surname, post = self.login_field.text(), self.password_field.text(), self.name_field.text(), self.surname_field.text(), self.post_combobox.currentText()
        login = login.lower()
        if login == '' or login.__contains__(' ') or password == '' or password.__contains__(' ') or name == '' or name.__contains__(' ') or surname == '' or surname.__contains__(' '):
            self.error_label.setText('Заполните все поля,\nполя не должны содержать\nпробелов')
            self.error_label.setVisible(True)
            QTimer.singleShot(3000, self.hide_error)
        else:
            usr.execute(f'SELECT * FROM users WHERE login == "{login}"')
            err = usr.fetchall()
            if err == []:
                password = hashlib.md5(password.encode())
                password = password.hexdigest()
                usr.execute(f'INSERT INTO users VALUES("{login}", "{password}", "{name}", "{surname}", "{post}")')
                users_db.commit()
                self.acc_list_widget.addItem(f'{name} {surname} | {login} | {post}')
                self.login_field.clear()
                self.password_field.clear()
                self.name_field.clear()
                self.surname_field.clear()
            elif err[0][1] == login:
                self.error_label.setText('Пользователь уже существует')
                self.error_label.setVisible(True)
                QTimer.singleShot(3000, self.hide_error)

    def hide_error(self):
        self.error_label.setVisible(False)

    def selected_user_from_list(self):
        user = self.acc_list_widget.currentItem()
        user = user.text()
        self.change_login_field.setVisible(True)
        self.change_login_label.setVisible(True)
        self.change_login_btn.setVisible(True)
        self.change_password_btn.setVisible(True)
        self.Change_password_label.setVisible(True)
        self.change_password_field.setVisible(True)
        self.change_post_label.setVisible(True)
        self.change_post_btn.setVisible(True)
        self.change_post_combobox.setVisible(True)
        self.chosen_acc_text_label.setVisible(True)
        self.chosen_acc_label.setText(user)
        self.delete_acc_btn.setVisible(True)
        self.chosen_acc_label.setVisible(True)

    def delete_user(self):
        items = self.acc_list_widget.currentItem().text().split(' | ')
        usr.execute(f'DELETE FROM users WHERE login == "{items[1]}"')
        users_db.commit()
        self.acc_list_widget.takeItem(self.acc_list_widget.currentIndex().row())
        self.hide_user_account_settings()

    def change_login(self):
        old_login = self.acc_list_widget.currentItem().text().split(' | ')
        login = self.change_login_field.text()
        usr.execute(f'SELECT * FROM users WHERE login = "{login}"')
        same_login = usr.fetchall()
        if login == []:
            usr.execute(f'UPDATE users SET login = "{login.lower()}" WHERE login = "{old_login[1]}"')
            users_db.commit()
            self.change_login_field.clear()
            self.acc_list_widget.takeItem(self.acc_list_widget.currentIndex().row())
            usr.execute(f'SELECT * FROM users WHERE login = "{login}"')
            result = usr.fetchall()
            self.acc_list_widget.addItem(f'{result[0][2]} {result[0][3]} | {result[0][0]} | {result[0][4]}')
            self.hide_user_account_settings()
        else:
            self.change_login_btn.setGeometry(QtCore.QRect(250, 420, 171, 31))
            self.change_login_btn.setStyleSheet('background-color: red;\ncolor: black')
            self.change_login_btn.setText('Логин уже существует')
            QTimer.singleShot(2000, self.normal_btn)
        

    def normal_btn(self):
        self.change_login_btn.setGeometry(QtCore.QRect(250, 420, 101, 31))
        self.change_login_btn.setText('Изменить')
        self.change_login_btn.setStyleSheet(style)

    def change_password(self):
        login = self.acc_list_widget.currentItem().text().split(' | ')
        password = self.change_password_field.text()
        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        usr.execute(f'UPDATE users SET password = "{password}" WHERE login = "{login[1]}"')
        users_db.commit()
        self.change_password_field.clear()

    def change_post(self):
        post = self.change_post_combobox.currentText()
        login = self.acc_list_widget.currentItem().text().split(' | ')
        usr.execute(f'UPDATE users SET post = "{post}" WHERE login = "{login[1]}"')
        users_db.commit()
        self.acc_list_widget.takeItem(self.acc_list_widget.currentIndex().row())
        usr.execute(f'SELECT * FROM users WHERE login = "{login[1]}"')
        result = usr.fetchall()
        self.acc_list_widget.addItem(f'{result[0][2]} {result[0][3]} | {result[0][0]} | {result[0][4]}')
        self.hide_user_account_settings()


    def hide_user_account_settings(self):
        self.change_login_field.setVisible(False)
        self.change_login_label.setVisible(False)
        self.change_login_btn.setVisible(False)
        self.change_password_btn.setVisible(False)
        self.Change_password_label.setVisible(False)
        self.change_password_field.setVisible(False)
        self.change_post_label.setVisible(False)
        self.change_post_btn.setVisible(False)
        self.change_post_combobox.setVisible(False)
        self.chosen_acc_text_label.setVisible(False)
        self.delete_acc_btn.setVisible(False)
        self.chosen_acc_label.setVisible(False)


    def change_window(self, window):
        self.close()
        window.show()


class Stock(QMainWindow, Ui_Stock):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.to_menu_btn.clicked.connect(lambda: self.change_window(main_window))
        self.confirm_btn.clicked.connect(self.confirm)
        cur.execute('SELECT * FROM positions')
        res = cur.fetchall()
        s = 0
        for item in res:
            object_0 = QtWidgets.QLabel(f'{item[0]}')
            object_0.setStyleSheet('color: white')
            object_1 = QtWidgets.QSpinBox()
            object_1.setMaximum(99999)
            if item[2] != None:
                object_1.setValue(item[2])
            object_1.setStyleSheet(style)
            self.grid.addWidget(object_0, s, 0)
            self.grid.addWidget(object_1, s, 1)
            s += 1

    def change_window(self, window):
        self.close()
        window.show()

    def confirm(self):
        i = 0
        while i < self.grid.rowCount():
            name = self.grid.itemAtPosition(i, 0).widget().text()
            value = self.grid.itemAtPosition(i, 1).widget().value()
            cur.execute(f'UPDATE positions SET at_stock = {int(value)} WHERE name = "{name}"')
            conn.commit()
            i += 1
        self.confirm_btn.setStyleSheet('background-color: rgb(45,45,45);\ncolor:green')
        self.confirm_btn.setText('Сохранено')
        self.confirm_btn.setDisabled(True)
        QTimer.singleShot(2500, lambda: self.confirm_btn.setText('Применить'))
        QTimer.singleShot(2500, lambda: self.confirm_btn.setStyleSheet(style))
        QTimer.singleShot(2500, lambda: self.confirm_btn.setEnabled(True))

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()


class Select_promo(QMainWindow, Ui_Choose_promo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_to_menu_btn.clicked.connect(lambda: self.change_window(main_window))
        self.bonus_night.clicked.connect(lambda: self.change_window(six_nights_window))

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()


    def change_window(self, window):
        self.close()
        window.show()


class Six_nights(QMainWindow, Ui_six_night):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.change_window(choose_promo_window))
        self.comboBox.lineEdit().textChanged.connect(self.format_phone_number)
        self.comboBox.lineEdit().returnPressed.connect(self.find_or_add_user)
        self.nights_label.setVisible(False)
        self.nights_value_label.setVisible(False)
        self.pushButton.setVisible(False)
        try:
            cur_promo.execute('SELECT * FROM users')
            users = cur_promo.fetchall()
            for user in users:
                self.comboBox.addItem(user[0])
        except:
            pass
        self.comboBox.setCurrentText('')
        self.pushButton.clicked.connect(self.add_night)


    def format_phone_number(self):
        
        text = self.comboBox.currentText()
        if len(text) < 12:
            self.nights_label.setVisible(False)
            self.nights_value_label.setVisible(False)
            self.pushButton.setVisible(False)


        try:
            cur_promo.execute(f'SELECT * FROM users WHERE number LIKE "{text}%"')
            users = cur_promo.fetchall()
            for user in users:
                self.comboBox.addItem(user[0])
        except Exception as ext:
            pass
        try:
            for letter in text:
                if letter == '+':
                    pass
                elif letter.isdigit() == False:
                    text = text[:-1]
            if text[0] == '+':
                pass
            if text[0] != '+' and text[1] != '7':
                self.comboBox.clear()
                text = '+7'+text
            if len(text) > 12:
                text = text[:-1]
        except Exception as ext:
            pass
        self.comboBox.setEditText(text)

    def find_or_add_user(self):
        text = self.comboBox.currentText()
        if len(text) < 12:
            print('Text less than 12 charcters')
            pass
        else:
            cur_promo.execute(f'SELECT * FROM users WHERE number = "{text}"')
            result = cur_promo.fetchone()
            if result == None:
                cur_promo.execute(f'INSERT INTO users VALUES("{text}", "0", "0")')
                promo_db.commit()
                self.update_label_and_set_visible()
            else:
                self.update_label_and_set_visible()
                
    def update_label_and_set_visible(self):
        text = self.comboBox.currentText()
        cur_promo.execute(f'SELECT * FROM users WHERE number = "{text}"')
        user = cur_promo.fetchone()
        try:
            if user[1] < 5:
                self.nights_value_label.setText(f'{user[1]}')
                self.nights_label.setVisible(True)
                self.nights_value_label.setVisible(True)
                self.pushButton.setVisible(True)
            else:
                self.nights_value_label.setText(f'{user[1]}')
                self.nights_label.setVisible(True)
                self.nights_value_label.setVisible(True)
                self.pushButton.setVisible(True)
                self.pushButton.setText('Использовать')
                self.pushButton.setStyleSheet("background-color: green;\ncolor:black")
        except:
            pass
        
    
    def add_night(self):
        text = self.comboBox.currentText()
        cur_promo.execute(f'SELECT * FROM users WHERE number = "{text}"')
        user = cur_promo.fetchone()
        night = user[1]
        if (night == 5) and (self.pushButton.text() == "Использовать"):
            cur_promo.execute(f'UPDATE users SET nights = 0 WHERE number = "{text}"')
            promo_db.commit()
            self.pushButton.setText('Добавить')
            self.pushButton.setStyleSheet(style)
            self.update_label_and_set_visible()

        elif night == 5:
            pass
        else:
            night+=1
            cur_promo.execute(f'UPDATE users SET nights = "{night}" WHERE number = "{text}"')
            promo_db.commit()
            self.update_label_and_set_visible()


    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.oldPosition)
        self.oldPosition = event.globalPosition().toPoint()
        event.accept()



    def change_window(self, window):
        self.close()
        window.show()






if __name__ == '__main__':
    path = 'settings.ini'
    app = QApplication(sys.argv)

    authorize_window = Authorize()
    main_window = Main_Menu()
    admin_bar_window = Admin_bar()
    inventory_window = Invent()
    inv_history_window = History_inv()
    settings_window = Settings()
    second_settings_window = Settings_Second()
    manager_menu_window = Manager_menu()
    add_user_window = Add_User()
    stock_window = Stock()
    choose_promo_window = Select_promo()
    six_nights_window = Six_nights()

    
    sys.exit(app.exec())