# 7 Entry

Entryウィジェットはユーザがテキストを入力できるようにしてくれます.
`Gtk.Entry.set_text()`メソッドにより, 内容を変更することができ,
`Gtk.Entry.get_text()`メソッドで現在の内容を読み取ることができます.
`Gtk.Entry.set_max_length()`メソッドを使うことで, Entryが保持できる
文字の長さを制限することができます.

Entryウィジェットを読み取りのみ可能なことにしたい場合があるでしょう.
そのときは `Gtk.Entry.set_editable()`メソッドに `False`を渡してください.

Entryウィジェットはユーザからパスワードを入力させる場合にも
利用することができます. パスワードは普通第三者に見られないために,
入力している文字を隠します. これは `Gtk.Entry.set_visibility()`に
`False`を渡すことで実現できます.

`Gtk.Entry`は進捗表示を表示することもできます.
これは `Gtk.ProgressBar`ウィジェットと類似しており, ウェブブラウザの
ページがどれだけダウンロードされたかを示すものとしてよく使われています.
これらの情報を表示するのに, `Gtk.Entry.set_progress_fraction()`,
`Gtk.Entry.set_progress_pulse_step()`, `Gtk.Entry.progress_pulse()`
を使うことが可能です.

加えて, Entryは端それぞれにアイコンを表示することが可能です.
このアイコンはクリックで表示, ドラッグでセットアップができ,
ツールチップも持つことができます. アイコンを追加するには,
`Gtk.entry.set_icon_from_stock()`もしくはアイコン名, pixbuf,
アイコンテーマからアイコンの設定を行う他の関数を利用します.
アイコンにツールチップを設定するには, `Gtk.Entry.set_icon_tooltip_text()`
もしくはマークアップの機能を使います.

## 7.1 例

[Entry Example](entry_example.py)
