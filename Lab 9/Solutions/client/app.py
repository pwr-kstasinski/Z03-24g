import datetime
import sys

from client import login_window

from PyQt5.QtCore import QAbstractListModel, QMargins, QPoint, Qt, QSize, QTimer
from PyQt5.QtGui import QColor, QTextDocument, QTextOption, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QLineEdit,
    QListView,
    QMainWindow,
    QPushButton,
    QStyledItemDelegate,
    QGridLayout,
    QWidget,
    QScrollArea,
    QVBoxLayout,
    QHBoxLayout,
    QLabel, QFrame
)
from openapi_client.model.message import Message
from openapi_client.api.users_api import UsersApi
from openapi_client.api.messages_api import MessagesApi


USER_ME = 0
USER_THEM = 1

BUBBLE_COLORS = {USER_ME: "#90caf9", USER_THEM: "#a5d6a7"}
USER_TRANSLATE = {USER_ME: QPoint(20, 0), USER_THEM: QPoint(0, 0)}

BUBBLE_PADDING = QMargins(15, 5, 35, 5)
TEXT_PADDING = QMargins(25, 15, 45, 15)


class MessageDelegate(QStyledItemDelegate):
    """
    Draws each message.
    """

    _font = None

    def paint(self, painter, option, index):
        painter.save()
        user, text, timestamp, name = index.model().data(index, Qt.DisplayRole)

        trans = USER_TRANSLATE[user]
        painter.translate(trans)

        bubblerect = option.rect.marginsRemoved(BUBBLE_PADDING)
        textrect = option.rect.marginsRemoved(TEXT_PADDING)

        painter.setPen(Qt.NoPen)
        color = QColor(BUBBLE_COLORS[user])
        painter.setBrush(color)
        painter.drawRoundedRect(bubblerect, 10, 10)

        if user == USER_ME:
            p1 = bubblerect.bottomRight()
        else:
            p1 = bubblerect.bottomLeft()
        painter.drawPolygon(p1 + QPoint(-20, 1), p1 + QPoint(20, 1), p1 + QPoint(0, -20))

        toption = QTextOption()
        toption.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        # draw time stamp
        font = painter.font()

        font.setPointSize(7)
        painter.setFont(font)
        painter.setPen(Qt.black)
        time_str = timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        if user == USER_ME:
            painter.drawText(textrect.bottomRight() + QPoint(-80, 8), time_str)
        else:
            painter.drawText(textrect.bottomLeft() + QPoint(0, 8), time_str)
            painter.setPen(Qt.darkCyan)
            font.setPointSize(8)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(textrect.topLeft(), name)

        # draw the text
        doc = QTextDocument(text)
        doc.setTextWidth(textrect.width())
        doc.setDefaultTextOption(toption)
        doc.setDocumentMargin(0)

        painter.translate(textrect.topLeft())
        doc.drawContents(painter)
        painter.restore()

    def sizeHint(self, option, index):
        _, text, _, _ = index.model().data(index, Qt.DisplayRole)
        textrect = option.rect.marginsRemoved(TEXT_PADDING)

        toption = QTextOption()
        toption.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        doc = QTextDocument(text)
        doc.setTextWidth(textrect.width())
        doc.setDefaultTextOption(toption)
        doc.setDocumentMargin(0)

        textrect.setHeight(int(doc.size().height()))
        textrect = textrect.marginsAdded(TEXT_PADDING)
        return textrect.size() + QSize(0, 20)


class MessageModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(MessageModel, self).__init__(*args, **kwargs)
        self.messages = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.messages[index.row()]

    def setData(self, index, role, value):
        self._size[index.row()]

    def rowCount(self, index):
        return len(self.messages)

    def add_message(self, who, text, timestamp, name):
        """
        Add an message to our message list, getting the text from the QLineEdit
        """
        if text:
            self.messages.append((who, text, timestamp, name))
            # refresh
            self.layoutChanged.emit()

    def refresh(self):
        self.layoutChanged.emit()

    def clear(self):
        self.removeRows(0, self.rowCount(0))
        self.messages.clear()
        self.layoutChanged.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        layout = QGridLayout()
        self.user_api = UsersApi()
        self.message_api = MessagesApi()

        self.nick = ''
        self.id = -1
        self.users = []
        self.partner_id = -1
        self.partner_name = ''
        self.buttons = []

        self.message_input = QLineEdit()
        self.message_input.returnPressed.connect(lambda: self.message_to(self.message_input.text(), datetime.datetime.
                                                                         today(), ''))

        self.setWindowIcon(QIcon('icons/app_icon.png'))
        self.setWindowTitle('ChatApp')

        self.send_button = QPushButton()
        self.send_button.setIcon(QIcon('icons/send_icon.png'))

        self.messages = QListView()
        self.messages.setResizeMode(QListView.Adjust)
        # Use delegate to draw items in this view
        self.messages.setItemDelegate(MessageDelegate())

        self.model = MessageModel()
        self.messages.setModel(self.model)

        self.send_button.pressed.connect(lambda: self.message_to(self.message_input.text(), datetime.datetime.today(),
                                                                 ''))

        self.lists = QWidget()
        self.lists.setLayout(QHBoxLayout())
        self.lists.setMinimumWidth(5)

        layout.addWidget(self.lists, 0, 0, 3, 1)
        layout.addWidget(self.messages, 0, 1, 3, 5)
        layout.addWidget(self.message_input, 3, 0, 1, 5)
        layout.addWidget(self.send_button, 3, 5, 1, 1)

        self.all_scroll = QScrollArea()
        self.all_scroll.setWidgetResizable(True)
        self.logged_scroll = QScrollArea()
        self.logged_scroll.setWidgetResizable(True)

        self.lists.layout().addWidget(self.logged_scroll)
        self.lists.layout().addWidget(self.all_scroll)

        self.logged_layout = QVBoxLayout()
        self.users_layout = QVBoxLayout()
        self.logged_frame = QFrame(self.logged_scroll)
        self.users_frame = QFrame(self.all_scroll)
        self.logged_frame.setLayout(self.logged_layout)
        self.users_frame.setLayout(self.users_layout)
        self.logged_scroll.setWidget(self.logged_frame)
        self.all_scroll.setWidget(self.users_frame)

        self.w = QWidget()
        self.w.setLayout(layout)
        self.setCentralWidget(self.w)
        self.message_input.setFocus()

        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.setInterval(4000)
        self.timer.timeout.connect(self.refresh)
        self.timer.start()

    def closeEvent(self, event):
        self.user_api.logout(username=self.nick)

    def resizeEvent(self, event):
        self.model.layoutChanged.emit()

    def message_to(self, message, timestamp, name):
        if self.partner_id < 0:
            return
        self.model.add_message(USER_ME, message, timestamp, name)
        msg = Message(
            sender_id=self.id,
            receiver_id=self.partner_id,
            message=message,
            date=timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
        )
        self.message_api.send(msg)
        self.message_input.clear()

    def message_from(self, message, timestamp, name):
        self.model.add_message(USER_THEM, message, timestamp, name)

    def list_users(self):
        for b in self.buttons:
            b.setParent(None)
        self.buttons.clear()
        self.users = self.user_api.list_users()
        self.buttons.append(QLabel('Active users'))
        self.logged_layout.addWidget(self.buttons[-1])
        self.buttons.append(QLabel('Not active'))
        self.users_layout.addWidget(self.buttons[-1])
        for u in self.users:
            if u['username'] == self.nick:
                self.id = u['id']
        for u in self.users:
            if self.id != u['id']:
                self.buttons.append(QPushButton(str(u['id'])+' '+u['username']))
                self.buttons[-1].pressed.connect(lambda: self.select_user())
                if u['logged']:
                    self.logged_layout.addWidget(self.buttons[-1])
                else:
                    self.users_layout.addWidget(self.buttons[-1])
        self.buttons.append(QPushButton('Refresh'))
        self.logged_layout.addWidget(self.buttons[-1])
        self.buttons[-1].pressed.connect(lambda: self.list_users())

    def select_user(self):
        self.model.clear()
        name = self.sender().text()
        name = name.split()
        self.partner_id = int(name[0])
        self.partner_name = name[1]
        messages = self.message_api.receive(user_id=self.id, partner_id=self.partner_id)
        for m in messages:
            date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S')
            if m['sender_id'] == self.id:
                self.model.add_message(USER_ME, m['message'], date, self.nick)
            else:
                self.message_from(m['message'], date, self.partner_name)
        self.messages.scrollToBottom()

    def refresh(self):
        if self.partner_id < 0:
            return
        self.model.clear()
        messages = self.message_api.receive(user_id=self.id, partner_id=self.partner_id)
        for m in messages:
            date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S')
            if m['sender_id'] == self.id:
                self.model.add_message(USER_ME, m['message'], date, self.nick)
            else:
                self.message_from(m['message'], date, self.partner_name)
        self.messages.scrollToBottom()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login_window.LoginWindow()
    window.show()
    app.exec_()
