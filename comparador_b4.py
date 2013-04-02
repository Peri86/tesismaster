#!/usr/bin/env python

#import Tkinter llibreria grafica

from igraph import *
import networkx as nx
import community as cp

import glob
import cairo
import matplotlib.pyplot as plt

from pprint import pprint
import inspect

############Funcio dibuixar################
def dibuixar(pos,layout,com):
    plot(com,vertex_label=pos,layout=layout)
    return 
####################################

############Funcio dibuixar networkx################
def nxdibuixar(G1,pos,p):
    #pos = nx.spring_layout(G1)
    dmin=1
    ncenter=0
    for n in pos:
        x,y=pos[n]
        d=(x-0.5)**2+(y-0.5)**2
        if d<dmin:
            ncenter=n
            dmin=d
    
    
    plt.figure(figsize=(8,8))
    nx.draw_networkx_edges(G1,pos,nodelist=[ncenter],alpha=0.4)
    nx.draw_networkx_nodes(G1,pos,nodelist=p.keys(),
                           node_size=80,
                           node_color=p.values(),
                           cmap=plt.cm.Reds_r)
    
    
    nx.draw_networkx_labels(G1,pos)
    
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    plt.axis('off')
    plt.savefig('prova.png')
    plt.show()
    return 
####################################

#####Funcio escollir algoritmes######
def escollir(arllegit,nllegit):
    
    ###layout de la xarxa sera igual per tots els algoritmes##
    layout =  arllegit.layout()    
    pos = arllegit.vs["id"]
    #####
    ###No directe###
    #print inspect.getmembers(arllegit)
    und_arllegit=nx.Graph(nllegit)
    nxpos = nx.spring_layout(und_arllegit)
    #####
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n"
    print 'infomap'    
    print 'spinglass'    
    print 'multilevel'
    print 'fastgreedy'
    print 'louvain'
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
        elif sel[i] == "louvain":
            print "funcio louvain o best_partition \n"
            particio = cp.best_partition(und_arllegit)
            nxdibuixar(und_arllegit,nxpos,particio)
            print particio

    return
####################################


#print glob.glob('./networks/*.*')
ruta = glob.glob('./networks/*.*') #troba la ruta dels arxius que idiquem

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
    arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml") #llegit per igraph
    nllegit = nx.read_graphml("./networks/"+nb+".graphml") #llegit per networkx
except IOError:
    print 'cannot open', arllegit
else:
    print 'ok\n'

####FER FUNCIo?###
num = escollir(arllegit,nllegit)
print num


