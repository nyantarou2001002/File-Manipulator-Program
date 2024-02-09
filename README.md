## ファイル操作プログラム

テキストファイルを対象に以下に記載するコマンドを入力することで
ファイルの内容を逆にしたり、ファイルの中の特定の文字を別の文字に置き換えることができます。

## コマンドの入力方法及びそれぞれの機能

・reverse inputpath outputpath
→inputpathにあるファイルを受取り、outputpathにinputpathの内容を逆にした新しいファイルを作成します。
・copy inputpath outputpath
→inputpathにあるファイルのコピーを作成し、outputpathとして保存します。
・duplicate-contents inputpath n
→inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回複製します。
・replace-string inputpath needle newstring
→inputpathにあるファイルの内容から文字列'needle'を検索し、'needle'の全てを'newstring'に置き換えます。

## エラーについて

入力をスペルミスなどで間違えた際は'Error!! Please input your command in the right way referencing README.md'と表示されるのでもう一度入力し直してください。
