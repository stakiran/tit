# 開発用 README

## requirement
- Windows 10+
- Python 3.6+

## build
readme.md をつくる:

```
$ python build.py
```

インプットは以下のとおり:

```
<readme_header.md の内容>
<パースした md ファイルからつくった目次>
<readme_footer.md の内容>
```

## running

### add new article
n.bat を実行する。

ファイル名を入力すると、現在日付ベースで `yyyy/mm/(YourFileName).md` が作成され、オープンされる。

オープンは「md ファイルに関連付けられたアプリ」で開く。

## build and commit and upload
b.bat を実行する。

build.py が走った後、commit と push も走る（コミットメッセージは都度入力だが適当で良い）。

ただし commit と push については upload.bat を使用

- [物置としての GitHub - Qiita](https://qiita.com/sta/items/9f146817f1335a6d9306)
  - [GitHub - stakiran/gaas_for_windows: GitHub As A Storage for Windows](https://github.com/stakiran/gaas_for_windows)
    - [upload.bat](https://github.com/stakiran/gaas_for_windows/blob/master/upload.bat)

## faq

### q: what is inbox?
インボックスとは「気になることなどをとりあえず置いておく場所」。未処理を溜めるエリア。

すぐに n.bat でファイル名が思い浮かばない場合は、inbox.md に溜める。

### q: why write '.md' extension need?
手間を考えれば .md は自動入力させるのが良いが、私の癖でファイル名につい .md と書いてしまう（結果 .md.md になってしまう :smirk:）ので、あえて自動入力させてない。
