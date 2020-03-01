from PyQt5.QtWidgets import QDialog

import Dialog_add
import add_note_dialog
import edit_note_dialog
import connection_dialog


class AddTaskDialog(QDialog, Dialog_add.Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def hello(self):
        pass


class AddNoteDialog(QDialog, add_note_dialog.Ui_Dialog):
    """
    Вызывает диалоговое окно создания заметки.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class EditNoteDialog(QDialog, edit_note_dialog.Ui_Dialog):
    need_to_save = None

    def __init__(self, parent=None):
        """
        Вызывает диалоговое окно редактирования заметки

        """
        super().__init__(parent)
        self.setupUi(self)

    def start_input(self):
        """
        Привязывает события к полям для ввода
        """
        self.title_line.textChanged.connect(self.allow_to_save)
        self.note_text.textChanged.connect(self.allow_to_save)

    def allow_to_save(self):
        """
        Делает кнопку "Сохранить" доступной
        """
        self.save_button.setEnabled(True)

    def save(self):
        self.need_to_save = True
        self.close()

    def delete(self):
        self.need_to_save = False
        self.close()

    def exec(self):
        super().exec()
        if self.need_to_save:
            return "save"
        elif self.need_to_save is False:
            return "delete"
        elif self.need_to_save is None:
            return "cancel"


import server_connection


class ConnectDialog(QDialog, connection_dialog.Ui_Dialog):
    is_connected = False
    username = None
    password = None

    def __init__(self, flag_to_change=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_button.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        url = self.server_line.text()
        if (result := server_connection.check_connection(url,
                                           self.username_line.text(),
                                           self.password_line.text())) == 1:
            # Если соединение прошло
            self.label_3.setText("OK")
            self.is_connected = True
            self.username, self.password = self.username_line.text(), self.password_line.text()
        elif result == -1:  # requests.exceptions.MissingSchema
            self.label_3.setText("Ошибка в URL сервера")  # Изменения статуса подключения
        elif result == -2:  # requests.exceptions.InvalidURL
            self.label_3.setText("Ошибка в URL сервера")  # Изменения статуса подключения
        elif result == -3:  # requests.exceptions.ConnectionError
            self.label_3.setText("Ошибка при подключении к серверу")  # Изменения статуса подключения
        else:  # my_req.text != payload['username']
            self.label_3.setText(result)