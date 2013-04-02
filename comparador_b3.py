#!/usr/bin/env python

#import Tkinter llibreria grafica
from igraph import *

import glob
import cairo

from pprint import pprint
import inspect

############Funcio dibuixar################
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
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n"
    print 'infomap'    
    print 'spinglass'    
    print 'multilevel'
    print 'fastgreedy'
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
        elif sel[i] == "fastgreedy":
            print "funcio fastgreedy \n"
            arllegit.simplify()
            #pprint (vars(arllegit))# comprovar variables de objecte
            #print inspect.getmembers(arllegit)# inspecionar objecte
            cl3 = arllegit.community_fastgreedy().as_clustering()
            #cl3.__plot__()
            print cl3
            #pprint (vars(cl3))#
            colors = ["red", "green", "blue", "yellow", "magenta"]
            dibuixar(pos,layout,cl3)
            #plot(arllegit, vertex_color=[colors[i] for i in cl3.membership]) #

    return
####################################


#print glob.glob('./networks/*.*')
ruta = glob.glob('./networks/*.*')

print "Xarxes disponibles:"

#for i in ruta:
for i in range(len(ruta)):
     stemp = ruta[i].split('/')
     semp = stemp[2].split('.')
     print i, semp[0]
     #print i, stemp[2]


nb = raw_input("Escriu el nom de l'arxiu a llegir\n")
print ('Arxiu %s' % (nb))

try:
    arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml")
except IOError:
    print 'cannot open', arllegit
else:
    print 'ok\n'

####FER FUNCIo?###
num = escollir(arllegit)
print num


