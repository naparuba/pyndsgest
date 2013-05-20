#!/usr/bin/python
# -*- coding: utf-8 -*-


class TableauLangues:
    tableauCorrespondance = {
                             0: u"Français",
                             1: u"Anglais",
                             2: u"Chinois",
                             3: u"Inconnu2",
                             4: u"Néerlandais",
                             5: u"Inconnu3",
                             6: u"Allemand",
                             7: u"Italien",
                             8: u"Japonais",
                             9: u"Inconnu4",
                             10: u"Inconnu5",
                             11: u"Inconnu6",
                             12: u"Espagnol",
                             13: u"Inconnu7",
                             14: u"Inconnu8",
                             15: u"Inconnu9",
                             16: u"Coréen"
                             }
    
    tableauCorrespondanceInverse = {
                             u"Français" : 0,
                             u"Anglais" : 1,
                             u"Chinois" : 2,
                             u"Inconnu2" : 3,
                             u"Néerlandais" : 4,
                             u"Inconnu3" : 5,
                             u"Allemand" : 6,
                             u"Italien" : 7,
                             u"Japonais" : 8,
                             u"Inconnu4" : 9,
                             u"Inconnu5" : 10,
                             u"Inconnu6" : 11,
                             u"Espagnol" : 12,
                             u"Inconnu7" : 13,
                             u"Inconnu8" : 14,
                             u"Inconnu9" : 15,
                             u"Coréen" : 16
                             }
    
    def __init__(self,tab):
        self.tab=tab
    
#prends une chaine du type français et renvoi vrai ou faux
    def gotLangue(self,langue):
        import re, string
        index = self.tableauCorrespondanceInverse[langue]
        #print "index = %s" % index
        return self.tab[16 - index] == 1
#        return True       
        
    def __str__(self):
        firstAdd = True
        s = u""
        for i in range(len(self.tab)):
            if self.tab[i] == 1:
                if firstAdd == True:
                    s += self.tableauCorrespondance[16 - i] #attention, retournement
                    firstAdd = False
                else:
                    s += u", " + self.tableauCorrespondance[16 - i]
        return s