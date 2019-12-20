# -*- coding: utf-8 -*- 
# @Time : 2019/12/18 20:58 
# @Author : wuson
# @File : book.py

class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda X: True if X else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)

class BookCollection:
    def _init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

class _BookViewModel:
    # 描述特征（类变量、实例变量）
    # 行为（方法）
    def package_single(self, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [self.__cut_book_data(data)]
        return returned

    def package_collection(self, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [self.__cut_book_data(book) for book in data['books']]
        return returned

    def __cut_book_data(self, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'],
        }
        return book
