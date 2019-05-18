#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 12:58
# @Author  : Roger
# @File    : FirstMainWin.py


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class FirstWin(QMainWindow):
    def __init__(self):
        super(FirstWin,self).__init__()
        self.setWindowTitle('我的第一个窗口')
        self.resize(1000,500)
        self.status = self.statusBar()
        self.status.showMessage('我是谁',5000)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../icon/pycharm.ico'))
    mainWin = FirstWin()
    mainWin.show()
    sys.exit(app.exec_())
