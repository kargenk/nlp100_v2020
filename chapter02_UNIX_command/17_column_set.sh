#!/bin/sh

# 1列目の内容を取得(cut: フィールド単位で切り出し)
# (uniq: 重複の削除，ただし，ソート済みであることが条件)
cut -f1 -d$'\t' ./popular-names.txt | sort | uniq
