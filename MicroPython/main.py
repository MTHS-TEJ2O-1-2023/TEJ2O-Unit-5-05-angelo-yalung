"""
Created by: Angelo Yalung
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel


while True:
    if button_a.is_pressed():
        np[0] = (0, 255, 0)
        np.show()
        sleep(5000)
        clear()

        np[1] = (255, 255, 0)
        np.show()
        sleep(5000)
        clear()

        np[2] = (255, 0, 0)
        np.show()
        sleep(5000)
        clear()
