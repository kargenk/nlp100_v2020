#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''

import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
uk_text = wiki.query('title == "イギリス"')['text'].values[0]

uk_text_list = uk_text.split('\n')
category_row_list = list(filter(lambda x: 'Category:' in x, uk_text_list))
category_list = [cr.replace('[[Category:', '').replace('|*', '').replace(']]', '')
                    for cr in category_row_list]
print(category_list)
