#!/usr/bin/python
# -*- coding: utf8 -*-

import os, pickle

class romsDispos:
    def __init__(self,filename):
        self.roms = []
        self.filename=filename
        if(os.path.exists(filename)):
            f = file(filename,'r')
            self.roms = pickle.load(f)
            f.close()

    def sauver(self):
        f = file(self.filename,'w')
        pickle.dump(self.roms,f) 
        f.close()

    def ajouterRom(self, r):
        self.roms.append(r)
    
    def listerRoms(self):
        return [repr(rom) for rom in self.roms]