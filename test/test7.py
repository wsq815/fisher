# -*- coding: utf-8 -*- 
# @Time : 2019/12/15 16:00 
# @Author : wuson
# @File : test7.py
import threading
import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)
print('it is main thread stack '+ str(my_stack.top))

def worker():
    print('in new thread before push. value is:' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread after push, value is:' + str(my_stack.top))

new_t = threading.Thread(target= worker)
new_t.start()
time.sleep(1)

print('finally, in main thread value is:' + str(my_stack.top))