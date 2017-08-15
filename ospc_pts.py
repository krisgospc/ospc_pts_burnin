#!/usr/bin/env python3
""" This is the main call for the OSPC
    version of the Phoronix Test Suite """

import sys
from ospcpts.gui import GUI

ui = GUI()
exit_status = ui.run(sys.argv)
sys.exit(exit_status)