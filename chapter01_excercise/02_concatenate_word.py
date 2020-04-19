#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''

text1 = 'パトカー'
text2 = 'タクシー'
ans = ''

for i in range(len(text1)):
    ans += text1[i]
    ans += text2[i]

print(ans)
