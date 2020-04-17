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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
    <script src="./data.js"></script>
    <script src="./makeFig.js"></script>
      <!--
      -->
    </style>
  </head>
  <body onload="readFirstOnly()">
"""

html_lineCanvas = """
    <canvas id="myLineChart"></canvas>
"""

html_footer = """
  </body>
</html>
"""

# データ読み込み
csvData = pd.read_csv("./data.csv",encoding="utf_8")
print(csvData)
csvData.to_json("./data.json") 

# 折れ線グラフプロット
fig = sns.lineplot(x=csvData.day[153:],y=csvData.hour[153:],label="sleep[hour]")
fig = sns.lineplot(x=csvData.day[153:],y=csvData.coffee[153:]/100,label="Tea/Coffee[100ml]")

fig.set_xticklabels(csvData.day[153:], rotation="90")

# 凡例、タイトル
plt.legend()
plt.title("Sleep time (hour) with coffee Tea or coffee (100ml) intake the day before")  

# 画像の保存と画像データのリフレッシュ
plt.savefig("line.png")
plt.clf()


# 曜日ごとの睡眠時間グラフプロット
fig = sns.barplot(x="WoD",y="hour",data=csvData,color="0.9",order=['Sun.','Mon.','Tue.','Wed.','Thu.','Fri.','Sat.'])
fig = sns.swarmplot(x="WoD",y="hour",data=csvData,order=['Sun.','Mon.','Tue.','Wed.','Thu.','Fri.','Sat.'])
# 画像の保存と画像データのリフレッシュ
plt.savefig("bar.png")
plt.clf()

fig = sns.boxplot(x="WoD",y="hour",data=csvData,color="0.95",order=['Sun.','Mon.','Tue.','Wed.','Thu.','Fri.','Sat.'])
fig = sns.swarmplot(x="WoD",y="hour",data=csvData,order=['Sun.','Mon.','Tue.','Wed.','Thu.','Fri.','Sat.'])
plt.savefig("box.png")
plt.clf()

# 散布図と回帰分析(信頼区間95%)プロット
fig = sns.regplot(x="coffee", y="hour", data=csvData[153:], ci=95)
# 画像の保存と画像データのリフレッシュ
plt.savefig("reg.png")
plt.clf()


# 散布図行列プロット
fig = sns.pairplot(data=csvData,hue="WoD",hue_order=['Sun.','Mon.','Tue.','Wed.','Thu.','Fri.','Sat.'])
# 画像の保存と画像データのリフレッシュ
plt.savefig("pair.png")
plt.clf()


# html output
with open("index.html", mode="w", encoding="utf_8") as fileObj:
  fileObj.write(html_header)
  fileObj.write("その日の睡眠時間と<b>前日の</b>カフェイン飲料摂取量<br>")
  fileObj.write("<img src='line.png'>")
  fileObj.write("<br>")
  fileObj.write(html_lineCanvas)
  fileObj.write("<img src='reg.png'>")
  fileObj.write("<br>")
  fileObj.write("<img src='bar.png'>")
  fileObj.write("<br>")
  fileObj.write("<img src='box.png'>")
  fileObj.write("<br>")
  fileObj.write("<img src='pair.png'>")
  fileObj.write(html_footer)