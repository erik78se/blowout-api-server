#!/usr/bin/env python
from subprocess import call

# The GPIO numbers
gpios = [198,199,200,201]


def setGPIO_value(gpio_num, on=False):
    if on:
        value = 1
    else:
        value = 0
    cmd = "echo {} > /sys/class/gpio/gpio{}/value".format(value,gpio_num)
    call(cmd,shell=True)

setGPIO_value(198,on=False)
setGPIO_value(199,on=False)
setGPIO_value(200,on=False)
setGPIO_value(201,on=False)
