# -*- coding: utf-8 -*- 
# @Time : 2019/12/4 22:13 
# @Author : wuson
# @File : book.py

# 蓝图 blueprint 蓝本

# http://t.yushu.im/v2/book/isbn/9787501524044
from flask import jsonify, request, render_template, flash

from app.spider import yushu_book
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookCollection
import json

@web.route('/book/search')
def search():
    """
        q: 普通关键字 isbn
        page
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
         # a = request.args.to_dict() #转为可变字典
         # 验证层
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
        # return jsonify(books.__dict__)
    else:

        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 18
    }
    flash('hello, wuson')
    flash('hello, qiyue')
    # 模板 html
    return render_template('test.html', data=r)