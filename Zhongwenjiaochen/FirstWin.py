#!/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 21:56
# @Author  : Roger
# @File    : FirstWin.py

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QIcon
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    # w.setWindowIcon(QIcon('../Icon/pycharm.ico'))
    w.setWindowTitle('第一个窗口')
    w.show()
    sys.exit(app.exec_())