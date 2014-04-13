# 9 ProgressBar

`Gtk.ProgressBar`は時間がかかる処理の進捗状況を表示するために
使われます. 進行中の処理を視覚的に表示することができます.
`Gtk.ProgressBar`は, *percentageモード*と *activity mode*の 2種類の
モードを使うことができます.

アプリケーションがどのような処理を行うかを決定するとき,
(例えばファイルから固定サイズのデータを読み出す), その進捗を
見る場合は percentageモードを使うことができ, ユーザは
完了している割合でバーが伸びることを確認するこたおができます.
percentageモードでは, バーを更新するために`Gtk.ProgressBar.set_fraction()`を
呼ぶ必要あります. 値は 0から 1までの新しいパーセンテージとなる
値を渡します.

アプリケーションが進捗状況を正確に知る方法がない場合, `activity mode`が
使えます. `activity mode`では, 進捗エリアでブロックが前後に移動します.
このモードでは, アプリケーションはバーの更新のために,
`Gtk.ProgressBar.pulse()`を呼び出す必要があります. ステップサイズの
決定には `Gtk.ProgressBar.set_pulse_step()`メソッドが使えます.

デフォルトでは, `Gtk.ProgressBar`は水平方向で左から右に進みます.
`Gtk.ProgressBar.set_orientation()`メソッドで垂直方向のバーを
使用することが可能です. 進捗バーの方向を変更するには,
`Gtk.ProgressBar.set_inverted()`を利用します. `Gtk.ProgressBar`は
`Gtk.ProgressBar.set_text()`及び, `Gtk.ProgressBar.set_show_text()`
でテキストを設定することも可能です.

## 9.1 例

[ProgressBar Example](progressbar_example.py)
