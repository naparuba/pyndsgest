#!/usr/bin/python
# -*- coding: utf8 -*-


import struct,os


class Header:
    gameTitle = None
    gameCode = None
    makerCode = None
    unitCode = None
    deviceCode = None
    cardSize = None
    cardInfo = None
    flags = None
    arm9Source = None
    arm9ExecAddr = None
    arm9CopyAddr = None
    arm9BinSize = None
    arm7Source = None
    arm7ExecAddr = None
    arm7CopyAddr = None
    arm7BinSize = None
    filenameTableOffset = None
    filenameTableSize = None
    fatOffset = None
    fatSize = None
    arm9OverlaySrc = None
    arm9OverlaySize = None
    arm7OverlaySrc = None
    arm7OverlaySize = None
    controlRegisterFlagInit = None
    controlRegisterFlagRead = None
    iconAndTitle = None
    secureCRC16 = None
    romTimeout = None
    arm9UnkAddr = None
    arm7unkAddr = None
    magicNumber = None
    romSize = None
    headerSize = None
    unknown = None
    gbaLogo = None
    logoCRC16 = None
    headerCRC16 = None
    reserved = None
    
    
    def __init__(self, romFile):
        
        header = self
        
        f = open(romFile, "rb")
        
        #Game title
        s = f.read(12)
        header.gameTitle = s
        #print s
        
        #Game code
        s = f.read(4)
        header.gameCode = s
        #print s
        
        #Maker code
        s = f.read(2)
        header.makerCode = s
        #print s
        
        #Unit code
        s = f.read(1)
        z = struct.unpack("b",s)
        header.unitCode = z
        #print z
        
        #Device code
        s = f.read(1)
        z = struct.unpack("b",s)
        header.deviceCode = z
        #print z
        
        
        #Card size, 7=16Mo = 2^(20+7) = 128MB = 16Mo
        s = f.read(1)
        z = struct.unpack("b",s)
        header.cardSize = z
        #print z
        
        #Card Info
        s = f.read(10)
        z = struct.unpack("bbbbbbbbbb",s)
        header.cardInfo = z
        #z = tuple de 10elts
        
        
        #Flags
        s = f.read(1)
        z = struct.unpack("b",s)
        header.flags = z
        #print z
        
        #ARM9 source
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9Source = z
        #print z
        
        #ARM9 execute addr
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9ExecAddr = z
        #print z
        
        #ARM9 copy to addr
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9CopyAddr = z
        #print z
        
        #ARM9 binary size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9BinSize = z
        #print z
        
        #ARM7 source (ROM)
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7Source = z
        #print z
        
        #ARM7 execute addr
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7ExecAddr = z
        #print z
        
        #ARM7 copy to addr
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7CopyAddr = z
        #print z
        
        #ARM7 binary size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7BinSize = z
        #print z
        
        #Filename table offset (ROM)
        s = f.read(4)
        z = struct.unpack("l",s)
        header.filenameTableOffset = z
        #print z
        
        #Filename table size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.filenameTableSize = z
        #print z
        
        #FAT offset (ROM)
        s = f.read(4)
        z = struct.unpack("l",s)
        header.fatOffset = z
        #print z
        
        #FAT size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.fatSize = z
        #print z
        
        #ARM9 overlay src (ROM)
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9OverlaySrc = z
        #print z
        
        #ARM9 overlay size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9OverlaySize = z
        #print z
        
        #ARM7 overlay src (ROM)
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7OverlaySrc = z
        #print z
        
        #ARM7 overlay size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7OverlaySize = z
        #print z
        
        #Control register flags for read
        s = f.read(4)
        z = struct.unpack("l",s)
        header.controlRegisterFlagRead = z
        #print z
        
        #Control register flags for init
        s = f.read(4)
        z = struct.unpack("l",s)
        header.controlRegisterFlagInit = z
        #print z
        
        #Icon+titles (ROM)
        s = f.read(4)
        z = struct.unpack("l",s)
        header.iconAndTitle = z
        #print z
        
        #Secure CRC16
        s = f.read(2)
        z = struct.unpack("h",s)
        header.secureCRC16 = z
        #print z
        
        #ROM timeout
        s = f.read(2)
        z = struct.unpack("h",s)
        header.romTimeout = z
        #print z
        
        #ARM9 unk addr
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm9UnkAddr = z
        #print z
        
        #ARM7 unk addr
        s = f.read(4)
        z = struct.unpack("l",s)
        header.arm7unkAddr = z
        #print z
        
        #Magic number for unencrypted mode
        s = f.read(8)
        z = struct.unpack("bbbbbbbb",s)
        header.magicNumber = z
        #print z
        
        #ROM size  <-- utile pour troncatener un fichier...
        s = f.read(4)
        z = struct.unpack("l",s)
        header.romSize = z
        #print "rom size = %X" % z
        
        #Header size
        s = f.read(4)
        z = struct.unpack("l",s)
        header.headerSize = z
        #print z
        
        #Unknown 5
        s = f.read(56)
        #z = struct.unpack("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",s)
        z = struct.unpack("b"*56,s)
        header.unknown = z
        #print z
        
        #GBA logo 156!!
        s = f.read(156)
        z = struct.unpack("b" * 156,s)
        header.gbaLogo = z
        #print z
        
        #Logo CRC16
        s = f.read(2)
        z = struct.unpack("h",s)
        header.logoCRC16 = z
        #print z
        
        #Header CRC16
        s = f.read(2)
        z = struct.unpack("h",s)
        header.headerCRC16 = z
        #print z
        
        #Reserved 160!!
        s = f.read(160)
        z = struct.unpack("b" * 160,s)
        header.reserved = z
        #print z
        
        f.close()





def truncateRomFile(rom, romDest):
    h = Header(rom)
    taille = h.romSize
    #taille = tailleTmp[0]
    
    dest = open(romDest,'w', os.O_SYNC)

    fd = open(rom,'r')
    dest.write(fd.read(taille[0]))
    fd.flush()
    fd.close()
    
    dest.close()
    
    fd = open(rom,'rb')
    print "Len = %s" % len(fd.read())
    fd.close()
    
    fd = open(romDest,'rb')
    print "LenTrunc = %s" % len(fd.read())
    fd.close()
    
if __name__ == '__main__':
    import sys
    h = Header(sys.argv[1])
    
    print "adresse Icon and Title %s" % h.iconAndTitle[0]
    
    fd = open(sys.argv[1],'rb')
    print type(h.iconAndTitle[0])
    fd.seek(h.iconAndTitle[0])
    buffer = fd.read(2112)
    fd.close()
    
    #Version
    garbish = buffer[1:32]
    print "Garbish %s" % garbish 
    #z = struct.unpack("bb",s)
    
    #tile
    tile = buffer[32:544]
    print "tile %s" % tile
    
    palette = buffer[544:576]
    
    japTitle = buffer[576:832]
    print "JapTitle = %s" % japTitle
    
    englishTitle = buffer[832:1088]
    print "English = %s" % englishTitle
    
    print "Buffer = %s" % buffer
    
    truncateRomFile(sys.argv[1],sys.argv[2])
    print "Done."
