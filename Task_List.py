from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QGraphicsView, \
    QCheckBox, QLayout

IMAGE_SIZE = QSize(20, 20)

class TaskElemBox(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        # обьявления виджетов
        self.all_box_layout = QVBoxLayout()
        self.data_label = QLabel()
        self.task_elemenst_list = QListWidget()

        # настройка виджетов

        self.task_elemenst_list.setIconSize(IMAGE_SIZE)
        self.task_elemenst_list.setMinimumHeight(120)
        self.task_elemenst_list.setMaximumHeight(120)

        # ставим их на свои места
        self.all_box_layout.addWidget(self.data_label)
        self.all_box_layout.addWidget(self.task_elemenst_list)
        self.setLayout(self.all_box_layout)
        size = self.all_box_layout.sizeHint()

    def size_hint(self):
        pass

    def set_data(self, data):
        self.data_label.setText(data)

    def get_data(self):
        return self.data_label.text()

    def add_elem(self, task_image, task_text, task_checked):
        elem = Task_Elem()
        elem.set_task_check(task_checked)
        elem.set_text(task_text)

        item = QListWidgetItem(self.task_elemenst_list)
        item.setFlags(Qt.ItemIsDragEnabled)
        item.setIcon(task_image)
        item.setSizeHint(elem.sizeHint())

        self.task_elemenst_list.addItem(item)
        self.task_elemenst_list.setItemWidget(item, elem)


class Task_Elem(QWidget):
    def __init__(self, parent=None):

        super(Task_Elem, self).__init__(parent)
        # обьявления виджетов
        self.task_elem = QHBoxLayout()
        self.task_text = QLabel()
        self.task_image = QGraphicsView()
        self.task_check_box = QCheckBox()

        # настройка виджетов
        self.task_image.setMaximumSize(10, 10)
        self.task_text.setMinimumSize(30, 14)
        self.task_text.setMaximumSize(199999, 14)
        self.task_elem.setSizeConstraint(QLayout.SetMinimumSize)

        # ставим их на свои места
        self.task_elem.addWidget(self.task_image)
        self.task_elem.addWidget(self.task_text)
        self.task_elem.addWidget(self.task_check_box)

        self.setLayout(self.task_elem)

    def set_text(self, task_text):
        self.task_text.setText(task_text)

    def set_image(self, task_image_id):
        pass

    def set_task_check(self, task_checked):
        self.task_check_box.setChecked(task_checked)