#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''

import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
uk_text = wiki.query('title == "イギリス"')['text'].values[0]

uk_text_list = uk_text.split('\n')
category_row_list = list(filter(lambda x: 'Category:' in x, uk_text_list))
print(category_row_list)
