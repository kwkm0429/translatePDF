# translatePDF
## 使い方
1. ライブラリインストール
```
$ pip install PyPDF2
$ pip install python-docx
```

2. PDFのテキストを読み込んでワードファイルに保存
```
$ python ./src/transformPDFtoWord.py
```

3. ワードファイルを開いて、マニュアルで翻訳に不要な部分を削除

4. 不要な改行や単語のハイフン連結を削除
```
$ python ./src/formatWord.py
```

5. ワードファイルを開いて、Google翻訳の機能で翻訳していく