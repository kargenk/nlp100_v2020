#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
06. 集合
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

def n_gram(text, n):
    n_gram = [text[idx:idx + n] for idx in range(len(text) - n + 1)]
    return n_gram

text_X = 'paraparaparadise'
text_Y = 'paragraph'
X = n_gram(text_X, 2)
Y = n_gram(text_Y, 2)

print('集合X: ', set(X))
print('集合Y: ', set(Y))

print('和集合: ', set(X) | set(Y))
print('積集合: ', set(X) & set(Y))
print('差集合: ', set(X) - set(Y))
print('se' in set(X) & set(Y))