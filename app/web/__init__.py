# -*- coding: utf-8 -*- 
# @Time : 2019/12/4 22:44 
# @Author : wuson
# @File : __init__.py
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish