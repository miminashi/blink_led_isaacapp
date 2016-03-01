#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mraa
import time

print("Hello mraa\nVersion: %s" % mraa.getVersion())

gpio = mraa.Gpio(9)
gpio.dir(mraa.DIR_OUT)

while True:
    #gpio.write(1)
    #time.sleep(0.1)

    #gpio.write(0)
    #time.sleep(0.2)
    pass

gpio.dir(mraa.DIR_IN)
