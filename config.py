#!/usr/bin/python
# -*- coding: utf8 -*-

import os

DEFAULTDICT = {"repRoms": '/tmp',
               "titi": 1,
               "repFlash": '/media/DSX/apps'}

class Config:
    def __init__(self, file):
        #Open file: filename is... the filename.
        f = open(file,'r')
        try:
            #Read whole file as one string.
            data = f.read()
        finally:
            #Close file
            f.close()
        #Parse data string.
        
        """Parse a string into a dictionary."""
        #Fetch a *copy* of the default dictionary.
        ret = DEFAULTDICT.copy()
        #Split lines.
        lines = data.split("\n")
        #Loop through lines.
        for line in lines:
            #Strip whitespace.
            line = line.strip()
            #Skip comment and blank lines.
            if line and line[0] != "#":
                #Split the line in the pair key, value
                values = line.split('=')
                #Fill dictionary.
                ret[values[0]] = values[1]
        #Return dictionary.
        self.c = ret

if __name__ == '__main__':
    c = Config('config.txt')
    print c.c
    print "Done."
