#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(len(df))
