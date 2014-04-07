# 4 文字列の扱い

この章では, Python 2.x, Python 3.X, そして GTK+で文字列がどのように
表現されるかを示し, 文字列を扱う際に起こりがちなエラーについて述べて
いきます.

## 4.2 定義

概念的に, 文字列は 'A', 'B', 'C'といった文字のリストです.
**Characters**は抽象的な表現であり, その意味は言語や使われる
文脈に依存します. Unicode標準はコードポイントにより, 文字が
どう表現されるかを示しています. 例えば先にでた例はコードポイント,
`U+0041`, `U+0042`, `U+0043`とそれぞれ表現されます. 基本的に,
コードポイントとは 0から 0x10FFFFまでの数値となります.

先に述べたように, コードポイントのリストとして文字列を表現する
ことは抽象的です. この抽象的な表現を Unicode文字列のバイト列に
変換するためには, **エンコード**しなくてはなりません. 単純な
エンコードは ASCIIであり, 次のように行うことができます.

1. コードポイントが 128未満であれば, 各文字はコードポイントと同じである
2. コードポイントが 128以上であれば, この Unicode文字列は表現することができない.(このとき Pythonでは, `UnicodeEncodeError`例外が発生する)

ASCIIエンコーディングは単純ですが, 128の異なる文字しかエンコードする
ことができません. この問題を解決されるために最もよく使われている
エンコーディングは UTF-8で, 任意の Unicodeコードポイントを扱うことが
できます. UTFとは "Unicode Transformation Format"を示し, `8`は
エンコードに 8bit使われることを意味します.

## 4.2 Python2

### 4.2.1 Python2.xの Unicodeサポート

Python 2では, 文字列を表現するために `str`と `unicode`の 2つの
オブジェクトタイプを備えています. `unicode`インスタンスは Unicode文字列を
表現するために使われ, 一方 `str`インスタンスはバイト列(エンコードされた
文字列)を表現するために使われます. Pythonでは Unicode文字列を表現する
のに 16bitまたは 32bitの整数のいずれかが使われます. どちらになるかは
Pythonインタプリタをどのようにコンパイルしたかにより依存します.
Unicode文字列は `unicode.encode()`により, バイト列に変換することが
できます.

```
>>> unicode_string = u"Fu\u00dfb\u00e4lle"
>>> print unicode_string
>>> Fußbälle
>>> unicode_string.encode("utf-8")
>>> 'Fu\xc3\x9fb\xc3\xa4lle'
```

Pythonのバイト列には `str.decode()`メソッドがあり, 与えられた
エンコーディングに応じて, 文字を解釈することができます.

```
>>> utf8_string = unicode_string.encode("utf-8")
>>> type(utf8_string)
<type 'unicode'>
>>> u2 = utf8_string.decode("utf-8")
>>> unicode_string == u2
True
```

不幸なことに Python 2.xではバイト列に ASCIIしか存在しない場合,
`unicode`と `str`を混ぜることができ, ASCII以外の文字が含まれると
`UnicodeDecodeError`が発生してしまいます.

```
>>> utf8_string = " sind rund"
>>> unicode_string + utf8_string
u'Fu\xdfb\xe4lle sind rund'
>>> utf8_string = " k\xc3\xb6nnten rund sein"
>>> print utf8_string
 könnten rund sein
>>> unicode_string + utf8_string
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 2:
  ordinal not in range(128)
```


### 4.2.2 GTK+における Unicode

GTK+では, すべてのテキストに, UTF-8でエンコードされた文字列を使います.
これは文字列を返すメソッドを呼ぶとき, 常に `str`インスタンスを受け取る
ことを意味します. 同様に文字列を引数として受け取るメソッドでは, 引数は
UTF-8にエンコードされている必要があります. しかし利便性のため PyGObjectは
引数で与えられるとき自動的に `unicode`インスタンスを `str`インスタンスに
変換します.

```
>>> from gi.repository import Gtk
>>> label = Gtk.Label()
>>> unicode_string = u"Fu\u00dfb\u00e4lle"
>>> label.set_text(unicode_string)
>>> txt = label.get_text()
>>> type(txt), txt
(<type 'str'>, 'Fu\xc3\x9fb\xc3\xa4lle')
>>> txt == unicode_string
__main__:1: UnicodeWarning: Unicode equal comparison failed to convert
both arguments to Unicode - interpreting them as being unequal
False
```

最後の警告に注目してください. `Gtk.Label.set_text()`の引数を `unicode`
インスタンスを使って呼び出していますが, `Gtk.Label.get_text()`では
常に `str`インスタンスが返ってきています. よって `txt`と `unicode_string`が
等しくないわけです.

これは `gettext`を使って国際化対応させる場合にとても重要になります.
すべての言語において, gettextは UTF-8でエンコードされたバイト列を
返すことを保証しなくてはなりません. 一般的に GTK+アプリケーション
では, GTK+が完全に `unicode`オブジェクトを扱えるわけではないので
`unicode`オブジェクトを使うことは推奨されず, UTF-8にエンコード
された `str`オブジェクトのみを使うことが推奨されます. そうしなければ,
GTK+メソッドを呼ぶたびに Unicode文字列にデコードする必要があります.

```
>>> txt = label.get_text().decode("utf-8")
>>> txt == unicode_string
True
```

## 4.3 Python3

## 4.3.1 Python3.xでの Unicodeのサポート

Python 3.0から, すべての文字列は Unicodeとして `str`型のインスタンスに
保持されるようになりました. 一方エンコードされた文字列は, バイト列と
して `bytes`型で表現されるようになりました. 概念的に `str`はテキストで
あり, `bytes`はデータです. `str.encode()`を使うことで, `str`から `byte`に
`bytes.decode()`を使うことで `bytes`から `data`に変換できます.

加えて, Unicode文字列とエンコードされた文字列を混ぜあわせることは
型エラーによりできなくなりました.

```
>>> text = "Fu\u00dfb\u00e4lle"
>>> data = b" sind rund"
>>> text + data
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: Can't convert 'bytes' object to str implicitly
  >>> text + data.decode("utf-8")
  'Fußbälle sind rund'
  >>> text.encode("utf-8") + data
  b'Fu\xc3\x9fb\xc3\xa4lle sind rund'
```

### 4.3.2 GTK+における Unicode

結果的に Python3ではことが明白になったので, メソッドから文字列を
渡すときも, 受け取るときも自動で UTF-8に変換するようになりました.
文字列(テキスト)は常に `str`インスタンスとして表現されるように
なりました.

```
>>> from gi.repository import Gtk
>>> label = Gtk.Label()
>>> text = "Fu\u00dfb\u00e4lle"
>>> label.set_text(text)
>>> txt = label.get_text()
>>> type(txt), txt
(<class 'str'>, 'Fußbälle')
>>> txt == text
True
```

## 4.4 リファレンス

[What's new in Python3.0](http://docs.python.org/py3k/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)では, テキストとデータの明確な違いについて記されています.

[Unicode HOWTO](http://docs.python.org/howto/unicode.html)では, Python2.xでサポートされる Unicodeについて述べられており,
Unicodeを扱う上で頻繁に遭遇する問題について説明されています.

[Unicode HOWTO for Python3.x](http://docs.python.org/dev/howto/unicode.html)では, Python 3.xでの Unicodeのサポートについて述べられています.

[UTF-8 encoding table and Unicode characters](http://www.utf8-chartable.de/)では, Unicdodeコードポイントの一覧と UTF-8のエンコード結果が示されています.
