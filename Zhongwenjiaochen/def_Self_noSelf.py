#!/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 23:19
# @Author  : Roger
# @File    : def_Self_noSelf.py
class A(object):
    def go(self):
        num = 1
        print(num)
class B(object):
    def go(self):
        self.num = 1
        # print(self.num)


a = A()
a.go()

b = B()
b.go()
print(b.num)
