import datetime
import logging
import sys
from typing import List, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QPushButton

from apiCalls import *
from websocket_calls import *
from data_classes import User, Message, Conversation, Membership
from gui.message_widget import *
from gui.conversation_widget import *
from gui.user_widget import *
from gui.window import *

logging.basicConfig(level=logging.NOTSET)
log = logging.getLogger("client")

MAX_ONLINE_DIFFERENCE = 120
EVERYONE_CONVERSATION_NAME = "Everyone"

REGISTER_PAGE_INDEX = 0
CONVERSATION_PAGE_INDEX = 1
USERS_PAGE_INDEX = 2
LOADING_PAGE_INDEX = 3
LOGIN_PAGE_INDEX = 4
CONVERSATIONS_PAGE_INDEX = 5

WEBSOCKET_ADDRESS = 'ws://localhost:8765'


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
        if not self.user.logged:
            self.online_label.setHidden(True)


class ConversationWidget(QWidget, Ui_ConversationWidget):
    def __init__(self, conversation: Conversation, open_conversation_callback, logged_user: User, get_users):
        super().__init__()
        self.get_users = get_users
        self.logged_user = logged_user
        self.callback = open_conversation_callback
        self.conversation = conversation
        self.setupUi(self)

    def setupUi(self, widget):
        super(ConversationWidget, self).setupUi(widget)
        self.conversation_name_label.setText(self.conversation.name)
        self.open_conversation_button.clicked.connect(lambda: self.callback(self.conversation.id))
        online_users_id_without_logged = list(
            filter(lambda user_id: user_id != self.logged_user.id, self.online_users()))
        if len(online_users_id_without_logged) < 1:
            self.online_label.setHidden(True)
        if self.conversation.membership is None:
            self.not_readed_number_label.setHidden(True)
            return
        not_read_messages_number = len(self.conversation.membership.not_read_messages)
        if not_read_messages_number == 0:
            self.not_readed_number_label.setHidden(True)
            return
        self.not_readed_number_label.setText(str(not_read_messages_number))

    def online_users(self):
        return self.conversation.online_users(self.get_users(), MAX_ONLINE_DIFFERENCE)


class MessageWidget(QWidget, Ui_MessageWidget):
    def __init__(self, message: Message, right: bool, author: User):
        super(MessageWidget, self).__init__()
        self.author = author
        self.right = right
        self.message = message
        self.setupUi(self)

    def setupUi(self, widget):
        super(MessageWidget, self).setupUi(widget)
        self.message_label.setText(self.message.content)
        self.send_date_label.setText(self.message.send_date)
        self.status_label.setHidden(True)
        if self.right:
            self.setLayoutDirection(Qt.RightToLeft)
            self.author_label.setText(self.author.name)
        else:
            self.author_label.setHidden(True)

    def setStatus(self, status: str):
        self.status_label.setVisible(True)
        self.status_label.setText(status)


def disconnectButton(sendButton: QPushButton):
    try:
        sendButton.clicked.disconnect()
    except TypeError:
        pass


def clear_layout(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().deleteLater()


class MessagesClient(Ui_MainWindow):
    def __init__(self):
        super(MessagesClient, self).__init__()
        self.users: List[User] = []
        self.conversations: List[Conversation] = []
        self.logged_user: Optional[User] = None
        self.observers = []
        self.other_user = None
        self.showed_messages_widgets: List[MessageWidget] = []
        self.last_loaded_conversation: Optional[Conversation] = None

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
        self.setup_conversations_page_buttons()
        self.setup_loading_page_movie()
        self.setup_conversation_page()

    def setup_conversation_page(self):
        self.return_button.clicked.connect(self.show_conversations)
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
        self.return_button_2.clicked.connect(self.show_conversations)

    def setup_conversations_page_buttons(self):
        self.conversations_page_logout_button.clicked.connect(self.logout_user)
        self.new_conversation_button.clicked.connect(self.show_users)

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

    def change_page_on_conversations(self):
        self.change_page(CONVERSATIONS_PAGE_INDEX)
        log.info("Page changed on conversation")

    def change_page(self, page_number):
        self.stackedWidget.setCurrentIndex(page_number)

    def load_conversation(self, conversation_id: str):
        self.change_page_on_loading()

        def callback(conversation_data: dict):
            conversation_dict = conversation_data["data"]
            if self.logged_user is None:
                return
            conversation = Conversation.fromDict(conversation_dict)
            self.show_conversation(conversation)

        async_load_conversation(callback, conversation_id)

    def show_conversation(self, conversation: Conversation):
        disconnectButton(self.sendButton)
        self.sendButton.clicked.connect(
            lambda _: self.send_message(conversation.id, self.message_line_edit.text(), str(datetime.datetime.now())))
        self.sendButton.clicked.connect(lambda _: self.message_line_edit.setText(""))
        self.conversation_name_label.setText(conversation.name)
        self.last_loaded_conversation = conversation
        self.reload_messages()

    def show_message(self, message, status=None):
        display_on_right_side = self.logged_user.id != message.user_id
        filtered_list = list(filter(lambda u: u.id == message.user_id, self.users))
        if len(filtered_list) == 0:
            return
        user = filtered_list[0]
        message_widget = MessageWidget(message, display_on_right_side, user)
        self.showed_messages_widgets.append(message_widget)
        self.messages_layout.addWidget(message_widget)
        if status is not None:
            message_widget.setStatus(status)

    def send_message(self, conversation_id: str, message_content: str, send_date: str):
        message = Message("", message_content, send_date, self.logged_user.id, conversation_id)
        self.show_message(message, "sending...")

        def callback(data: dict):
            log.info("message sent")
            self.update_message_status(message, "sent")

        async_send_message(callback, message)

    def update_message_status(self, message: Message, status: str):
        for widget in self.showed_messages_widgets:
            if widget.message.id == message.id:
                widget.setStatus(status)
                break

    def load_conversations(self, after_load_callback):
        def callback(conversations_data: dict):
            conversations_dict = conversations_data["data"]
            if self.logged_user is None:
                return
            for conversation_dict in conversations_dict:
                conversation = Conversation.fromDict(conversation_dict)
                self.conversations.append(conversation)
            log.info("conversation loaded")
            after_load_callback()

        async_get_conversations(callback, self.logged_user.id)

    def show_conversations(self):
        self.change_page_on_loading()
        layout = self.conversations_list.layout()
        clear_layout(layout)
        self.conversations = reversed(sorted(self.conversations, key=lambda c: datetime.datetime.strptime(c.last_active, '%Y-%m-%d %H:%M:%S')))
        self.conversations = sorted(self.conversations, key=lambda c: len(c.online_users(self.users, MAX_ONLINE_DIFFERENCE)) == 1)
        for conversation in self.conversations:
            conversation_widget = ConversationWidget(conversation, self.load_conversation, self.logged_user, lambda: self.users)
            layout.addWidget(conversation_widget)
        self.change_page_on_conversations()

    def load_users(self):
        def callback(users_data: list):
            if self.logged_user is None:
                return
            for user_data in users_data:
                user = User.fromDict(user_data)
                self.users.append(user)
            log.info("users loaded")

        async_load_users(callback)

    def show_users(self):
        self.change_page_on_loading()
        layout = self.users_list.layout()
        clear_layout(layout)
        self.users = list(reversed(sorted(self.users, key=lambda u: u.logged)))

        for user in self.users:
            if user.id != self.logged_user.id:
                user_widget = UserWidget(user, self.create_conversation_with_user)
                layout.addWidget(user_widget)
        self.change_page_on_users()

    def create_conversation_with_user(self, user: User):
        self.change_page_on_loading()
        conversation_name = f"{self.logged_user.name} - {user.name}"

        def callback(conversation_data: dict):
            conversation_dict = conversation_data["data"]["data"]
            conversation = Conversation.fromDict(conversation_dict)
            self.add_user_to_conversation(self.logged_user, conversation, self.change_page_on_conversations)
            self.add_user_to_conversation(user, conversation)
            self.conversations.append(conversation)
            self.show_conversations()

        async_create_conversation(callback, conversation_name)

    def reload_messages(self):
        def callback(messages_data: dict):
            messages_list = messages_data["data"]
            log.info(f"{len(messages_list)} messages downloaded")
            self.last_loaded_conversation.messages = [Message.fromDict(m) for m in messages_list]
            self.show_messages(self.last_loaded_conversation)

        async_load_conversation_messages(callback, self.last_loaded_conversation.id)

    def show_messages(self, conversation: Conversation):
        self.change_page_on_loading()

        clear_layout(self.messages_layout)
        sorted_messages = sorted(conversation.messages, key=lambda m: m.send_date)
        for m in sorted_messages:
            self.show_message(m)
        self.change_page_on_conversation()

    def find_conversation_with_name(self, conversation_name: str, after_finding_callback):
        def callback(conversation_data: dict):
            conversation_dict = conversation_data["data"][0]
            conversation = Conversation.fromDict(conversation_dict)
            after_finding_callback(conversation)

        async_get_conversation_with_name(callback, conversation_name)

    def add_user_to_conversation(self, user: User, conversation: Conversation, after_add_callback=None):
        membership = Membership("", user.id, conversation.id, str(datetime.datetime.now()), [])
        async_create_membership(lambda _: after_add_callback, membership)
        if after_add_callback is not None:
            after_add_callback()

    def register_user(self):
        self.change_page_on_loading()

        name = self.login_line_edit.text()
        password = self.password_line_edit.text()
        set_name_and_password(name, password)

        def after_register_callback(data: dict):
            user = User.fromDict(data)
            log.info(f"User {user.name} registered")

            def after_add_callback():
                self.login_user_to_server(name, password)

            def after_finding_callback(conversation: Conversation):
                self.add_user_to_conversation(user, conversation, after_add_callback)

            self.find_conversation_with_name(EVERYONE_CONVERSATION_NAME, after_finding_callback)

        async_register_user(after_register_callback, name, password)

    def login_user(self):
        self.change_page_on_loading()

        name = self.name_login_page_line_edit.text()
        password = self.password_login_page_edit_line.text()
        self.login_user_to_server(name, password)

    def login_user_to_server(self, name, password):
        set_name_and_password(name, password)

        def _login_user(data):
            users_data = data["users"]
            if len(users_data) != 1:
                handle_failed_login()
                return
            user_data = users_data[0]
            user = User.fromDict(user_data)
            log.info(f"User {user.name} logged in")
            self.logged_user = user

            def after_get_conversations_callback():
                memberships_list = data["memberships"]
                for membership_dict in memberships_list:
                    membership = Membership.fromDict(membership_dict)
                    self.assign_membership_to_conversation(membership)
                self.show_conversations()
                async_connect_websocket(self.handle_websocket_update, WEBSOCKET_ADDRESS, asyncio.get_event_loop(), log, lambda: self.logged_user)

            self.load_conversations(after_get_conversations_callback)
            self.load_users()

        def handle_failed_login():
            self.login_page_message_label.setText("Log in failed.")
            self.change_page_on_login()
            log.warning("log in failed")

        async_get_user_with_name(_login_user, name)

    def assign_membership_to_conversation(self, membership: Membership):
        for conversation in self.conversations:
            if conversation.id == membership.conversation_id:
                conversation.membership = membership
                continue

    def logout_user(self):
        self.logged_user = None
        self.conversations = []
        self.users = []
        self.change_page_on_login()
        log.info("user logged out")
        clear_name_and_password()

    def handle_websocket_update(self, data: dict):
        target_type = data["type"]
        if target_type == "User":
            user = User.fromDict(data)

            inserted = False
            for i in range(len(self.users)):
                if self.users[i].id == user.id:
                    self.users.pop(i)
                    self.users.insert(i, user)
                    inserted = True
            if not inserted:
                self.users.append(user)

            if self.stackedWidget.currentIndex() == USERS_PAGE_INDEX:
                self.show_users()

            if self.stackedWidget.currentIndex() == CONVERSATIONS_PAGE_INDEX:
                self.show_conversations()

        elif target_type == "Message":
            message = Message.fromDict(data)
            if self.last_loaded_conversation.id == message.conversation_id:
                if message.user_id != self.logged_user.id:
                    self.last_loaded_conversation.messages.append(message)
                    if self.stackedWidget.currentIndex() == CONVERSATION_PAGE_INDEX:
                        self.show_messages(self.last_loaded_conversation)

        else:
            log.warning("websockets - not handled update")


if __name__ == '__main__':
    client = MessagesClient()
    client.run()
