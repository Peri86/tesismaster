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
    
    print 'Escull un o varis algorismes per la deteccio de comunitats:'
    print 'infomap'    
    print 'spinglass\n'    
    
    esc = raw_input()
    
    if esc == "infomap":
        print "funcio infomap \n"
        cl = arllegit.community_infomap()
        print cl
        dibuixar(pos,layout,cl)
    elif esc == "spinglass":
        print "funcio spinglass \n"
        cl1 = arllegit.community_spinglass()
        print cl1
    
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


