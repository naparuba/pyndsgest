#!/usr/bin/python
# -*- coding: utf8 -*-


from singleton import Singleton


class Librairies(Singleton):
    lib = []
    def __init__(self):
        pass

    def gotLib(name):
        for couple in self.lib:
            if name in couple:
                return True
        return False

    def addLib(couple):
        if not couple in self.lib:
            self.lib.append(couple)

    
