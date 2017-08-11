#!/usr/bin/env python3
""" This is a GUI frontend for the phronix-test-suite
that simplifies stress-test for burn-in"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BurninPTS(self):

    def on_window_destroy(self, object):
        Gtk.main_quit()

    def on_menu_quit(self, menuitem):
        Gtk.main_quit()

    def __init__(self):
        self.gladefile = "ptsgui.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("mainWindow")
        self.window.show()
        self.aboutdialog = self.builder.get_object("aboutdialog")

if __name__ == "__main__":
    main = BurninPTS()
    Gtk.main()
