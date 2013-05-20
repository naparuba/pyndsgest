#!/usr/bin/python
# -*- coding: utf8 -*-


import logging
#from   os.path import expanduser
import sys


#logFile = expanduser('~/svg2lvl.log')
logFile = 'pyndsgest.log'

def eraseLogFile():
    f = open(logFile, 'w')
    f.close()

#eraseLogFile()

logger = logging.getLogger('pyndsgest')
hdlr = logging.FileHandler(logFile)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


def writeInfo(msg):
    logger.info(msg)
    sys.stderr.write(msg + '\n')

def writeError(msg):
    logger.error(msg)
    sys.stderr.write(msg + '\n')
    
