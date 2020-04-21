#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''

import re
import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)
uk_text = wiki.query('title == "イギリス"')['text'].values[0]

# 基礎情報のテキスト群を抽出
pattern = re.compile(r'''
    ^\{\{     # 始まり
    基礎情報  # テンプレート
    (.*?)     # 抽出対象
    ^\}\}     # 終わり
    ''', re.MULTILINE + re.DOTALL + re.VERBOSE)
base_info_raw = pattern.findall(uk_text)[0]

# フィールド名と値を抽出
pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)\n', re.MULTILINE + re.DOTALL)
base_info = pattern.findall(base_info_raw)

# 辞書にまとめる
base_info_dict = {}
for k, v in base_info:
    base_info_dict[k] = v
    print(k, ':\t', v)
