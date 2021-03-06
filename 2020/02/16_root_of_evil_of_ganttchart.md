# ガントチャートの諸悪の根源
それは以下をいっしょくたにしていることだと思う。

- WBS
- いつからいつまでという「幅を持った」期限情報
- 担当者や進捗具合などのパラメータ

この性質上、以下の制約が生じる。

- ガントチャートは Excel レベルの高機能ツールでなければ実現できない
- ガントチャートは縦長にも横長にもなり、俯瞰するためには大きな画面が必要となる

この制約により、以下の弊害が生じる。

- WBS 構造の修正に手間がかかる（テキストエディタのような手軽さがなく「修正めんどくさ」となる）
- 各自が各自のペースで状況を更新できない（複数人編集ができないため調整作業が必要となる）

この弊害により、ガントチャートは「みんなが頼るべき唯一の拠り所」という役割を失う。どころか「とりあえず更新しなければばならないもの（しかも編集が面倒くさい）」として時間を奪う存在にもなる。

## どうすればよいか
いっしょくたにした役割を分離すれば良い。

以下のようにする。

- WBS には「幅を持った期限情報」と「パラメータ」を持たせない
- 各タスクの細かい状況は、BTS などの別システムで管理する
  - ブラウザから使えるものが望ましい
  - GitXub Issues、Trello、Microsoft Planner など
- 管理者または全員が把握するべき状況は「端的に」別途まとめる

順に例を見ていく。

### どうするか > WBS
WBS の例を以下に示す。

- 製品A ver3.0をリリースする
  - 開発
    - 自動テストのつくりこみ
    - 自動ビルドのつくりこみ
    - 機能１
    - 機能２
    - 機能３
  - ==== ここまで 2/14 までに ====
  - テスト
    - モンキーテスト一回目（チーム内で）
    - ガイドラインに従って手動テスト
    - モンキーテスト二回目（外部から有識者呼ぶ）
  - [努力] 性能改善
    - 改善ネタ1
    - 改善ネタ2
  - ==== ここまで 3/14 までに ====
  - リリース作業
    - リリース物件のアップロード
    - 各種宣伝文句作成
    - 広報部隊に提出
    - 広報部隊からのレビュー指摘反映
    - 広報部隊からＯＫもらうところまで指摘と反映を繰り返す
  - [努力] 開発ドキュメント刷新
  - ==== 4/1 公式 Twitter にて告知 ====

WBS はあくまで「全体を俯瞰する」用途に留める。進捗共有や議論時に使う「共通言語」と言い換えても良いだろう。ここに余分な情報は書かない。書くから混乱する。

ただし、見やすさのために少しだけ反映するのはアリだ。

- 製品A ver3.0をリリースする
  - 開発
    - x 自動テストのつくりこみ
    - s 自動ビルドのつくりこみ
    - ＞ 機能１
    - ＞ 機能２
    - 機能３

上記は終わった(x)、いったんスキップ(s)、着手中(>)を付与している。

### どうするか > 各タスクの細かい状況
BTS で管理するのが好ましい。

BTS を使えば 1-Task 1-Page を実現でき、あるタスクに関する事柄はそのページ内にまとめておくことができる。タスクの担当者はここで検討ややりとりを行いつつ、適宜要約もアップデートする。

BTS にはタスクを一覧表示したり、かんばんで視覚的に並べられるものもある。用途に応じて活用することになるだろう。

個人的には GitXub Issues をおすすめする。GitHub Issues や GitLab Issues などがある。どちらもエンジニア向けに高度に最適化されたツールであり、使いやすさと動作の軽さは他の追従を許さない。ただし「かんばん」機能にはあまり強くない（かんばんはなくても一覧があれば問題ないと私は思うが）。

しかし、GitXub 系は（知らない人には）ハードルが高いため、もうちょっと優しいツールが欲しいならば、Trello や Microsoft Planner など「かんばん」を推したツールを使うのが良いだろう。

### どうするか > 端的なサマリー
管理者または全員が把握するべき状況は「端的に」別途まとめるのが良い。

たとえば以下のようにする。

```
■サマリー
last updated: 2020/02/04

状況：

- スケジュールの遅れは無し
- 懸念
  - 機能３が技術的に難しいかも（2/6までに見解展開予定）
  - Aさん、祖父入院によりインパクトあるかも
  - 開発用 AWS アカウントの請求料金が高い（既に上から怒られてます）
  - 事業部内向けモンキーテストはそろそろ打診すべきでは？
```

この程度で良い。サマリーは本当に端的で良い。余計な詳細は一切要らない。詳細は各自が BTS なりコミュニケーションツール（健全な企業なら Slack が使えるはず）を見る、また各担当者はこまめに記入していく、とすればよい。つまり非同期的な共有を基本とする。

管理者については、そもそも詳細を知る必要さえない。必要ならヒアリングして（高度な判断を下すための）情報収集をすることはあるが、常に行うことはない。まして定例会議などで毎回説明させるのは愚の骨頂だ。貴重な時間を、実作業者でない管理者のために費やすなど（基本的には）馬鹿げている。

## おわりに
今回はアンチガントチャートを掲げ、三つの役割に分割した代替案を提示した。

とはいうものの、この代替案を運用するのは簡単ではないだろう。私であれば、どういうツールやフローを使っていけばいいかがわかるし、試行もしていけるが、おそらく大半の方はそうではない。

このあたりの「手段や運用の話」も別途必要そうか。
