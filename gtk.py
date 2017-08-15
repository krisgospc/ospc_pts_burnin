#!/usr/bin/env python3
""" Frontend for phoronix-test-suite"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk


class PTSfe(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="org.gnome.example",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.window = builder.get_object("mainWindow")
        self.aboutwindow = builder.get_object("aboutDialog")
        self.window.connect("delete-event", Gtk.main_quit)

class Handler:
    """ all Glade signals go here """

    #Main window items
    def on_buttonClose_clicked(self, button):
        Gtk.main_quit()

    def on_buttonRun_clicked(self, button):
        print("This is a placeholder")

    #Switches

    #Menu items
    def on_menuAbout_activate(self, menuitem):
        app.aboutwindow.show_all()

    def on_menuExit_activate(self, menuitem):
        Gtk.main_quit()

    #About dialog
    def on_aboutClose_clicked(self, button):
        app.aboutwindow.hide()

builder = Gtk.Builder()
builder.add_from_file("./data/ptsgui.glade")
builder.connect_signals(Handler())

if __name__ == "__main__":
    app = PTSfe()
    app.window.show_all()
    Gtk.main()