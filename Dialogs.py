from PyQt5.QtWidgets import QDialog

import Dialog_add
import add_note_dialog, edit_note_dialog


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
    """
    Вызывает диалоговое окно редактирования заметки
    """

    need_to_save = False

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def save(self):
        self.need_to_save = True
        self.close()

    def delete(self):
        self.close()

    def exec(self):
        super().exec()
        if self.need_to_save:
            return "save"
        else:
            return "delete"