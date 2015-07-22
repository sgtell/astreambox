#!/usr/bin/python

import sys
import time;
from subprocess import *
from Adafruit_CharLCD import Adafruit_CharLCD
from datetime import datetime

def printf(format, *args):
     sys.stdout.write(str(format) % args)

lcd = Adafruit_CharLCD(pin_rs=17,
                       pin_e=27,
                       pins_db=[22,10,9,11]);

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

lcd.begin(40, 2)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

lcd.clear()
lcd.message(datetime.now().strftime('%b %d  %H:%M:%S  01234567890123456789\n'))
lcd.message("WFUV WKNC KCRW KSDS  WBGO WSHA WNYC WWOZ");


nloops=100;
tstart = time.time();
for i in range(0,nloops):
    lcd.setCursor(0, 1);  # col,row
    lcd.message("WFUV WKNC KCRW KSDS  WBGO WSHA WNYC WWOZ");
tend = time.time();
ttime = tend-tstart;

printf("%d loops in %f sec; %f/sec\n", nloops, ttime, nloops/ttime);


