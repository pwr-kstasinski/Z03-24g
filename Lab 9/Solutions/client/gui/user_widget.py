# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserWidget(object):
    def setupUi(self, UserWidget):
        UserWidget.setObjectName("UserWidget")
        UserWidget.resize(543, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserWidget.sizePolicy().hasHeightForWidth())
        UserWidget.setSizePolicy(sizePolicy)
        UserWidget.setStyleSheet("background: white; border: 1px solid black;")
        self.gridLayout = QtWidgets.QGridLayout(UserWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(UserWidget)
        self.widget.setStyleSheet("border: 1px solid lightgrey;")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.online_label = QtWidgets.QLabel(self.widget)
        self.online_label.setEnabled(True)
        self.online_label.setStyleSheet("color: green; border: none;")
        self.online_label.setObjectName("online_label")
        self.horizontalLayout_2.addWidget(self.online_label)
        self.name_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("border: none")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("margin: 10px;border: 1px solid black;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 6)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(UserWidget)
        QtCore.QMetaObject.connectSlotsByName(UserWidget)

    def retranslateUi(self, UserWidget):
        _translate = QtCore.QCoreApplication.translate
        UserWidget.setWindowTitle(_translate("UserWidget", "Form"))
        self.online_label.setText(_translate("UserWidget", "Online"))
        self.name_label.setText(_translate("UserWidget", "userName"))
        self.pushButton.setText(_translate("UserWidget", "Open"))
