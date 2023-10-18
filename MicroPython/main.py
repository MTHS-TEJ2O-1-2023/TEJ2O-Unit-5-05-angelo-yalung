"""
Created by: Angelo Yalung
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *
from neopixel import NeoPixel

num_pixels = 4
np = neopixel.NeoPixel(pin16, 4)

while True:
    if button_a.is_pressed():
        np[1] = (0, 255, 0)
        np.show()
        sleep(5000)

        np[2] = (255, 255, 0)
        np.show()
        sleep(5000)

        np[3] = (255, 0, 0)
        np.show()
        sleep(500)
