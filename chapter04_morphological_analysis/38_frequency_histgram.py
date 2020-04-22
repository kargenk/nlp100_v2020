#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，
縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''

from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

def sequences_gen():
    """
    形態素解析結果の各要素を文単位で返す．
    
    Returns
    ----------
    sequences : list(dict)
        文単位の解析結果
    """
    
    sequences = []
    with open('neko.txt.ginza', encoding='utf-8') as f:
        sequence =[]
        for line in f:
            if line == 'EOS\n':
                sequences.append(sequence)  # 文終了なら出力
                sequence = []
                continue
            word_info = line.strip().split('\t')
            sequence.append({'surface': word_info[1],
                             'base': word_info[2],
                             'pos': word_info[3],
                             'pos1': word_info[4]})
    
    return sequences

sequences = sequences_gen()

d = defaultdict(int)
for sequence in sequences:
    for word in sequence:
        term = word['base'] + word['pos']
        d[term] += 1

values = d.values()
plt.hist(values, bins=1000)
plt.xlim(0, 100)
plt.show()
