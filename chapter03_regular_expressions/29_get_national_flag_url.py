#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
29. 国旗画像のURLを取得するPermalink
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
'''

import re
import requests
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

def remove_link_markup(text):
    """
    MediaWikiの内部リンクマークアップを除去する関数．
    
    Parameter
    ----------
    text : str
        対象の文字列
    
    Returns
    ----------
    removed : str
        内部リンクマークアップを除去した文字列
    """

    pattern = re.compile(r'\[\[(.*\|?.*?)\]\]', re.MULTILINE + re.DOTALL)  # [[]]で囲まれたものを指定
    removed = pattern.sub(r'\1', text)  # 後方参照で[[]]内のみに置換

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
    removed = remove_emphasis_markup(v)
    removed = remove_link_markup(removed)
    removed = removed.replace('<br />', '')
    removed = re.sub(r'<ref.*?>', '', removed).replace('</ref>', '')
    # 抽出例外の処理
    if k in ['ccTLD', '確立形態1', '確立形態3']:
        removed = removed.replace('[[', '').replace(']]', '')
    base_info_dict[k] = removed
    
url_file = base_info_dict['国旗画像'].replace(' ', '_')
url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
data = requests.get(url)
url = re.search(r'"url":"(.+?)"', data.text).group(1)
print(url)
