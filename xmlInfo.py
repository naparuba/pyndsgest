#!/usr/bin/python
# -*- coding: utf8 -*-

#Parcoure le xml situe sur
#http://www.advanscene.com/offline/datas/ADVANsCEne_NDS.zip

import os #parcours de rÃ©pertoire
import urllib, sys, xml.dom.minidom
import zipfile
import binascii # pour le calcul CRC

from webGrabber import WebGrabber
from gameInfo import GameInfo
from log import writeInfo, writeError

class ConfigurationInfo:
    datName = None
    datVersion = None
    system = None
    screenshotsWidth = None
    screenshotsHeight = None
    # a voir si on va vraiment remplir info
    info = None
    canOpen = None
    newDat = None
    search = None
    
    def __init__(self):
        pass

    def __str__(self):
        s = "datName = %s, datVersion = %s, system = %s, screenshotsWidth = %s, screenshotsHeight = %s, newDat = %s" % (self.datName, 
                                                                                                           self.datVersion,
                                                                                                           self.system,
                                                                                                           self.screenshotsWidth,
                                                                                                           self.screenshotsHeight,
                                                                                                           self.newDat)
        return s

class GuiInfo:
    def __init__(self):
        pass

class NewDat:
    datVersionURL = None
    datURL = None
    imURL = None
    def __init__(self):
        pass
    def __str__(self):
        s = "datVersionURL = %s, datURL = %s, imURL = %s" % (self.datVersionURL, self.datURL, self.imURL)
        return s

def getXmlDocument():
    #on se fiche de l'initialisation, elle est deja faite, simgleton
    g = WebGrabber()
    adress = 'http://www.advanscene.com/offline/datas/ADVANsCEne_NDS.zip'
    ziptmppath = 'data/ADVANsCEne_NDS.zip'
    xmltmppath = 'data/ADVANsCEne_NDS.xml'
    
    g.getWebFile(adress,ziptmppath)
    
    #maintenant on dezippe le fichier dans xmlpath
    xmltmp = open(xmltmppath,"wb")
    ziptmp = open(ziptmppath,"rb")
    #on read a l'intÃ©rieur du zip
    xmltmp.write(zipfile.ZipFile(ziptmp).read('ADVANsCEne_NDS.xml'))
    ziptmp.close()
    xmltmp.close()
    
    #On parse le document
    document = xml.dom.minidom.parse(xmltmppath)
    return document

def createGameInfoListFromDocument(document):
    listGamesBrut = document.childNodes[0].getElementsByTagName("games")[0].childNodes
    
    #on cree la liste des jeux
    games=[]
    listGames = [ gameNode for gameNode in listGamesBrut if gameNode.nodeType == gameNode.ELEMENT_NODE]
    
    for gameNode in listGames :
        #on chope le releaseNumber
        game=GameInfo()
        game.imageNumber = gameNode.getElementsByTagName("imageNumber")[0].childNodes[0].nodeValue
        game.releaseNumber = gameNode.getElementsByTagName("releaseNumber")[0].childNodes[0].nodeValue
        game.title = gameNode.getElementsByTagName("title")[0].childNodes[0].nodeValue
        game.saveType = gameNode.getElementsByTagName("saveType")[0].childNodes[0].nodeValue
        game.romSize = gameNode.getElementsByTagName("romSize")[0].childNodes[0].nodeValue
        game.publisher = gameNode.getElementsByTagName("publisher")[0].childNodes[0].nodeValue
        game.location = gameNode.getElementsByTagName("location")[0].childNodes[0].nodeValue
        game.sourceRom = gameNode.getElementsByTagName("sourceRom")[0].childNodes[0].nodeValue
        game.language = gameNode.getElementsByTagName("language")[0].childNodes[0].nodeValue
        #TODO: Peu etre un problème sur le files... surement vide
        game.files = gameNode.getElementsByTagName("files")[0].childNodes[0].nodeValue
        game.romCRC = gameNode.getElementsByTagName("romCRC")[0].childNodes[0].nodeValue
        game.im1CRC = gameNode.getElementsByTagName("im1CRC")[0].childNodes[0].nodeValue
        game.im2CRC = gameNode.getElementsByTagName("im2CRC")[0].childNodes[0].nodeValue
        game.comment = gameNode.getElementsByTagName("comment")[0].childNodes[0].nodeValue
        
        valString = "%s" % game.releaseNumber
        valInt = int(valString)
        games.append(game)
    return games

def createNewDatInfoFromNewDatNode(newDatNode):
    nd = NewDat()
    nd.datVersionURL = newDatNode.getElementsByTagName("datVersionURL")[0].childNodes[0].nodeValue
    nd.datURL = newDatNode.getElementsByTagName("datURL")[0].childNodes[0].nodeValue
    nd.imURL = newDatNode.getElementsByTagName("imURL")[0].childNodes[0].nodeValue
    return nd

def createConfigurationInfoFromDocument(document):
    configurationBrut = document.childNodes[0].getElementsByTagName("configuration")[0]#.childNodes

    configurationInfo = ConfigurationInfo()
    configurationInfo.datName = configurationBrut.getElementsByTagName("datName")[0].childNodes[0].nodeValue
    configurationInfo.datVersion = configurationBrut.getElementsByTagName("datVersion")[0].childNodes[0].nodeValue
    configurationInfo.system = configurationBrut.getElementsByTagName("system")[0].childNodes[0].nodeValue
    configurationInfo.screenshotsWidth = configurationBrut.getElementsByTagName("screenshotsWidth")[0].childNodes[0].nodeValue
    configurationInfo.screenshotsHeight = configurationBrut.getElementsByTagName("screenshotsHeight")[0].childNodes[0].nodeValue
    configurationInfo.newDat = createNewDatInfoFromNewDatNode(configurationBrut.getElementsByTagName("newDat")[0])
    #reste canOpen, newData, search    
    return configurationInfo




#chiffre = q * 500 + r
#attention, resultat 0 faux biensur.
def getURL500(chiffre):
    (q,r) = divmod(chiffre,500)
    #print "q= %d, r= %d" % (q,r)
    if r != 0 :
        return "%d-%d" % (q*500 + 1,(q+1)*500)
    else :
        return "%d-%d" % ((q-1)*500 + 1,q*500)
    


#renvoi le CRC meme avec un 0 sur un fichier
def getCRC(file):
    try:
        fd = open(file,'rb')
        i = binascii.crc32(fd.read())
        fd.close()
    except IOError:
        return "INEXISTANT"

    return getCRCFromInt(i)


def getCRCFromInt(i):
    maxValue = 0xFFFFFFFF
    if i < 0 :
        i = i + maxValue + 1
    r = "%X" % i
    if len(r) != 8 :
        r = "0"*(8-len(r)) + r
    return r


#pareil mais sur un buffer
def getCRCFromBuffer(buffer):
    i = binascii.crc32(buffer)
    return getCRCFromInt(i)


def isImgCRCIsGood(file,crc):
    return getCRC(file) == crc

#fonction qui chope toutes les images
def updateImgsForced(games, repDestination, configuration):
    g = WebGrabber()
    for game in games.values():
        #print type(game)
        numberInt = int(game.imageNumber)
        numberString = game.imageNumber
        g.getWebFile(configuration.newDat.imURL+"/"+getURL500(numberInt)+"/"+numberString+"a.png",repDestination+"/"+numberString+"a.png")
        crcAreel = getCRC(repDestination+"/"+numberString+"a.png")
        crcAattendu = game.im1CRC
        #print "%s : CRC reel %s, CRC attendu %s" % (numberString+"a",crcAreel,crcAattendu)
                
        crcBreel = getCRC(repDestination+"/"+numberString+"b.png")
        crcBattendu = game.im2CRC
        g.getWebFile(configuration.newDat.imURL+"/"+getURL500(numberInt)+"/"+numberString+"b.png",repDestination+"/"+numberString+"b.png")
        #print "%s : CRC reel %s, CRC attendu %s" % (numberString+"b",crcBreel,crcBattendu)
        
        if crcAreel != crcAattendu :
            writeError("%s CRC ERROR!" % (numberString+"a.png"))
        
        if crcBreel != crcBattendu :
            writeError("%s CRC ERROR!" % (numberString+"b.png"))
        
        
#tranforme un nombre 1 en 0001
def getNumberStringFourCaract(number):
   s = "%d" % number
   if len(s) != 4 :
       s = "0"*(4-len(s)) + s
   return s    
   

#Tente de voir si l'update est nécéssaire pour les images, si oui le fait
def updateImgsOnlyNecessary(games, repDestination, configuration, imagesValidees,stoper):
    g = WebGrabber()
    for game in games:
        #rearde si j'ai le droit de fonctionner
        if stoper.isDoStop():
            writeInfo("Je dois partir")
            return []
        numberInt = int(game.imageNumber)
        numberString = game.imageNumber
        fileDestA = repDestination+"/"+numberString+"a.png"
        fileDestB = repDestination+"/"+numberString+"b.png"
        webURLA = configuration.newDat.imURL+getURL500(numberInt)+"/"+numberString+"a.png"
        webURLB = configuration.newDat.imURL+"/"+getURL500(numberInt)+"/"+numberString+"b.png"
        
        #on ne rescan pas les images si on a deja fait et que c'est bon
        if not imagesValidees.contientImage(repDestination+"/"+numberString+"a.png"): 
            crcAreel = getCRC(repDestination+"/"+numberString+"a.png")
        else:
            crcAreel = game.im1CRC
        crcAattendu = game.im1CRC
        
        #pareil pour la b
        if not imagesValidees.contientImage(repDestination+"/"+numberString+"b.png"):
            crcBreel = getCRC(repDestination+"/"+numberString+"b.png")
        else:
            crcBreel = game.im2CRC
        
        crcBattendu = game.im2CRC
        
        #Si le fichier A a deja le bon CRC, on quitte
        if crcAreel == crcAattendu :
            imagesValidees.ajouterImage(repDestination+"/"+numberString+"a.png")
        else : #on get le fichier
            print webURLA, fileDestA
            g.getWebFile(webURLA,fileDestA)
            crcAreel = getCRC(repDestination+"/"+numberString+"a.png")
            if getCRC(repDestination+"/"+numberString+"a.png") == game.im1CRC :
                imagesValidees.ajouterImage(repDestination+"/"+numberString+"a.png")
            else :
                writeError("%s CRC ERROR!" % (numberString+"b.png"))
        
        if crcBreel == crcBattendu :
            imagesValidees.ajouterImage(repDestination+"/"+numberString+"b.png")
        else :
            g.getWebFile(webURLB,fileDestB)
            crcBreel = getCRC(repDestination+"/"+numberString+"b.png")
            if getCRC(repDestination+"/"+numberString+"b.png") == game.im2CRC :
                imagesValidees.ajouterImage(repDestination+"/"+numberString+"b.png")
            else :
                writeError("%s CRC ERROR!" % (numberString+"b.png"))
        if not os.path.exists(repDestination+"/"+getNumberStringFourCaract(numberInt) + ".png") :
            writeInfo("Get web File %s" % "http://www.advanscene.com/offline/imgs/NDSicon/"+getURL500(numberInt)+"/"+getNumberStringFourCaract(numberInt) + ".png")
            g.getWebFile("http://www.advanscene.com/offline/imgs/NDSicon/"+getURL500(numberInt)+"/"+getNumberStringFourCaract(numberInt) + ".png",repDestination+"/"+getNumberStringFourCaract(numberInt) + ".png")
    return imagesValidees

def dec2bin(n):
    q, r = -1, -1
    res = ""
    while q != 0:
        q, r = divmod(n, 2)
        res = `r` + res
        n = q
    res = (17 - len(res))*'0' + res
    res2 = [int(chiffre) for chiffre in res]
    return res2

if __name__ == '__main__':
    print "Done."
    
