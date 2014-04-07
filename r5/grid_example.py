#!/usr/bin/python2

from gi.repository import Gtk

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button1")
        button2 = Gtk.Button(label="Button2")
        button3 = Gtk.Button(label="Button3")
        button4 = Gtk.Button(label="Button4")
        button5 = Gtk.Button(label="Button5")
        button6 = Gtk.Button(label="Button6")

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
