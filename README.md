# Daily Tracker
[睡眠時間とカフェイン飲料摂取量の推移グラフ](https://kahiro-m.github.io/DailyTracker/)

その日の睡眠時間と**前日の**カフェイン飲料摂取量を折れ線グラフでプロットします。

## 環境

|package|ver.|
|:--|:--|
|python |3.7.5 |
|numpy |1.17.4 |
|pandas |1.0.1 |
|matplotlib |3.2.1 |
|seaborn |0.10.0 |

## インストール方法

```
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
```

## 実行方法

1. csvデータを用意
2. `py makeFig.py`　もしくは　build.batかbuild.shを実行
3. 生成されたindex.htmlを開く　もしくは　GitHub pageにアクセス

### データ構造
data.csvのデータ構造（例）

|No.|日付|睡眠時間|コーヒー摂取量(ml)|ビール摂取量(ml)|備考|
|:--|:--|:--|:--|:--|:--|
|1|`day`|`hour`|`coffee`|`beer`|この行は変更不可。|
|2|2020.04.01 |7.5|800|0|起床した日の睡眠時間と|
|3|2020.04.02 |5.5|300|350|**前日の**摂取量を記載する。|
|4|2020.04.03 |8.5|300|0|摂取摂取量は`ml`単位で記入する。|
|5... |...|...|...|...||
