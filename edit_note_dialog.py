# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Work\Organiser_Qt\edit_note_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 278)
        self.title_line = QtWidgets.QLineEdit(Dialog)
        self.title_line.setGeometry(QtCore.QRect(120, 10, 261, 20))
        self.title_line.setObjectName("title_line")
        self.note_text = QtWidgets.QTextEdit(Dialog)
        self.note_text.setGeometry(QtCore.QRect(10, 40, 371, 201))
        self.note_text.setObjectName("note_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 243, 371, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_button.setEnabled(False)
        self.save_button.setCheckable(False)
        self.save_button.setAutoRepeatDelay(298)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.delete_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.note_text.raise_()
        self.title_line.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        self.save_button.clicked.connect(Dialog.save)
        self.delete_button.clicked.connect(Dialog.delete)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название заметки"))
        self.save_button.setText(_translate("Dialog", "Сохранить изменения"))
        self.delete_button.setText(_translate("Dialog", "Удалить заметку"))
