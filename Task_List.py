from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QGraphicsView, \
    QCheckBox, QLayout, QPushButton, QSpacerItem, QSizePolicy

IMAGE_SIZE = QSize(20, 20)


class TaskElemBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # обьявления виджетов
        self.all_box_layout = QVBoxLayout()
        self.head_box_layout = QHBoxLayout()
        self.date_label = QLabel()
        self.spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding)
        self.spacer2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding)
        self.delete_button = QPushButton()
        self.task_elements_list = QListWidget()

        # настройка виджетов
        self.delete_button.setMaximumSize(25,23)
        self.delete_button.setText("X")
        self.delete_button.clicked.connect(self.delete_this_task_box)
        #self.delete_button.setVisible(False)
        self.task_elements_list.setIconSize(IMAGE_SIZE)
        self.task_elements_list.setMinimumHeight(125)
        self.task_elements_list.setMaximumHeight(125)

        # ставим их на свои места
        self.head_box_layout.addItem(self.spacer1)
        self.head_box_layout.addWidget(self.date_label)
        self.head_box_layout.addItem(self.spacer2)
        self.head_box_layout.addWidget(self.delete_button)

        self.all_box_layout.addItem(self.head_box_layout)
        self.all_box_layout.addWidget(self.task_elements_list)
        self.setLayout(self.all_box_layout)

    def compare(self, TaskElemBox):
        return self.get_data() == TaskElemBox.get_data()

    def size_hint(self):
        pass

    def set_date(self, date):
        self.date_label.setText(date)

    def get_data(self):
        return self.date_label.text()

    def add_elem(self, task_image, task_text, task_checked):
        elem = TaskElem()
        elem.set_task_check(task_checked)
        elem.set_text(task_text)

        item = QListWidgetItem(self.task_elements_list)
        item.setFlags(Qt.ItemIsDragEnabled)
        item.setIcon(task_image)
        item.setSizeHint(elem.sizeHint())

        self.task_elements_list.addItem(item)
        self.task_elements_list.setItemWidget(item, elem)

    def delete_this_task_box(self):
        self.delete_task_box()

    def delete_task_box(self, task_box=None):
        if(task_box == None):
            task_box = self
        task_list = task_box.parent().parent()
        item = None
        for i in range(0, task_list.count()):
            item = task_list.item(i) # получаем QlistWidgetItem
            if(task_box.compare(task_list.itemWidget(item)) == True):
                break
        #task_list.removeItemWidget(item)
        task_list.takeItem(i)


class TaskElem(QWidget):
    def __init__(self, parent=None):
        super(TaskElem, self).__init__(parent)
        # обьявления виджетов
        self.all_task_box = QHBoxLayout()
        self.task_text = QLabel()
        self.delete_button = QPushButton()
        self.task_check_box = QCheckBox()

        # настройка виджетов
        self.delete_button.setText("X")
        self.delete_button.setMaximumSize(23, 20)
        self.delete_button.clicked.connect(self.delete_task)
        #self.delete_button.setVisible(False)
        self.task_text.setMinimumSize(30, 14)
        self.task_text.setMaximumSize(199999, 14)


        self.all_task_box.setSizeConstraint(QLayout.SetMinimumSize)

        # ставим их на свои места
        self.all_task_box.addWidget(self.task_text)
        self.all_task_box.addStretch(2)
        self.all_task_box.addWidget(self.task_check_box)
        self.all_task_box.addWidget(self.delete_button)

        self.setLayout(self.all_task_box)

    def compare(self, TaskElem):
        return self.task_text == TaskElem.task_text

    def set_text(self, task_text):
        self.task_text.setText(task_text)

    def set_image(self, task_image_id):
        pass

    def set_task_check(self, task_checked):
        self.task_check_box.setChecked(task_checked)

    def delete_task(self):
        task_list = self.parent().parent()
        item = None
        for i in range(0, task_list.count()):
            item = task_list.item(i) # получаем QlistWidgetItem
            if(self.compare(task_list.itemWidget(item)) == True):
                break
        task_list.takeItem(i)
        if(task_list.count() == 0): # если задач в текущем дне нет удаляем его
            task_box = task_list.parent()
            task_box.delete_task_box(task_box)
        #task_list.removeItemWidget(item)
