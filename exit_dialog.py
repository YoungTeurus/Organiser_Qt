# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Work\Organiser_Qt\exit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 99)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_always_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(9)
        self.yes_always_button.setFont(font)
        self.yes_always_button.setObjectName("yes_always_button")
        self.horizontalLayout.addWidget(self.yes_always_button)
        self.yes_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(9)
        self.yes_button.setFont(font)
        self.yes_button.setObjectName("yes_button")
        self.horizontalLayout.addWidget(self.yes_button)
        self.no_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(9)
        self.no_button.setFont(font)
        self.no_button.setObjectName("no_button")
        self.horizontalLayout.addWidget(self.no_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(9)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.yes_button.clicked.connect(Dialog.accept)
        self.no_button.clicked.connect(Dialog.reject)
        self.cancel_button.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выход из программы"))
        self.label.setText(_translate("Dialog", "Желаете синхронизировать данные перед выходом?"))
        self.yes_always_button.setText(_translate("Dialog", "Да, всегда"))
        self.yes_button.setText(_translate("Dialog", "Да"))
        self.no_button.setText(_translate("Dialog", "Нет"))
        self.cancel_button.setText(_translate("Dialog", "Отмена"))
