#!/usr/bin/python
# -*- coding: utf8 -*-

#from qt import *

from PyQt4 import QtCore, QtGui

#Todo: gérer le cas où n sélectionne un élément pour le changer de couleur
#class MyQListBoxText(QListBoxText):
#    color = {'OK':QColor(0,170,127),'NOOK':QColor(170,2,86),'BADCOMPRESSION':QColor('lightgray'),'SELECTED':QColor('lightgray')}
#    state = 'NOOK'
#    def paint(self, arg2):
#        colorAppliquee = self.color[self.state]
#        arg2.setBackgroundColor(colorAppliquee)
#        arg2.setPen(colorAppliquee)
#        QListBoxText.paint(self,arg2)
        
#    def setState(self,state):
#        if state in self.color.keys():
#            self.state = state


class MyQListBoxText(QtGui.QListWidgetItem):
    color = {'OK':QtGui.QColor(0,170,127),'NOOK':QtGui.QColor(170,2,86),'BADCOMPRESSION':QtGui.QColor('lightgray')}
    state = 'NOOK'    
    def paintEvent(self, event):
        print "PaintEvent"
        painter = QtGui.QPainter()
        colorAppliquee = self.color[self.state]
        painter.setBackgroundColor(colorAppliquee)
        painter.setPen(colorAppliquee)
        QListWidget.paintEvent(self,event)
        
    def setState(self,state):
        if state in self.color.keys():
            self.state = state
            self.setTextColor(self.color[self.state])
