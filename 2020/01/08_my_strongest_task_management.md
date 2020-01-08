# ぼくがかんがえたさいきょうのたすくかんり
- 現時点の自分のタスク管理を晒したい
- なんなら電子書籍にまとめたい
- 誰得
- でも書きたい
- むしゃくしゃしてる
- 良い落とし所ないか
- ……とりあえず tit るか

というわけでやってみよー :runner:

使っているもの

- 術(Method)
  - TaskChute
  - GTD
- 道具(Tool)
  - 秀丸エディタ
  - Python
  - AutoHotkey
  - fenrir
  - Git
- ストレージ
  - PC(Windows)
  - GitHub

tree

```
D:.
│  .gitignore
│  apull.bat
│  apush.bat
│  calendar.md
│  galapagosta.md
│  galapagosta_posted.md
│  i_love_task_management.md
│  profile_health.md
│  stamemo.md
│  statil.md
│  tilbox.md
│  
├─bridge
│      bookbrast.md
│      gistfile1.md
│      gistfile1_150401_151128.txt
│      gistfile1_151201_160130.txt
│      gistfile1_160201_160404.txt
│      gistfile1_160405_161130.txt
│      gistfile1_161201_161209.txt
│      gistfile1_161212_171127.md
│      gistfile1_171128_181203.md
│      gistfile1_181204_191028.md
│      gistfile1__reference.md
│      
├─calendar
│      1970.txt
│      ...
│      2100.txt
│      
├─gomi
│  │  gomi.gtdlist
│  │  
│  ├─181212_tweet
│  ...
│  └─190911_work
│          
├─gtd
│  │  context.txt
│  │  height.md
│  │  inbox.gtdlist
│  │  project.md
│  │  review_daily.md
│  │  review_log.md
│  │  someday.gtdlist
│  │  workflow.md
│  │  
│  └─doc
│          buy.md
│          careea_anchor.md
│          environment_home.md
│          kiyu_list.md
│          monitorlist.md
│          neta.gtdlist
│          strengthfinder.md
│          trigger_list_GET_IMPROVEMENT.md
│          trigger_list_IF_ENVIRONMENT_PROBLEM.md
│          ...
│          trigger_list_IF_MINIMALIST_MINIMALISM.md
│          
├─knowledge
│      7z.txt
│      acroread.txt
│      aeron_chair.txt
│      ...
│      yum.txt
│      zabbix.txt
│      zoom.md
│      
├─tenkin
│  │  tenkin.md
│  │  tenkin.trita
│  │  
│  └─201710_tokyo
│          tenkin.md
│          tenkin.trita
│          tenkin_calender.md
│          tenkin_naiken_checklist.md
│          
└─tritask
    │  .gitignore
    │  home.trita
    │  report_daily.md
    │  report_hourly.md
    │  report_monthly.md
    │  template_zikka_back.trita
    │  template_zikka_go.trita
    │  
    └─ref
            190306_151942_todochute.md
            ...
            191226_084738.md
            
```

ブレスト

- GTD ベース
  - 基本的に各種リストを plain text で書いてる
    - :file_folder: text/gtd フォルダ
    - inbox → inbox.gtdlist
    - project → project.md
    - 高度2000m, 3000, 4000, 5000 → height.md
    - ……
  - 高度 0m(next action) で TaskChute 使ってる
    - :file_folder: tritask フォルダ
    - tritask(オレオレな plain text taskchute) を使っている
    - home.trita ← これが一日の行動全部入ってるたすくまみたいなやつ
  - 資料
    - :file_folder: text/tritask フォルダ
    - テクニカルなメモ → text/knowledge
    - ブログ下書き → text/stamemo.md、text/galapagosta.md ……
    - ネットサーフィン時の備忘録 → text/statil.md
    - 日々の検討や思考で書いてる備忘録 → text/bridge/gistfile1.md
    - 引っ越し系 → text/tenkin
  - カレンダー
    - :file_folder: text/calendar.md に未来の予定を一行一つで書いてる
    - :file_folder: text/calendar/YYYY.txt に YYYY 年のカレンダー(gcalコマンド使用)

一日のワークフロー

- 起床
- PC をスリープから復帰して home.trita 開く
- (home.trita に従って行動していく)
  - :memo: この過程で各種ファイルにも適宜リーチする
  - :memo: いつ、どのファイルをどう更新するかは全部書いてるので迷わない
  - :memo: ぼくは home.trita に従って動いていくだけでいい
- (出勤)
- (会社PC の comp.trita に従って行動していく)
- (退勤)
- (home.trita の続きから行動していく)
- (home.trita の今日のタスクを全部終えた)
- PC をスリープにする
- (まったり)
- 就寝

タスク数消化データ

- home.trita
  - 平日は 20-30 個、休日は 50-100 個くらい
  - 休日は家事とレビューがある＆手順細かくタスク化してるので増えがち
- comp.trita
  - 平日は 40-80 個、休日は 0 個

思想

- そもそもタスク管理しなくても暮らせるくらいに小さな暮らしを死守する
  - 例: 毎日定時退社する、家族を持たない、組織運営などを負わない
- なるべく自席 PC で完結できるような暮らしを死守する
  - 例: 移動の多い仕事に従事しない
- ルーチンタスクで忘迷怠を防ぐ
  - 忘れないために
  - 迷わないために
  - 怠けないために
  - :robot: とにかく機械的に従っておけば問題なく回る ← これを目指す

FAQ こんなときはどうする？どうしてる？

- Q: リマインダーは？
  - Ans: [commainder](https://github.com/stakiran/commainder) を使用。`r 3 カップラーメン` を実行したら 3 分後に「カップラーメン」と表示されるツール。5秒で仕込める。
  - PC の前にいないときはキッチンタイマーやケータイのアラーム
- Q: レビューはどうしてる？
  - Ans: home.trita の中で daily@1、weekly@7、monthly@30 を設定している。
- Q: 「気になること」が思いついたら？
  - Ans: inbox.gtdlist を開いて記入しとく。2秒で開いて、書いて、保存して、すぐ閉じる
- Q: インボックスはいつ処理してる？
  - Ans: 3日に1回で処理するルーチンタスク。あと週次レビューのプロセスにも入れてる
- Q: プロジェクトはどのように書いている？
  - Ans: いくつかカテゴリがある
  - 大きなプロジェクト
    - MUST ← 直近絶対やらないといけない
    - Active ← 直近やる（やらなくても最悪死なない）
    - Pending ← あとでいい（MUST や Active の後でいい）
  - 未分類 ← まだプロジェクト化 or タスク化してない
  - やった ← 終わったらこっちに。週次レビューでログファイルに移す
- Q: 連絡待ちリストはどうしてる？
  - Ans: 発生した時点で home.trita に `2020/01/08 Aさん 承認依頼出した` ← こういう行を追加
  - ルーチンとして「連絡リスト確認して適宜対処せい @1」がある
- Q: カレンダーはどうしてる？
  - Ans: calendar.md ← ここだけ見れば網羅できるようにしている
  - calendar.md に集めるためのタスクはルーチン化
    - 例1: (会社 trita)outlook を眺めて手帳に書け @1
    - 例2: (自宅)手帳に書いてある予定を calendar.md に書き写せ @1
    - 例3: 直近一ヶ月の「平日が休日になってるところ」を調べて追記しろ @30
    - ……
- Q: ？
  - Ans: 
- Q: ？
  - Ans: 
- ……
