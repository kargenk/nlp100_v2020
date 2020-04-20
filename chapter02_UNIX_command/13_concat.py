#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
14. 先頭からN行を出力Permalink
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''

import pandas as pd

col1 = pd.read_csv('col1.txt', sep='\t', header=None)
col2 = pd.read_csv('col2.txt', sep='\t', header=None)

concat_data = pd.concat([col1, col2], axis=1)

concat_data.to_csv('ans13.txt', sep='\t', index=False, header=None)
