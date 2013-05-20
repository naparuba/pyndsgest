#!/usr/bin/python
# -*- coding: utf8 -*-


import os, pickle


from gamePath import getPathFromCrc
from filtres import *


class Carnet:
    def __init__(self, filename):
        self.games = []
        self.gameFiltered = []
        
        self.filename = filename
        if(os.path.exists(filename)):
            fd = file(filename,'r')
            self.games = pickle.load(fd)
            fd.close()
        self.gameFiltered = self.createGamesFiltered()
        #print "game filtered = %s" % self.gameFiltered
    
    def sauver(self):
        fd = file(self.filename,'w')
        pickle.dump(self.games, fd) 
        fd.close()
        
    def game(self,indice):
        return self.gamesFiltered[indice]
        
    def supprimer(self, indice):
        del self.games[indice]
    
    # trie les clients selon la fonction de comparaison "sortFunc"    
    def trier(self):
        #print "appel a trier"
        self.games.sort(self.sortFunc)
        #print "Entre deux"
        self.gamesFiltered.sort(self.sortFunc)
        #print "Fin tier"
    
    # fonction de tri sur les noms des clients
    def sortFunc(self,x,y):
        #print "SortFunct"
        return cmp(x.comment , y.comment)

    def createGamesFiltered(self, filtres = [(alwaysTrue, None)]):
        print "on cré la liste filtrée avec %s" % filtres
        return [game for game in self.games if self.isFiltered(game, filtres)]
        #print "Res = %s" % res
        #return res

    #les filtres sont (fonction, arg), on filtre suivant TOUS les filtres
    def isFiltered(self, game, filtres):
        r = True
        for (filtre, arg) in filtres:
            r = r & filtre(game, arg)
        return r
        
    # representation des jeux sous forme de liste pour l'affichage
    def listerGames(self, romsList, filtres = [(alwaysTrue, None)]):
        self.gamesFiltered = self.createGamesFiltered(filtres)
        liste = []
        for game in self.gamesFiltered:
            if getPathFromCrc(romsList, game.romCRC) != []:#la on a la rom
                liste.append(('OK', repr(game)))
            else:
                liste.append(('NOOK', repr(game)))
        return liste

    def __repr__(self):
        return "\n".join(self.listerGames([]))
    
