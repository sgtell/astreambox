#!/usr/bin/python

import sys;

def printf(format, *args):
     sys.stdout.write(str(format) % args)

def fprintf(fp, format, *args): 
    fp.write(str(format) % args)

def sprintf(format, *args):
    return (str(format) % args);
