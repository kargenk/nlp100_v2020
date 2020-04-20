#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''

import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)

col1 = df.iloc[:, 0]
col1.to_csv('col1.txt', sep='\t', index=False, header=None)

col2 = df.iloc[:, 1]
col2.to_csv('col2.txt', sep='\t', index=False, header=None)
