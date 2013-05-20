#!/usr/bin/python
# -*- coding: utf8 -*-

from threadStoper import *
import threading
from gamePath import *
from parcoursRep import createRomsInfosListFromRep, cleanNonExistentPath
from log import writeInfo, writeError

#oui un nompourri, mais au moins on le confont pas :)
class Parcourateur(threading.Thread):
    def __init__(self,app):
        threading.Thread.__init__(self)
        self.app = app
        self.running = False

    def run(self):
        self.running = True
        writeInfo("Je run le Parcourateur")
        self.app.setStateText("Parcours in progress...")
        self.stoper = ThreadStoper()
        
        rep = self.app.config.c['repRoms']
        
        cleanNonExistentPath(self.app.p.pathAlreadyExplored)
        
        listCrc = createRomsInfosListFromRep(rep, self.app.p, self.stoper)
        for elt in listCrc:
            if elt not in self.app.r.roms:
                self.app.r.roms.append(elt)
        updateGamesInfoWithPath(self.app.r.roms, self.app.c.games)
        self.app.needRefresh = True
        
        self.running = False
        
        self.app.setStateText("Parcours Done.")
        writeInfo("Parcours Done.")
        
    def stop(self):
        writeInfo("On décide d'arréter le parcourateur")
        self.stoper.doStop()

    def isRunning(self):
        return self.running
