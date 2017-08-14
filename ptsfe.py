#!/usr/bin/env python
""" Frontend for phoronix-test-suite"""

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk


class PTSfe(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="org.gnome.example",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

class Handler:
    """ all Glade signals go here """
    #Main window
    def on_mainWindow_destroy(self):
        Gtk.main_quit()

    #Menu items
    def on_menuAbout_activate(self, menuitem):
        aboutwindow.show_all()

    def on_menuExit_activate(self, menuitem):
        Gtk.main_quit()

    #About dialog
    def on_aboutClose_activate(self, button):
        aboutwindow.hide()

builder = Gtk.Builder()
builder.add_from_file("ptsgui.glade")
builder.connect_signals(Handler())

if __name__ == "__main__":
    #define common variables
    window = builder.get_object("mainWindow")
    aboutwindow = builder.get_object("aboutDialog")
    app = PTSfe()

    #actions 
    window.show_all()
    Gtk.main()