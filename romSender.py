#!/usr/bin/python
# -*- coding: utf8 -*-

from threadStoper import *
import threading
from gamePath import *
from parcoursRep import extractFromPathAndCrc


#nom classe mais qui au final ne fait pas grand chose...
class RomSender(threading.Thread):
    def __init__(self,app):
        threading.Thread.__init__(self)
        self.app = app
        self.running = False
        
    def run(self):
        self.running = True
        print "Je run RomSender"
        self.app.setStateText("RomSender in progress...")
        self.stoper = ThreadStoper()
        
        pathFlash = self.app.config.c['repFlash']
        crc = self.app.c.game(self.app.index).romCRC
        path = getPathFromCrc(self.app.r.roms,crc)
        if path != []:
            extractFromPathAndCrc(path, crc, pathFlash)
        
        if path != []:
            self.app.setStateText("Rom %s sent." % self.app.c.game(self.app.index).title)
        else:
            self.app.setStateText("No rom to send.")
        self.running = False
        print "RomSender Done."
        
    def stop(self):
        print "On décide d'arréter le romSenderr"
        self.stoper.doStop()

    def isRunning(self):
        return self.running
