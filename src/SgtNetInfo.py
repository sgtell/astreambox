#!/usr/bin/python

import sys
import os
import pprint
import time
import re
import subprocess
from perlish import *

class SgtNetInfo:
    def __init__(self):
        self.clear()

    def clear(self):
        self.interface = None
        self.ipaddr = None
        self.up = False

    def getinfo(self):
        self.clear()
        self.get_interface("eth0")
        if(self.up):
            return
        self.get_interface("wlan0")
        
    def get_interface(self, intf):

        proc = subprocess.Popen(['ip','addr','show',intf],stdout=subprocess.PIPE)
        for line in proc.stdout:
            line = line.rstrip()
#            printf("line: %s\n", line.rstrip())
            if(re.search( " "+intf+": ", line)):
#                printf("  found interface line\n");
                if(re.search("UP", line)):
                    self.interface = intf
                    self.up = True
            else:
                m = re.search(" inet ([.0-9]+)/", line)
                if(m):
                    #printf("found inet line\n");
                    if(re.search("scope global", line)):
                        self.ipaddr = m.group(1)
                        #printf("ip=%s scope=global\n", self.ipaddr)

    def printinfo(self):
        printf("up=%s\n", str(self.up))
        printf("interface=%s\n", self.interface)
        printf("ipaddr=%s\n", self.ipaddr)


# Script starts here
if __name__ == "__main__":
    netinf = SgtNetInfo()
    netinf.getinfo()
    netinf.printinfo()

    
    
