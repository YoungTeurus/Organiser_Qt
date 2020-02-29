# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_add.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 148)
        Dialog.setModal(True)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.task_data = QtWidgets.QDateEdit(Dialog)
        self.task_data.setMinimumSize(QtCore.QSize(70, 20))
        self.task_data.setMaximumSize(QtCore.QSize(100, 20))
        self.task_data.setObjectName("task_data")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.task_data)
        self.label_text = QtWidgets.QLabel(Dialog)
        self.label_text.setObjectName("label_text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_text)
        self.label_data = QtWidgets.QLabel(Dialog)
        self.label_data.setObjectName("label_data")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_data)
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setObjectName("label_image")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_image)
        self.image_box = QtWidgets.QComboBox(Dialog)
        self.image_box.setObjectName("image_box")
        self.image_box.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.image_box)
        self.task_text = QtWidgets.QLineEdit(Dialog)
        self.task_text.setMinimumSize(QtCore.QSize(140, 20))
        self.task_text.setObjectName("task_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.task_text)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_text.setText(_translate("Dialog", "Текст задачи"))
        self.label_data.setText(_translate("Dialog", "Крайняя дата выполнения задачи"))
        self.label_image.setText(_translate("Dialog", "Иконка задачи"))
        self.image_box.setItemText(0, _translate("Dialog", "картиночка 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
