#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''

import re
import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
uk_text = wiki.query('title == "イギリス"')['text'].values[0]

for file in re.findall(r'\[\[(ファイル):([^]|]+?)(\|.*?)+\]\]', uk_text):
    print(file[1])
