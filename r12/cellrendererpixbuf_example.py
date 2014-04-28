#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class CellRendererPixbufWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererPixbuf Example")

        self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["New", Gtk.STOCK_NEW])
        self.liststore.append(["Open", Gtk.STOCK_OPEN])
        self.liststore.append(["Save", Gtk.STOCK_SAVE])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_pixbuf = Gtk.CellRendererPixbuf()

        column_pixbuf = Gtk.TreeViewColumn("Image", renderer_pixbuf, stock_id=1)
        treeview.append_column(column_pixbuf)

        self.add(treeview)

win = CellRendererPixbufWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()