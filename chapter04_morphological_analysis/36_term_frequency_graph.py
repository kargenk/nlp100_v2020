#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
36. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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
        term = word['base'] + '_' + word['pos']
        d[term] += 1

# 頻度順にソート
d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

target = d_sorted[:10]
labels = [x[0] for x in target]
values = [x[1] for x in target]
plt.barh(labels[::-1], values[::-1])  # 降順になるように調整
plt.show()
