# plpr - plain presentation プレプレ プレインプレゼンテーション
プレーンテキストでプレゼンを行うこと

なぜ？:

- プレゼン資料をつくるのには時間がかかるから
- 要点はシンプルに伝えるべきだから
- シンプルであればプレーンテキストで表現できるはずだから

プレプレの三原則:

- Short Noting
  - 極限まで文字数を減らす
- Setto Frame
  - 構造をつくるのではなく構造に当てはめる
- Stoic Readable
  - 読みやすさはストイックに追求する

Short Noting:

- 常にサマリーだけ書く
- 図表よりも文章、文章よりもフレーズ、フレーズよりも単語
- 語彙力が(書き手はもちろん読み手にも)必要
- トップダウン(概念的・抽象的)に理解させる
  - 読み手はトップダウンに書かれた表現の方が理解しやすい(自身が持つ知見をフル活用しやすい)

Setto Frame:

- フレーム(Frame)とは
  - 文章の構造的・表記的制約のこと
- フレームはよく知られたもの or 効果が高かったものを使う
- 一度つくったフレームは使い回す
  - 資料作成のたびに新たにつくろうとしない
  - プログラミングでいう関数、ライブラリ、フレームワークみたいに扱う

Stoic Readable:

- Readability(読みやすさ) はできるだけ追求する
- 読みやすさとは構文的(Syntax)なもの
  - 意味的(Semantic)な読みやすさは Short Noting で担保する

## フレームの例:
- what(これは何？/定義)、why(なぜ？/理由・意義)、example(具体例)、metaphor(たとえ) etc
- SL ルール
  - 見出し(Section)と箇条書き(List)だけで構成せよ、というルール
  - 例
    - 1S-3L: 大見出しと箇条書き3行
    - 1S-S3L: 中見出しと箇条書き3行
    - 1S-3SS: 大見出しと中見出し3つ

## SL ルール例

### 1S-3L

```
# プレプレの三原則
- Short Noting
- Setto Frame
- Stoic Readable
```

### 1SS-3L
大見出しは表示時にフォントがでかすぎるので、中見出しを使って回避するテクニック。

```
## プレプレの三原則
- Short Noting
- Setto Frame
- Stoic Readable
```

### 1S-3SS
大きなフォントで見せたい場合は（大きなフォントで描画される）大見出しと中見出しを使う。

```
# プレプレの三原則
## Short Noting
## Setto Frame
## Stoic Readable
```
