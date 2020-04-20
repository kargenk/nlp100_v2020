#!/bin/sh

# データの行数を取得(awk: テキスト加工)
n=`wc -l ./popular-names.txt | awk '{print $1}'`

# 分割する行を計算(expr: 式を評価)
ln=`expr $n / $1`

# ln行ごとのファイルに分割
split -l $ln -d ./popular-names.txt ans16_ 