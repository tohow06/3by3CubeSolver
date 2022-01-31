"""
 Copyright (c) 2015-2017 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

This file demonstrates using PyMata to control a stepper motor. It requires the use of the FirmataPlus
Arduino sketch included with this release.

It is based upon the following tutorial: https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors/overview
"""

import signal
import sys
import time

from PyMata.pymata import PyMata

# create a PyMata instance
firmata = PyMata("/dev/cu.wchusbserial14510")


def signal_handler(sig, frm):
    print('You pressed Ctrl+C!!!!')
    if firmata is not None:
        firmata.reset()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# send the arduino a firmata reset
firmata.reset()

# configure the stepper to use pins 9.10,11,12 and specify 512 steps per revolution

# move motor #0 500 steps forward at a speed of 20

for i in range(25):
	firmata.stepper_config(512, [12, 11, 10, 9])
	time.sleep(.5)
	firmata.stepper_request_library_version()
	print('ro')
	time.sleep(.5)



# close firmata
firmata.close()