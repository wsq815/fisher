# -*- coding: utf-8 -*- 
# @Time : 2019/12/10 22:22 
# @Author : wuson
# @File : book.py
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)