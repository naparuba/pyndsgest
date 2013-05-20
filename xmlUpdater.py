#!/usr/bin/python
# -*- coding: utf8 -*-

from threadStoper import *
import threading
from xmlInfo import *
from gamePath import *

class XMLUpdater(threading.Thread):
    def __init__(self,app):
        threading.Thread.__init__(self)
        self.app = app
        self.running = False
        
    def run(self):
        self.running = True
        print "Je run XMLUpdater"
        self.app.setStateText("XmlDowloading in progress...")
        self.stoper = ThreadStoper()
        
        document = getXmlDocument()
        self.app.c.games = createGameInfoListFromDocument(document)
        configuration = createConfigurationInfoFromDocument(document)
        updateGamesInfoWithPath(self.app.r.roms, self.app.c.games)
        self.app.i = updateImgsOnlyNecessary(self.app.c.games,
                                             "data",
                                             configuration,
                                             self.app.i,self.stoper)
        self.app.needRefresh = True
        
        self.running = False
        self.app.setStateText("XmlDowloading Done.")
        print "XmlDowloading Done."
        
    def stop(self):
        print "On décide d'arréter le xmlUpdater"
        self.stoper.doStop()
        
    def isRunning(self):
        return self.running
