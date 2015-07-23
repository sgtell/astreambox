#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pprint
import time;
from perlish import *

class SgtStationEntry:
    def __init__(self, ncall, nurl):
        self.call = ncall;  # 4-character callsign/display-tag
        self.url = nurl;  # streaming URL

    def str(self):
        return sprintf("%s: %s", self.call, self.url);

    def callsign(self):
        return self.call;

    def url(self):
        return self.url;


class SgtStationList:
    def __init__(self):
        self.list = [];


    def initfixed(self):  
        "init from fixed list for early testing"
        self.list.append( SgtStationEntry("WFUV", "http://wfuv-music.streamguys.org:80/music-hi"))
        self.list.append( SgtStationEntry("WKNC", "http://wknc.sma.ncsu.edu:8000/wknchq.ogg"));
        self.list.append( SgtStationEntry("KCRW", "http://kcrw.ic.llnwd.net/stream/kcrw_live"));
        self.list.append( SgtStationEntry("KSDS", "http://listen.jazz88.org/ksds.mp3"));
        self.list.append( SgtStationEntry("WBGO", "http://wbgo.streamguys.net:8000"));

    def printall(self):
        for i in range(0, len(self.list)):

            printf("[%2d] %s\n", i, self.list[i].str() );

def main():
    ss = SgtStationList();
    ss.initfixed();
    ss.printall();

# test script starts here
if __name__ == "__main__":
    main()

            
