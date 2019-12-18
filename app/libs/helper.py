# -*- coding: utf-8 -*- 
# @Time : 2019/12/1 22:29 
# @Author : wuson
# @File : helper.py.py

def is_isbn_or_key(word):
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些 ' - '
    # isdigit() 方法可以判断一个变量的值是否全部是数字
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key