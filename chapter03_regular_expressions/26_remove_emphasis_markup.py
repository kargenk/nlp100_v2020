#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
（参考: マークアップ早見表）．
'''

import re
import pandas as pd

def remove_emphasis_markup(text):
    """
    MediaWikiの強調マークアップを除去する関数．
    
    Parameter
    ----------
    text : str
        対象の文字列
    
    Returns
    ----------
    removed : str
        強調マークアップを除去した文字列
    """

    pattern = re.compile(r'\'{2,5}', re.MULTILINE)  # 2~5個のクオートを指定
    removed = pattern.sub('', text)                 # 空文字に置換

    return removed

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
    base_info_dict[k] = remove_emphasis_markup(v)
    print(k, ':\t', remove_emphasis_markup(v))
