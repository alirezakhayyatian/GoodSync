import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QProgressBar
import matplotlib
matplotlib.use("QT5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QThread
import random


print(os.getcwd())
Form = uic.loadUiType(os.path.join(os.getcwd(), 'gui.ui'))[0]


class IntroWindow(Form, QMainWindow):
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.arr = [[i,j] for i in range(8) for j in range(8)]
        self.generate.clicked.connect(self.generate_func)
        self.reset.clicked.connect(self.reset_func)
        self.fig = Figure()
        self.ax = self.fig.add_axes([0.1,0.1,0.8,0.8], frameon = False)
        self.canvas = FigureCanvas(self.fig)
        self.fig.patch.set_color('wheat')
        for i in range(9):
            self.line1, = self.ax.plot([0,8], [i,i],'r-.')

        for j in range(9):
            self.line2, = self.ax.plot([j,j], [0,8],'r-.')
            self.ver_lay2.addWidget(self.canvas)

    def generate_func(self):

        self.rand = random.randint(0, len(self.arr))
        selected = self.arr[self.rand]
        self.arr.remove(selected)
        print(type(self.ax))
        print(self.arr)
        progressbar = QProgressBar(self)
        self.ver_lay.addWidget(progressbar)
        self.ax.text(int(self.rand / 8) + 0.5,int(self.rand/8) +0.5, str(self.rand))
        progressbar.setValue(self.rand)
        self.fig.canvas.draw()
    def reset_func(self):
        print("SdfsdV")



app = QApplication(sys.argv)
w = IntroWindow()
w.show()
sys.exit(app.exec())
