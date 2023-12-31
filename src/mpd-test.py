#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORTS
import sys
import pprint
import time;
from perlish import *;

from mpd import (MPDClient, CommandError)
from Adafruit_CharLCD import Adafruit_CharLCD
from socket import error as SocketError

HOST = 'localhost'
PORT = '6600'
PASSWORD = False
##
CON_ID = {'host':HOST, 'port':PORT}
##  

## Some functions
def mpdConnect(client, con_id):
    """
    Simple wrapper to connect MPD.
    """
    try:
        client.connect(**con_id)
    except SocketError:
        return False
    return True

def mpdAuth(client, secret):
    """
    Authenticate
    """
    try:
        client.password(secret)
    except CommandError:
        return False
    return True
##

def main(dobench):
    ## MPD object instance
    client = MPDClient()
    if mpdConnect(client, CON_ID):
        print('Got connected!')
    else:
        print('fail to connect MPD server.')
        sys.exit(1)

    # Auth if password is set non False
    if PASSWORD:
        if mpdAuth(client, PASSWORD):
            print('Pass auth!')
        else:
            print('Error trying to pass auth.')
            client.disconnect()
            sys.exit(2)

    ## Fancy output
    pp = pprint.PrettyPrinter(indent=4)

    ## Print out MPD stats & disconnect
    st = client.status();
    print('\nCurrent MPD state:')
    pp.pprint(st);

    song = client.currentsong()
    print('\nCurrent Song:'); 
    pp.pprint(song);

    plist = client.playlist()
    print('\nPlaylist'); 
    pp.pprint(plist);

#    decoders = client.decoders()
#    print('\nDecoders'); 
#    pp.pprint(decoders);


#    print('\nMusic Library stats:')
#    pp.pprint(client.stats())

    if(st['state'] == 'stop'):
        nt = 'stopped';
    elif(st['state']== 'play'):
        song = client.currentsong();
        nt = '';
        if('name' in song):
            nt += song['name'];
        if('title' in song):
            nt += song['title'];
        if(len(nt) < 1):
            nd = sprintf("%s:%s", song['id'], song['file']);

    s = sprintf("%-40.40s", nt);
    printf("[%s]\n", s);

    if(dobench):
        nloops=100;
        tstart = time.time();
        for i in range(0,nloops):
            st = client.status();

        tend = time.time();
        ttime = tend-tstart;

        printf("%d loops in %f sec; %f/sec\n", nloops, ttime, nloops/ttime);
    
    client.disconnect()
    sys.exit(0)

# Script starts here
if __name__ == "__main__":
    if(len(sys.argv)>1 and sys.argv[1] == '--benchmark'):
        dobench = 1
    else:
        dobench = 0
    main(dobench)
