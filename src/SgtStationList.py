#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os
import pprint
import time;
from perlish import *
from stat import *

class SgtStationList:
    def __init__(self):
        self.list = [];
        self.lastfiletime = 0;

    def length(self):
        return len(self.list);

    def append(self, call, url):
        ent = { "call":call, "url":url};
        self.list.append(ent);

    def calli(self, i):
        if(i < len(self.list)):
               return self.list[i]['call']
        else:
            return None

    def urli(self, i):
        if(i < len(self.list)):
            return self.list[i]['url']
        else:
            return None

    def initfixed(self):  
        "init from fixed list for early testing"
        self.append( "WFUV", "http://wfuv-onair.streamguys.org:80/onair-hi");
#        self.append( "FUV2", "http://wfuv-music.streamguys.org:80/music-hi")
        self.append( "WKNC", "https://streaming.live365.com/a45877");
        self.append( "KCRW", "https://kcrw.streamguys1.com/kcrw_128k_mp3_e24");
        self.append( "KSDS", "http://listen.jazz88.org/ksds.mp3");
        self.append( "WBGO", "https://wbgo.streamguys1.com/wbgo128");
#        self.append( "WWOZ", "https://wwoz-sc.streamguys1.com/wwoz-hi.mp3");
        self.append( "WWOZ", "http://wwoz.org/listen/hi");
        self.append( "WNYC", "http://fm939.wnyc.org/wnycfm.aac");
        self.append( "KRVS", "http://playerservices.streamtheworld.com/api/livestream-redirect/krvsfm.mp3");

        self.append( "KEXP", "http://kexp.streamguys1.com/kexp160.aac");
        self.append( "WAMU", "http://wamu-1.streamguys.com:80");
#        self.append( "KPCC", "http://live.wostreaming.net/direct/southerncalipr-kpccfmmp3-imc.mp3?source=kpcc");
#        self.append( "WSHA", "http://live.wshafm.org/WSHA?MSWMExt=.asf");
#        self.append( "WNCU", "http://stream.publicbroadcasting.net/production/mp3/wncu/local-wncu-974743.mp3");
#        self.append( "WJMU", "http://ice24.securenetsystems.net/WJMU?type=.mp3");
        self.append( "WEXT", "http://wmht.streamguys1.com/wext1");
        self.append( "WGFR", "http://wgfr.streamon.fm:8000/WGFR-24k.aac");

        self.append( "WUNC", "http://wunc-ice.streamguys1.com:80/wunc-128-mp3");
        self.append( "UNC2", "http://wunc-ice.streamguys1.com:80/wunc-hd2-128-mp3");
        
    def writefile(self, fname):
        fp = open(fname,  "w");
        pp = pprint.PrettyPrinter(indent=2, depth=2, stream=fp)
        pp.pprint(self.list);
        fp.close();
        pass

    def readfile(self, fname):
        fp = open(fname,  "r");
        fstr = fp.read(10000);
        st = os.fstat(fp.fileno());
        fp.close();
        newlist = eval(fstr, {"__builtins__": {}})
        if(type(newlist) == list):
            self.lastfiletime = st[ST_MTIME];
            self.list = newlist;
    
    def readfile_if_newer(self, fname):
        st = os.stat(fname);
        mtime = st[ST_MTIME];
        if(mtime > self.lastfiletime):
            printf("mtime=%d last=%d; reading.\n", mtime, self.lastfiletime);
            self.readfile(fname);
            return True;
        else:
            printf("mtime=%d last=%d; OK.\n", mtime, self.lastfiletime);
            return False;

    def printall(self):
        for i in range(0, self.length() ):
            printf("[%2d] %s: %s\n", i, self.calli(i), self.urli(i));

    def mpdplaylist(self, mpd):
        mpd.clear();
        for i in range(0, self.length() ):
            mpd.add( self.urli(i) );

    def mpdplaylist_one(self, mpd, entry):
        if(entry >= 0 and entry < self.length()):
            mpd.clear();
            mpd.add( self.urli(entry) );

    def mpdchecklist(self, mpd):
        plist = mpd.playlist()
        print('\nMPD Playlist'); 
        print(str(plist));
        # future: check MPDs list agains ours, return status.


# test script starts here
def main():
    ss = SgtStationList();
    ss.initfixed();
    ss.printall();
    ss.writefile("/tmp/stationlist");
    oldlist = ss.list;
    ss.readfile("/tmp/stationlist");
    ss.readfile_if_newer("/tmp/stationlist");
    ss.printall();


if __name__ == "__main__":
    main()

            
