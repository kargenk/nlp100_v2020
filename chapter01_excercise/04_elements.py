#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
04. 元素記号
“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
連想配列（辞書型もしくはマップ型）を作成せよ．
'''

def extract_word(i, word):
    """題意を満たす単語を取り出す関数．"""
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (word[0], i)
    elif i == 12:
        return (word[:3:2], i)
    else:
        return (word[:2], i)

raw_text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
text = raw_text.replace('.', '')

elements = text.split()
_ans = [extract_word(i, e) for i, e in enumerate(elements, 1)]
ans = dict(_ans)

print(ans)
