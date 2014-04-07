# 5 コンテナのレイアウト

多くの GUIツールキットでは, Window内にウィジェットを配置するとき,
絶対的な位置を使い正確に配置することを要求しますが, GTK+では異なる
アプローチを採用しています. ウインドウ内の各ウィジェットの位置や
サイズを指定するのではなく, テーブルの行や列としてウィジェットを
調整するという方法です. これにより, Windowのサイズは, それが含む
ウィジェットのサイズに基づいて, 自動的に決定することができます.
ウィジェットのサイズもテキストの量や最低サイズ, 最大サイズに
基づいて決定することができます. パディング, 各ウィジェットの中央値
を指定することで完璧にレイアウトすることができます.
GTK+はこの情報を使い, リサイズ, 再配置を行うので, Window操作を
行ったとき正確にそしてスムーズにすべてを行えます.

GTK+ではウィジェットは**コンテナ**を使い, 階層上に構成されます.
コンテナはエンドユーザに見えないか, 他のレイアウトコンテナに置かれます.
コンテナには 2種類あり, 1つは single-childコンテナで, それらはすべて
`Gtk.Bin`の子クラスで, もう 1つは multiple-childコンテナで, こちらは
`Gtk.Container`の子クラスです. よく使われるものは, 垂直, 水平ボックスで
ある `Gtk.Box`, 表形式の `Gtk.Table`, グリッド形式の `Gtk.Grid`です.


## 5.1 Boxes

Boxは不可視のコンテナでその中には複数のウィジェットを置くことが
できます. ウィジェットが水平ボックスに格納されるとき, オブジェクトは
左から右, もしくは右から左に挿入されます. 挿入方向は, `Gtk.Box.pack_start`
と `Gtk.Box.pack_end()`が使われたかどうかに依存します. 垂直ボックスの場合,
ウィジェットは上から下またはその逆に置かれます. ボックスを組み合わせる
ことで任意のレイアウトを実現することができるでしょう.

### 5.1.1 例

2つのボタンを使う例を見ていきましょう.

[Two Button Example](two_button.py)

初めに子の間が 6ピクセルとなる, 水平ボックスコンテナを作成します.
このボックスはトップレベルウインドウの子となります.

```python
    self.box = Gtk.Box(spacing=6)
    self.add(self.box)
```

続いて, ボックスコンテナに 2つの異なるボタンを追加します.

```python
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
```

`Gtk.Box.pack_start()`を呼ぶことで左から右に配置され,
`Gtk.Box.pack_end()`を呼ぶことで, 右から左に配置されます.

## 5.2 Grid

`Gtk.Grid`は, 行, 列で子ウィジェットを配置することができるコンテナです.
しかしコンテナの次元数を指定する必要はありません. 子は `Gtk.Grid.attach()`
を使って追加されます. 複数の行, 列にまたがらせることも可能です.
`Gtk.Grid.attach_next_to`により既存の子のとなりに追加することも可能です.


`Gtk.Grid`は `Gtk.Grid.add()`を使うだけであれば, `Gtk.Box`のように
使うこともできます. `Gtk.Grid.add()`は `orientation`プロパティに
よって決められた方向に次々廃していきます(デフォルトの配置方法は,
`Gtk.Orientation.HORIZONTAL`です).

### 5.2.1 例

[Grid Example](grid_example.py)

## 5.3 Table

テーブルは `Gtk.Grid`のようにウィジェットをグリッドに配置できます.

グリッドの次元数は `Gtk.Table`コンストラクタで指定する必要があります.
ボックスにウィジェットを配置するには, `Gtk.Table.attach()`を使います.

`Gtk.Table.set_row_spacing`と `Gtk.Table.set_col_spacing()`は,
特定の行または列のスペースを設定します. 列ではカラムの右にスペースが,
行では下にスペースができます.

`Gtk.Table.set_row_spacings`ですべての行(または, もしくは)列にスペースを
設定することができます. これらすべての呼び出しでは, 最後の行, 列については
スペースが入りません.

### 5.3.1 例

[Table Example](table_example.py)

## 5.4 ListBox

`Gtk.ListBox`は `Gtk.ListBoxRow`を子として持つ垂直方向のコンテナです.
これらの行は動的に並べ替えたり, フィルタリングをオコナウことができ,
ヘッダも行の内容に応じて動的に追加することができます. 典型的なリストの
ようにキーボード, マウスナビゲーションなどが可能です.

`Gtk.ListBox`は `GtkTreeView`の変わりになります. 特にリストの内容が
`Gtk.CellRender`で表現できるものより複雑な場合や内容がインタラクティブで
ある場合です(その中にボタンがあるなど)

`Gtk.ListBox`は `Gtk.ListBoxRow`のみを子として持ちますが,
`Gtk.Container.add()`を使うことで, 任意のウィジェットを追加
することができ, `Gtk.ListBoxRow`ウィジェットはリストとウィジェットの
間に自動で追加されます.

### 5.4.1 例

[ListBox Example](listbox_example.py)
