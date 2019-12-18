# -*- coding: utf-8 -*- 
# @Time : 2019/12/15 15:50 
# @Author : wuson
# @File : test06.py

from werkzeug.local import LocalStack

# push、pop、top
# 数据结构 限制某些能力

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

