# ダブルウォンツリスト
ダブルウォンツとは **やりたいことを確実に一つずつ終わらせる仕組み** である。ブレイン・プログラミングにおける「やりたいこと」を管理する一手法として、吉良野すたにより考案された。

## 概要を 5 行で
- ダブルウォンツでは「やりたいことリスト(A)」と「今やっていることリスト(B)」の二種類を用意する
  - A として want to xxx リストが複数存在する。want to be、want to eat、want to go……。
  - B として doing、done、surrendered の三つのリストが存在する
- つまり A では「やりたいことを **動詞別に** 貯める」
- そのうち、やること・やったこと・やったけどダメだったものを B という形で **別途管理する**

## メリット
- やりたいことリストを書きやすい・貯めやすい
  - 動詞別なので書きやすい
  - 動詞を見ることで連想的に「実はやりたかったこと」も思い浮かびやすい
- やりたいことを一つずつ消化していける
  - doing リストさえ見れば良いので、混乱しない
- surrendered（やったけどダメだった）リストがあるため、やりたいことをやる際の心理的抵抗感が少ない
- シンプルな構成なので覚えやすく、取り組みやすい

## ファイル構造

```
1_doing.txt
2_done.txt
3_surrendered.txt
want_to_be.txt
want_to_eat.txt
want_to_go.txt
want_to_play.txt
want_to_reduce.txt
...
```

## ファイルフォーマット
- 一行に一つの「やりたいこと」を書く

## ファイルフォーマット > surrendered リスト
ただし surrendered リストだけはフォーマットが少し特殊である。

以下のように **降参した日付も書く**。

```
2020/02/26 (やったけどダメだったこと)
2020/02/12 (やったけどダメだったこと)
2020/02/09 (やったけどダメだったこと)
……
```

日付を書いておけば、あとで振り返りやすい。

## ダブルウォンツの運用

### はじめて取り組む場合
- 1: 上記ファイル構造を用意する
  - その際、want_to_xxxx の xxxx 部分は思いつく限りを
- 2: want_to_xxxx に、やりたいことを書きなぐっていく
- 3: 2 から、直近取り組むことを一つ選んで、doing に移す
  - 移す = テキストエディタで行ごとコピペする

### やりたいことを補充する場合
- 定期的に時間を取って書くのもよし、思いついたときに書くのもよし
- ただし todo やタスクは書かない、書くのはあくまでも **あなたがやりたい（けど今すぐにはできない）こと** だけ

### やりたいことが終わった場合
- done リストに移す
- 日付は書かなくてもいい（終わったことは振り返らなくて良い）

### やりたいことをやってみたけどダメだった場合
- 潔く surrendered リストに移す
  - その際、日付も書いておく

## FAQ

### Q: doing に書いた「やりたいこと」の進捗はどうやって管理するのですか？
Ans: お好きにどうぞ。

ただし **ダブルウォンツで管理してはいけません**。

ダブルウォンツはあくまでも「あなたのやりたいこと」を可視化・ストックするため "だけ" のものです。これ以上の役割を与えるとすぐに破綻します。

### Q: やりたいことが中々できません。どうすればいいですか？
Ans: おおよそ以下のいずれかが当てはまります

- 一つずつやりましょう。一つもできないうちは、**doing には一つだけ書くようにします**
- 本当にやりたいのなら、手段を選ばず、強引にでもやりましょう。できないのではなく、あなたがやらないのです
- 直近進めていける「やりたいこと」の数には限度がありますので、それを尊重しましょう
  - **doing capacity(キャパシティ)** と呼びます
  - キャパシティは人それぞれです（忙しさと能力で変わります）
  - 1～7 個であることが多いです

### Q: doing に 8 つ以上のやりたいことが並んでいますが、問題なく処理できています、私はおかしいですか？
Ans: おかしくはないですが、そういうあなたはそもそもダブルウォンツを必要としない人だと思います。