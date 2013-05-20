#!/usr/bin/python
# -*- coding: utf8 -*-

class TableauLocations:
    tableauCorrespondance = {
                             0: u"Europe",
                             1: u"USA",
                             2: u"Allemagne",
                             3: u"Chine",
                             4: u"Espagne",
                             5: u"France",
                             6: u"Italie",
                             7: u"Japon",
                             8: u"Inconnu2",
                             9: u"Inconnu3",
                             10: u"Inconnu4",
                             11: u"Inconnu5",
                             12: u"Inconnu6",
                             13: u"Inconnu7",
                             14: u"Inconnu8",
                             15: u"Inconnu9",
                             16: u"Inconnu10",
                             17: u"Inconnu11",
                             18: u"Inconnu12",
                             19: u"Inconnu13",
                             20: u"Inconnu14",
                             21: u"Inconnu15",
                             22: u"Corée du sud"
                             }
    def __init__(self,val):
        self.val = val
        
    def __str__(self):
        return self.tableauCorrespondance[self.val]