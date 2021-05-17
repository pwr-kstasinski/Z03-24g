import datetime
import sys
from client import login_window

from PyQt5.QtCore import QAbstractListModel, QMargins, QPoint, Qt, QSize
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
    QHBoxLayout, QVBoxLayout
)
from openapi_client.model.message import Message
from openapi_client.model.user import User
from openapi_client.model.user_public import UserPublic
from openapi_client.api.users_api import UsersApi
from openapi_client.api.messages_api import MessagesApi

USER_ME = 0
USER_THEM = 1

BUBBLE_COLORS = {USER_ME: "#90caf9", USER_THEM: "#a5d6a7"}
USER_TRANSLATE = {USER_ME: QPoint(20, 0), USER_THEM: QPoint(0, 0)}

BUBBLE_PADDING = QMargins(15, 5, 35, 5)
TEXT_PADDING = QMargins(25, 15, 45, 15)

MESSAGES = []
PARTNER_NAME = ''


class MessageDelegate(QStyledItemDelegate):
    """
    Draws each message.
    """

    _font = None

    def paint(self, painter, option, index):
        painter.save()
        # Retrieve the user,message tuple from our model.data method.
        user, text, timestamp, = index.model().data(index, Qt.DisplayRole)

        trans = USER_TRANSLATE[user]
        painter.translate(trans)

        # option.rect contains our item dimensions. We need to pad it a bit
        # to give us space from the edge to draw our shape.
        bubblerect = option.rect.marginsRemoved(BUBBLE_PADDING)
        textrect = option.rect.marginsRemoved(TEXT_PADDING)

        # draw the bubble, changing color + arrow position depending on who
        # sent the message. the bubble is a rounded rect, with a triangle in
        # the edge.
        painter.setPen(Qt.NoPen)
        color = QColor(BUBBLE_COLORS[user])
        painter.setBrush(color)
        painter.drawRoundedRect(bubblerect, 10, 10)

        # draw the triangle bubble-pointer, starting from the top left/right.
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
        time_str = datetime.datetime.strftime(timestamp)
        if user == USER_ME:
            painter.drawText(textrect.bottomRight() + QPoint(-80, 5), time_str)
        else:
            painter.drawText(textrect.bottomLeft() + QPoint(0, 5), time_str)
            painter.setPen(Qt.darkCyan)
            font.setPointSize(8)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(textrect.topLeft(), PARTNER_NAME)

        # draw the text
        doc = QTextDocument(text)
        doc.setTextWidth(textrect.width())
        doc.setDefaultTextOption(toption)
        doc.setDocumentMargin(0)

        painter.translate(textrect.topLeft())
        doc.drawContents(painter)
        painter.restore()

    def sizeHint(self, option, index):
        _, text, _ = index.model().data(index, Qt.DisplayRole)
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

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Here we pass the delegate the user, message tuple.
            return MESSAGES[index.row()]

    def rowCount(self, index):
        return len(MESSAGES)

    def add_message(self, who, text, timestamp):
        """
        Add an message to our message list, getting the text from the QLineEdit
        """
        if text:  # Don't add empty strings.
            # Access the list via the model.
            MESSAGES.append((who, text, timestamp))
            # Trigger refresh.
            self.layoutChanged.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Layout the UI
        layout = QGridLayout()
        self.user_api = UsersApi()
        self.message_api = MessagesApi()

        self.nick = ''
        self.id = -1
        self.users = []
        self.partner_id = -1
        self.partner_name = ''

        self.message_input = QLineEdit()
        self.message_input.returnPressed.connect(self.message_to)

        self.setWindowIcon(QIcon('app_icon.png'))
        self.setWindowTitle('ChatApp')

        # Buttons for from/to messages.
        self.btn1 = QPushButton()
        self.btn1.setIcon(QIcon('send_icon.png'))

        self.messages = QListView()
        self.messages.setResizeMode(QListView.Adjust)
        # Use our delegate to draw items in this view.
        self.messages.setItemDelegate(MessageDelegate())

        self.model = MessageModel()
        self.messages.setModel(self.model)

        self.btn1.pressed.connect(self.message_to)

        self.list = QScrollArea()
        layout.addWidget(self.list, 0, 0, 3, 1)
        layout.addWidget(self.messages, 0, 1, 3, 3)
        layout.addWidget(self.message_input, 3, 0, 1, 3)
        layout.addWidget(self.btn1, 3, 3, 1, 1)

        self.w = QWidget()
        self.w.setLayout(layout)
        self.setCentralWidget(self.w)
        self.message_input.setFocus()
        self.lay = QVBoxLayout()
        self.list.setLayout(self.lay)

    def closeEvent(self, event):
        self.user_api.logout(username=self.nick)

    def resizeEvent(self, e):
        self.model.layoutChanged.emit()

    def message_to(self):
        self.model.add_message(USER_ME, self.message_input.text(), datetime.datetime.today())
        msg = Message(sender_ip=self.id, receiver_ip=self.partner_id, message=self.message_input.text(),
                      date=datetime.datetime.today())
        self.message_api.send(msg)
        self.message_input.clear()

    def list_users(self):
        for u in self.users:
            button = QPushButton(str(u['id'])+' '+u['username'])
            self.lay.addWidget(button)
            button.pressed.connect(lambda: self.select_user())

    def select_user(self):
        name = self.sender().text()
        name = name.split()
        self.partner_id = int(name[0])
        self.partner_name = name[1]
        global PARTNER_NAME
        PARTNER_NAME = name[1]
        messages = self.message_api.receive(user_id=self.id, partner_id=self.partner_id)
        for m in messages:
            if self.id == m['sender_id']:
                self.model.add_message(USER_ME, m['message'], datetime.datetime.today())
            else:
                self.model.add_message(USER_THEM, m['message'], datetime.datetime.today())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login_window.LoginWindow()
    window.show()
    app.exec_()
