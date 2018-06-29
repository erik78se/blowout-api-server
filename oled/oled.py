#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from time import sleep
import urllib3
import json
import bakebit_128_32_oled as oledlib

__query_time__ = 10 # Config, query server every N seconds
__api_endpoint__ = 'http://127.0.0.1:9999/api/info'

# {"blowout":false,"blowout_weight":100,"current_weight":1,"increment":1}

def init():
    oledlib.init()                  #initialze SEEED OLED display
    oledlib.clearDisplay()          #clear the screen and set start position to top left corner
    oledlib.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
    oledlib.setPageMode()           #Set addressing mode to Page Mode

def main():
    init()
    while True:
        sleep(__query_time__)
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', __api_endpoint__)
            status_dict = json.loads(response.data.decode('UTF-8'))
        except:
            status_dict = {"blowout":'Unknown',
                           "blowout_weight":'Unknown',
                           "current_weight":'Unknown',
                           "increment":'Unknown'}
            pass
        
        oledlib.setTextXY(0,0)
        oledlib.putString("Blowout: {}".format(status_dict['blowout']))
        oledlib.setTextXY(0,1)
        oledlib.putString("Current: {}".format(status_dict['current_weight']))
        oledlib.setTextXY(0,2)
        oledlib.putString("Max: {}".format(status_dict['blowout_weight']))
        oledlib.setTextXY(0,3)
        oledlib.putString("Increment: {}".format(status_dict['increment']))
    
