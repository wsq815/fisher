# -*- coding: utf-8 -*- 
# @Time : 2019/12/14 11:39 
# @Author : wuson
# @File : test05.py

# 原理 字典 保存数据
# 操作数据
# werkzeug local local对象 字典

# LocalStack Local 字典
# Local 线程隔离对象，使用字典的方式实现的线程隔离
# LocalStack 线程隔离的栈结构
# 封装 如果一次分钟解决不了问题，那么就再来一次

import threading
import time
from werkzeug.local import Local

class A:
    b = 1

my_obj = Local()
my_obj.b = 1

def worker():
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))

new_t = threading.Thread(target=worker, name="wuson")
new_t.start()
time.sleep(1)
#主线程
print('in main thread b is:' + str(my_obj.b))