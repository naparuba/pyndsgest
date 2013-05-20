#!/usr/bin/python
# -*- coding: utf8 -*-

import os,pickle

class pathExplored:
    def __init__(self,filename):
        self.pathAlreadyExplored = []
        
        self.filename=filename
        if(os.path.exists(filename)):
            f = file(filename,'r')
            self.pathAlreadyExplored = pickle.load(f)
            f.close()
        
    def sauver(self):
        f = file(self.filename,'w')
        pickle.dump(self.pathAlreadyExplored,f) 
        f.close()

    def ajouterPath(self, p):
        if p not in self.pathAlreadyExplored:
            self.pathAlreadyExplored.append(p)

    def contientPath(self,p):
        return p in self.pathAlreadyExplored