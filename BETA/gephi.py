#!/usr/bin/env python
import os
import sys
#f = os.popen("ls -l")
#for i in f.readlines():
#     print "myresult:",i,
def sistema():
    print sys.platform
    return
def obrir(nom):
    os.popen("/Applications/gephi.app/Contents/Resources/gephi/bin/gephi " "/Users/paupericay/Dropbox/MIIACS/Projecte/Programes/Comparador/networks/"+nom+".graphml")
    return
def obrirnet(nom):
    os.popen("/Applications/gephi.app/Contents/Resources/gephi/bin/gephi " "/Users/paupericay/Dropbox/MIIACS/Projecte/Programes/Comparador/networks/"+nom+".net")
    return
