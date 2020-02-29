import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

import organaiser_test2
from Dialogs import AddTaskDialog, QDialog, AddNoteDialog, EditNoteDialog
from Task_List import TaskElemBox, QListWidgetItem

data = {
    "notes": [
        {
            "title": "My title",
            "text": "My text"
        },
        {
            "title": "My title",
            "text": "My text"
        },
    ],
    "schedule": {
        "Понедельник": [
            {"number": 1, "name": "Математика", "type": "always", "teacher": "prepod1", "cabinet": "315"},
            {"number": 2, "name": "Физика практика", "type": "odd", "teacher": "prepod2", "cabinet": "215"},
            {"number": 2, "name": "Физика лекция", "type": "even", "teacher": "prepod2", "cabinet": "115"},
        ],
        "Вторник": [],
        "Среда": [],
        "Четверг": [],
        "Пятница": []
    }
}


class ExampleOrganaiser(QtWidgets.QMainWindow, organaiser_test2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.add_task_button.clicked.connect(self.add_task)
        self.add_note_button.clicked.connect(self.add_note)
        self.notes_list.doubleClicked.connect(self.edit_note)
        self.update_notes()

    def add_task(self):
        """
        Добавляет задачу в список задач.
        """
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

    def add_note(self):
        """
        Добавляет заметку в список заметок.
        """
        add_note_dialog = AddNoteDialog()
        add_note_dialog.setModal(True)
        if add_note_dialog.exec() == QDialog.Accepted:
            data["notes"].append(dict(
                title=str(add_note_dialog.title_line.text()),
                text=str(add_note_dialog.note_text.toPlainText())
            ))
            # self.notes_list.addItem(str(add_note_dialog.title_line.text()))
            self.update_notes()

    def update_notes(self):
        """
        Обновляет список записок, подгружая их из data.
        """
        self.notes_list.clear()
        for note in data["notes"]:
            self.notes_list.addItem(note["title"])

    def edit_note(self):
        """
        Запуск диалога изменения заметки
        """
        # print("row {}".format(self.notes_list.currentRow()))
        edit_note_dialog = EditNoteDialog()

        # Установка заголовка и текста заметки
        note_to_edit = data["notes"][self.notes_list.currentRow()]
        edit_note_dialog.title_line.setText(note_to_edit["title"])
        edit_note_dialog.note_text.setText(note_to_edit["text"])

        edit_note_dialog.setModal(True)
        edit_note_dialog.start_input()  # Начинаем реагировать на события с данного момента
        if (state := edit_note_dialog.exec()) == "save":
            note_to_edit["title"] = str(edit_note_dialog.title_line.text())
            note_to_edit["text"] = str(edit_note_dialog.note_text.toPlainText())
        elif state == "delete":
            data["notes"].remove(note_to_edit)
        elif state == "cancel":
            return
        self.update_notes()

    def update_schedule(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleOrganaiser()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
