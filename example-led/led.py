#!/usr/bin/python3

import time

import mraa

gpio = mraa.Gpio(23)
gpio.dir(mraa.DIR_OUT)

print("turning on, sleeping 2")
gpio.write(1)
time.sleep(2)

print("turning off")
gpio.write(0)
