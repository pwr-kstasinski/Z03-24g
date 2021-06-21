# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversation_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConversationWidget(object):
    def setupUi(self, ConversationWidget):
        ConversationWidget.setObjectName("ConversationWidget")
        ConversationWidget.resize(681, 74)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConversationWidget.sizePolicy().hasHeightForWidth())
        ConversationWidget.setSizePolicy(sizePolicy)
        ConversationWidget.setMinimumSize(QtCore.QSize(0, 30))
        ConversationWidget.setStyleSheet("background: white;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(ConversationWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.online_label = QtWidgets.QLabel(ConversationWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.online_label.sizePolicy().hasHeightForWidth())
        self.online_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.online_label.setFont(font)
        self.online_label.setStyleSheet("color: green;")
        self.online_label.setAlignment(QtCore.Qt.AlignCenter)
        self.online_label.setObjectName("online_label")
        self.horizontalLayout.addWidget(self.online_label)
        self.conversation_name_label = QtWidgets.QLabel(ConversationWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.conversation_name_label.setFont(font)
        self.conversation_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.conversation_name_label.setObjectName("conversation_name_label")
        self.horizontalLayout.addWidget(self.conversation_name_label)
        self.not_readed_number_label = QtWidgets.QLabel(ConversationWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.not_readed_number_label.setFont(font)
        self.not_readed_number_label.setStyleSheet("color: red; margin: 5;")
        self.not_readed_number_label.setObjectName("not_readed_number_label")
        self.horizontalLayout.addWidget(self.not_readed_number_label)
        spacerItem1 = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(4, 1)

        self.retranslateUi(ConversationWidget)
        QtCore.QMetaObject.connectSlotsByName(ConversationWidget)

    def retranslateUi(self, ConversationWidget):
        _translate = QtCore.QCoreApplication.translate
        ConversationWidget.setWindowTitle(_translate("ConversationWidget", "Form"))
        self.online_label.setText(_translate("ConversationWidget", "Online"))
        self.conversation_name_label.setText(_translate("ConversationWidget", "conversationName"))
        self.not_readed_number_label.setText(_translate("ConversationWidget", "2"))
