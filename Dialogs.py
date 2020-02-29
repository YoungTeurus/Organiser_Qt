from PyQt5.QtWidgets import QDialog

import Dialog_add
import add_note_dialog
import edit_note_dialog


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
