#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        self.append( "WFUV", "http://wfuv-onair.streamguys.org:80/onair-hi")
        self.append( "FUV2", "http://wfuv-music.streamguys.org:80/music-hi")
        self.append( "WKNC", "http://wknc.sma.ncsu.edu:8000/wknchq.ogg");
        self.append( "KCRW", "http://kcrw.ic.llnwd.net/stream/kcrw_live");
        self.append( "KSDS", "http://listen.jazz88.org/ksds.mp3");
        self.append( "WBGO", "http://wbgo.streamguys.net:8000");
        self.append( "WWOZ", "http://50.31.135.43:80/wwoz-hi.mp3");
        self.append( "WNYC", "http://fm939.wnyc.org/wnycfm.aac");

        self.append( "WAMU", "http://wamu-1.streamguys.com:80");
        self.append( "KPCC", "http://live.scpr.org/kpcclive");
        self.append( "WSHA", "http://live.wshafm.org/WSHA?MSWMExt=.asf");
        self.append( "WNCU", "http://stream.publicbroadcasting.net/production/mp3/wncu/local-wncu-974743.mp3");
        self.append( "KLCK", "http://edgev1.den.echo.liquidcompass.net/KLCKFMMP3?ats=1");
        self.append( "WJMU", "mms://streaming.millikin.edu/wjmu");
        self.append( "WEXT", "http://live.str3am.com:2080/wext1");
        self.append( "WGFR", "http://wgfr.streamon.fm:8000/WGFR-24k.aac");

        self.append( "WUNC", "http://mediaserver.wuncfm.unc.edu:8000/wunc128");
        self.append( "UNC2", "http://marconi.wuncfm.unc.edu:8000/wunc_hd2_mp3");
        
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
    ss.writefile("/tmp/stationlist");
    oldlist = ss.list;
    ss.readfile("/tmp/stationlist");
    ss.readfile_if_newer("/tmp/stationlist");
    ss.printall();


if __name__ == "__main__":
    main()

            
