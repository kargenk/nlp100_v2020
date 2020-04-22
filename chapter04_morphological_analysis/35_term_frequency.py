#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
35. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''

from collections import defaultdict

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
print(d_sorted[:5])
