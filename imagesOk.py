#!/usr/bin/python
# -*- coding: utf8 -*-

import os, pickle

class imagesOk:
    def __init__(self,filename):
        self.imagesOk = []
        
        self.filename=filename
        if(os.path.exists(filename)):
            f = file(filename,'r')
            self.imagesOk = pickle.load(f)
            f.close()
        
    def sauver(self):
        f = file(self.filename,'w')
        pickle.dump(self.imagesOk,f) 
        f.close()

    def ajouterImage(self, i):
        if i not in self.imagesOk:
            self.imagesOk.append(i)

    def contientImage(self,i):
        return i in self.imagesOk