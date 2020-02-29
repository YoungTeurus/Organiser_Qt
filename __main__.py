'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
'''

'''
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()
'''

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import table, dates, organaiser_test

'''class ExampleApp(QtWidgets.QMainWindow, table.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_2.clicked.connect(self.do_stuff)  # Присоединяю к кнопке функцию

    def do_stuff(self):
        """
        Вызывается при нажатии на левую кнопку
        """
        table_model = QtGui.QStandardItemModel()
        for j in range(1,4):
            row_of_items = list()
            for i in range(5):
                a = QtGui.QStandardItem(str(i*j))
                a.setCheckable(True)
                row_of_items.append(a)
            table_model.appendRow(row_of_items)
        table_model.setHorizontalHeaderLabels(["Первый", "Второй", "Третий",
                                               "Четвёртый", "Пятый"])
        table_model.setVerticalHeaderLabels(["A", "B", "C"])
        self.tableView.setModel(table_model)'''

'''class ExampleApp2(QtWidgets.QMainWindow, dates.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.do_stuff1)
        self.pushButton_2.clicked.connect(self.do_stuff2)

    def do_stuff1(self):
        a = self.dateEdit.dateTime().toString("dd MMMM yyyy")
        self.lineEdit.setText(a)

    def do_stuff2(self):
        a = QtCore.QDate.fromString(self.lineEdit.text(), "ddMMyyyy")
        self.dateEdit.setDate(a)'''

class ExampleOrganaiser(QtWidgets.QMainWindow, organaiser_test.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

def main():

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleOrganaiser()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()