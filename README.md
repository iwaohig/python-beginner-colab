# はじめての Python (Google Colab 版)

Python を初めて触る人向けのトレーニング教材です。Google Colab で動くので、受講者はブラウザだけで始められます。
大学の 1 期 (週 1 回 90 分 × 15 回) を想定したカリキュラムのうち、第 1〜5 回のノートを置いています。
対象は、情報系以外の学生や社会人など、プログラミングが初めての人です。

| 回 | 受講者用ノート | 内容 |
|---|---|---|
| 1 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwaohig/python-beginner-colab/blob/main/notebooks/01_hello_colab.ipynb) `01_hello_colab` | Colab の使い方、`print`、計算、コメント、おみくじ、はじめてのエラー |
| 2 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwaohig/python-beginner-colab/blob/main/notebooks/02_variables.ipynb) `02_variables` | 変数、型 (`int` / `float` / `str`)、f 文字列、`input`、割り勘・BMI |
| 3 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwaohig/python-beginner-colab/blob/main/notebooks/03_errors.ipynb) `03_errors` | エラーの読み方、よく出るエラー、全角の落とし穴、実行順の罠、エラー直し 5 問 |
| 4 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwaohig/python-beginner-colab/blob/main/notebooks/04_if.ipynb) `04_if` | 比較、`if` / `elif` / `else`、`and` / `or`、服装アドバイス・成績判定・入場料 |
| 5 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iwaohig/python-beginner-colab/blob/main/notebooks/05_list_for.ipynb) `05_list_for` | リスト、`for`、`range`、合計・平均、1 週間の歩数、九九 |

## 受講者の方へ

1. 上の表の「Open in Colab」を押す (Google アカウントでのログインが必要です)
2. メニューの「ファイル」→「ドライブにコピーを保存」を押す。**コピーしないで書いた内容は、閉じると消えます**
3. コピーしたノートで、上から順にセルを実行しながら進める

## フォルダ

- `notebooks/` 受講者用 (演習は空欄、「エラーを直そう」は壊れたまま)
- `solutions/` 解答例 (講師向け)
- `tools/build.py` 両方を 1 つの元から作るスクリプト。**ノートを直すときはここを直して作り直す** (`.ipynb` を直接直さない)
- `tools/check.py` 全ノートのコードを上から実行して確かめる (`input` は決まった値に差し替え)

```bash
python tools/build.py
python tools/check.py
```

`check.py` は、エラーの見本と「エラーを直そう」のセル (`raises-exception` の印) がエラーになること、それ以外がエラーなく動くことを確かめます。

## 各回の作り

どの回も、次の順に並んでいます。

1. 「ドライブにコピーを保存」の案内
2. 今日のゴール
3. 説明と見本
4. やってみよう (2〜3 問)
5. エラーを直そう
6. まとめ
7. ふりかえり (受講者が書き込む)
8. 次回の予告

- AI の補完 (Gemini) は、第 1〜7 回はオフにして自分で書く方針です (第 1 回で案内しています)
- 題材は身近なもの (割り勘、服装、歩数、成績) にしています

## ライセンス

MIT
