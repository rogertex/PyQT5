#!/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 22:33
# @Author  : Roger
# @File    : Icon_class.py
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QIcon

class example(QWidget):
    def __init__(self):
        super(example, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('第二个窗口')
        self.resize(300, 300)
        self.setWindowIcon(QIcon('../icon/pycharm.ico'))
        # self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = example()
    w.show()
    sys.exit(app.exec_())