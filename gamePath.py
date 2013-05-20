#!/usr/bin/python
# -*- coding: utf8 -*-

import os

def checkPath(path):
    if path is not None:
        if len(path) > 0:
            if os.path.exists(path):
                #print "C'est True!!!!"
                return True
    return False


def getPathFromCrc(romsDispos,crc):
    for couple in romsDispos:
        if crc in couple:              
           if len(couple) > 1:
              path = couple[-1]
              if checkPath(path):
                  return path
    return []

            
#met à jour dans les gamesInfos le path pour lecture avec juste le game
def updateGamesInfoWithPath(romsDispos,games):
    for game in games:
        path = getPathFromCrc(romsDispos,game.romCRC)
        #print path
        if not checkPath(game.path):
            #print "Put None in game.path %s" % game.path
            game.path = None
        game.path = getPathFromCrc(romsDispos,game.romCRC)
        
