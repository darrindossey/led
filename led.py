#!/usr/bin/python

import threading
import leds

red="red"
on="on"
off="off"

 leds.control(red, on)
 leds.control(red,off)

 def gfg():
     print("Darrin Dossey Geek Control")
     leds.control(red, off)


timer = threading.Timer(.5, gfg)
timer.start()
leds.control(red, on)
print("Exit\n")
     
