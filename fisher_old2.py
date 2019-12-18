# @Time : 2019/11/30
# @Author : wuson
# @File : secure.py

from flask import Flask, jsonify
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
__author__ = 'wuson'

app = Flask(__name__)
app.config.from_object('config')

# http://t.yushu.im/v2/book/isbn/9787501524044
@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通关键字 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200 , {'content-type':'application/json'}




def helloo():
    return 'hello, wuson'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=app.config['DEBUG'])