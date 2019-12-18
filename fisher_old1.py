# @Time : 2019/11/30
# @Author : wuson
# @File : secure.py
from flask import Flask, make_response

__author__ = 'wuson'

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    #基于类的视图（即插视图）
    headers = {
        # 'content-type': 'text/plain',
        'content-type': 'application/json',
        'location': 'http://www.bind.com' #重定向地址
    }
    # response = make_response('<html><h1>hello Wuson</h1></html>',200)
    # response.headers = headers
    return '<html><h1>hello Wuson</h1></html>', 200, headers
# app.add_url_rule('/hello', view_func=hello)

def helloo():
    return 'hello, wuson'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=app.config['DEBUG'])