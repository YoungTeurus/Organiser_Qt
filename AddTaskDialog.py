from PyQt5.QtWidgets import QDialog

import Dialog_add


class AddTaskDialog(QDialog, Dialog_add.Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def hello(self):
        pass
