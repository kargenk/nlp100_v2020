#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

- 英小文字ならば(219 - 文字コード)の文字に置換
- その他の文字はそのまま出力

この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''

def cipher(text):
    text = [chr(219 - ord(w)) if 97 <= ord(w) <= 122 else w for w in text]
    return ''.join(text)

text = 'this is a test. Thank you! 765 MILLIONSTARS!'

text_en = cipher(text)
print(text_en)

text_de = cipher(text_en)
print(text_de)