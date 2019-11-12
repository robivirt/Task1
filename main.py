from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(100, 600)
        y = randint(100, 600)
        diametre = randint(20, 80)
        qp.drawEllipse(x, y, diametre, diametre)



app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
