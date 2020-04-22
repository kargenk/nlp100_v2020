#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，
両対数グラフをプロットせよ．
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

values = sorted(list(d.values()), reverse=True)
plt.loglog(range(1, len(values) + 1), values)
plt.show()
