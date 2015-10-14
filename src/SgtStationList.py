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

    def length(self):
        return len(self.list);

    def calli(self, i):
        if(i < len(self.list)):
               return self.list[i].call;
        else:
            return None

    def urli(self, i):
        if(i < len(self.list)):
            return self.list[i].url;
        else:
            return None

    def initfixed(self):  
        "init from fixed list for early testing"
        self.list.append( SgtStationEntry("WFUV", "http://wfuv-music.streamguys.org:80/onair-hi"))
        self.list.append( SgtStationEntry("FUV2", "http://wfuv-music.streamguys.org:80/music-hi"))
        self.list.append( SgtStationEntry("WKNC", "http://wknc.sma.ncsu.edu:8000/wknchq.ogg"));
        self.list.append( SgtStationEntry("KCRW", "http://kcrw.ic.llnwd.net/stream/kcrw_live"));
        self.list.append( SgtStationEntry("KSDS", "http://listen.jazz88.org/ksds.mp3"));
        self.list.append( SgtStationEntry("WBGO", "http://wbgo.streamguys.net:8000"));
        self.list.append( SgtStationEntry("WWOZ", "http://50.31.135.43:80/wwoz-hi.mp3"));
        self.list.append( SgtStationEntry("WNYC", "http://fm939.wnyc.org/wnycfm.aac"));

        self.list.append( SgtStationEntry("WAMU", "http://wamu-1.streamguys.com:80"));
        self.list.append( SgtStationEntry("KPCC", "http://live.scpr.org/kpcclive"));
        self.list.append( SgtStationEntry("WSHA", "http://live.wshafm.org/WSHA?MSWMExt=.asf"));
        self.list.append( SgtStationEntry("WNCU", "http://stream.publicbroadcasting.net/production/mp3/wncu/local-wncu-974743.mp3"));
        self.list.append( SgtStationEntry("KLCK", "http://edgev1.den.echo.liquidcompass.net/KLCKFMMP3?ats=1"));
        self.list.append( SgtStationEntry("WJMU", "mms://streaming.millikin.edu/wjmu"));
        self.list.append( SgtStationEntry("WEXT", "http://live.str3am.com:2080/wext1"));
        self.list.append( SgtStationEntry("WGFR", "http://wgfr.streamon.fm:8000/WGFR-24k.aac"));


    def writefile(self):
        pass

    def readfile(self):
        pass

    def printall(self):
        for i in range(0, len(self.list)):
            printf("[%2d] %s\n", i, self.list[i].str() );

    def mpdplaylist(self, mpd):
        mpd.clear();
        for i in range(0, len(self.list)):
            mpd.add(self.list[i].url);

    def mpdchecklist(self, mpd):
        plist = mpd.playlist()
        print('\nMPD Playlist'); 
        print str(plist);
        # future: check MPDs list agains ours, return status.



# test script starts here
def main():
    ss = SgtStationList();
    ss.initfixed();
    ss.printall();

if __name__ == "__main__":
    main()

            
