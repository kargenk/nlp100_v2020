#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''

import pandas as pd

wiki = pd.read_json('jawiki-country.json', lines=True)

uk_text = wiki.query('title == "イギリス"')['text'].values[0]
# # or
# uk_text = wiki[wiki['title'] == 'イギリス']['text'].values[0]

print(uk_text)
