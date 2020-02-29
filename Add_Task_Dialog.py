
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Dialog_add

class Add_Task_Dialog(QDialog, Dialog_add.Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


    def hello(self):
        pass


