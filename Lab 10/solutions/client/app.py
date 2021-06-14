import datetime
import json
import sys

import socketio
import asyncio

from client import login_window, openapi_client
from PyQt5.QtCore import QAbstractListModel, QMargins, QPoint, Qt, QSize, QObject, QThread, pyqtSignal
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
    QFrame
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

style_sheet = '''QPushButton {
    background-color: rgb(175, 175, 175);
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: rgb(100, 112, 124);
    font: 10px;
    min-width: 5em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: rgb(100, 112, 124);
    border-style: inset;
}'''

style_sheet_bold = '''QPushButton {
    background-color: rgb(175, 175, 175);
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: rgb(100, 112, 124);
    font: bold 10px;
    min-width: 5em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: rgb(100, 112, 124);
    border-style: inset;
}'''

sio = socketio.AsyncClient()


class MessageDelegate(QStyledItemDelegate):
    """
    Draws each message.
    """

    _font = None

    def paint(self, painter, option, index):
        painter.save()
        user, text, timestamp, name, read = index.model().data(index, Qt.DisplayRole)

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
            if read is True:
                painter.drawText(textrect.bottomRight() + QPoint(-20, 20),  'Read ✓')

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
        _, text, _, _, _ = index.model().data(index, Qt.DisplayRole)
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

    def add_message(self, who, text, timestamp, name, read):
        """
        Add an message to our message list, getting the text from the QLineEdit
        """
        if text:
            self.messages.append((who, text, timestamp, name, read))
            # refresh
            self.layoutChanged.emit()

    def refresh(self):
        self.layoutChanged.emit()

    def clear(self):
        self.removeRows(0, self.rowCount(0))
        self.messages.clear()
        self.layoutChanged.emit()


class Worker(QObject):
    finished = pyqtSignal()
    newData = pyqtSignal(object)
    messages = pyqtSignal(object)
    progress = pyqtSignal(int)
    user_api = UsersApi()
    message_api = MessagesApi()
    message = None
    user_id: int
    partner_id: int

    def list_users(self):
        """Long-running task."""
        users = self.user_api.list_users(id=self.user_id)
        self.finished.emit()
        self.newData.emit(users)

    def send_message(self):
        self.message_api.send(self.message)
        self.finished.emit()


class SocketThread(QObject):
    emitter = pyqtSignal(object)

    @sio.on('all')
    async def on_msg(data):
        s_thread.emitter.emit(data)
    async def main(self):
        await sio.connect('http://localhost:5000')
        await sio.wait()

    def func(self):
        asyncio.run(self.main())


s_thread = SocketThread()


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

        self.lists.layout().addWidget(self.all_scroll)

        self.users_layout = QVBoxLayout()
        self.users_frame = QFrame(self.all_scroll)
        self.users_frame.setLayout(self.users_layout)
        self.all_scroll.setWidget(self.users_frame)

        self.w = QWidget()
        self.w.setLayout(layout)
        self.setCentralWidget(self.w)
        self.message_input.setFocus()

        self.thread = QThread()
        self.thread2 = QThread()
        self.worker = Worker()

        self.socket = s_thread
        self.socket.moveToThread(self.thread2)
        self.thread2.started.connect(self.socket.func)
        self.thread2.start()
        s_thread.emitter.connect(
            lambda s: self.handle_socket(s)
        )

    def closeEvent(self, event):
        self.thread.terminate()
        self.thread2.terminate()
        self.user_api.logout(username=self.nick)

    def resizeEvent(self, event):
        self.model.layoutChanged.emit()

    def message_to(self, message, timestamp, name):
        if self.thread.isRunning():
            self.thread.terminate()
        if self.partner_id < 0:
            return
        self.model.add_message(USER_ME, message, timestamp, name, False)
        msg = Message(
            sender_id=self.id,
            receiver_id=self.partner_id,
            message=message,
            date=timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
            read=False
        )
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.send_message)
        self.worker.message = msg
        self.thread.start()
        self.message_input.clear()
        self.messages.scrollToBottom()
        self.list_users_data()

    def message_from(self, message, timestamp, name, read):
        self.model.add_message(USER_THEM, message, timestamp, name, read)

    def list_users_data(self):
        if self.thread.isRunning():
            self.thread.terminate()
        self.worker.user_id = self.id
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.list_users)
        self.thread.start()
        self.worker.newData.connect(
            lambda s: self.list_users(s)
        )

    def list_users(self, users=None):
        for b in self.buttons:
            b.setParent(None)
        self.buttons.clear()
        if users is not None:
            self.users = users
        self.buttons.append(QPushButton('#General'))
        self.users_layout.addWidget(self.buttons[-1])
        self.buttons[-1].setStyleSheet(style_sheet)
        self.buttons[-1].pressed.connect(lambda: self.select_user())
        if self.users[-1]['unread'] > 0:
            self.buttons[-1].setText('#General'+' ('+str(self.users[-1]['unread'])+')')
            self.buttons[-1].setStyleSheet(style_sheet_bold)
        for u in self.users:
            if u['username'] == self.nick:
                self.id = u['id']
        for u in self.users:
            if self.id != u['id'] and u['id'] != 0:
                self.buttons.append(QPushButton(str(u['id'])+' '+u['username']))
                self.buttons[-1].setStyleSheet(style_sheet)
                self.buttons[-1].pressed.connect(lambda: self.select_user())
                if u['logged']:
                    self.users_layout.addWidget(self.buttons[-1])
                    self.buttons[-1].setIcon(QIcon('icons/Active_icon.png'))
                else:
                    self.users_layout.addWidget(self.buttons[-1])
                    self.buttons[-1].setIcon(QIcon('icons/Not_active_icon.png'))
                if u['unread'] > 0:
                    self.buttons[-1].setText(str(u['id'])+' '+u['username']+' ('+str(u['unread'])+')')
                    self.buttons[-1].setStyleSheet(style_sheet_bold)

    def select_user(self):
        name = self.sender().text()
        if name.split()[0] == self.partner_id:
            return
        self.model.clear()
        if name.split()[0] == '#General':
            self.partner_name = name
            self.partner_id = 0
            self.message_api.mark_read(user_id=self.id, partner_id=self.partner_id)
            messages = self.message_api.receive(user_id=self.id, partner_id=self.partner_id)
            for m in messages:
                date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S')
                if m['sender_id'] == self.id:
                    self.model.add_message(USER_ME, m['message'], date, self.nick, m['read'])
                else:
                    sender_name = ''
                    for u in self.users:
                        if m['sender_id'] == u['id']:
                            sender_name = u['username']
                            break
                    self.message_from(m['message'], date, sender_name, m['read'])
        else:
            name = name.split()
            self.partner_id = int(name[0])
            self.partner_name = name[1]
            self.message_api.mark_read(user_id=self.id, partner_id=self.partner_id)
            messages = self.message_api.receive(user_id=self.id, partner_id=self.partner_id)
            for m in messages:
                date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S')
                if m['sender_id'] == self.id:
                    self.model.add_message(USER_ME, m['message'], date, self.nick, m['read'])
                else:
                    self.message_from(m['message'], date, self.partner_name, m['read'])
        self.messages.scrollToBottom()
        self.list_users_data()

    def show_msg(self):
        print('raz')
        messages = self.message_api.receive(user_id=self.id, partner_id=self.partner_id)
        print('dwa')
        print(messages)
        self.model.clear()
        if self.partner_name == '#General':
            for m in messages:
                date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S')
                if m['sender_id'] == self.id:
                    self.model.add_message(USER_ME, m['message'], date, self.nick, m['read'])
                else:
                    sender_name = ''
                    for u in self.users:
                        if m['sender_id'] == u['id']:
                            sender_name = u['username']
                            break
                    self.message_from(m['message'], date, sender_name, m['read'])
        else:
            for m in messages:
                date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S')
                if m['sender_id'] == self.id:
                    self.model.add_message(USER_ME, m['message'], date, self.nick, m['read'])
                else:
                    self.message_from(m['message'], date, self.partner_name, m['read'])
        self.messages.scrollToBottom()

    def handle_socket(self, data):
        data1 = json.loads(data)
        print(data1)
        if data1['action'] == 'read':
            if data1['sender_id'] == str(self.id) and data1['receiver_id'] == str(self.partner_id):
                self.show_msg()
        elif data1['action'] == 'user_refresh':
            if self.thread.isRunning():
                self.thread.terminate()
                self.list_users_data()
            else:
                self.list_users_data()
        else:
            if data1['sender_id'] == self.partner_id and data1['receiver_id'] == self.id:
                self.message_api.mark_read(user_id=self.id, partner_id=self.partner_id)
                self.message_from(data1['message'], datetime.datetime.strptime(data1['date'], "%m/%d/%Y, %H:%M:%S"),
                                  self.partner_name, True)
                self.messages.scrollToBottom()
            if data1['receiver_id'] == 0 and self.partner_id == 0:
                self.message_api.mark_read(user_id=self.id, partner_id=self.partner_id)
                for u in self.users:
                    if data1['sender_id'] == u['id']:
                        sender_name = u['username']
                        break
                self.message_from(data1['message'], datetime.datetime.strptime(data1['date'], "%m/%d/%Y, %H:%M:%S"),
                                  sender_name, True)
                self.message_api.mark_read(user_id=self.id, partner_id=self.partner_id)
                self.messages.scrollToBottom()
                return
            if data1['receiver_id'] == 0 or data1['receiver_id'] == self.id:
                if self.thread.isRunning():
                    self.thread.terminate()
                    self.list_users_data()
                else:
                    self.list_users_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login_window.LoginWindow()
    window.show()
    app.exec_()
