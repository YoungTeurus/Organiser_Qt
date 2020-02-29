# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 465)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Task_list = QtWidgets.QFrame(self.centralwidget)
        self.Task_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Task_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Task_list.setObjectName("Task_list")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Task_list)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Task_head = QtWidgets.QFrame(self.Task_list)
        self.Task_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Task_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Task_head.setObjectName("Task_head")
        self.gridLayout_2.addWidget(self.Task_head, 0, 0, 1, 1)
        self.but_add = QtWidgets.QPushButton(self.Task_list)
        self.but_add.setObjectName("but_add")
        self.gridLayout_2.addWidget(self.but_add, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.Task_list)
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.Task_list, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_add.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
