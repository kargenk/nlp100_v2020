#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''

def preprocessing(text):
    """前処理関数．ここではカンマ・ピリオドの除去と単語への分割を行う．"""
    
    text = text.replace(',', '').replace('.', '')
    text = text.split()

    return text

def ngram(text, n):
    """
    n-gramを作成する関数．
    
    Parameter
    ----------
    text : str
        入力文
    n : int
        n-gramの数を指定する
    
    Returns
    ----------
    ngram : list
        n-gramのリスト
    """
    
    words = preprocessing(text)
    ngram = [words[idx:idx + n] for idx in range(len(words) - n + 1)]

    return ngram

text = 'I am an NLPer'
for i in range(1, 5):
    print('{}-gram: {}'.format(i, ngram(text, i)))
