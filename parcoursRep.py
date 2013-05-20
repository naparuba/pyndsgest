#!/usr/bin/python
# -*- coding: utf8 -*-


import os
import zipfile, tarfile
from tempfile import NamedTemporaryFile
from xmlInfo import *
from header import truncateRomFile
from log import writeInfo, writeError
from singleton import Singleton

#Interface pour gérer les fichier
class FileHandler(object):
    def __init__(self, file):
        self.file = file
        pass

    def getRomInfoListFromFile(self):
        pass

    def extractFromFileAndCrc(self, crc, dest):
        pass

#Vide
class VoidHandler(FileHandler):
    def getRomInfoListFromFile(self):
        writeError("Désolé, ce type de fichier n'est pas géré %s" % self.file)
        return []
        
    def extractFromFileAndCrc(self, crc, dest):
        writeError("Désolé, ce type de fichier n'est pas géré %s" % self.file)

#Gérer les .gz
class GzHandler(FileHandler):
    def getRomInfoListFromFile(self):
        writeError("Désolé, ce type de fichier n'est pas géré %s" % self.file)
        return []
    
    def extractFromFileAndCrc(self, crc, dest):
        writeError("Désolé, ce type de fichier n'est pas géré %s" % self.file)


#Gérer les 7z
class SevenZHandler(FileHandler):
    def getRomInfoListFromFile(self):
        if not gotLib7z:
            writeError("Sorry, You cannot use 7z file")
            return []
        listCrc = []
        writeInfo("Open 7Z file")
        fp = open(self.file, 'rb')
        archive = Archive7z(fp)
        for name in archive.getnames():
            crc = getCRCFromBuffer(archive.getmember(name).read())
            listCrc.append(crc)
        fp.close()  
        return listCrc

    def extractFromFileAndCrc(self, crc, dest):
        if not gotLib7z:
            writeError("Sorry, You cannot use 7z file")
            return False
        writeInfo("Extract 7Z file")
        fp = open(self.file, 'rb')
        archive = Archive7z(fp)
        for name in archive.getnames():
            fd = archive.getmember(name)
            crcFd = getCRCFromBuffer(fd.read())
            if crc == crcFd:
                writeInfo("On extracte un 7z %s" % file)
                fd.reset()
                data = fd.read()
                nameDest = os.path.basename(name)
                writeInfo("On extract du 7z " + nameDest)
                fdest = NamedTemporaryFile()
                #fdest = open("tmp" + "/" + nameDest, 'w+b', os.O_SYNC)
                fdest.write(data)
                fdest.flush()
                #fdest.close()
                print "Utilisation du fichier temporaire %s" % fdest.name
                #truncateRomFile("tmp" + "/" + nameDest, dest + "/" + nameDest)
                truncateRomFile(fdest.name, dest + "/" + nameDest)
                fdest.close()
                #os.remove("tmp" + "/" + nameDest)
            fp.close()
        writeInfo("Ecriture Finie")

#Gérer les zip
class ZipHandler(FileHandler):
    def getRomInfoListFromFile(self):
        listCrc = []
        writeInfo("Open Zip file %s" % self.file)
        fd = zipfile.ZipFile(self.file, "r")
        for name in fd.namelist():
            crc = getCRCFromInt(fd.getinfo(name).CRC)
            listCrc.append(crc)
        return listCrc

    def extractFromFileAndCrc(self, crc, dest):
        fd = zipfile.ZipFile(self.file, "r")
        for name in fd.namelist():
            crcFd = getCRCFromInt(fd.getinfo(name).CRC)
            #crcFd = getCRCFromBuffer(fd.read(name))
            if crc == crcFd:
                writeInfo("On extracte un Zip %s" % name)
                data = fd.read(name)
                fdest = NamedTemporaryFile()
                #fdest = open("tmp" + "/" + name, 'w+b', os.O_SYNC)
                fdest.write(data)
                fdest.flush()
                #fdest.close()
                #truncateRomFile("tmp" + "/" + name, dest + "/" + name)
                truncateRomFile(fdest.name, dest + "/" + name)
                #os.remove("tmp" + "/" + name)
                fdest.close()
        writeInfo("Ecriture Finie")

#Gérer les tar.gz
class TarGzHandler(FileHandler):
    def getRomInfoListFromFile(self):
        listCrc = []
        writeInfo("Open TarGz file")
        tar = tarfile.open(self.file, "r:gz")
        for element in tar:
            if element.isreg():
                fd = tar.extractfile(element)
                crc = getCRCFromBuffer(fd.read())
                fd.close()
                listCrc.append(crc)
        return listCrc

    def extractFromFileAndCrc(self, crc, dest):
        tar = tarfile.open(archive, "r:gz")
        for file in tar:
            if file.isreg():
                fd = tar.extractfile(file)
                crcFd = getCRCFromBuffer(fd.read())
                fd.close()
                if crc == crcFd:
                    writeInfo("On extracte un TarGz %s" % file)
                    fd = tar.extractfile(file)
                    data = fd.read()
                    print file.__dict__
                    name = os.path.basename(file.name)
                    writeInfo("On extract du TarGz ", name)
                    fdest = NamedTemporaryFile()
                    #fdest = open("tmp" + "/" + name, 'w+b', os.O_SYNC)
                    fdest.write(data)
                    fdest.flush()
                    #fdest.close()
                    #truncateRomFile("tmp" + "/" + name, dest + "/" + name)
                    truncateRomFile(fdest.name, dest + "/" + name)
                    fdest.close()
                    #os.remove("tmp" + "/" + name)
        writeInfo("Ecriture Finie")

#Gérer les fichiers à plat
class NdsHandler(FileHandler):
    def getRomInfoListFromFile(self):
        listCrc = []
        writeInfo("Open Nds file")
        fd = open(self.file, "rb")
        crc = getCRCFromBuffer(fd.read())
        listCrc.append(crc)
        fd.close()
        return listCrc
        
    def extractFromFileAndCrc(self, crc, dest):
        import shutil
        writeInfo("On copie direct le fichier %s vers %s" % (self.file,
                                                         dest + '/' + os.path.basename(self.file)))
        truncateRomFile(self.file,dest + '/' + os.path.basename(self.file))

#La factory des file handler
class FactoryFileHandler(Singleton):
    def __init__(self):
        pass
    
    def getFileHandler(self, file):

        #Attention, tar.gz avant gz tout cours
        associator = [('.zip', ZipHandler),
                      ('tar.gz', TarGzHandler),
                      ('.gz', GzHandler),
                      ('.7z', SevenZHandler),
                      ('.nds', NdsHandler)]

        for (extention, classe) in associator:
            if file.endswith(extention):
                return classe(file)
        
        writeError("File format not reconized")
        return VoidHandler(file)


gotLib7z = True
try:
    from py7zlib import Archive7z
    writeInfo("Got 7z Lib")
except:
    writeError('You cannot got 7z file.')
    writeError('See http://www.joachim-bauch.de/projects/python/pylzma/')
    gotLib7z = False

#cre une liste d'infos sur les roms a partir d'un répertoire
def createRomsInfosListFromRep(rep, pathExplored,stoper):
    '''fonction principale qui parcours les repertoires '''
    listCrc = []

    #on cré la factory de FileHandler
    ffh = FactoryFileHandler()
    
    for repertoire, sous_reps, fichiers in os.walk(rep):
        for fichier in fichiers:
            #on gère l'arrêt
            if stoper.isDoStop():
                writeInfo("Ordre d'arret du parcours de roms, on doit partir")
                return []
            path = os.path.join(repertoire,fichier)
            #print path
            if not pathExplored.contientPath(path):
                #on cré le FileHandler qui va gérer le fichier
                fh = ffh.getFileHandler(path)
                if fh is not None:
                    for item in fh.getRomInfoListFromFile():
                        listCrc.append([item,path])
                    pathExplored.ajouterPath(path)
    return listCrc

def extractFromPathAndCrc(archive,crc,dest):
    writeInfo("Extact From : %s to %s" % (archive, dest))

    #on cré la factory de FileHandler
    ffh = FactoryFileHandler()
    fh = ffh.getFileHandler(archive)    
    fh.extractFromFileAndCrc(crc, dest)

#Parcours une liste de path, nétoi ceux qui n'existent plus
def cleanNonExistentPath(liste):
    #print liste.__dict__
    for path in liste:
        if not os.path.exists(path):
            liste.remove(path)
#    return True
