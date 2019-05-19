#!/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 23:08
# @Author  : Roger
# @File    : Hint.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QToolTip,QPushButton
from PyQt5.QtGui import QIcon, QFont


class example(QWidget):
    def __init__(self):
        super(example, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget.')
        btn = QPushButton('pushbutton', self)
        btn.setToolTip('This is a <b>Pushbutton</b> widget.')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('the first tooltip demo')



app = QApplication(sys.argv)
a = example()
a.show()
sys.exit(app.exec_())


