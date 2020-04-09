#!/usr/bin/python
# coding: UTF-8
# -*- Coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

html_header = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style type="text/css">
      <!--
      -->
    </style>
  </head>
  <body>
"""

html_footer = """
  </body>
</html>
"""

# データ読み込み
csvData = pd.read_csv("./data.csv",encoding="utf_8")
print(csvData)

# 飲んだ飲み物の量は翌日の睡眠時間に関係があるので、
# 飲んだ量を翌日の日付と紐づけるために一日ずらしたデータに整形する。
anlyDf=pd.DataFrame({
  "day":np.concatenate([
      csvData.day,
      csvData.day,
      [0], # 飲み物の日付が一日後ろにずれるので行列の大きさを調整する
    ]),
  "type":np.concatenate([
      np.tile("Sleep(hour)",len(csvData.hour)),
      (np.tile("Tea/Coffe(100ml)",len(csvData.drank))),
      ["Tea/Coffe(100ml)"], # 飲み物の日付が一日後ろにずれるので行列の大きさを調整する
    ]),
  "data":np.concatenate([
      csvData.hour,
      [0], # この0mlを挿入することで飲み物の日付を翌日の睡眠時間と合わせる
      csvData.drank,
    ]),
  })  
print(anlyDf)

# プロット
fig = sns.lineplot(x="day", y="data",data=anlyDf,hue="type",style="type",markers=True)

# x軸ラベルを設定＆ラベル表示を90度回転
fig.set_xticklabels(anlyDf.day, rotation="90")

# 凡例、タイトル
plt.legend()
plt.title("Sleep time (hour) with drank Tea or Caffee (100ml)")  

# 画像の保存と画像データのリフレッシュ
plt.savefig("line.png")
plt.clf()

# html output
with open("index.html", mode="w", encoding="utf_8") as fileObj:
  fileObj.write(html_header)
  fileObj.write("<img src='line.png'>")
  fileObj.write(html_footer)