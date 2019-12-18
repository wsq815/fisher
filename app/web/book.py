# -*- coding: utf-8 -*- 
# @Time : 2019/12/4 22:13 
# @Author : wuson
# @File : book.py

# 蓝图 blueprint 蓝本

# http://t.yushu.im/v2/book/isbn/9787501524044
from flask import jsonify, request

from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm

@web.route('/test')
def test1():
    from flask import request
    from app.libs.node_local import n
    print(n.v)
    n.v = 2
    print('-------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-------')
    return ''

@web.route('/book/search')
def search():
    """
        q: 普通关键字 isbn
        page
    """
    form = SearchForm(request.args)

    if form.validate():
         # a = request.args.to_dict() #转为可变字典
         # 验证层
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200 , {'content-type':'application/json'}