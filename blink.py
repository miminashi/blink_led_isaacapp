#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mraa
import time
import signal

print("Hello mraa\nVersion: %s" % mraa.getVersion())

def exit_signal_handler(signo, frame):
    gpio = mraa.Gpio(9)
    gpio.write(0)
    gpio.enable(False)
    time.sleep(0.5)
    print("exitting...")
    exit()

# register signal handlers
signal.signal(signal.SIGHUP, exit_signal_handler)
signal.signal(signal.SIGINT, exit_signal_handler)
signal.signal(signal.SIGTERM, exit_signal_handler)

gpio = mraa.Gpio(9)
gpio.dir(mraa.DIR_OUT)

while True:
    gpio.write(1)
    time.sleep(0.1)

    gpio.write(0)
    time.sleep(0.2)

gpio.dir(mraa.DIR_IN)
