# -*- coding: utf-8 -*- 
# @Time : 2019/12/15 22:37 
# @Author : wuson
# @File : test08.py

# 以线程ID号作为key的字典 -> Local -> LocalStack

# AppContext RequestContext -> LocalStack

# Flask -> AppContext   Request -> RequestContext

# current_app -> (LocalStack.top = AppContext top.app = Falsk)

# request -> (LocalStack.top = RequestContext top.request = Request)