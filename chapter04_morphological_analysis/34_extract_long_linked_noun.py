#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

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

linked_noun = []
tmp = []
for sequence in sequences:
    for word in sequence:
        if word['pos'] == '名詞':
            tmp.append(word['surface'])
        elif len(tmp) >= 2:
            linked_noun.append(''.join(tmp))
            tmp = []
        else:
            tmp = []
print(linked_noun)