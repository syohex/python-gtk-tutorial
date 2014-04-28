# 14 IconView

`Gtk.IconView`は gridビューに複数のアイコンを表示するためのウィジェットです.
ドラッグアンドドロップ, 複数候補の選択, 並べ替えをサポートしています.

`Gtk.TreeView`と類似していて, `Gtk.IconView`はモデルとして,
`Gtk.ListStore`を利用しています. `cell renderers`を利用する代わりに
`Gtk.IconView`は `Gtk.ListStore`のカラムの一つに `GtkPixBuf.Pixbuf`
オブジェクトを含むことを要求します.

`Gtk.IconView`には複数のアイコンを選ぶ, 1つのアイコンのみを選ぶ,
アイテムを選べなくする, モードがあります. モードの指定は,
`Gtk.IconView.set_selection_mode()`をメソッドを `Gtk.SelectionMode`を
指定することにより行えます.

## 14.1 例

[IconView Example](iconview_example.py)
