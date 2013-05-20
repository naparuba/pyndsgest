# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Feb 14 20:13:20 2007
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(QtCore.QSize(QtCore.QRect(0,0,736,654).size()).expandedTo(Main.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")

        self.labelSize = QtGui.QLabel(self.centralwidget)
        self.labelSize.setGeometry(QtCore.QRect(390,470,50,20))
        self.labelSize.setMinimumSize(QtCore.QSize(50,0))
        self.labelSize.setWordWrap(False)
        self.labelSize.setObjectName("labelSize")

        self.labelPath = QtGui.QLabel(self.centralwidget)
        self.labelPath.setGeometry(QtCore.QRect(390,490,50,20))
        self.labelPath.setMinimumSize(QtCore.QSize(50,0))
        self.labelPath.setWordWrap(False)
        self.labelPath.setObjectName("labelPath")

        self.textLabel3 = QtGui.QLabel(self.centralwidget)
        self.textLabel3.setGeometry(QtCore.QRect(320,470,50,20))
        self.textLabel3.setMinimumSize(QtCore.QSize(50,0))
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")

        self.labelTitle = QtGui.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(390,410,340,20))
        self.labelTitle.setMinimumSize(QtCore.QSize(50,0))
        self.labelTitle.setWordWrap(False)
        self.labelTitle.setObjectName("labelTitle")

        self.textLabel6 = QtGui.QLabel(self.centralwidget)
        self.textLabel6.setGeometry(QtCore.QRect(320,490,50,20))
        self.textLabel6.setMinimumSize(QtCore.QSize(50,0))
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")

        self.labelRelease = QtGui.QLabel(self.centralwidget)
        self.labelRelease.setGeometry(QtCore.QRect(320,410,54,20))
        self.labelRelease.setMinimumSize(QtCore.QSize(50,0))

        font = QtGui.QFont(self.labelRelease.font())
        font.setWeight(75)
        font.setBold(True)
        self.labelRelease.setFont(font)
        self.labelRelease.setWordWrap(False)
        self.labelRelease.setObjectName("labelRelease")

        self.textLabel5 = QtGui.QLabel(self.centralwidget)
        self.textLabel5.setGeometry(QtCore.QRect(320,450,62,20))
        self.textLabel5.setMinimumSize(QtCore.QSize(50,0))
        self.textLabel5.setWordWrap(False)
        self.textLabel5.setObjectName("textLabel5")

        self.pixmapLabel3 = QtGui.QLabel(self.centralwidget)
        self.pixmapLabel3.setGeometry(QtCore.QRect(280,410,32,32))
        self.pixmapLabel3.setScaledContents(True)
        self.pixmapLabel3.setWordWrap(False)
        self.pixmapLabel3.setObjectName("pixmapLabel3")

        self.labelLanguage = QtGui.QLabel(self.centralwidget)
        self.labelLanguage.setGeometry(QtCore.QRect(390,450,340,20))
        self.labelLanguage.setMinimumSize(QtCore.QSize(50,0))
        self.labelLanguage.setWordWrap(False)
        self.labelLanguage.setObjectName("labelLanguage")

        self.liste = QtGui.QListWidget(self.centralwidget)
        self.liste.setGeometry(QtCore.QRect(11,11,249,570))
        self.liste.setObjectName("liste")

        self.pixmapLabel1 = QtGui.QLabel(self.centralwidget)
        self.pixmapLabel1.setGeometry(QtCore.QRect(280,20,214,384))
        self.pixmapLabel1.setPixmap(QtGui.QPixmap("1a.png"))
        self.pixmapLabel1.setScaledContents(True)
        self.pixmapLabel1.setWordWrap(False)
        self.pixmapLabel1.setObjectName("pixmapLabel1")

        self.pixmapLabel2 = QtGui.QLabel(self.centralwidget)
        self.pixmapLabel2.setGeometry(QtCore.QRect(520,20,214,384))
        self.pixmapLabel2.setPixmap(QtGui.QPixmap("1a.png"))
        self.pixmapLabel2.setScaledContents(True)
        self.pixmapLabel2.setWordWrap(False)
        self.pixmapLabel2.setObjectName("pixmapLabel2")

        self.spinBoxNote = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxNote.setGeometry(QtCore.QRect(460,470,55,29))
        self.spinBoxNote.setMaximum(5)
        self.spinBoxNote.setMinimum(-1)
        self.spinBoxNote.setObjectName("spinBoxNote")

        self.titleEdit = QtGui.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(320,510,160,21))
        self.titleEdit.setObjectName("titleEdit")

        self.comboSize = QtGui.QComboBox(self.centralwidget)
        self.comboSize.setGeometry(QtCore.QRect(320,540,101,21))
        self.comboSize.setObjectName("comboSize")

        self.comboLangues = QtGui.QComboBox(self.centralwidget)
        self.comboLangues.setGeometry(QtCore.QRect(320,570,101,21))
        self.comboLangues.setObjectName("comboLangues")

        self.spinBoxSearchNote = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxSearchNote.setGeometry(QtCore.QRect(480,540,55,29))
        self.spinBoxSearchNote.setMaximum(5)
        self.spinBoxSearchNote.setMinimum(-1)
        self.spinBoxSearchNote.setObjectName("spinBoxSearchNote")

        self.updateXML = QtGui.QPushButton(self.centralwidget)
        self.updateXML.setGeometry(QtCore.QRect(670,550,61,51))
        self.updateXML.setIcon(QtGui.QIcon("stock-refresh-bis.png"))
        self.updateXML.setIconSize(QtCore.QSize(50,50))
        self.updateXML.setObjectName("updateXML")

        self.parcoursRep = QtGui.QPushButton(self.centralwidget)
        self.parcoursRep.setGeometry(QtCore.QRect(600,550,61,51))
        self.parcoursRep.setIcon(QtGui.QIcon("hd2-backup-bis.png"))
        self.parcoursRep.setIconSize(QtCore.QSize(50,50))
        self.parcoursRep.setObjectName("parcoursRep")

        self.envoyer = QtGui.QPushButton(self.centralwidget)
        self.envoyer.setGeometry(QtCore.QRect(670,480,61,61))
        self.envoyer.setIcon(QtGui.QIcon("stock-goto-bottom-bis.png"))
        self.envoyer.setIconSize(QtCore.QSize(50,50))
        self.envoyer.setObjectName("envoyer")
        Main.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0,0,736,25))
        self.menubar.setObjectName("menubar")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Main.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.fileSaveAction = QtGui.QAction(Main)
        self.fileSaveAction.setIcon(QtGui.QIcon("i-floppy-192.png"))
        self.fileSaveAction.setObjectName("fileSaveAction")

        self.fileExitAction = QtGui.QAction(Main)
        self.fileExitAction.setIcon(QtGui.QIcon("gtk-quit.png"))
        self.fileExitAction.setObjectName("fileExitAction")

        self.helpAboutAction = QtGui.QAction(Main)
        self.helpAboutAction.setObjectName("helpAboutAction")
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.helpAboutAction)
        self.menuEdit.addSeparator()
        self.menuEdit.addSeparator()
        self.menuFile.addAction(self.fileSaveAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.fileExitAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "PyNdsGest", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSize.setText(QtGui.QApplication.translate("Main", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPath.setText(QtGui.QApplication.translate("Main", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("Main", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTitle.setText(QtGui.QApplication.translate("Main", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("Main", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRelease.setText(QtGui.QApplication.translate("Main", "Release", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel5.setText(QtGui.QApplication.translate("Main", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLanguage.setText(QtGui.QApplication.translate("Main", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSize.addItem(QtGui.QApplication.translate("Main", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSize.addItem(QtGui.QApplication.translate("Main", "8Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSize.addItem(QtGui.QApplication.translate("Main", "16Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSize.addItem(QtGui.QApplication.translate("Main", "32Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSize.addItem(QtGui.QApplication.translate("Main", "64Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboSize.addItem(QtGui.QApplication.translate("Main", "128Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Français", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Anglais", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Chinois", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Néerlandais", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Allemand", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Italien", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Japonais", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Espagnol", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Inconnu9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboLangues.addItem(QtGui.QApplication.translate("Main", "Coréen", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Main", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Main", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Main", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSaveAction.setText(QtGui.QApplication.translate("Main", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setText(QtGui.QApplication.translate("Main", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.helpAboutAction.setText(QtGui.QApplication.translate("Main", "&About", None, QtGui.QApplication.UnicodeUTF8))
