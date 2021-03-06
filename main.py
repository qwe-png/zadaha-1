import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Шестая программа')
        self.pushButton = QPushButton('0-0', self)
        self.pushButton.move(40, 120)
        self.label2 = QLabel(self)
        self.label2.move(0, 0)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        tt = random.randint(1, 250)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(0, 0, tt, tt)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
