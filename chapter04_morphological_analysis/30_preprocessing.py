#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．
'''

import spacy
nlp = spacy.load('ja_ginza')

with open('neko.txt', encoding='utf-8') as f_orig, open('neko.txt.ginza', 'w', encoding='utf-8') as f_morph:
    for line in f_orig:
        for sent in nlp(line.strip()).sents:
            for token in sent:
                pos = token.tag_.split('-')[0]
                # i:トークン番号，orth_:表層形，lemma_:基本形
                # pos_:品詞(英語)，tag_:品詞細分類(日本語)
                f_morph.write(f'{token.i}\t{token.orth_}\t{token.lemma_}\t'
                              f'{pos}\t{token.tag_}\n')
            f_morph.write('EOS\n')
