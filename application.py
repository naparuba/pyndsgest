#!/usr/bin/python
# -*- coding: utf8 -*-

import sys, string, pickle, os, copy, threading
#from qt import *
from main import *

from xmlInfo import *
from parcoursRep import createRomsInfosListFromRep, extractFromPathAndCrc
from config import Config
from tableauLangues import *
from tableauLocations import *
from threadStoper import *
from xmlUpdater import *
from gamePath import *
from parcourateur import *
from romSender import *
from myQListBoxText import *
from pathExplorated import *
from imagesOk import *
from romsDispos import *
from filtres import *
from carnet import *
from log import *
#from getlib import Librairies

from PyQt4 import QtCore, QtGui

try: 
    import psyco
    psyco.full() 
    writeInfo("Psyco activated")
#    Librairies().addLib(("psyco",psyco)
except:
    writeError("Psyco not used")
    pass

    
class app:
    index = -1
    def __init__(self,args):         
        self.config = Config('config.txt')
        
       #on le pose lors qu'il faut remettre à jour la liste
        self.needRefresh = False
        
        #on cré le grabber web
        g = WebGrabber(self.config.c)
        
        # l'application Qt
        self.qtapp = QtGui.QApplication(args)
        
        #Mise en place d'un splash Screen
        fd = open("Bleu.png",'rb')
        buffer = fd.read()
        fd.close()
        img = QtGui.QPixmap();
        img.loadFromData(buffer,"PNG")
        splash = QtGui.QSplashScreen(img)
        splash.show()
                
        self.c = Carnet(self.config.c['gamesList'])
        #print self.c.__dict__
        self.r = romsDispos(self.config.c['romsList'])
        self.p = pathExplored(self.config.c['pathExplored'])
        self.i = imagesOk(self.config.c['imagesVerifiee'])
        
        # creation de la fenetre principale
        #self.win = Main()

        #print "Youhou"
        window = QtGui.QMainWindow()
        self.win = Ui_Main()
        self.win.setupUi(window)

        
        #On initilise le singleton des lib
        #self.lib = Librairies()

        #print "Youhou2"
        
        #On fait un test de changement d'adresse sur le label: pixmapLabel1
        fd = open("2a.png",'rb')
        buffer = fd.read()
        fd.close()
        
        img = QtGui.QPixmap();
        img.loadFromData(buffer,"PNG")
        self.win.pixmapLabel1.setPixmap(img)

        #print "Youhou2.5"
        
        # affichage de la liste des clients dans la fenetre
        self.updateList()
        # affichage de la fenetre
        #self.win.show()

        #print "Youhou3"

        self.statusBar = self.win.statusbar
        #print self.statusBar.__dict__
        self.statusBar.showMessage('The application is launched')
        
        #Les threads de l'application
        self.listThread = {'parcourateur' : None,
                            'xmlUpdater' : None,
                            'romSender' : None
                            }

        #print "Youhou2"
        
        #Tentative de Timer
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer,QtCore.SIGNAL("timeout()"),self.periodicCall)
        self.timer.start(100)
        
        #print "After Timer"
        
        #connect pour la recherche
        self.qtapp.connect(self.win.titleEdit,
                           QtCore.SIGNAL("textChanged(QString)"),
                           self.changedResearch)
        
        self.qtapp.connect(self.win.comboSize,
                           QtCore.SIGNAL("activated(int)"),
                           self.changedResearch)
        self.qtapp.connect(self.win.comboLangues,
                           QtCore.SIGNAL("activated(int)"),
                           self.changedResearch)
        
        #on modifie le niveau de recherche
        self.qtapp.connect(self.win.spinBoxSearchNote,
                           QtCore.SIGNAL("valueChanged(int)"),
                           self.changedResearch)
        

        
        #Connect pour les notes
        self.qtapp.connect(self.win.spinBoxNote,
                           QtCore.SIGNAL("valueChanged(int)"),
                           self.changedNote)
        
        # connection SLOT/SIGNAL de Qt
        self.qtapp.connect(self.win.fileSaveAction,
                           QtCore.SIGNAL("activated()"),
                           self.sauver)
        self.qtapp.connect(self.win.fileExitAction,
                           QtCore.SIGNAL("activated()"),
                           self.qtapp,QtCore.SLOT("quit()"))
        
        
        #rajout du bouton de listage XML
        self.qtapp.connect(self.win.updateXML,
                           QtCore.SIGNAL("clicked()"),
                           self.updateXML)
        
        #rajout du bouton de parcoursRep
        self.qtapp.connect(self.win.parcoursRep,
                           QtCore.SIGNAL("clicked()"),
                           self.parcoursRep)
        
        #bouton pour l'envoi de la rom vers la flash
        self.qtapp.connect(self.win.envoyer,
                           QtCore.SIGNAL("clicked()"),
                           self.envoyerVersFlash)
        
        self.qtapp.connect(self.win.liste,
                           QtCore.SIGNAL("currentRowChanged(int)"),
                           self.selectionListe)
        self.qtapp.connect(self.qtapp,
                           QtCore.SIGNAL("lastWindowClosed()"),
                           self.quitApplication)
        #self.trier()
        
        #on ferme le splash
        splash.finish(window)

        #print "Youhou final"
        window.show()        
        self.qtapp.exec_()


    def sauver(self):
        self.c.sauver()
        self.r.sauver()
        self.p.sauver()
        self.i.sauver()
    

    #Est appele de temps en temps
    def periodicCall(self):
        if self.needRefresh:
            writeInfo("On a besoin de refresh, on le fait")
            self.trier()
            self.needRefresh = False
        
    
    #Mettre la liste a jour
    def updateList(self):
        #print "Debut update"
        self.win.liste.clear()
        #print "After win.clear"
        #il faut creer une liste de filtres
        filtres = self.getfiltres()
        #print "Filtres = %s" % filtres
        stringCoupleList = self.c.listerGames(self.r.roms,filtres)
        #print "milieu update"
        for (state, string) in stringCoupleList:
            listBoxItem = MyQListBoxText(string)
            listBoxItem.setTextColor(QtGui.QColor(0,170,127))
            #brush.setColor(QtGui.QColor(0,170,127))
            #listBoxItem.setForeground(brush)
            listBoxItem.setState(state)
            #listBoxItem = MyQListBoxText(string)
            #listBoxItem.setState(state)
            self.win.liste.addItem(listBoxItem)
        #print "Fin update"

    #Cré les filtres suivants ce qu'a rentré l'utilisateur
    def getfiltres(self):
        filtres = []
        #deja le titre
        titleSearch = unicode(self.win.titleEdit.text())
        if titleSearch != u"":
            filtres.append((fromTitleName,titleSearch))
              
        #La taille
        sizeString = unicode(self.win.comboSize.currentText())

        if sizeString != u"All":
            #La taille compte....
            tailleString = {u"8Mo" : 8388608,
                            u"16Mo" : 16777216,
                            u"32Mo" : 33554432,
                            u"64Mo" : 67108864,
                            u"128Mo" : 134217728                        
                            }
        
            valSize = tailleString[sizeString]
            filtres.append((fromRomSize,valSize))
        
        #La langue
        langue = unicode(self.win.comboLangues.currentText())
        if langue != u"All":
            #La langue compte aussi :)
            filtres.append((fromLangues,langue))
        
        #La note
        note = self.win.spinBoxSearchNote.value()
        filtres.append((fromNote, note))
                
        return filtres

    
    # quand un element est selectionne dans la liste
    def selectionListe(self,index):
        self.index = index

        #print "On selectionne %s" % index
        
        #creation de la location
        #location = TableauLocations(int(self.c.game(index).location))
        
        #on cre la liste des langues et on envoi
        indexLangues = dec2bin(int(self.c.game(index).language))
        langues = TableauLangues(indexLangues)
        
        self.win.labelRelease.setText(self.c.game(index).comment)
        self.win.labelTitle.setText(self.c.game(index).title)
        sSize = str(int(self.c.game(index).romSize) /(1024 *1024)) + "Mo"
        self.win.labelSize.setText(sSize)
        self.win.labelLanguage.setText(langues.__str__())
        self.win.labelPath.setText("here")

        self.win.labelPath.setToolTip(str(self.c.game(index).path))
        #QToolTip.add(self.win.labelPath,str(self.c.game(index).path))
        
        #on positionne l'indicateur de note
        if self.c.game(index).note == None:
            self.c.game(index).note = 0
        self.win.spinBoxNote.setValue(self.c.game(index).note)
        
        #Et maintenant les images
        self.updateImages(self.c.game(index).imageNumber)

        
    #Met les images a jour
    def updateImages(self,index):
        #On fait un test de changement d'adresse sur le label: pixmapLabel1
        valeur = "%s" % index
        fd = open("data/"+valeur+"a.png",'rb')
        buffer = fd.read()
        fd.close()
        
        img = QtGui.QPixmap();
        img.loadFromData(buffer,"PNG")
        self.win.pixmapLabel1.setPixmap(img)
        
        #Image 2 (=b)
        valeur = "%s" % index
        fd = open("data/"+valeur+"b.png",'rb')
        buffer = fd.read()
        fd.close()
        
        img = QtGui.QPixmap();
        img.loadFromData(buffer,"PNG")
        self.win.pixmapLabel2.setPixmap(img)
        
        #Image 3 (la petite)
        valeur = getNumberStringFourCaract(int(index))
        fd = open("data/"+valeur+".png",'rb')
        buffer = fd.read()
        fd.close()
        
        img = QtGui.QPixmap();
        img.loadFromData(buffer,"PNG")
        self.win.pixmapLabel3.setPixmap(img)
    

    #Savoir si un autre thread est lancé
    def isAnotherThreadRunning(self):
        for thread in self.listThread.values():
            if thread != None:
                if thread.isRunning():
                    return True
        return False
    
    #Bouton parcoursRep
    def parcoursRep(self):
        if self.isAnotherThreadRunning():
            self.setStateText("Sorry, another thread is running")
            writeError("Sorry, another thread is running")
            return False
        self.listThread['parcourateur'] = Parcourateur(self)
        self.listThread['parcourateur'].start()

    
    # Action de tier
    def trier(self):
        #print "Print tier"
        self.c.trier()
        #print "On va appeler update"
        self.updateList()
        self.index=-1


    #Bouton de mise à jour du flux XML
    def updateXML(self):
        if self.isAnotherThreadRunning():
            self.setStateText("Sorry, another thread is running")
            writeError("Sorry, another thread is running")
            return False
        self.listThread['xmlUpdater'] = XMLUpdater(self)
        self.listThread['xmlUpdater'].start()


    #Bouton pour envoyer vers la carte flash
    def envoyerVersFlash(self):
        if self.isAnotherThreadRunning():
            self.setStateText("Sorry, another thread is running")
            writeError("Sorry, another thread is running")
            return False
        self.listThread['romSender'] = RomSender(self)
        self.listThread['romSender'].start()
        
        
    def changedResearch(self):
        self.trier()
    
    def changedNote(self, i):
        self.c.game(self.index).note = i
        #writeInfo("Note changée en " + str(i))
        
    def setStateText(self,text):
        self.statusBar.showMessage(text)
        #self.statusBar.message(text)
        #return 1
        
    def quitApplication(self):
        writeInfo("On quitte l'application")
        if self.listThread['parcourateur'] != None:
            writeInfo("on rejoint le parcourateur")
            self.listThread['parcourateur'].stop()
            self.listThread['parcourateur'].join()
        if self.listThread['xmlUpdater'] != None:
            writeInfo("On rejoint le xmlUpdater")
            self.listThread['xmlUpdater'].stop()
            self.listThread['xmlUpdater'].join()
        if self.listThread['romSender'] != None:
            writeInfo("on rejoint le romSender")
            self.listThread['romSender'].stop()
            self.listThread['romSender'].join()
        writeInfo("On a rejoint les threads")
        sys.exit(1)

        
def main(args):
    mapp = app(args)

if __name__=="__main__":
    main(sys.argv)
