#!/usr/bin/python

import time;
import sys

import RPi.GPIO as GPIO
from perlish import *

kdebug = False

class SgtMatrixKBD:
    def __init__(self, pin_rows=[5,6,13], pin_columns=[26,7,12,16]):
        self.GPIO = GPIO;
        self.pinR = pin_rows;
        self.pinC = pin_columns;
        self.keymap = { 0:  'P',
                        1:  'B',
                        2:  's',
                        3:  'D',
                        4:  '1',
                        5:  '2',
                        6:  '3',
                        7:  '4',
                        8:  '5',
                        9:  '6',
                        10: '7',
                        11: '8',
                        12: '',
                        13: '',
                        14: '',
                        15: ''};

        self.nkeys = len(self.pinR) * len(self.pinC);
        printf("nkeys=%d\n", self.nkeys);
        self.GPIO.setmode(GPIO.BCM)

        for r in range(0,3):
            GPIO.setup(self.pinR[r], GPIO.OUT)
            GPIO.output(self.pinR[r], 1);
        
        for c in range(0,4):
            GPIO.setup(self.pinC[c], GPIO.IN);

        self.oldbits = self.read_raw();

    def read_row(self,r):
        cbits = 0;
        self.GPIO.output(self.pinR[r], 0);
        for c in range(0,4):
            cbits <<= 1;
            cbits |= self.GPIO.input(self.pinC[c]);
        self.GPIO.output(self.pinR[r], 1);
        return cbits;

    def read_raw(self):
        rawbits = 0;
        for r in range(0,3):
            rawbits <<= 4;
            rawbits |= self.read_row(r);
        return rawbits;
    
    def poll_keycodes(self):
        global kdebug;
        keybits = self.read_raw();
        codes = [];
        if(keybits != self.oldbits):
            delta = keybits ^ self.oldbits;
            if(kdebug):
                printf("keybits: %03x  %03x\n", keybits, delta);

            for k in range(0, self.nkeys):
                m = 1<<k;
                if(delta & m):
                    if(keybits & m):
                        code = k | 0x80;  # pullup: 1=release
                    else:
                        code = k;	# press
                    if(kdebug):
                        printf("keycode: %02x\n", code);
                    codes.append(code);
                        
            self.oldbits = keybits;
        return codes;

    def code_to_symbol(self, c):
        cn = c & 0x7f
        if cn in self.keymap:
            if(c & 0x80):
                return('!' + self.keymap[c & 0x7f]);
            else:
                return(self.keymap[c]);
        else:
            return None;
            
    def poll(self):
        codes = self.poll_keycodes();
        syms = [];
        if(len(codes)>0):
            for c in codes:
                sym = self.code_to_symbol(c)
                if(sym):
                    syms.append(sym)
        return syms;

def main():
    global kdebug;
    kb = SgtMatrixKBD();
    kdebug = True
    raw = kb.read_raw()
    printf("initial: 0x%03x\n", raw);
    while(True):
        syms = kb.poll();
        if(len(syms)>0):
            printf("%s\n", str(syms));

    codes = kb.poll_keycodes();
    if(len(codes)>0):
        for c in codes:
            sym = kb.code_to_symbol(c)
            printf("0x02x   %s\n", c, str(sym))


# Script starts here
if __name__ == "__main__":
    main()

