# 13 ComboBox

`Gtk.ComboBox`はドロップダウンメニューからの項目を選択する機能を
提供します. ラジオボタンがたくさんある場合よりも, 好まれます.
ComboBoxでは各項目に付加的な情報, テキスト, 写真, チェックボックス,
進捗バーといった付加的な情報を追加することもできます.

`Gtk.ComboBox`は `Gtk.TreeView`ととても類似しており, 共に
model-viewパターンを使います.

もし ComboBoxが大量のアイテムを含む場合, リストよりもグリッド形式で
表示する方が良いでしょう. `Gtk.ComboBox.set_wrap_width()`により,
そうすることができます.

`Gtk.ComboBox`ウィジェットは通常ユーザが利用できる選択肢を限定します.

テキスト形式のシンプルな選択リストの場合, `Gtk.ComboBox`の
model-view APIは ???
この場合, `Gtk.ComboBoxText`がシンプルな代替となります.
`Gtk.ComboBox`, `Gtk.ComboBoxText`共にエントリを含むことが
できます.

## 13.1 例

[ComboBox Example](combobox_example.py)
