#!/usr/bin/python
# -*- coding: utf8 -*-

class ThreadStoper:
    def __init__(self,b = False):
        self.toStop = b
    
    #Dit si on doit s'arréter
    def isDoStop(self):
        return self.toStop

    #c'est l'ordre d'arret.
    def doStop(self):
        self.toStop = True