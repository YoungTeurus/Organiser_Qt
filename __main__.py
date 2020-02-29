import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

import organaiser_test2
from AddTaskDialog import AddTaskDialog, QDialog
from Task_List import TaskElemBox, QListWidgetItem


class ExampleOrganaiser(QtWidgets.QMainWindow, organaiser_test2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.add_task_button.clicked.connect(self.add_task)

    def add_task(self):
        add_task_message_box = AddTaskDialog()
        add_task_message_box.setModal(True)

        if add_task_message_box.exec() == QDialog.Accepted:
            e = TaskElemBox()
            e.set_data(add_task_message_box.task_data.text())
            e.add_elem(QIcon("icon.png"), add_task_message_box.task_text.text(), True)

            item = QListWidgetItem(self.tasks_list)
            item.setSizeHint(e.sizeHint())
            self.tasks_list.addItem(item)
            self.tasks_list.setItemWidget(item, e)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleOrganaiser()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
