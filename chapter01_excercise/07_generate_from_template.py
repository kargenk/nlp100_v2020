#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
'''

def generate_text(x, y, z):
    """
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数．

    Parameter
    ----------
    x : int
        時
    y : str
        事象名
    z : int
        値

    Returns
    ----------
    text : str
        x時のyはz という形の文
    """
    return '{}時の{}は{}'.format(x, y, z)

print(generate_text(x=12, y='気温', z=22.4))
