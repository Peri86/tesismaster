#!/usr/bin/env python
__author__ = """Pau Pericay Vendrell"""

##################### TO DO #####################
# Formats de arxius per cargar correctes
# Posar nom a les finestres dels grafs
# Arreclar errors - eigenvectornaive
# Afegir algorismes nous
# Afegir pagerank?
# Classificar algorismes
# Implementar grafs direcionals o no direcionals
# Modificar el menu per fer-lo mes agradable
# Funcio per guardar el dibuix
# Funcio per guardar les comunitats



#import Tkinter llibreria grafica

from igraph import *
import networkx as nx
import community as cp
import community_jolleycraig as cj

import glob
import cairo
import matplotlib.pyplot as plt

from pprint import pprint
import inspect

############Funcio guardar graf################
def guardargraf(nom):
    plot(com,nom+".pdf",vertex_label=pos,layout=layout)
    return
############Funcio dibuixar################
def dibuixar(pos,layout,com):
    plot(com,vertex_label=pos,layout=layout,name = "prova2")
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
    ###Networkx - No directe###
    #print inspect.getmembers(arllegit)
    und_arllegit=nx.Graph(nllegit)
    nxpos = nx.spring_layout(und_arllegit)
    #####
    ############ DIVIDIR PER TIPUS DE ALGORISMES ############
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n\n"
    print 'infomap\n'    
    print "             Maps of random walks on complex networks reveal community structure. Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    print 'spinglass\n'
    print "             Statistical Mechanics of Community Detection. Joerg Reichardt, Stefan Bornholdt. 2006.\n"
    print "             Finding and evaluating community structure in networks. M.E.J. Newman, M. Girvan. 2004.\n"
    print 'multilevel\n'
    print "             Fast unfolding of communities in large networks. V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    print 'edgebettweenness\n'
    print "             Finding and evaluating community structure in networks. M.E.J. Newman, M. Girvan. 2004.\n"
    print 'fastgreedy\n'
    print "             Finding community structure in very large networks. A Clauset, MEJ Newman, C Moore. 2004.\n"
    print 'labelpropagation\n'
    print "             Near linear time algorithm to detect community structures in large-scale networks. Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"    
    print 'leadingeigenvector\n'
    print "             Finding community structure in networks using the eigenvectors of matrices. M. E. J. Newman. 2006.\n"
    print 'leadingeigenvectornaive\n'
    print "             Finding community structure in networks using the eigenvectors of matrices. M. E. J. Newman. 2006.\n"
    print 'walktrap\n'
    print "             Computing communities in large networks using random walks. Pascal Pons, Matthieu Latapy. 2005.\n"
    ######## externs al igraph ##########    
    print 'louvain\n'
    print "             Fast unfolding of communities in large networks. V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    print 'jolleycraig\n'
    print "             Modularity and community structure in networks. M. E. J. Newman. 2006.\n"
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
        elif sel[i] == "edgebettweenness":
            print "funcio edgebettweenness\n"
            cl3 = arllegit.community_edge_betweenness().as_clustering()
            print cl3
            dibuixar(pos,layout,cl3)
        elif sel[i] == "fastgreedy":
            print "funcio fastgreedy \n"
            arllegit.simplify()
            #pprint (vars(arllegit))# comprovar variables de objecte
            #print inspect.getmembers(arllegit)# inspecionar objecte
            cl4 = arllegit.community_fastgreedy().as_clustering()
            #cl4.__plot__()
            print cl4
            #pprint (vars(cl4))#
            colors = ["red", "green", "blue", "yellow", "magenta"]
            dibuixar(pos,layout,cl4)
            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"
            cl5 = arllegit.community_label_propagation()
            print cl5
            dibuixar(pos,layout,cl5)
        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            cl6 = arllegit.community_leading_eigenvector()
            print cl6
            dibuixar(pos,layout,cl6)
        elif sel[i] == "leadingeigenvectornaive": ##### DONA ERROR #####
            print "funcio leadingeigenvectornaive\n"
            cl7 = arllegit.community_leading_eigenvector_naive()
            print cl7
            dibuixar(pos,layout,cl7)
        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            cl8 = arllegit.community_walktrap().as_clustering()
            print cl8
            dibuixar(pos,layout,cl8)
        elif sel[i] == "louvain":
            print "funcio louvain o best_partition \n"
            particio = cp.best_partition(und_arllegit)
            #print particio.values()
            ####################
            #print particio.items()
            #items=particio.items()
            #backitems=[ [int(v[0].lstrip('n')),v[1]] for v in items]
            #print sorted(backitems)
            #spart = dict(backitems)
            #print spart
            ####################
            #svcpart = VertexClustering(spart)
            #dibuixar(pos,layout,svcpart) #Intentar per dibuixar-ho tot amb igraph-cairo
            nxdibuixar(und_arllegit,nxpos,particio) #Dibuixar amb networkx
            #nxdibuixar(und_arllegit,nxpos,backitems)
            #print particio
        elif sel[i] == "jolleycraig":
            print "funcio de newman - jolleycraig"
            particiocj = cj.detect_communities(und_arllegit)
            print particiocj
            #nxdibuixar(und_arllegit,nxpos,particiocj)

    return
####################################


#print glob.glob('./networks/*.*')
ruta = glob.glob('./networks/*.*') #troba la ruta dels arxius que idiquem

print "\nXarxes disponibles a la carpeta networks:"

#for i in ruta:
for i in range(len(ruta)):
     stemp = ruta[i].split('/')
     semp = stemp[2].split('.')
     print i, semp[0]
     print " disponible en format: ", semp[1]


nb = raw_input("Escriu el nom de la xarxa a llegir\n")
print ('Xarxa %s' % (nb))

formats = list() #llista dels formats disponibles buida

for o in range(len(ruta)):
    stemp = ruta[o].split('/')
    semp = stemp[2].split('.')
    if(semp[0] == nb): #comprovo si coincideix amb el nom de l'arxiu
        #print "catch"
        #print semp[1]
        formats.append(semp[1]) #afegeixo format a la llista

if len(formats) > 1:
    print "Tria en quin format vols cargar l'arxiu.\n Formats disponibles:"
    print formats
    fm = raw_input("Escriu el nom del format escollit\n")
else:
    fm = formats
    fm = fm[0] #converteixo de list a string

######  cargar el graf depenent del fomat de l'arxiu #####
if fm == 'graphml':
    try:
        #print 'estic dins del graphml'
        arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml") #llegit per igraph
        nllegit = nx.read_graphml("./networks/"+nb+".graphml") #llegit per networkx
    except IOError:
        print 'cannot open', arllegit
    else:
        print 'ok\n'
    
    ####FER FUNCIo?###
    num = escollir(arllegit,nllegit)
    print num
    
elif fm == 'net':
    try:
        #print 'estic dins del net'
        arllegitnet = Graph.Read_Pajek("./networks/"+nb+".net") #llegit per igraph
        nllegitnet = nx.read_pajek("./networks/"+nb+".net") #llegit per networkx
    except IOError:
        print 'cannot open', arllegitnet
    else:
        print 'ok\n'
    
    ####FER FUNCIo?###
    num = escollir(arllegitnet,nllegitnet)
    print num

#print 'estic al final'