#!/usr/bin/env python
from subprocess import call
from pathlib import Path
import sys

# The GPIO numbers
gpios = [198,199,200,201]

def usage():
    print("<gpionumber> <on|off>")

def setGPIO_value(gpio_num, on=False):
    p = Path("/sys/class/gpio/gpio{}".format(gpio_num))
    assert(p.exists())
    if on:
        value = 1
    else:
        value = 0
    cmd = "echo {} > /sys/class/gpio/gpio{}/value".format(value,gpio_num)
    call(cmd,shell=True)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if not sys.argv[1].isdigit():
            raise("First argument must be a gpio number")
        else:
            gn = sys.argv[1]

        if sys.argv[2] == "on":
            setGPIO_value(gn, on=True)
        elif sys.argv[2] == "off":
            setGPIO_value(gn, on=False)
        else:
            usage()

    else:
        usage()
            
