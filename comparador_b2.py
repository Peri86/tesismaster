#!/usr/bin/env python

#import Tkinter llibreria grafica
from igraph import *

import glob
import cairo

############Dibuixar################
def dibuixar(pos,layout,com):
    plot(com,vertex_label=pos,layout=layout)
    return 
####################################

#####Funcio escollir algoritmes######
def escollir(arllegit):
    
    ###layout de la xarxa sera igual per tots els algoritmes##
    layout =  arllegit.layout()    
    pos = arllegit.vs["id"]
    #####
    
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algoritmes han d'estar separats per comes\n"
    print 'infomap'    
    print 'spinglass'    
    print 'multilevel'
    print '\n'
    
    
    esc = raw_input()
    sel = esc.split(',')
    
    for i in range(len(sel)):
        if sel[i] == "infomap":
            print "funcio infomap \n"
            cl = arllegit.community_infomap()
            print cl
            dibuixar(pos,layout,cl)
        elif sel[i] == "spinglass":
            print "funcio spinglass \n"
            cl1 = arllegit.community_spinglass()
            print cl1
            dibuixar(pos,layout,cl1)
        elif sel[i] == "multilevel":
            print "funcio multilevel \n"
            cl2 = arllegit.community_multilevel()
            print cl2
            dibuixar(pos,layout,cl2)

    return
####################################


#print glob.glob('./networks/*.*')
ruta = glob.glob('./networks/*.*')

#for i in ruta:
for i in range(len(ruta)):
     stemp = ruta[i].split('/')
     semp = stemp[2].split('.')
     print i, semp[0]
     #print i, stemp[2]


nb = raw_input("Escriu el nom de l'arxiu a llegir\n")
print ('Arxiu %s \n' % (nb))

try:
    arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml")
except IOError:
    print 'cannot open', arllegit
else:
    print 'ok'

####FER FUNCIo?###
num = escollir(arllegit)
print num


