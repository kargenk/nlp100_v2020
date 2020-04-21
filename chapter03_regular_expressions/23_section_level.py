#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
'''

import re
import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
uk_text = wiki.query('title == "イギリス"')['text'].values[0]

uk_text_list = uk_text.split('\n')
section_list = list(filter(lambda x: '==' in x, uk_text_list))
for section in section_list:
    s = section.strip('=')
    l = ((len(section) - len(s)) / 2) - 1
    print(s.strip(), '\t', int(l))
print(len(section_list))

# # or
# # \1は後方参照，1つ目でマッチングしたものを指す
# for section in re.findall(r'(=+)([^=]+)\1\n', uk_text):
#     print(section[1].strip(), '\t', len(section[0]) - 1)
