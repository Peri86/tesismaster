#!/usr/bin/env python
#__author__ = """Pau Pericay Vendrell"""

##################### TO DO #####################
# Formats de arxius per cargar correctes [X]
# Posar nom a les finestres dels grafs
# Arreclar errors - eigenvectornaive
# Afegir algorismes nous
# Mantenir la posicio per tots els grafs [/]
# Classificar algorismes
# Implementar grafs direcionals o no direcionals
# Modificar el menu per fer-lo mes agradable
# Funcio per guardar el dibuix
# Funcio per guardar les comunitats
# Parametres a comparar entre els algorismes escollits a nivell general
# Parametres a comparar entre els algorismes escollits a nivell de node
# Comparar algorismes tinguent en compte els parametres resultants
# Conversor amb python


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

import itertools

############Funcio guardar graf################
def guardargraf(nom):
    plot(com,nom+".pdf",vertex_label=pos,layout=layout)
    return
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

def assortativitymeu(graph, degrees=None):
    if degrees is None: degrees = graph.degree()
    degrees_sq = [deg**2 for deg in degrees]
 
    m = float(graph.ecount())
    num1, num2, den1 = 0, 0, 0
    for source, target in graph.get_edgelist():
        num1 += degrees[source] * degrees[target]
        num2 += degrees[source] + degrees[target]
        den1 += degrees_sq[source] + degrees_sq[target]
 
    num1 /= m
    den1 /= 2*m
    num2 = (num2 / (2*m)) ** 2
 
    return (num1 - num2) / (den1 - num2)
####################################

def betweenness_centralization(G):
    vnum = G.vcount()
    if vnum < 3:
        raise ValueError("graph must have at least three vertices")
    denom = (vnum-1)*(vnum-2)
 
    temparr = [2*i/denom for i in G.betweenness()]
    max_temparr = max(temparr)
    return sum(max_temparr-i for i in temparr)/(vnum-1)
####################################
def parametres(G,nG):
    print "\nParametres disponibles:\n"
    
    ###################################
    print "\tParametres Globals: \n"
    print "\t[1] Betweenness Centralization\n"
    print "\t[2] Average path length\n"
    print "\t[3] Assortativity degree\n"
    print "\t[4] Diameter\n"
    print "\t[5] Density\n"
    print "\t[6] Cohesion\n"
    print "\t[7] Radius\n"
    
    print "\tParametres per cada node de la xarxa: \n"
    print "\t[11] Betweenness\n"
    print "\t[12] Pagerank\n"
    print "\t[13] EigenVectorCentrality\n"
    print "\t[14] Average degree connectivity\n"
    print "\t[15] Periphery\n"
    print "\t[16] Eccentricity\n"
    print "\t[17] Center nodes\n"
    
    
    se = raw_input('Escriu els numeros dels parametres que vulguis amb una coma entre mig:\n')
    secom = se.split(',')
    
    for i in range(len(secom)):
        if secom[i] == "1":
                print "\nBetweenness Centralization:"
                print betweenness_centralization(G)
        elif secom[i] == "2":
                print "\nAverage path length:"
                print G.average_path_length()            
        elif secom[i] == "3":
                print "\nAssortativity degree:"
                print G.assortativity_degree()            
        elif secom[i] == "4":
                print "\nDiameter:"
                print G.diameter()          
        elif secom[i] == "5":
                print "\nDensity:"
                print G.density()            
        elif secom[i] == "6":
                print "\nCohesion:"
                print G.cohesion()            
        elif secom[i] == "7":
                print("\nRadius:")
                print nx.radius(nG)            
    ###################################
        elif secom[i] == "11":
                print "\nBetweenness:"
                print G.betweenness(directed=False, cutoff=16)            
        elif secom[i] == "12":
                print "\nPagerank:"
                print G.pagerank()           
        elif secom[i] == "13":
                print "\nEigenVectorCentrality:"
                print G.eigenvector_centrality()            
        elif secom[i] == "14":
                print "\nAverage degree connectivity:"
                print nx.average_degree_connectivity(nG)            
        elif secom[i] == "15":
                print "\nPeriphery:"
                print nx.periphery(nG)            
        elif secom[i] == "16":
                print("\nEccentricity:")
                print nx.eccentricity(nG)            
        elif secom[i] == "17":
                print("\nCenter:")
                print nx.center(nG)            
    
    #####Parametres exclosos#####
    #print "Assortativity meu:" # es el mateix que el degree?
    #print assortativitymeu(G)  
    #print("diameter: %d" % nx.diameter(nG))
    #print("density: %s" % nx.density(nG))
    #print("richclub coefficient: %s" % nx.rich_club_coefficient(nG.to_undirected()))
    #print("richclub coefficient: %s" % nx.rich_club_coefficient(nG))
    
    return 2

#####Funcio escollir algoritmes######
def escollir(arllegit,nllegit):
    ###layout de la xarxa sera igual per tots els algoritmes##
    layout =  arllegit.layout()
    pos = arllegit.vs["id"]
    ## El layout de igraph conte les posicions, no confondre amb el pos
    #print pos
    #####
    ###Networkx - No directe###
    #print inspect.getmembers(arllegit)
    und_arllegit=nx.Graph(nllegit)
    nxpos = nx.spring_layout(und_arllegit)
    #print layout
    #print nxpos
    #####
    ############ DIVIDIR PER TIPUS DE ALGORISMES ############
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n\n"
    print 'infomap\n'    
    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    print 'spinglass\n'
    print "\tStatistical Mechanics of Community Detection.\n\t Joerg Reichardt, Stefan Bornholdt. 2006.\n"
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    print 'multilevel\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    print 'edgebettweenness\n'
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    print 'fastgreedy\n'
    print "\tFinding community structure in very large networks.\n\t A Clauset, MEJ Newman, C Moore. 2004.\n"
    print 'labelpropagation\n'
    print "\tNear linear time algorithm to detect community structures in large-scale networks.\n\t Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"    
    print 'leadingeigenvector\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    print 'leadingeigenvectornaive\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    print 'walktrap\n'
    print "\tComputing communities in large networks using random walks.\n\t Pascal Pons, Matthieu Latapy. 2005.\n"
    ######## externs al igraph ##########    
    print 'louvain\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    print 'jolleycraig\n'
    print "\tModularity and community structure in networks.\n\t M. E. J. Newman. 2006.\n"
    print '\n'
    #####################################
    print '\nPer sortir del programa escriu: sortir\n'
    
    esc = raw_input()
    sel = esc.split(',')
    
    for i in range(len(sel)):
        if sel[i] == "infomap":
            print "funcio infomap \n"
            cl = arllegit.community_infomap()
            ############parametre###############
            #parametres(arllegit,nllegit)
            print "Modularity:"
            print arllegit.modularity(cl)
            ###########################
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
            particio = cp.best_partition(und_arllegit) # particio es un dicionari
            print 'particio values : '
            print particio.values()
            #print particio.keys()
            print 'list(enumerate(particio.items'
            print list(enumerate(particio.items()))
            osaa = particio.items()
            osaa.sort()
            print 'osaa : '
            print osaa
            
            dosa = dict(osaa)
            print 'dosa : '
            print dosa
            par = list(enumerate(dosa.values()))
            print 'par : '
            print par
            #gen = UniqueIdGenerator()
            #parti = Graph(edges= [(gen[v], gen[a]) for v in particio.keys() for a in particio[v]])
            parti = Graph(par)
            print 'parti: '
            print parti
            #perti = VertexClustering(parti)
            perti = VertexClustering(arllegit,sorted(particio.values()))
            print 'perti: '
            print perti
            dibuixar(pos,layout,perti) #Per dibuixar-ho tot amb igraph-cairo
            ################################################################################
            nxdibuixar(und_arllegit,nxpos,particio) #Dibuixar amb networkx
            
        elif sel[i] == "jolleycraig":
            print "funcio de newman - jolleycraig"
            particiocj = cj.detect_communities(und_arllegit)
            print particiocj[1]
            
            a = particiocj[1]
            #o = dict()
            #print 'a : '
            #print a
            #gid = 0
            #for i in a:
            #    print a[i]
            #    #o[i] = map(a[i],gid)
            #    gid += 1
            #print o
            la = dict()
            for item in a:
                for stem in item:
                    la=(stem,item)
            
            print la
            #cosavx = VertexClustering(arllegit,px)
            #print cosavx
            
            #d = dict()
            #for i in particiocj[1]:
            #    for j in particiocj[1][i]:
            #        print i,j
            
                #for j in range(int(i), int(i) + 2):
                #    d[j].append(i)
            
            nxdibuixar(und_arllegit,nxpos,particiocj[1])
        elif sel[i] == "sortir":
            sys.exit()

    return 1

####################################

#####Funcio escollir algoritmes NET PAJEK ######
def netescollir(arllegit,nllegit):
    
    ###layout de la xarxa sera igual per tots els algoritmes##
    layout =  arllegit.layout()
    print arllegit.vs()
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
    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    print 'spinglass\n'
    print "\tStatistical Mechanics of Community Detection.\n\t Joerg Reichardt, Stefan Bornholdt. 2006.\n"
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    print 'multilevel\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    print 'edgebettweenness\n'
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    print 'fastgreedy\n'
    print "\tFinding community structure in very large networks.\n\t A Clauset, MEJ Newman, C Moore. 2004.\n"
    print 'labelpropagation\n'
    print "\tNear linear time algorithm to detect community structures in large-scale networks.\n\t Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"    
    print 'leadingeigenvector\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    print 'leadingeigenvectornaive\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    print 'walktrap\n'
    print "\tComputing communities in large networks using random walks.\n\t Pascal Pons, Matthieu Latapy. 2005.\n"
    ######## externs al igraph ##########    
    print 'louvain\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    print 'jolleycraig\n'
    print "\tModularity and community structure in networks.\n\t M. E. J. Newman. 2006.\n"
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
        elif sel[i] == "leadingeigenvectornaive": ##### DONA ERROR NO EXISTEIX #####
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
        elif sel[i] == "jolleycraig": # NO FUNCIONA DEMANA DICTIONARY I ES LLISTA
            print "funcio de newman - jolleycraig"
            particiocj = cj.detect_communities(und_arllegit)
            print particiocj[1]
            for ji in particiocj[1]:
                #print particiocj[1].index(ji)
                print dict(zip(particiocj[1],particiocj[1].index(ji)))
            #print particiocj[1]
            #cosa = list()
            #for u in range(len(particiocj[1])):
            #    cosa.append(u)
            #d = dict(zip(cosa,particiocj[1]))
            #nxdibuixar(und_arllegit,nxpos,d)

    return

####################################################################

def menugraphml(arllegit,nllegit):
    print '\n Escull una de les opcions:'
    print "\n [1] Calcular parametres de la xarxa\n"
    print "\n [2] Aplicar algorisme de deteccio de comunitats\n"

    op = raw_input("Escriu el numero de la opcio: \n")
    
    if op == '1':
        num = parametres(arllegit,nllegit)
    elif op == '2':
        num = escollir(arllegit,nllegit)
    
    if num == 1 or num == 2:
        return
    else:
        print 'Error'
        return

####################################################################

def menunet(arllegitnet,nllegitnet):
    print '\n Escull una de les opcions:'
    print "\n [1] Calcular parametres de la xarxa\n"
    print "\n [2] Aplicar algorisme de deteccio de comunitats\n"

    op = raw_input("Escriu el numero de la opcio: \n")
    
    if op == '1':
        parametres(arllegitnet,nllegitnet)
    elif op == '2':
        num = netescollir(arllegitnet,nllegitnet)
    return

####################################
####################################
####################################

if __name__ == "__main__":
    print "\n\nPrograma per l'analisi de xarxes complexes i la deteccio de comunitats."
    
    #print glob.glob('./networks/*.*')
    ruta = glob.glob('./networks/*.*') #troba la ruta dels arxius que idiquem
    
    print "\nXarxes disponibles a la carpeta networks:"
    
    llista = []
    
    for i in range(len(ruta)):
         stemp = ruta[i].split('/')
         semp = stemp[2].split('.')
         llista.append(semp)
         #print "[",i,"]", semp[0]
         #print " disponible en format: ", semp[1]
    conta = 1
    for y in range(len(llista)):
        if llista[y][0]!=llista[y-1][0]:
            print '[',conta,']',llista[y][0]
            print 'disponible en format: ',llista[y][1]
            conta+=1 #per tal de que el numero de xarxa apareixi correcte
        else:
            print '                      ',llista[y][1]
    
    nb = raw_input("\nEscriu el nom de la xarxa a llegir\n")
    #print ('Xarxa %s' % (nb))
    print "\n"
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
    
    ######  cargar el graf depenent del format de l'arxiu #####
    if fm == 'graphml':
        try:
            #print 'estic dins del graphml'
            arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml") #llegit per igraph
            nllegit = nx.read_graphml("./networks/"+nb+".graphml") #llegit per networkx
        except IOError:
            print 'Error', arllegit
        else:
            print 'ok\n'
        
        
        menugraphml(arllegit,nllegit)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER GRAPHML###
        #num = escollir(arllegit,nllegit)
        #print num
        
    elif fm == 'net':
        try:
            #print 'estic dins del net'
            arllegitnet = Graph.Read_Pajek("./networks/"+nb+".net") #llegit per igraph
            nllegitnet = nx.read_pajek("./networks/"+nb+".net") #llegit per networkx
        except IOError:
            print 'Error', arllegitnet
        else:
            print 'ok\n'
        
        menunet(arllegitnet,nllegitnet)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER NET PAJEK###
        #num = escollir(arllegitnet,nllegitnet)
        #num =  netescollir(arllegitnet,nllegitnet)
        #print num
    
    #print 'estic al final'