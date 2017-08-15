#!/usr/bin/env python3
""" This is the main call for the OSPC
    version of the Phoronix Test Suite """

import sys
if sys.version_info < (3, 6):
    sys.exit('ERROR: This program requires Python 3.6 or newer')

from ospc_pts.gtk import PTSfe

ui = PTSfe()
ui.run()