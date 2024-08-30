# hackathon_practice

## 準備
- iphoneにDroidCamを入れる
- iphoneとパソコンを同じwifiにつなげる
- testapp/camera_get.pyのcap.open()のpathを、DroidCamを開いたときに表示されているwifi ipのipアドレスに置き換える
- slackにあるスライドに従ってAWS bedrockを準備
- poetryを入れる(`curl -sSL https://install.python-poetry.org | python3 -`　で行けるはず)

## 実行
1. ターミナルで`poetry install`
2. **スマホでDroidCamを開いた状態で**、ターミナルで`poetry run python app.py`
3. あとはタッキーのと同じ(webページを開いて、ボタンを押す)。**DroidCamは開いたまま。**

## 備考
現状「一応動く」って状況だから、さすがにリファクタはします

## formatter, linter
`make fmt`でコードの見た目が綺麗になって、`make lint`で型の不一致とかformatterで直せない細かいフォーマットのダメ出しをしてくれる。linterはマジでうるさくて面倒だからやらなくてもいいけど、formatterはぜひ活用してほしい