#!/usr/bin/env python3
""" Frontend for phoronix-test-suite"""

from gi.repository import Gio, GLib, Gtk
import gi
gi.require_version('Gtk', '3.0')


class frontend(Gtk.Application):
    def __repr__(self):
        return '<Application>'

    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="com.opensourcepc.ptsfrontend",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.new_window)

    def new_window(self, *args):
        AppWindow(self)

    def new_about_window(self, *args):
        AboutWindow(self)


class Handler:
    """ all Glade signals go here """

    # Main window items
    def on_quit(self):
        Gtk.Application.quit(Application)

    def on_buttonClose_clicked(self, button):
        self.on_quit()

    def on_buttonRun_clicked(self, button):
        print("This is a placeholder for the start of the logic.")

    def on_deleteWindow(self, event, args):
        self.on_quit()

    # Menu items
    def on_menuAbout_activate(self, menuitem):
        AboutWindow.open_about()

    def on_menuExit_activate(self, menuitem):
        self.on_quit()

    def on_aboutClose_clicked(self, button):
        AboutWindow.close_about()


class Builder():
        # try to read Glade file
        try:
            global builder
            builder = Gtk.Builder()
            builder.add_from_file("./data/ptsgui.glade")
        except GObject.GError:
            print("Error reading GUI file")
            raise
        builder.connect_signals(Handler())


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        self.Application = application
        mainWindow = builder.get_object("mainWindow")
        mainWindow.set_application(application)
        mainWindow.show()


class AboutWindow(Gtk.AboutDialog):
    def __init__(self):
        global awopen
        awopen = builder.get_object("aboutWindow")

    @classmethod
    def open_about(self):
        AboutWindow.__init__(self)
        awopen.show()

    @classmethod
    def close_about(self):
        awopen.hide()


def main():
    global Application
    Application = frontend()
    Application.run()


if __name__ == "__main__":
    main()
