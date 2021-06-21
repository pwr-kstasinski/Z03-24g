import logging
import sys
from typing import Dict, List, Set

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLayout, QPushButton

from apiCalls import *
from data_classes import User, Message
from gui.message_widget import *
from gui.user_widget import *
from gui.window import *

logging.basicConfig(level=logging.NOTSET)
log = logging.getLogger("client")


REGISTER_PAGE_INDEX = 0
CONVERSATION_PAGE_INDEX = 1
USERS_PAGE_INDEX = 2
LOADING_PAGE_INDEX = 3
LOGIN_PAGE_INDEX = 4


class UserWidget(QWidget, Ui_UserWidget):
    def __init__(self, user: User, button_click_callback):
        super().__init__()
        self.callback = button_click_callback
        self.user = user
        self.setupUi(self)

    def setupUi(self, widget):
        super(UserWidget, self).setupUi(widget)
        self.name_label.setText(self.user.name)
        self.pushButton.clicked.connect(lambda: self.callback(self.user))


class MessageWidget(QWidget, Ui_MessageWidget):
    def __init__(self, message: Message, right: bool):
        super(MessageWidget, self).__init__()
        self.right = right
        self.message = message
        self.setupUi(self)

    def setupUi(self, widget):
        super(MessageWidget, self).setupUi(widget)
        self.message_label.setText(self.message.content)
        self.horizontalLayout.setStretch(0, 1 - self.right)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, self.right)


def disconnectButton(sendButton: QPushButton):
    try:
        sendButton.clicked.disconnect()
    except TypeError:
        pass


def clear_layout(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().deleteLater()


def delete_message(message):

    def callback(data: dict):
        log.info(f"Message {message.id} deleted")

    async_delete_message(callback, message.id)


class MessagesClient(Ui_MainWindow):
    def __init__(self):
        super(MessagesClient, self).__init__()
        self.logged_user = None
        self.users_downloading = False
        self.messages_downloading = False
        self.messages: Dict[str, List[Message]] = {}
        self.observers = []
        self.other_user = None

    def run(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QMainWindow()
        w.closeEvent = self.closeEvent
        self.setupUi(w)
        w.show()
        sys.exit(app.exec_())

    def closeEvent(self, _):
        self.logout_user()

    def setupUi(self, MainWindow):
        super(MessagesClient, self).setupUi(MainWindow)

        self.setup_default_pages()
        self.change_page_on_login()

        self.name_login_page_line_edit.setText("test1")
        self.password_login_page_edit_line.setText("test2")

    def setup_default_pages(self):
        self.setup_register_page_buttons()
        self.setup_login_page_buttons()
        self.setup_users_page_buttons()
        self.setup_loading_page_movie()
        self.setup_conversation_page()

    def setup_conversation_page(self):
        self.return_button.clicked.connect(self.load_users_and_messages)
        self.messages_scroll_area.verticalScrollBar().setFixedWidth(0)
        self.messages_layout.setAlignment(Qt.AlignBottom)

        def on_range_change():
            scroll_bar = self.messages_scroll_area.verticalScrollBar()
            maximum = scroll_bar.maximum()
            scroll_bar.setValue(maximum)

        self.messages_scroll_area.verticalScrollBar().rangeChanged.connect(on_range_change)

    def setup_loading_page_movie(self):
        q_movie = QMovie("gui/loading.gif")
        self.loading_label.setMovie(q_movie)
        q_movie.start()

    def setup_users_page_buttons(self):
        self.logout_button.clicked.connect(self.logout_user)

    def setup_login_page_buttons(self):
        self.login_page_register_button.clicked.connect(self.change_page_on_register)
        self.login_page_login_button.clicked.connect(self.login_user)

    def setup_register_page_buttons(self):
        self.register_page_register_button.clicked.connect(self.register_user)
        self.register_page_login_button.clicked.connect(self.change_page_on_login)

    def change_page_on_register(self):
        self.change_page(REGISTER_PAGE_INDEX)
        log.info("Page changed on register")

    def change_page_on_login(self):
        self.change_page(LOGIN_PAGE_INDEX)
        log.info("Page changed on login")

    def change_page_on_conversation(self):
        self.change_page(CONVERSATION_PAGE_INDEX)
        log.info("Page changed on conversation")

    def change_page_on_users(self):
        self.change_page(USERS_PAGE_INDEX)
        log.info("Page changed on users")

    def change_page_on_loading(self):
        self.change_page(LOADING_PAGE_INDEX)
        log.info("Page changed on loading")

    def change_page(self, page_number):
        self.stackedWidget.setCurrentIndex(page_number)

    def show_conversation_with_user(self, user: User):
        self.other_user = user
        self.show_conversation()

    def show_conversation(self):
        self.setup_conversation_page_for_user()
        self.reload_messages()
        self.change_page_on_conversation()

    def save_message(self, message: Message, user_id):
        self.messages.setdefault(user_id, [])

        is_massage_not_added = hash(message) not in [hash(m) for m in self.messages[user_id]]
        if is_massage_not_added:
            self.messages[user_id].append(message)
            self.show_message(message)
            log.info(f"message {message.id} saved")
        else:
            log.info(f"message {message.id} not saved")

    def get_saved_messages_for_conversation_with_user(self, user_id: str):
        keys = self.messages.keys()
        result = []
        if user_id in keys:
            result = self.messages[user_id]
            log.info(f"{len(result)} messages to display")
        else:
            log.debug("messages to display not found")
        return result

    def reload_messages(self):
        if self.other_user is not None:
            log.info(f"Reloading displayed messages for user with id{self.other_user.id}")
            layout = self.messages_layout
            clear_layout(layout)
            self.load_saved_messages_to_conversation(self.other_user)
        else:
            log.info("Reload displayed messages: other user not loaded")

    def show_message(self, message):
        display_on_right_side = self.logged_user.id == message.sender_id
        message_widget = MessageWidget(message, display_on_right_side)
        self.messages_layout.addWidget(message_widget)

    def setup_conversation_page_for_user(self):
        disconnectButton(self.sendButton)
        self.sendButton.clicked.connect(lambda _: self.send_message(self.other_user, self.message_line_edit.text()))
        self.other_user_name_label.setText(self.other_user.name)

    def load_saved_messages_to_conversation(self, user):
        saved_messages = self.get_saved_messages_for_conversation_with_user(user.id)
        log.info(f"{len(saved_messages)} saved messages loaded to display")
        for message in saved_messages:
            self.show_message(message)

    def send_message(self, receiver: User, message_content: str):
        message = Message("", message_content, self.logged_user.id, receiver.id)

        def callback(data: dict):
            data_ = data["data"]["data"]
            saved_message = Message.fromDict(data_)
            self.save_message(saved_message, receiver.id)
            log.info("message sent")

        async_send_message(callback, message)

    def load_users_and_messages(self):
        self.change_page_on_loading()
        self.load_messages()
        self.load_and_show_users()
        self.change_page_on_users()

    def load_and_show_users(self):
        if not self.users_downloading:
            self.users_downloading = True

        def callback(users_data: list):
            if self.logged_user is None:
                return
            self.reload_users(users_data)

        repeat_async_load_users(callback, lambda: not self.users_downloading)

    def reload_users(self, users_data):
        layout = self.users_list.layout()
        clear_layout(layout)
        for user_data in users_data:
            user = User.fromDict(user_data)
            if user.id != self.logged_user.id:
                user_widget = UserWidget(user, self.show_conversation_with_user)
                layout.addWidget(user_widget)

    def load_messages(self):
        if not self.messages_downloading:
            self.messages_downloading = True

            def callback(messages_data: list):
                log.info(f"{len(messages_data)} messages downloaded")
                for message_data in messages_data:
                    message = Message.fromDict(message_data)
                    self.save_message(message, message.sender_id)
                    delete_message(message)

            repeat_async_load_user_messages(callback, self.logged_user.id, lambda: not self.messages_downloading)

    def register_user(self):
        self.change_page_on_loading()

        def callback(data: dict):
            user = User.fromDict(data)
            self.logged_user = user
            self.load_users_and_messages()
            log.info(f"User {user.name} registered")

        async_register_user(callback, self.login_line_edit.text(), self.password_line_edit.text())

    def login_user(self):
        self.change_page_on_loading()

        def callback(data: dict):
            users_data = data["users"]
            if len(users_data) == 0:
                self.login_page_message_label.setText("Log in failed.")
                self.change_page_on_login()
                log.warning("log in failed")
            else:
                user_data = users_data[0]
                user = User.fromDict(user_data)
                self.logged_user = user
                self.load_users_and_messages()
                log.info(f"User {user.name} logged in")

        async_login_user(callback, self.name_login_page_line_edit.text(), self.password_login_page_edit_line.text())

    def logout_user(self):
        self.logged_user = None
        self.users_downloading = False
        self.messages_downloading = False
        self.change_page_on_login()
        log.info("user logged out")


if __name__ == '__main__':
    client = MessagesClient()
    client.run()
