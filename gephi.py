#!/usr/bin/env python
import os
import sys
from igraph import *
#f = os.popen("ls -l")
#for i in f.readlines():
#     print "myresult:",i,
def sistema():
    print sys.platform
    return
def obrir(nom):
    if sys.platform == 'darwin':
        os.popen("/Applications/gephi.app/Contents/Resources/gephi/bin/gephi " "/Users/paupericay/Dropbox/MIIACS/Projecte/Programes/Comparador/networks/"+nom+".graphml")

    if sys.platform == 'linux2':
        os.popen("/home/pau/gephi/bin/gephi " "./networks/"+nom+".graphml")
    
    return
def obrirnet(nom):
    if sys.platform == 'darwin':
        os.popen("/Applications/gephi.app/Contents/Resources/gephi/bin/gephi " "/Users/paupericay/Dropbox/MIIACS/Projecte/Programes/Comparador/networks/"+nom+".net")
    
    if sys.platform == 'linux2':
        os.popen("/home/pau/gephi/bin/gephi " "./networks/"+nom+".net")    
    
    return
def escriuregraf(graf,llistacomunitats):
    print "\nTot seguit es procedira a guardar les comunitats com un atribut del graphml i carregar-lo amb el Gephi. Cal tenir en compte que les comunitats apareixeran com un atribut a la pestanya anomenada 'Ranking'\n"
    print '\nParticions disponibles:\n'
    con=0
    i=0
    while(i != len(llistacomunitats)):
        print '[',i,']', llistacomunitats[i]
        i+=2
        con+=1
    print '\nSelecciona una o varies particions per guardarles en format graphml.\n'
    ca = raw_input()
    caint = int(ca)
    membership = llistacomunitats[caint+1]
    nu = 0
    for m in membership:
        for l in m:
            graf.vs[l]['comunitat'] = nu
            #print graf.vs[l]
        nu+=1
    print '\nEscriu el nom del fitxer que es guardara el graphml:\n'
    nom = raw_input()
    graf.write_graphml('./graphmlcom/'+nom+".graphml")
    if sys.platform == 'darwin':
        os.popen("/Applications/gephi.app/Contents/Resources/gephi/bin/gephi " './graphmlcom/'+nom+".graphml")
    if sys.platform == 'linux2':
        os.popen("/home/pau/gephi/bin/gephi " './graphmlcom/'+nom+".graphml")
    return