#!/usr/bin/python
# -*- coding: utf8 -*-
from tableauLangues import *
from xmlInfo import dec2bin

def alwaysTrue(objet,args):
    return True

def justAvailableGames(game,arg=None):
    return game.path != []

def justNonAvailableGames(game,arg=None):
    return not justAvailableGames(game)

#Vieile feinte: le search permet de trouver dans toute la string
def fromTitleName(game,name):
    import re, string
    return bool(re.search(string.lower(name),string.lower(game.title)))

def fromNote(game,note):
    if game.note == None:
        game.note = 0
    return game.note >= note

def fromRomSize(game,size):
    return int(game.romSize) == size

def fromLangues(game,langueCherchee):
    indexLangues = dec2bin(int(game.language))
    langues = TableauLangues(indexLangues)
    return langues.gotLangue(langueCherchee)