import openapi_client.exceptions
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
    QGridLayout,
    QLabel, QMessageBox
)
from PyQt5.QtCore import Qt
import app
from openapi_client.model.user import User
from openapi_client.api.users_api import UsersApi
from openapi_client.api.messages_api import MessagesApi


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.user_api = UsersApi()
        self.message_api = MessagesApi()
        other = app.MainWindow()
        self.centralwidget = QWidget()
        self.other = other
        self.gridLayout = QGridLayout(self.centralwidget)

        self.password = QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.password, 1, 2, 1, 2)

        self.host_name = QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.host_name, 0, 2, 1, 2)

        self.host_label = QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.host_label, 0, 0, 1, 1)

        self.login_button = QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.login_button, 2, 2, 1, 2)

        self.id_label = QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.id_label, 1, 0, 1, 1)

        self.register_button = QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.register_button, 3, 2, 1, 2)
        self.setCentralWidget(self.centralwidget)

        # setting labels and button functionality
        self.id_label.setText('Password')
        self.id_label.setAlignment(Qt.AlignCenter)
        self.login_button.setText('Login')
        self.host_label.setText('Nick')
        self.host_label.setAlignment(Qt.AlignCenter)
        self.register_button.setText('Register')
        self.login_button.pressed.connect(self.login)
        self.register_button.pressed.connect(self.register)
        self.setWindowTitle('ChatApp Login')
        self.setWindowIcon(QIcon('icons/app_icon.png'))
        self.resize(250, 150)
        self.host_name.setFocus()
        self.host_name.returnPressed.connect(lambda: self.room_id.setFocus())
        self.password.returnPressed.connect(self.login)
        self.setTabOrder(self.host_name, self.password)
        self.setTabOrder(self.password, self.login_button)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignRight)
        self.host_name.setAlignment(Qt.AlignRight)

    def login(self):
        nick = self.host_name.text()
        password = self.password.text()
        try:
            self.user_api.login(username=nick, password=password)
            data = self.user_api.get_user(username=nick)
            self.other.nick = nick
            self.other.id = data['id']
            self.hide()
            self.other.users = self.user_api.list_users(self.other.id)
            self.other.list_users()
            self.other.show()
        except openapi_client.exceptions.ApiException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Wrond password or username")
            msg.setInformativeText("We couldnt login, if user doesnt exist you can register")
            msg.setWindowTitle("Wrong credentials")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            self.host_name.clear()
            self.password.clear()

    def register(self):
        name = self.host_name.text()
        password = self.password.text()
        try:
            self.user_api.register(User(username=name, password=password, logged=False))
            self.other.nick = name
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Registered')
            msg.setInformativeText('You have been succesfully registered')
            msg.setWindowTitle('Registered')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            self.host_name.clear()
            self.password.clear()
        except openapi_client.exceptions.ApiException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('User already exists')
            msg.setInformativeText('We couldnt register, user already exists')
            msg.setWindowTitle('User exist')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            self.host_name.clear()
            self.password.clear()
