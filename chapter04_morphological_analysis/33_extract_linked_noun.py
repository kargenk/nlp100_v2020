#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
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

for s in sequences:
    for i in range(1, len(s) - 1):
        if s[i - 1]['pos'] == '名詞' and s[i]['surface'] == 'の' and s[i + 1]['pos'] == '名詞':
            print(s[i - 1]['surface'] + s[i]['surface'] + s[i + 1]['surface'])
