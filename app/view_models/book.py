# -*- coding: utf-8 -*- 
# @Time : 2019/12/18 20:58 
# @Author : wuson
# @File : book.py

class BookViewModel:

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
