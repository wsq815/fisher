# -*- coding: utf-8 -*- 
# @Time : 2019/12/11 20:12 
# @Author : wuson
# @File : book.py

#sqlalchemy
#Flask_SQLAlchemy
#WTFOROMS
#Flask_WTFORMS
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# ORM 对象关系映射    Code first
class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
