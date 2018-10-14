# -*- coding: utf-8 -*-
import sys
import math
# Импортируем наш интерфейс из файла
from Form import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from MyMplCanc import MtMplCanv
import math_part
from numpy import float64
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets, QtGui, QtCore
from MyMplCanc import MtMplCanv
from matplotlib.figure import Figure
class MyWin(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.sec_win = None
        self.figure = Figure()

        # добавление шаблона размещения на виджет
        self.companovka_for_mpl = QtWidgets.QVBoxLayout(self.Widget)
        # получение объекта класса холста с нашим рисунком

        self.canvas = MtMplCanv(self.figure)
        # Размещение экземпляра класса холста в шаблоне размещения
        self.companovka_for_mpl.addWidget(self.canvas)
        # получение объекта класса панели управления холста
        self.toolbar = NavigationToolbar(self.canvas, self)
        # Размещение экземпляра класса панели управления в шаблоне размещения
        self.companovka_for_mpl.addWidget(self.toolbar)
        # Здесь прописываем событие нажатия на кнопку
        self.pushButton.clicked.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        p = float64(self.textEdit.toPlainText())
        v = float64(self.textEdit_2.toPlainText())
        y = float64(self.textEdit_3.toPlainText())
        k = float64(self.textEdit_4.toPlainText())
        c = float64(self.textEdit_5.toPlainText())

        u10 = float64(self.textEdit_6.toPlainText())
        u20 = float64(self.textEdit_7.toPlainText())
        x0 = float64(self.textEdit_10.toPlainText())

        eps = float64(self.textEdit_8.toPlainText())
        d = float64(self.textEdit_9.toPlainText())
        step = float64(self.textEdit_11.toPlainText())
        
        self.sec_win = second_window(self)
        math_part.mathpart.building(self, p, v, y, k, c, u10, u20, eps, d, x0, step)
        self.sec_win.show()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
