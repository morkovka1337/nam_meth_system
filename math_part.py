import math
import pylab
from numpy import float64
from matplotlib import mlab
from matplotlib.figure import Figure
from label_for_graphic import Ui_MainWindow
from tab_widg import Ui_MainWindow_tab
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from main import MyWin
from main import second_window

class mathpart(Ui_MainWindow):
    def building(self, p, v, y, k, c, u10, u20, eps, d, x0, step):
        def du1(u1, u2):
            nonlocal p, y, k
            return p + k * (u1**2 /u2) - y * u1

        def du2(u1, u2):
            nonlocal c, v
            return c * (u1**2) - v * u2
        
        def next_point(x, v1, v2, step):
            
            x_new = x + step
            k11 = du1(v1, v2)
            k12 = du1(v1 + step * k1 / 3, v2 + step * k11 / 3)
            k13 = du1(v1 + step * (k11 + k12) / 6, v2 + step * (k11 + k12) / 6)
            k14 = du1(v1 + step * (k11 + 3*k13)/8, v1 + step * (k11 + 3*k13)/8)
            k15 = du1(v1 + step*(k11-3*k13+4*k14)/2, v2 + step*(k11-3*k13+4*k14)/2)

            k21 = du2(v1, v2)
            k22 = du2(v1 + step * k1 / 3, v2 + step * k11 / 3)
            k23 = du2(v1 + step * (k11 + k12) / 6, v2 + step * (k11 + k12) / 6)
            k24 = du2(v1 + step * (k11 + 3*k13)/8, v2 + step * (k11 + 3*k13)/8)
            k25 = du2(v1 + step*(k11-3*k13+4*k14)/2, v2 + step*(k11-3*k13+4*k14)/2)

            s1 = step*(2*k11 - 9*k13 + 8*k14 - k15)/30
            s2 = step*(2*k21 - 9*k23 + 8*k24 - k25)/30

            v1_new = v + step*(k11 + 4*k14 + k15)
            v2_new = v + step*(k21 + 4*k24 + k25)

            if self.checkBox.isChecked():
                
                if abs(s1) >= eps/16 and abs(s2) >= eps/16 and abs(s1) <= eps and abs(s2) <= eps:
                    return x_new, v1_new, v2_new
                elif abs(s1) > eps or abs(s2) > eps:
                    nonlocal step
                    step /= 2
                    return next_point_v(x, v1, v2, step)
                elif elif abs(s1) < eps/16 and abs(s2) < eps/16:
                    nonlocal step
                    step *= 2
                    return x_new, v1_new, v2_new
                else: 
                    return x_new, v1_new, v2_new
                    
            else: 
                return x_new, v1_new, v2_new
        self.progressBar.setMinimum(x0)
        self.progressBar.setMaximum(d)
        ax_1 = self.figure_1.add_subplot(111)
        ax_2 = self.figure_2.add_subplot(111)
        if self.checkBox2.isChecked():
            ax_1.clear()
            ax_2.clear()
        ax_1.axis([-5, 10, -5, 20])
        ax_2.axis([-5, 10, -5, 20])
        v1, v2 = u10, u20
        x = x0
        while x < d:
            x_old, v1_old, v2_old = x, v1, v2
            x, v1, v2 = next_point_v(x, v1, v2, step)
            self.progressBar.setValue(d-x)
            ax_1.plot([x_old, x], [v1_old, v1], '-r')
            ax_2.plot([x_old, x], [v2_old, v2], '-r')
            
        
        