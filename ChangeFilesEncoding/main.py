# -*- coding: utf-8 -*-
import sys
sourceEncoding = "utf-8"
targetEncoding = "Windows-1256"
source = open("/Users/diasaleh/Desktop/GP/test.txt")
target = open("/Users/diasaleh/Desktop/GP/testC.txt", "w")

target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))