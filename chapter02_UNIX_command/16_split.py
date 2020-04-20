#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
'''

import sys
import pandas as pd

if len(sys.argv) == 1:
    print('set n: split num, like "python 16_split.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    nrow = len(df) // n
    for i in range(n):
        df.loc[nrow * i: nrow * (i + 1)].to_csv('ans16_{}.txt'.format(i), sep='\t', index=False, header=None)
