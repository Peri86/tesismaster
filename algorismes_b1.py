#!/usr/bin/env python

import grafics as gr

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

global cl,cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8

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
    
    llistacomuni = []
    
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
            gr.dibuixar(pos,layout,cl)
            llistacomuni.append('infomap') #inserto el nom de la funcio i el calcul de comunitat per saberho a comunitats.py
            llistacomuni.append(cl)
        elif sel[i] == "spinglass":
            print "funcio spinglass \n"
            cl1 = arllegit.community_spinglass()
            print cl1
            gr.dibuixar(pos,layout,cl1)
            llistacomuni.append('spinglass')
            llistacomuni.append(cl1)
        elif sel[i] == "multilevel":
            print "funcio multilevel \n"
            cl2 = arllegit.community_multilevel()
            print cl2
            gr.dibuixar(pos,layout,cl2)
            llistacomuni.append('multilevel')
            llistacomuni.append(cl2)
        elif sel[i] == "edgebettweenness":
            print "funcio edgebettweenness\n"
            cl3 = arllegit.community_edge_betweenness().as_clustering()
            print cl3
            gr.dibuixar(pos,layout,cl3)
            llistacomuni.append('edgebettweenness')
            llistacomuni.append(cl3)
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
            gr.dibuixar(pos,layout,cl4)
            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
            llistacomuni.append('fastgreedy')
            llistacomuni.append(cl4)
        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"
            cl5 = arllegit.community_label_propagation()
            print cl5
            gr.dibuixar(pos,layout,cl5)
            llistacomuni.append('labelpropagation')
            llistacomuni.append(cl5)
        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            cl6 = arllegit.community_leading_eigenvector()
            print cl6
            gr.dibuixar(pos,layout,cl6)
            llistacomuni.append('leadingeigenvector')
            llistacomuni.append(cl6)
        elif sel[i] == "leadingeigenvectornaive": ##### DONA ERROR #####
            print "funcio leadingeigenvectornaive\n"
            cl7 = arllegit.community_leading_eigenvector_naive()
            print cl7
            gr.dibuixar(pos,layout,cl7)
            llistacomuni.append('leadingeigenvectornaive')
            llistacomuni.append(cl7)
        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            cl8 = arllegit.community_walktrap().as_clustering()
            print cl8
            gr.dibuixar(pos,layout,cl8)
            llistacomuni.append('walktrap')
            llistacomuni.append(cl8)
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
            gr.dibuixar(pos,layout,perti) #Per dibuixar-ho tot amb igraph-cairo
            ################################################################################
            gr.nxdibuixar(und_arllegit,nxpos,particio) #Dibuixar amb networkx
            llistacomuni.append('louvain')
            llistacomuni.append(perti)
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
            
            gr.nxdibuixar(und_arllegit,nxpos,particiocj[1])
        elif sel[i] == "sortir":
            sys.exit()

    return llistacomuni   
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
            gr.dibuixar(pos,layout,cl)
        elif sel[i] == "spinglass":
            print "funcio spinglass \n"
            cl1 = arllegit.community_spinglass()
            print cl1
            gr.dibuixar(pos,layout,cl1)
        elif sel[i] == "multilevel":
            print "funcio multilevel \n"
            cl2 = arllegit.community_multilevel()
            print cl2
            gr.dibuixar(pos,layout,cl2)
        elif sel[i] == "edgebettweenness":
            print "funcio edgebettweenness\n"
            cl3 = arllegit.community_edge_betweenness().as_clustering()
            print cl3
            gr.dibuixar(pos,layout,cl3)
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
            gr.dibuixar(pos,layout,cl4)
            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"
            cl5 = arllegit.community_label_propagation()
            print cl5
            gr.dibuixar(pos,layout,cl5)
        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            cl6 = arllegit.community_leading_eigenvector()
            print cl6
            gr.dibuixar(pos,layout,cl6)
        elif sel[i] == "leadingeigenvectornaive": ##### DONA ERROR NO EXISTEIX #####
            print "funcio leadingeigenvectornaive\n"
            cl7 = arllegit.community_leading_eigenvector_naive()
            print cl7
            gr.dibuixar(pos,layout,cl7)
        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            cl8 = arllegit.community_walktrap().as_clustering()
            print cl8
            gr.dibuixar(pos,layout,cl8)
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
            gr.nxdibuixar(und_arllegit,nxpos,particio) #Dibuixar amb networkx
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
