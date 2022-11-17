import sqlite3
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('main.ui', self)
        self.init_ui()

    def init_ui(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute('select * from coffee').fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                print(elem)
                if isinstance(elem, int):
                    elem = str(elem)
                item = QTableWidgetItem(elem)
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
