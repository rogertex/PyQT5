#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 10:36
# @Author  : Roger
# @File    : OP_Menu.py
import sys
import Menu
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Menu.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())