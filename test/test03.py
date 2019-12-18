# -*- coding: utf-8 -*- 
# @Time : 2019/12/14 10:10 
# @Author : wuson
# @File : test03.py
import threading
import time

# 字典
# request = {key1: value2, key2: value2...}
# 多线程 唯一标识
# request = {thread_key1: Request1, ...}
# id号
# 线程隔离

def worker():
    print('I am thread')
    t = threading.current_thread()
    time.sleep(100)
    print(t.getName())

new_t = threading.Thread(target = worker, name="wuson_thread")
new_t.start()

# 更充分的利用CPU的性能优势
# 异步编程
# python 不能充分利用多核CPU优势
# GIL 全局解释器锁 global interpreter lock
# 锁 线程安全

# 内存资源 一个进程 有多个线程 共享
# 线程不安全

 # 锁
 # 细粒度锁 程序员 主动加锁
 # 粗粒度锁 解释器 GIL 多核cpu 1个线程执行 一定程度上保证线程安全


t = threading.current_thread()
print(t.getName())
