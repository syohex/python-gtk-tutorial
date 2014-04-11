# 8 Buttonウィジェット

## 8.1 Button

Buttonウィジェットは頻繁に利用されるウィジェットです. ボタンを
押したときに何かしたいという機能を付与するために一般的に利用されます.

`Gtk.Button`ウィジェットは, 任意の子ウィジェットを持つことが可能です.
`Gtk.Widget`に準拠するものであれば持つことができます. 子として最も
よく利用されるのは, `Gtk.Label`です.

通常ボタンには `"clicked"`シグナルを関連付けます. `"clicked"`シグナルは
ボタンを押したり, 離したりするときに発生するシグナルです.

### 8.1.1 例

[Button Example](button_example.py)

## 8.2 ToggleButton

`Gtk.ToggleButton`は, `Gtk.Button`ととても類似していまが,
クリックしたとき, 再クリックするまで押されたという情報が残ります.
ボタンに状態が変化したとき, `toggled`シグナルが発生します.

`Gtk.ToggleButton`の状態を取得するためには, `Gtk.ToggleButton.get_active()`
メソッドを使用します. このメソッドの結果が `True`であるとき, ボタンは
押された状態であることを示します. `toggled`シグナルは状態が実際に
変わったときに発生します.

### 8.2.1 例

[ToggleButton Example](togglebutton_example.py)

## 8.3 CheckButton

`Gtk.CheckButton`は `Gtk.ToggleButton`を継承したクラスです.
それらの違いは `Gtk.CheckButton`があらわれるかどうかです.
`Gtk.CheckButton`はウィジェットのとなり(通常は `Gtk.Label`)に
置かれます. `toggled`シグナルは, `Gtk.ToggleButton.set_active()`と
`Gtk.ToggleButton.get_active()`が継承されます.

## 8.4 RadioButton

チェックボックスのような, ラジオボタンは `Gtk.ToggleButton`から
継承されます. それはグループを持ち, グループ内の一つのものだけ
選択することが可能です. そのため `Gtk.RadioButton`はたくさんの
オプションから一つ選ばせるような場合に利用できます.

ラジオボタンはスタティックメソッドである `Gtk.RadioButton.new_from_widget()`,
`Gtk.RadioButton.new_with_label_from_widget()`,
`Gtk.RadioButton.new_with_mnemonic_from_widget()`
により作成することができます.

グループの初めのラジオボタンは `group`
引数に `None`を渡すことで作成できます. それに続く呼び出しで,
ボタンに加えたいグループを引数として渡します.

初めて実行されるとき, グループの一番初めのラジオボタンがアクティブに
なっています. これは, `Gtk.ToggleButton.set_active`に `True`を渡す
ことで変更することが可能です.

作成したのちに`Gtk.RadioButton`ウィジェットグループを変更するには,
`Gtk.RadioButton.join_group()`を呼び出します.

### 8.4.1 例

[RadioButton Example](radiobutton_example.py)

## 8.5 LinkButton

`Gtk.LinkButton`は(ウェブブラウザ)で見られるハイパーリンクを伴う
`Gtk.Button`で, クリックしたときにアクションを実行することができます.
リソースのリンクを手早く引くときなどに便利です.

`Gtk.LinkButton`に紐付けられる URIは, `Gtk.LinkButton.set_url()`に
より設定することができ, `Gtk.LinkButton.get_uri()`で取り出すことが
できます.

### 8.5.1 例

[LinkButton Example](linkbutton_example.py)

## 8.6 SpinButton

`Gtk.SpinButton`は, ある属性の値をユーザに設定させる場合に持ってこいの
ものです. `Gtk.Entry`で直接値を入力させるのではなく, `Gtk.SpinButton`
では二つの矢印をクリックさせることで値の増減を行うことができます.
値は直接入力することができ, 指定された範囲に収まっているかを確認
することもできます. `Gtk.SpinButton`の主要な属性は, `Gtk.Adjustment`に
より設定します.

表示されている`Gtk.SpinButton`の値を変更するには, `Gtk.SpinButton.set_value()`
を利用します. 入力値は整数または浮動小数点数を指定させることが可能で,
それぞれ `Gtk.SpinButton.get_value()`, `Gtk.SpinButton.get_value_as_init()`
により取り出すことができます.

`SpinButton`の中に浮動小数点数を表示させる場合, `Gtk.SpinButton.set_digits()`
により, 表示する桁数を調整するとよいでしょう.

デフォルトでは, `Gtk.SpinButton`はテキストっぽいデータを許容します.
整数値に限る場合は, `Gtk.SpinButton.set_numeric()`に `True`を渡して
ください.

`Gtk.SpinButton`の更新のポリシーは変更することが可能です.
ここでは二つ紹介します. デフォルトである, 入力されたデータが不正で
ある場合でも spin butoonを更新するというもの. もうひとつ正当なデータが
入力された場合にのみ更新するというもの. これらは,
`Gtk.SpinButton.set_update_policy()`で決定することができます.

### 8.6.1 例

[SpinButton Example](spinbutton_example.py)

## 8.7 Switch

`Gtk.Switch`は on, offのいずれかの状態を持つウィジェットです.
空のエリアをクリックするか, ハンドルをドラッグすることで,
状態を変更することが可能です.

`Gtk.Switch`の`active`シグナルは使うべきではありません.
`active`シグナルはアクションシグナルでアニメーションの原因となります.
アプリケーションはこのシグナルに関連付けられるべきではなく,
変わりに `notify::active`を使うべきです.

### 8.7.1 例

[Switch Example](switch_example.py)
