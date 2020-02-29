import sys

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import ui1 as ui

import Add_Task_Dialog # было
from Add_Task_Dialog import *# я хотел
from Task_List import *


class MyApp(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.but_add.clicked.connect(self.add_task)

    def add_task(self):
        add_task_message_box = Add_Task_Dialog()
        add_task_message_box.setModal(True)
        if(add_task_message_box.exec() == QDialog.Accepted):
            task_finded = False
            for i in range(0, self.listWidget.count()):
                item = self.listWidget.itemWidget(self.listWidget.item(i)) # получаем виджет из возвращенного QlistWidgetItem

                if item.get_data() == add_task_message_box.task_data.text():
                    e = item
                    task_finded = True
                    break
            if task_finded and self.listWidget.count() != 0:
                e.add_elem(QIcon("icon.png"), add_task_message_box.task_text.text(), False)
            else:
                e = Task_Elem_Box()
                print(self.listWidget.sizeHint().width())
                #e.setMaximumSize(self.listWidget.sizeHint().width(), 100)
                #e.setMinimumSize(self.listWidget.sizeHint().width(), 100)
                e.add_elem(QIcon("icon.png"), add_task_message_box.task_text.text(), False)
                e.set_data(add_task_message_box.task_data.text())
                item = QListWidgetItem(self.listWidget)
                item.setSizeHint(e.sizeHint())
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, e)


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main();
