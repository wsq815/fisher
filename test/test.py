# -*- coding: utf-8 -*- 
# @Time : 2019/12/11 20:56 
# @Author : wuson
# @File : test.py

from flask import Flask, current_app

app = Flask(__name__)

#应用上下文 对象 Flask
#请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
#离线应用、单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()


with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']


#with
# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器
#

# 1. 连接数据库  __enter__
# 2. sql
# 3. 释放资源   __exit__

#文件读写
# try:
#     f = open(r'D:\t.txt')
#     print(f.read())
# finally:
#     f.close()
# #改写
# with open(r'') as f:
#     print(f.read())

class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource conenction')
        return False
        #返回False将不会抛出异常
        #返回True将抛出异常

    def query(self):
        print('query data')
with MyResource() as resource:
    1/0
    resource.query()