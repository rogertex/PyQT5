#!/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 20:41
# @Author  : Roger
# @File    : test.py
class clseest():
    y = '我 '

    def __init__(self):
        self.y = '你'


x = clseest
print(x.y)  # 我

x = clseest()
print(x.y)  # 你