"""
Программа "Органайзер для студента".
Подготовила команда "BOLT" специально для весеннего Хакатона 2020.

https://github.com/YoungTeurus/Organiser_Qt
"""
import sys  # sys нужен для передачи argv в QApplication
import json
from datetime import datetime as dt

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
import organaiser_test2
import server_connection
from Dialogs import AddTaskDialog, QDialog, AddNoteDialog, EditNoteDialog, ConnectDialog
from Task_List import TaskElemBox, QListWidgetItem

"""data = {
    "settings": {
            "last_server": "http://localhost:80"
        },
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
            {"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
             "cabinet": "315"},
            {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd", "teacher": "prepod2",
             "cabinet": "215"},
            {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
             "cabinet": "115"},
        ],
        "Вторник": [{"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
                     "cabinet": "315"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd",
                     "teacher": "prepod2",
                     "cabinet": "215"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
                     "cabinet": "115"},
                    ],
        "Среда": [{"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
                   "cabinet": "315"},
                  {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd",
                   "teacher": "prepod2",
                   "cabinet": "215"},
                  {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
                   "cabinet": "115"},
                  ],
        "Четверг": [{"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
                     "cabinet": "315"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd",
                     "teacher": "prepod2",
                     "cabinet": "215"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
                     "cabinet": "115"},
                    ],
        "Пятница": [{"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
                     "cabinet": "315"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd",
                     "teacher": "prepod2",
                     "cabinet": "215"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
                     "cabinet": "115"},
                    ],
        "Суббота": [{"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
                     "cabinet": "315"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd",
                     "teacher": "prepod2",
                     "cabinet": "215"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
                     "cabinet": "115"},
                    ],
        "Воскресенье": [{"number": "1", "time": "8.00-9.35", "name": "Математика", "type": "always", "teacher": "prepod1",
                     "cabinet": "315"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика практика", "type": "odd",
                     "teacher": "prepod2",
                     "cabinet": "215"},
                    {"number": "2", "time": "9.45-11.20", "name": "Физика лекция", "type": "even", "teacher": "prepod2",
                     "cabinet": "115"},
                    ],
    },
    "tasks": [
        {
            "title": "Priyti na hackaton",
            "date": "28.02.2020",
            "done": True,
            "img_id": 2
        },
        {
            "title": "Rgr po VSEMU",
            "date": "3.03.2020",
            "done": False,
            "img_id": 1
        }
    ]
}"""

data = {}

# Та data, которая будет создана при отсутствии data.json
first_settings = {
    "settings":
        {
            "last_server": "http://localhost:80",
        },
    "notes": [],
    "schedule": {},
    "tasks": []
}

days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")


class ExampleOrganaiser(QtWidgets.QMainWindow, organaiser_test2.Ui_MainWindow):
    tables = []  # Список таблиц для расписания
    date_for_task = QDate()
    is_Online = False  # Имеется ли подключение к серверу в данной сессии
    username = None
    password = None
    server = None

    def __init__(self):
        super().__init__()
        # Дизайн модели и связывание событий
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.add_task_button.clicked.connect(self.add_task)  # Добавление задачи
        self.add_note_button.clicked.connect(self.add_note)  # Добавление заметки
        self.notes_list.doubleClicked.connect(self.edit_note)  # Редактирование заметки
        self.sync_action.triggered.connect(self.sync_up)  # Пунет меню "Синхронизировать" записывает data в файл
        self.calendarWidget.selectionChanged.connect(self.set_date_for_task)  # Выделение даты в календаре
        self.exit_action.triggered.connect(self.close)  # Пункт меню "Выход" заканчивает выполнение приложения
        self.connect_action.triggered.connect(self.connect_to_server)  # Пункт меню "Подключение к серверу"

        # Всё, связанное с синхронизацией
        self.sync_down()  # Первоначальная синхронизация

        # Временный дебаг:
        self.delete_task_button.setText("Скачать с сервера")
        # self.delete_task_button.clicked.connect(lambda: print(data["tasks"]))
        self.delete_task_button.clicked.connect(self.sync_down)
        # Всё временное лучше вставлять выше.

    def add_task(self):
        """
        Добавляет задачу в data.
        """
        add_task_message_box = AddTaskDialog()
        add_task_message_box.setModal(True)
        add_task_message_box.task_date.setDate(self.date_for_task)  # Установка начального значения даты
        if add_task_message_box.exec() == QDialog.Accepted:
            task_finded = False

            ind_oldest_item = 0
            oldest_item = self.tasks_list.itemWidget(self.tasks_list.item(0))
            for i in range(0, self.tasks_list.count()):
                item = self.tasks_list.itemWidget(
                    self.tasks_list.item(i))  # получаем виджет из возвращенного QlistWidgetItem

                def to_date(str_date):
                    return dt.strptime(str_date, '%d.%m.%Y')

                # в oldest_item храним задачу, после которой вставляем
                if (to_date(oldest_item.get_data()) <= to_date(add_task_message_box.task_date.text())
                        and to_date(oldest_item.get_data()) <= to_date(item.get_data()) <= to_date(
                            add_task_message_box.task_date.text())):
                    ind_oldest_item = i + 1
                    oldest_item = item

                if item.get_data() == add_task_message_box.task_date.text():
                    e = item
                    task_finded = True
                    break
            # Собственно добавление задачи в data
            a = dict(
                title=add_task_message_box.task_text.text(), date=add_task_message_box.task_date.text(),
                done=False, img_id=1
            )  # Добавляемый словарь в словарь
            data["tasks"].append(a)
            # если уже создана коробка с нужной датой, добавим к ней, иначе делаем новую
            if task_finded and self.tasks_list.count() != 0:
                e.add_elem(QIcon("icon.png"), add_task_message_box.task_text.text(), False, self.set_checked_for_task,
                           self.delete_task_from_data, a)
            else:
                e = TaskElemBox()
                e.add_elem(QIcon("icon.png"), add_task_message_box.task_text.text(), False, self.set_checked_for_task,
                           self.delete_task_from_data, a)
                e.set_date(add_task_message_box.task_date.text())

                item = QListWidgetItem()
                item.setSizeHint(e.sizeHint())
                self.tasks_list.insertItem(ind_oldest_item, item)
                self.tasks_list.setItemWidget(item, e)
            self.tasks_list.sortItems(True)

    def update_tasks(self):
        """
        Обновляет список задач, подгружая их из data.
        В текущей реализации очищает весь список перед загрузкой.
        """
        self.tasks_list.clear()
        for task in data["tasks"]:
            # Код ниже был скопирован из add_task
            task_finded = False
            for i in range(0, self.tasks_list.count()):
                item = self.tasks_list.itemWidget(
                    self.tasks_list.item(i))  # получаем виджет из возвращенного QlistWidgetItem

                if item.get_data() == task["date"]:
                    e = item
                    task_finded = True
                    break
            if task_finded and self.tasks_list.count() != 0:
                e.add_elem(QIcon("icon.png"), task["title"], task["done"], self.set_checked_for_task,
                           self.delete_task_from_data, task)
            else:
                e = TaskElemBox()
                e.add_elem(QIcon("icon.png"), task["title"], task["done"], self.set_checked_for_task,
                           self.delete_task_from_data, task)
                e.set_date(task["date"])

                item = QListWidgetItem(self.tasks_list)
                item.setSizeHint(e.sizeHint())
                self.tasks_list.addItem(item)
                self.tasks_list.setItemWidget(item, e)
            # Нужно как-то добавить связь события checked у "галочки" с функцией "поменять в data переменную "done"".
            # a = e.task_elements_list.items
            # a = e.task_elements_list.itemWidget(внутри или e.task_elements_list.item()
            # или e.task_elements_list.indexAt())
            # в а будет нужный элем от кот возьмем галочку дальше
            # a = e.task_elements_list  # Получили список задач
            # print(a.indexAt(0))  # Получаем первый элемент(?!)
            # print(a)
            # print(a.task_check_box.isChecked())

    def set_checked_for_task(self, obj):
        obj.ptr_to_data["done"] = obj.task_check_box.isChecked()

    def delete_task_from_data(self, obj):
        global data
        data["tasks"].remove(obj.ptr_to_data)

    def add_note(self):
        """
        Добавляет заметку в data.
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

    def setup_schedule(self):
        """
        Первоначальная настройка таблицы расписания.
        Очищает все таблицы, задаёт название столбиков
        """
        self.tables.clear()  # Очищаем список таблиц
        self.tables.append(self.schedule_table_1)
        self.tables.append(self.schedule_table_2)
        self.tables.append(self.schedule_table_3)
        self.tables.append(self.schedule_table_4)
        self.tables.append(self.schedule_table_5)
        self.tables.append(self.schedule_table_6)
        self.tables.append(self.schedule_table_7)
        for table in self.tables:
            table.clear()  # Очищаем сами таблицы
            horizontalheaderlabels = ["Пара", "Время", "Наименование предмета", "Преподаватель", "Кабинет"]
            table.setColumnCount(horizontalheaderlabels.__len__())  # Всего 5 столбиков
            table.setHorizontalHeaderLabels(horizontalheaderlabels)
            table.resizeColumnsToContents()
        self.update_schedule()

    def update_schedule(self):
        """
        Обновление таблицы расписания.
        Заполняет таблицу данными из data
        """
        num_of_days = len(days)  # Количество дней в неделе
        for day in range(num_of_days):
            current_table = self.tables[day]  # Текущая таблица
            cur_day_schedule = data["schedule"][days[day]]  # Текущая "база данных" таблицы
            num_of_par = len(cur_day_schedule)  # Количество пар
            current_table.setRowCount(num_of_par)  # Устанавливаем количество строк
            for para in range(num_of_par):  # Заполняем таблицу
                # Если в data есть две записи на одну пару, то объединяем эти ячейки
                if para > 0 and cur_day_schedule[para]["number"] == cur_day_schedule[para - 1]["number"]:
                    current_table.setSpan(para - 1, 0, 2, 1)  # Объединяем пары
                    current_table.setSpan(para - 1, 1, 2, 1)  # Объединяем время
                else:
                    # Установка номера пары и времени
                    current_table.setItem(para, 0, QTableWidgetItem(cur_day_schedule[para]["number"]))
                    current_table.setItem(para, 1, QTableWidgetItem(cur_day_schedule[para]["time"]))
                current_table.setItem(para, 2, QTableWidgetItem(cur_day_schedule[para]["name"]))
                current_table.setItem(para, 3, QTableWidgetItem(cur_day_schedule[para]["teacher"]))
                current_table.setItem(para, 4, QTableWidgetItem(cur_day_schedule[para]["cabinet"]))
                current_table.setItem(para, 4, QTableWidgetItem(cur_day_schedule[para]["cabinet"]))

            # Код ниже нужен, чтобы избавиться от подписи строчек
            blank_labels = []
            for i in range(num_of_par):
                blank_labels.append("")
            current_table.setVerticalHeaderLabels(blank_labels)
            current_table.resizeColumnsToContents()

    def sync_down(self):
        """
        Загрузка информации с сервера.
        В данной реализации - из файла.
        """
        if self.is_Online:
            # Здесь скачивание .json файла с сервера
            server_connection.download_file(self.server, self.username, self.password, "data.json")

        # Чтение локальной версии json файла
        try:
            with open("data.json", "r") as read_file:
                global data
                data = json.load(read_file)
        except FileNotFoundError:  # Если такого файла нет
            data.update(first_settings)  # Подгружаем первоначальную data
        self.update_notes()  # Обновляем список заметок (загружаем начальный вид)
        self.setup_schedule()  # Задаём начальный вид расписанию
        self.update_tasks()

    def sync_up(self):
        """
        Выгрузка информации на сервер.
        В данной реализации - в файл.
        """
        # Запись локальной версии json файла
        with open("data.json", "w") as write_file:
            json.dump(data, write_file, indent=4)

        if self.is_Online:
            # Здесь отправка .json файла на сервер
            if server_connection.check_connection(self.server, self.username,self.password) == 1:
                server_connection.upload_json_file(self.server, "data.json")

    def set_date_for_task(self):
        """
        Устанавливает дату по умолчанию (то есть, она будет выбрана сразу же) для задачи.
        """
        self.date_for_task = self.calendarWidget.selectedDate()

    def connect_to_server(self):
        """
        Запускает диалог подключения к серверу.
        :return:
        """
        connect_dialog = ConnectDialog()
        connect_dialog.setModal(True)
        connect_dialog.server_line.setText(data["settings"]["last_server"])
        connect_dialog.exec()
        self.is_Online = connect_dialog.is_connected  # Получаем статус подключения к серверу
        if self.is_Online:
            self.username, self.password, self.server = connect_dialog.username, connect_dialog.password, connect_dialog.server_line.text()
        # print(self.username, self.password)
        pass

    def close(self):
        """
        Заготовка для реализации синхронизации данных перед выходом.
        """
        pass  # Заменить на синхронизацию
        super().close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleOrganaiser()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
