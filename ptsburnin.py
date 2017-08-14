#!/usr/bin/env python3
""" This is a GUI frontend for the phronix-test-suite
that simplifies stress-test for burn-in"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BurninPTS:

    def __init__(self):
        self.gladefile = "ptsgui.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("mainWindow")
        self.aboutdialog = self.builder.get_object("aboutdialog")
        self.window.show()

    def on_window_destroy(self, object):
        Gtk.main_quit()

    def on_menu_quit(self, menu_quit):
        Gtk.main_quit()

    def on_gtk_about_activate(self, menu_about):
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()
    
    def on_butonabout_ok_activate(self, button_aboutok):
        self.aboutdialog.hide()

    # def on_ok_about_activate(self, button_aboutok):

if __name__ == "__main__":
    main = BurninPTS()
    Gtk.main()
