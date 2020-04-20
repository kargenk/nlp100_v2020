#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
'''

import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)

name = df.iloc[:, 0]
print(set(name))

# # or
# print(df[0].unique())
