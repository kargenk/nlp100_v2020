#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
'''

import sys
import pandas as pd

if len(sys.argv) == 1:
    print('set length n, like "python 14_head.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    print(df.head(n))
