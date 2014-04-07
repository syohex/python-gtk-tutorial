# 2 はじめよう

## 2.1 シンプルな例

可能な限りシンプルなプログラムを作るところからチュートリアルを始めます.
初めのプログラムでは 200x200ピクセルのウインドウを作成していきます.

[simple_example](simple1.py)

この例のそれぞれの行について説明していきます.

```python
#!/usr/bin/python
```

すべての Pythonプログラムの 1行目は, `#!`ではじまり, その後に
実行したい Pythonインタプリタのパスを書きます.

```python
from gi.repository import Gtk
```

**GTK+**クラスと関数にアクセスするために, 初めに Gtkモジュールを
インポートしなくてはなりません.

次の行では, 空ウインドウを作成しています.

```python
win = Gtk.Window()
```

続いて, ウインドウの閉じるボタンをクリックしたときに, アプリケーションが
終了することを保証するように, ウインドウの削除イベントに接続します.

```python
win.connect("delete-event", Gtk.main_quit)
```

次のステップで, ウインドウを表示します.

```python
win.show_all()
```

最後に, `GTK+`のメインループを開始します. このループはウインドウを
閉じることで終了します.

```python
Gtk.main()
```

このプログラムを動かすために, ターミナルエミュレータを開いて,
ファイルのあるディレクトリに移動し, 次のコマンドを実行します.

```
python simple_example.py
```

## 2.2 発展例

もう少し便利なものを作るために, ここでは **PyGObject**を使った
"Hello World"プログラムを作成してみましょう.

[hello world](simple2.py)

この例は先ほどの単純例と異なり, `Gtk.Window`のサブクラスである
`MyWindow`クラスを作成しています.

```python
class MyWindow(Gtk.Window):
```

`MyWindow`クラスのコンストラクタでは, superクラスのコンストラクタを
呼び出す必要があります. 加えて, `title`プロパティを設定する必要が
あります. ここでは **Hello World**としています.

```python
    Gtk.Window.__init__(self, title="Hello World")
```

続く 3行では, ボタンウィジェットを作成, クリックシグナルへの関連付け,
トップレベルウィンドウの子としての追加を行っています.

```python
    self.button = Gtk.Button(label="Click Here")
    self.button.connect("clicked", self.on_button_clicked)
    self.add(self.button)
```

`on_button_clicked()`メソッドはボタンをクリックすると呼び出されます.

```
    def on_button_clicked(self, widget):
        print("Hello World")
```

最後のブロック, クラス定義の外側は, 一番初めの単純な例ととても
よく似ています. しかし一般的な `Gtk.Window`ではなく, 我々が
作成した `MyWindow`インスタンスを使っています.
