/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Angelo Yalung
 * Created on: Oct 2023
 * This program turns the microbit into a traffic light
*/

// so i dont see a massive amount of errors
let neopixelStrip: neopixel.Strip = null

input.onButtonPressed(Button.A, function () {
  neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Green))
  neopixelStrip.show()
  basic.pause(5000)

  neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
  neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
  neopixelStrip.show()
  basic.pause(5000)

  neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
  neopixelStrip.show()
  basic.pause(5000)
})
