#!/usr/bin/python
# -*- coding: utf8 -*-



class GameInfo:
    imageNumber = None
    releaseNumber = None
    title = None
    saveType = None
    romSize = None
    publisher = None
    location = None
    sourceRom = None
    language = None
    files = None
    romCRC = None
    im1CRC = None
    im2CRC = None
    comment = None
    
    #liste de path où il est (les roms)
    path = None
    trimmedSize = None
    note = None
    
    def __init__(self):
        pass

    def __str__(self):
        s = "%s : %s" % (self.comment, self.title)
        return s
    
    def __repr__(self):
        return self.__str__()