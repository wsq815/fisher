# @Time : 2019/11/30
# @Author : wuson
# @File : secure.py

from app import create_app

__author__ = 'wuson'

app = create_app()



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=app.config['DEBUG'], threaded=True)
    # 单进程、多线程
    # 多请求

    #开启多进程 processes = 1