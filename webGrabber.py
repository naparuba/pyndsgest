#!/usr/bin/python
# -*- coding: utf-8 -*-

from log import writeInfo, writeError

from singleton import Singleton

class WebGrabber(Singleton):
    g = None
    
    def __init__(self,config = {}):
        self.gotLibUrlGrabber = False
        try:
            from urlgrabber.grabber import URLGrabber
        except:
            writeError('This script is better with URLBrabber.')
            writeError('See http://linux.duke.edu/projects/urlgrabber/')
            self.gotLibUrlGrabber = False
            
        if not self.gotLibUrlGrabber:
            return
        if config.has_key('proxy'):
            writeInfo("URLGrabberWithProxy : %s" % config['proxy'])
            self.g = URLGrabber(proxies= {'http' : config['proxy']})
        else:
            writeInfo("URLGrabbersansProxy")
            self.g = URLGrabber()

    def getWebFile(self,url, dest):
        if not self.gotLibUrlGrabber:
            import urllib
            fd = open(dest,"wb")
            fd.write(urllib.urlopen(url).read())
            fd.close()
        else:
            urllib.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
            self.g.urlgrab(url, filename=dest)


if __name__ == '__main__':
    g = URLGrabber(proxies={'http' : 'http://proxy.free.fr:3128'})
    url = 'http://www.advanscene.com/offline/datas/ADVANsCEne_NDS.zip'
    g.urlgrab(url, filename='moncul.zip')

    g1 = WebGrabber(config={'proxy':'http://proxy.free.fr:3128'})
    g2 = WebGrabber()
    print "g1 is g2 %s" % (g1 is g2)
    
    g1.getWebFile('http://www.advanscene.com/offline/datas/ADVANsCEne_NDS.zip','moncul.zip')
    
    print "Done."
