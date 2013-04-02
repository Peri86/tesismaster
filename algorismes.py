#!/usr/bin/env python


from igraph import *
import networkx as nx #################
import community as cp
import community_jolleycraig as cj
import glob
import cairo
import matplotlib.pyplot as plt
from pprint import pprint
import inspect
import itertools

import MCL as mc
import CFinder as cf

import os
import subprocess
import time
import sys

import grafics as gr
import gephi as gp
import netcarto as nt

global cl,cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8

def modularitat(xarxa,comun):
    #print "Modularity:"
    modu = xarxa.modularity(comun)
    #print modu
    return modu

#####Funcio escollir algoritmes######
def escollir(arllegit,nllegit,nomar,pes):
    #print "Menu per deteccio de comunitats"
    #### El numero de nodes que conte la xarxa, per passar el dibuixar ####
    unmm = arllegit.ecount()
    unmv = arllegit.vcount()

    try: #nomes per gml ?
        pos = arllegit.vs["id"]
    except KeyError:
        conot = 1
        while conot < unmm:
            arllegit.vs[int(conot)]["id"] = conot
            conot+=1
        pos = arllegit.vs["id"]
    #mida = arllegit.vs["size"]
    
    ###layout de la xarxa###
    layout =  arllegit.layout("kk")
    #Pesos, si la xarxa en te
    if pes == True: #Comprovo si la xarxa te pesos
        pesos = arllegit.es["weight"]
    
#La caracter??stica especial de Fruchterman-Reingold es que las fuerzas se apli-can de manera que distribuyen los nodos de forma homog?enea en el ?area dedibujo prede?nida,
#dando a los dise?nos basados en Fruchterman-Reingold un aspecto m?as expandido, En contraste,
#Kamada-Kawai hace uso de las distanciaste?oricas del grafo como medida durante el proceso de colocaci?on del nodo en lu-gar
#de la informaci?on de adyacencia. Si bien la informaci?on de adyacencia puedeser f?acilmente encontrada en los grafos, las distancias
#te?oricas del grafo tienenque ser calculadas de forma expl??cita. El bene?cio de las distancias te?oricas delgrafo es que establecen una
#medida entre cualquier par de nodos que se re?ejadirectamente en la distancia entre estos nodos
    
    #if unmm <= 500:
    #    layout =  arllegit.layout("kk")
    #    print 'kk'
    #elif unmm > 501:
    #    layout =  arllegit.layout("kk")
    #    print 'kk'


    ## El layout de igraph conte les posicions, no confondre amb el pos
    #print pos
    #####
    #####
    ############ DIVIDIR PER TIPUS DE ALGORISMES ############
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n\n"
    ##########Nomes per xarxes no directes##########
    print "\n\n\tAlgorismes per xarxes no directes:\n"
    print 'multilevel\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    #Modularity > Modularity optimitzation > Greedy Techniques. Amb Pesos.
    
    print 'fastgreedy\n'
    print "\tFinding community structure in very large networks.\n\t A Clauset, MEJ Newman, C Moore. 2004.\n"
    #Modularity > Modularity optimitzation > Greedy Techniques. Amb Pesos.
    
    ##########Nomes per xarxes directes##########
    print "\n\n\tAlgorismes per xarxes directes:\n"
    print 'leadingeigenvector\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    #Modularity Based > Modularity optimitzation > Spectral optimitzation. Sense Pesos.
    
    #########Per xarxes directes i no directes##########
    print "\n\n\tAlgorismes per xarxes directes i no directes:\n"
    print 'walktrap\n'
    print "\tComputing communities in large networks using random walks.\n\t Pascal Pons, Matthieu Latapy. 2005.\n"
    #Dynamic algorithms > Random Walk. Amb Pesos.
    
    print 'spinglass\n'
    print "\tStatistical Mechanics of Community Detection.\n\t Joerg Reichardt, Stefan Bornholdt. 2006.\n" #Aquest es el bo?
    #print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    #Modularity Based > Modifications of modularity. Amb Pesos.
    
    print 'labelpropagation\n'
    print "\tNear linear time algorithm to detect community structures in large-scale networks.\n\t Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"
    #Alternative Methods > Label Propagation. Amb Pesos.
    
    print 'infomap\n'    
    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    #Methods based on statistical inference > Blockmodeling. Amb Pesos als vertex i als enllacos.
    
    print 'edgebetweenness\n'
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    #Divisive algorithms > Girvan and Newman. Sense Pesos.

    print 'CFinder\n'
    print "\tUncovering the overlapping community structure of complex networks in nature and society. Palla et. al., Nature 435, 814-818 (2005)\n"    
    #Overlapping Communities > Clique percolation
    
    if sys.platform == 'linux2':    
        print 'netcarto\n'
        print "\tGuimera, R. & Amaral, L.A.N., Functional cartography of complex metabolic networks, Nature 433, 895-900 (2005).\n"
        print "\tGuimera, R. & Amaral, L.A.N., Cartography of complex networks: modules and universal roles, J. Stat. Mech.-Theory Exp., art. no. P02001 (2005).\n"
        #Modularity based methods > Simulated anneling
    
    ######## externs al igraph ##########
    #####################################
    #print '\nPer sortir del programa escriu: sortir\n'
    
    esc = raw_input()
    sel = esc.split(',')
    
    llistacomuni = []
    llistalgori = []
    
    for i in range(len(sel)):
        if sel[i] == "infomap":
            print "funcio infomap \n"
            
            print "Especificar numero de iteracions (trials)"
            tr = raw_input("Per defecte (son 10) premer enter\n:")
            if tr == '':
                
                if pes == False:
                    t1 = time.time()
                    cl = arllegit.community_infomap()
                    t2 = time.time()
                    print 'algorisme infomap SENSE pesos'
                else:
                    t1 = time.time()
                    cl = arllegit.community_infomap(vertex_weights=pesos)
                    t2 = time.time()
                    print 'algorisme infomap AMB pesos'                

                
                tem0 = (t2-t1)
                if (tem0 < 1):
                    temp0 = ((t2-t1)*1000.0)
                    print 'La funcio ha tardat %0.3f ms' % temp0
                elif (tem0 > 1) and (tem0 < 60):
                    temp0 = ((t2-t1))
                    print 'La funcio ha tardat %0.3f s' % temp0
                else:
                    temp0 = ((t2-t1)/60.0)                
                    print 'La funcio ha tardat %0.3f min' % temp0

                print cl
            else:
                tri = int(tr)
                if tri <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    
                    
                    if pes == False:
                        t1 = time.time()
                        cl = arllegit.community_infomap(trials=tri)
                        t2 = time.time()
                        print 'algorisme infomap SENSE pesos'
                    else:
                        t1 = time.time()
                        cl = arllegit.community_infomap(vertex_weights=pesos,trials=tri)
                        t2 = time.time()
                        print 'algorisme infomap AMB pesos'                    
                    

                    tem0 = (t2-t1)
                    if (tem0 < 1):
                        temp0 = ((t2-t1)*1000.0)
                        print 'La funcio ha tardat %0.3f ms' % temp0
                    elif (tem0 > 1) and (tem0 < 60):
                        temp0 = ((t2-t1))
                        print 'La funcio ha tardat %0.3f s' % temp0
                    else:
                        temp0 = ((t2-t1)/60.0)                
                        print 'La funcio ha tardat %0.3f min' % temp0

                    print cl
            
            gr.dibuixar(pos,layout,cl,unmm)
            llistacomuni.append('infomap') #inserto el nom de la funcio i el calcul de comunitat per saberho a comunitats.py
            llistacomuni.append(cl)
            ####
            modu = modularitat(arllegit,cl) #funcio de calcular la modularitat del graf respecte el clustering donat
            ####
            ##############################            
            llistalgori.append('infomap')
            llistalgori.append(cl)            
            llistalgori.append(temp0)
            llistalgori.append(modu)
            ##############################
            #gp.escriuregraf(arllegit,cl)############
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl,unmm)
        #elif sel[i] == "infomap_help":
        #    print "Methods based on statistical inference > Blockmodeling.\nAmb Pesos als vertex i als enllacos."
        #    print ""
        #    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
        #    return

        elif sel[i] == "spinglass":
            print "funcio spinglass \n"
            
            print "Especificar numero de iteracions (spins)"
            tr1 = raw_input("Per defecte (son 25) premer enter\n:")
            if tr1 == '':
                
                if pes == False:
                    t1 = time.time()
                    cl1 = arllegit.community_spinglass()
                    t2 = time.time()
                    print 'algorisme spinglass SENSE pesos'
                else:
                    t1 = time.time()
                    cl1 = arllegit.community_spinglass(weights=pesos)
                    t2 = time.time()
                    print 'algorisme spinglass AMB pesos'
                
                tem1 = (t2-t1)
                if (tem1 < 1):
                    temp1 = ((t2-t1)*1000.0)
                    print 'La funcio ha tardat %0.3f ms' % temp1
                elif (tem1 > 1) and (tem1 < 60):
                    temp1 = ((t2-t1))
                    print 'La funcio ha tardat %0.3f s' % temp1
                else:
                    temp1 = ((t2-t1)/60.0)                
                    print 'La funcio ha tardat %0.3f min' % temp1
                
                print cl1
            else:
                tri1 = int(tr1)
                if tri1 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    
                    if pes == False:
                        t1 = time.time()
                        cl1 = arllegit.community_spinglass(spins=tri1)
                        t2 = time.time()
                        print 'algorisme spinglass SENSE pesos'
                    else:
                        t1 = time.time()
                        cl1 = arllegit.community_spinglass(weights=pesos,spins=tri1)
                        t2 = time.time()
                        print 'algorisme spinglass AMB pesos'                    

                    
                    tem1 = (t2-t1)
                    if (tem1 < 1):
                        temp1 = ((t2-t1)*1000.0)
                        print 'La funcio ha tardat %0.3f ms' % temp1
                    elif (tem1 > 1) and (tem1 < 60):
                        temp1 = ((t2-t1))
                        print 'La funcio ha tardat %0.3f s' % temp1
                    else:
                        temp1 = ((t2-t1)/60.0)                
                        print 'La funcio ha tardat %0.3f min' % temp1                    
                    
                    print cl1
            
            
            gr.dibuixar(pos,layout,cl1,unmm)
            llistacomuni.append('spinglass')
            llistacomuni.append(cl1)
            modu1 = modularitat(arllegit,cl1) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('spinglass')
            llistalgori.append(cl1)            
            llistalgori.append(temp1)
            llistalgori.append(modu1)
            ##############################


            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl1,unmm)

        elif sel[i] == "multilevel":
            print "funcio multilevel \n"
            
            if pes == False:
                t1 = time.time()
                cl2 = arllegit.community_multilevel()
                t2 = time.time()
                print 'algorisme multilevel SENSE pesos'
            else:
                t1 = time.time()
                cl2 = arllegit.community_multilevel(weights=pesos)
                t2 = time.time()
                print 'algorisme multilevel AMB pesos'             

            tem2 = (t2-t1)
            if (tem2 < 1):
               temp2 = ((t2-t1)*1000.0)
               print 'La funcio ha tardat %0.3f ms' % temp2
            elif (tem2 > 1) and (tem2 < 60):
               temp2 = ((t2-t1))
               print 'La funcio ha tardat %0.3f s' % temp2
            else:
               temp2 = ((t2-t1)/60.0)                
               print 'La funcio ha tardat %0.3f min' % temp2

            print cl2
            
            gr.dibuixar(pos,layout,cl2,unmm)
            llistacomuni.append('multilevel')
            llistacomuni.append(cl2)
            modu2 = modularitat(arllegit,cl2) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('multilevel')
            llistalgori.append(cl2)            
            llistalgori.append(temp2)
            llistalgori.append(modu2)
            ##############################


            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl2,unmm)

        elif sel[i] == "edgebetweenness":
            print "funcio edgebetweenness\n"
            
            print "Especificar numero de clusters"
            tr3 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr3 == '':
                
                #L'algorisme no admet pesos(?)
                t1 = time.time()
                cl3 = arllegit.community_edge_betweenness().as_clustering()
                t2 = time.time()
                
                tem3 = (t2-t1)
                if (tem3 < 1):
                    temp3 = ((t2-t1)*1000.0)
                    print 'La funcio ha tardat %0.3f ms' % temp3
                elif (tem3 > 1) and (tem3 < 60):
                    temp3 = ((t2-t1))
                    print 'La funcio ha tardat %0.3f s' % temp3
                else:
                    temp3 = ((t2-t1)/60.0)                
                    print 'La funcio ha tardat %0.3f min' % temp3
                print cl3

            else:
                tri3 = int(tr3)
                if tri3 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    t1 = time.time()
                    cl3 = arllegit.community_edge_betweenness(clusters=tri3).as_clustering()
                    t2 = time.time()
                    
                    tem3 = (t2-t1)
                    if (tem3 < 1):
                        temp3 = ((t2-t1)*1000.0)
                        print 'La funcio ha tardat %0.3f ms' % temp3
                    elif (tem3 > 1) and (tem3 < 60):
                        temp3 = ((t2-t1))
                        print 'La funcio ha tardat %0.3f s' % temp3
                    else:
                        temp3 = ((t2-t1)/60.0)                
                        print 'La funcio ha tardat %0.3f min' % temp3
                    
                    print cl3            
            
            gr.dibuixar(pos,layout,cl3,unmm)
            llistacomuni.append('edgebetweenness')
            llistacomuni.append(cl3)
            modu3 = modularitat(arllegit,cl3) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('edgebetweenness')
            llistalgori.append(cl3)            
            llistalgori.append(temp3)
            llistalgori.append(modu3)
            ##############################


            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl3,unmm)

        elif sel[i] == "fastgreedy":
            print "funcio fastgreedy \n"
            arllegit.simplify()
            #pprint (vars(arllegit))# comprovar variables de objecte
            #print inspect.getmembers(arllegit)# inspecionar objecte
            
            if pes == False:
                t1 = time.time()
                cl4 = arllegit.community_fastgreedy().as_clustering() # Maximitza la modularitat
                t2 = time.time()
                print 'algorisme fastgreedy SENSE pesos'
            else:
                t1 = time.time()
                cl4 = arllegit.community_fastgreedy(weights=pesos).as_clustering()
                t2 = time.time()
                print 'algorisme fastgreedy AMB pesos' 

            tem4 = (t2-t1)
            if (tem4 < 1):
               temp4 = ((t2-t1)*1000.0)
               print 'La funcio ha tardat %0.3f ms' % temp4
            elif (tem4 > 1) and (tem4 < 60):
               temp4 = ((t2-t1))
               print 'La funcio ha tardat %0.3f s' % temp4
            else:
               temp4 = ((t2-t1)/60.0)                
               print 'La funcio ha tardat %0.3f min' % temp4

            print cl4
            
            colors = ["red", "green", "blue", "yellow", "magenta"]
            gr.dibuixar(pos,layout,cl4,unmm)
            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
            llistacomuni.append('fastgreedy')
            llistacomuni.append(cl4)
            modu4 = modularitat(arllegit,cl4) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('fastgreedy')
            llistalgori.append(cl4)            
            llistalgori.append(temp4)
            llistalgori.append(modu4)
            ##############################

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl4,unmm)

        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"

            print "L'algorisme 'labelpropagation' en cada execusio dona un resultat diferent a causa de la aleatorietat dels calculs que realitza"
            print "Veure: 'Near linear time algorithm to detect community structures in large-scale networks' U. N. Raghavan, R. Albert, S. Kumara. Sep. 2007"
            print "Per aixo es pot escollir si es vol realitzar una sola iteracio o varies"
            vega = raw_input("Esciu la opcio: 'una' o 'varies'\n")
            
            if vega == 'una':
                
                if pes == False:
                    t1 = time.time()
                    cl5 = arllegit.community_label_propagation()
                    t2 = time.time()
                    print 'algorisme labelpropagation SENSE pesos'
                else:
                    t1 = time.time()
                    cl5 = arllegit.community_label_propagation(weights=pesos)
                    t2 = time.time()
                    print 'algorisme labelpropagation AMB pesos'                

                tem5 = (t2-t1)
                if (tem5 < 1):
                   temp5 = ((t2-t1)*1000.0)
                   print 'La funcio ha tardat %0.3f ms' % temp5
                elif (tem5 > 1) and (tem5 < 60):
                   temp5 = ((t2-t1))
                   print 'La funcio ha tardat %0.3f s' % temp5
                else:
                   temp5 = ((t2-t1)/60.0)                
                   print 'La funcio ha tardat %0.3f min' % temp5
                
                print cl5
                
                gr.dibuixar(pos,layout,cl5,unmm)
                llistacomuni.append('labelpropagation')
                llistacomuni.append(cl5)
                modu5 = modularitat(arllegit,cl5) #funcio de calcular la modularitat del graf respecte el clustering donat
                ##############################            
                llistalgori.append('labelpropagation')
                llistalgori.append(cl5)            
                llistalgori.append(temp5)
                llistalgori.append(modu5)
                ##############################                
                
                
            elif vega == 'varies':
                print "\nIntrodueix el nombre de vegades que vols que s'executi l'algorisme"
                print "Automaticament s'escullira el resultat que maximitzi el valor de modularitat\n"
                vegavar = raw_input("Escriu el nombre de iteracions:")
                contt = 0
                modu5 = 0
                limitv = int(vegavar)
                print limitv
                while contt != limitv:
                    
                    if pes == False:
                        t1 = time.time()
                        clmod = arllegit.community_label_propagation()
                        t2 = time.time()
                        #print 'algorisme labelpropagation SENSE pesos'
                    else:
                        t1 = time.time()
                        clmod = arllegit.community_label_propagation(weights=pesos)
                        t2 = time.time()
                        #print 'algorisme labelpropagation AMB pesos'
                    tempmod = ((t2-t1)*1000.0)
                    
                    modular = modularitat(arllegit,clmod)
                    if modular > modu5:
                        modu5 = modular
                        cl5 = clmod
                        temp5 = tempmod
                    contt+=1

                if modu5 == 0:
                    print "\nLa modularitat es zero, aixo vol dir que no m'ha trobat cap comunitat"
                    break
                else:
                    if (temp5 < 1):
                       temp5 = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % temp5
                    elif (temp5 > 1) and (temp5 < 60):
                       temp5 = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % temp5
                    else:
                       temp5 = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % temp5
    
                    print cl5
    
                    gr.dibuixar(pos,layout,cl5,unmm)
                    llistacomuni.append('labelpropagation')
                    llistacomuni.append(cl5)
                    modu5 = modularitat(arllegit,cl5) #funcio de calcular la modularitat del graf respecte el clustering donat
                    ##############################            
                    llistalgori.append('labelpropagation')
                    llistalgori.append(cl5)            
                    llistalgori.append(temp5)
                    llistalgori.append(modu5)
                    ##############################

            else:
                print "Error, entrada no valida"
                return llistacomuni,llistalgori


            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl5,unmm)

        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            
            print "Especificar numero de comunitats"
            tr6 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr6 == '':
                t1 = time.time()
                cl6 = arllegit.community_edge_betweenness().as_clustering()
                t2 = time.time()
                

                tem6 = (t2-t1)
                if (tem6 < 1):
                   temp6 = ((t2-t1)*1000.0)
                   print 'La funcio ha tardat %0.3f ms' % temp6
                elif (tem6 > 1) and (tem6 < 60):
                   temp6 = ((t2-t1))
                   print 'La funcio ha tardat %0.3f s' % temp6
                else:
                   temp6 = ((t2-t1)/60.0)                
                   print 'La funcio ha tardat %0.3f min' % temp6

                print cl6

            else:
                tri6 = int(tr6)
                if tri6 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    t1 = time.time()
                    cl6 = arllegit.community_edge_betweenness(clusters=tri6).as_clustering()
                    t2 = time.time()
                    

                    tem6 = (t2-t1)
                    if (tem6 < 1):
                       temp6 = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % temp6
                    elif (tem6 > 1) and (tem6 < 60):
                       temp6 = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % temp6
                    else:
                       temp6 = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % temp6
                    
                    print cl6                   
            
            
            gr.dibuixar(pos,layout,cl6,unmm)
            llistacomuni.append('leadingeigenvector')
            llistacomuni.append(cl6)
            modu6 = modularitat(arllegit,cl6) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('leadingeigenvector')
            llistalgori.append(cl6)            
            llistalgori.append(temp6)
            llistalgori.append(modu6)
            ##############################

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl6,unmm)

        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            
            print "Especificar numero de pasos (steps)"
            tr8 = raw_input("Per defecte el numero de steps es 4, premer enter per defecte\n:")
            if tr8 == '':
                
                if pes == False:
                    t1 = time.time()
                    cl8 = arllegit.community_walktrap().as_clustering()
                    t2 = time.time()
                    print 'algorisme walktrap SENSE pesos'
                else:
                    t1 = time.time()
                    cl8 = arllegit.community_walktrap(weights=pesos).as_clustering()
                    t2 = time.time()
                    print 'algorisme walktrap AMB pesos'                   


                tem8 = (t2-t1)
                if (tem8 < 1):
                   temp8 = ((t2-t1)*1000.0)
                   print 'La funcio ha tardat %0.3f ms' % temp8
                elif (tem8 > 1) and (tem8 < 60):
                   temp8 = ((t2-t1))
                   print 'La funcio ha tardat %0.3f s' % temp8
                else:
                   temp8 = ((t2-t1)/60.0)                
                   print 'La funcio ha tardat %0.3f min' % temp8

                print cl8

            else:
                tri8 = int(tr8)
                if tri8 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    
                    if pes == False:
                        t1 = time.time()
                        cl8 = arllegit.community_walktrap(steps=tri8).as_clustering()
                        t2 = time.time()
                        print 'algorisme walktrap SENSE pesos'
                    else:
                        t1 = time.time()
                        cl8 = arllegit.community_walktrap(weights=pesos,steps=tri8).as_clustering()
                        t2 = time.time()
                        print 'algorisme walktrap AMB pesos'
                    
                    tem8 = (t2-t1)
                    if (tem8 < 1):
                       temp8 = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % temp8
                    elif (tem8 > 1) and (tem8 < 60):
                       temp8 = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % temp8
                    else:
                       temp8 = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % temp8
                    
                    print cl8
            
            gr.dibuixar(pos,layout,cl8,unmm)
            llistacomuni.append('walktrap')
            llistacomuni.append(cl8)
            modu8 = modularitat(arllegit,cl8) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('walktrap')
            llistalgori.append(cl8)            
            llistalgori.append(temp8)
            llistalgori.append(modu8)
            ##############################


            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl8,unmm)

        elif sel[i] == "CFinder":
            print "funcio CFinder\n"
            #arx = arllegit.write_edgelist("./cfinder/arxiu.dat")
            #os.popen("./cfinder/CFinder_commandline_mac -i arxiu.dat")
            ###
            ### Afegir al menu graphml i net opcio per mac i linux
            ### amb linux em fa mostra errors pero dona el resultat be
            ###
            arx = arllegit.write_edgelist("./cfinder/"+nomar+".dat")
            #print "\nL'arxiu de la xarxa que llegira el cfinder es dira: "+nomar+".dat\n"
            
            t1 = time.time()
            
            p = subprocess.Popen("./cfinder/CFinder_commandline_mac -i ./cfinder/"+nomar+".dat -l ./cfinder/licence.txt", shell=True)
            p.communicate()
            
            t2 = time.time()
            

            temcf = (t2-t1)
            if (temcf < 1):
               tempcf = ((t2-t1)*1000.0)
               print 'La funcio ha tardat %0.3f ms' % tempcf
            elif (temcf > 1) and (temcf < 60):
               tempcf = ((t2-t1))
               print 'La funcio ha tardat %0.3f s' % tempcf
            else:
               tempcf = ((t2-t1)/60.0)                
               print 'La funcio ha tardat %0.3f min' % tempcf
            
            rutacf = glob.glob("./cfinder/"+nomar+".dat_files/*") 

            llistanum = []
            varis = False

            for i in range(len(rutacf)):
                stemp = rutacf[i].split('/')
                semp = stemp[3].split('=')
                #print semp
                if len(semp) > 1:
                    sem = semp[1]
                    #print sem
                    llistanum.append(sem)
                    varis = True
            if varis == True:
                print "\nK disponibles:"
                #contnum = 0
                for i in range(len(llistanum)):
                    numaro = llistanum[i]
                    print numaro
                    #contnum+=1

                knum = raw_input('\nEscull una de les k\n')
                #print numaro
                #print int(knum)
                #if int(knum) > numaro  or int(knum) < 1:
                #    "\nError, especifica un dels numeros disponibles\n"
                #    return
            else:
                knum = 3

            try:
                cfx = open("./cfinder/"+nomar+".dat_files/k="+knum+"/communities", "r")
            except IOError:
                print "L'algorisme no ha trobat cap comunitat amb aquesta K\n"
                return llistacomuni,llistalgori
            
            member = cf.convertir(cfx,unmv)
            
            particiocf = VertexClustering(arllegit, member)
            
            gr.dibuixar(pos,layout,particiocf,unmm)
            llistacomuni.append('cfinder')
            llistacomuni.append(particiocf)
            moducf = modularitat(arllegit,particiocf) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('cfinder')
            llistalgori.append(particiocf)            
            llistalgori.append(tempcf)
            llistalgori.append(moducf)
            ##############################

            
            subprocess.Popen("rm ./cfinder/"+nomar+".dat",shell=True)
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,particiocf,unmm)

        elif sel[i] == "netcarto":
            #Nomes em funciona per Linux, macosx no deixa compilar i tampoc executar el binari.
            
            
            #netcarto_cl es l'executable
            #> netcarto_cl net_file_name seed T_ini iteration_factor cooling_factor
            ##_randomizations
            #
            #T_ini, iteration_factor, and cooling_factor can be set to -1 to use
            #the defaults (2/size_of_network, 1.0, and 0.995, respectively).
            if sys.platform == 'linux2':
                
                re = Graph.write_ncol(arllegit,nomar+".ncol")
                
                try: #Conversio a format que enten el netcarto
                    nx.write_multiline_adjlist(arllegit,"provaed.edgelist")
                    re = Graph.write_edgelist(arllegit,nomar+".edgelist")
                    
                except IOError:
                    print 'Error', re
                else:
                    print 'ok\n'  
                
                print "Cal especificar els seguents parametres:"
                llavor = raw_input("La llavor per el generador de nombre aleatori (cal que sigui un enter positiu).\n")
                if llavor < 0:
                    print "Error el nombre ha de ser positiu"
                else:
                    print "\nAra especifica els parametres 'temperatura inicial', 'factor de iteracio' i 'factor de refredament'\n"
                    print "\t default= 2/mida_de_la_xarxa, 1.0 i 0.995\n"
                    pararg = raw_input("Introduexi els nombres dividits per comes. Si vol usar els elements per defecte escrigui 'default'\n")                
                    
                    if pararg == "default":
                        try:
                            t1 = time.time()                            
                            p = subprocess.Popen("./rgraph-1.0.0/netcarto/netcarto_cl ./"+nomar+".edgelist "+llavor+" -1 -1 -1 0", shell=True)
                            p.communicate()
                            t2 = time.time()
                        except IOError:
                            print "Error en l'execusio de l'algorisme netcarto\n"
                    else:
                        parrg = pararg.split(',')
                        try:
                            t1 = time.time()
                            p = subprocess.Popen("./rgraph-1.0.0/netcarto/netcarto_cl ./"+nomar+".edgelist "+llavor+" "+parrg[0]+" "+parrg[1]+" "+parrg[2]+" 0 ", shell=True)
                            p.communicate()
                            t2 = time.time()
                        except IOError:
                            print "Error en l'execusio de l'algorisme netcarto\n"

                    temnc = (t2-t1)
                    if (temnc < 1):
                       tempnc = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % tempnc
                    elif (temnc > 1) and (temnc < 60):
                       tempnc = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % tempnc
                    else:
                       tempnc = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % tempnc

                    try:
                        arxt = open("./modules.clu", "r")
                    except IOError:
                        print "Error l'arxiu de particions del netcarto no s'ha trobat\n"
                        return llistacomuni,llistalgori
                    
                    mebr = nt.convertir(arxt)
                    
                    particionc = VertexClustering(arllegit, mebr)

                    gr.dibuixar(pos,layout,particionc,unmm)
                    llistacomuni.append('netcarto')
                    llistacomuni.append(particionc)
                    modunc = modularitat(arllegit,particionc) #funcio de calcular la modularitat del graf respecte el clustering donat
                    print modunc #
                    ##############################            
                    llistalgori.append('netcarto')
                    llistalgori.append(particionc)            
                    llistalgori.append(tempnc)
                    llistalgori.append(modunc)

            else:
                print "\nAquest algorisme no esta disponible en aquest sistema\n"




        else:
            print "\nL'algorisme especificat no existeix\n"

    return llistacomuni,llistalgori   
####################################

#####Funcio escollir algoritmes NET PAJEK ######
def netescollir(arllegit,nllegit,nomar,pes):
    #print "Menu per netpajek"    
    
    ###layout de la xarxa sera igual per tots els algoritmes##
    layout =  arllegit.layout()
    #### El numero de nodes que conte la xarxa, per passar el dibuixar ####
    unmm = arllegit.ecount()
    unmv = arllegit.vcount()
    
    #print arllegit.vs()
    pos = arllegit.vs["id"]
    
    if pes == True: #Comprovo si la xarxa te pesos
        pesos = arllegit.es["weight"]
    
    
    #####
    #####
    ############ DIVIDIR PER TIPUS DE ALGORISMES ############
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n\n"
    ##########Nomes per xarxes no directes##########
    print "\n\n\tAlgorismes per xarxes no directes:\n"
    print 'multilevel\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    #Modularity > Modularity optimitzation > Greedy Techniques. Amb Pesos.
    
    print 'fastgreedy\n'
    print "\tFinding community structure in very large networks.\n\t A Clauset, MEJ Newman, C Moore. 2004.\n"
    #Modularity > Modularity optimitzation > Greedy Techniques. Amb Pesos.
    
    ##########Nomes per xarxes directes##########
    print "\n\n\tAlgorismes per xarxes directes:\n"
    print 'leadingeigenvector\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    #Modularity Based > Modularity optimitzation > Spectral optimitzation. Sense Pesos.
    
    #########Per xarxes directes i no directes##########
    print "\n\n\tAlgorismes per xarxes directes i no directes:\n"
    print 'walktrap\n'
    print "\tComputing communities in large networks using random walks.\n\t Pascal Pons, Matthieu Latapy. 2005.\n"
    #Dynamic algorithms > Random Walk. Amb Pesos.
    
    print 'spinglass\n'
    print "\tStatistical Mechanics of Community Detection.\n\t Joerg Reichardt, Stefan Bornholdt. 2006.\n" #Aquest es el bo?
    #print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    #Modularity Based > Modifications of modularity. Amb Pesos.
    
    print 'labelpropagation\n'
    print "\tNear linear time algorithm to detect community structures in large-scale networks.\n\t Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"
    #Alternative Methods > Label Propagation. Amb Pesos.
    
    print 'infomap\n'    
    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    #Methods based on statistical inference > Blockmodeling. Amb Pesos als vertex i als enllacos.
    
    print 'edgebetweenness\n'
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    #Divisive algorithms > Girvan and Newman. Sense Pesos.

    print 'CFinder\n'
    print "\tUncovering the overlapping community structure of complex networks in nature and society. Palla et. al., Nature 435, 814-818 (2005)\n"    
    #Overlapping Communities > Clique percolation

    if sys.platform == 'linux2':    
        print 'netcarto\n'
        print "\tGuimera, R. & Amaral, L.A.N., Functional cartography of complex metabolic networks, Nature 433, 895-900 (2005).\n"
        print "\tGuimera, R. & Amaral, L.A.N., Cartography of complex networks: modules and universal roles, J. Stat. Mech.-Theory Exp., art. no. P02001 (2005).\n"
        #Modularity based methods > Simulated anneling
    
    ######## externs al igraph ##########
    #####################################
    esc = raw_input()
    sel = esc.split(',')
    
    llistacomuni = []
    llistalgori = []    
    
    for i in range(len(sel)):
        if sel[i] == "infomap":
            print "funcio infomap \n"
            
            print "Especificar numero de iteracions (trials)"
            tr = raw_input("Per defecte (son 10) premer enter\n:")
            if tr == '':
                
                if pes == False:
                    t1 = time.time()
                    cl = arllegit.community_infomap()
                    t2 = time.time()
                    print 'algorisme infomap SENSE pesos'
                else:
                    t1 = time.time()
                    cl = arllegit.community_infomap(vertex_weights=pesos)
                    t2 = time.time()
                    print 'algorisme infomap AMB pesos'
                    
                    
                    
                tem0 = (t2-t1)
                if (tem0 < 1):
                    temp0 = ((t2-t1)*1000.0)
                    print 'La funcio ha tardat %0.3f ms' % temp0
                elif (tem0 > 1) and (tem0 < 60):
                    temp0 = ((t2-t1))
                    print 'La funcio ha tardat %0.3f s' % temp0
                else:
                    temp0 = ((t2-t1)/60.0)                
                    print 'La funcio ha tardat %0.3f min' % temp0

                print cl
            else:
                tri = int(tr)
                if tri <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    if pes == False:
                        t1 = time.time()
                        cl = arllegit.community_infomap(trials=tri)
                        t2 = time.time()
                        print 'algorisme infomap SENSE pesos'
                    else:
                        t1 = time.time()
                        cl = arllegit.community_infomap(vertex_weights=pesos,trials=tri)
                        t2 = time.time()
                        print 'algorisme infomap AMB pesos'
                    
                    tem0 = (t2-t1)
                    if (tem0 < 1):
                        temp0 = ((t2-t1)*1000.0)
                        print 'La funcio ha tardat %0.3f ms' % temp0
                    elif (tem0 > 1) and (tem0 < 60):
                        temp0 = ((t2-t1))
                        print 'La funcio ha tardat %0.3f s' % temp0
                    else:
                        temp0 = ((t2-t1)/60.0)                
                        print 'La funcio ha tardat %0.3f min' % temp0                    
                    
                    print cl
            
            gr.dibuixar(pos,layout,cl,unmm)
            llistacomuni.append('infomap')
            llistacomuni.append(cl)
            modu = modularitat(arllegit,cl) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('infomap')
            llistalgori.append(cl)            
            llistalgori.append(temp0)
            llistalgori.append(modu)
            ##############################

            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl,unmm)
            
        elif sel[i] == "spinglass":
            print "funcio spinglass \n"

            print "Especificar numero de iteracions (spins)"
            tr1 = raw_input("Per defecte (son 25) premer enter\n:")
            if tr1 == '':
                
                if pes == False:
                    t1 = time.time()
                    cl1 = arllegit.community_spinglass()
                    t2 = time.time()
                    print 'algorisme spinglass SENSE pesos'
                else:
                    t1 = time.time()
                    cl1 = arllegit.community_spinglass(weights=pesos)
                    t2 = time.time()
                    print 'algorisme spinglass AMB pesos'                
                
                
                tem1 = (t2-t1)
                if (tem1 < 1):
                    temp1 = ((t2-t1)*1000.0)
                    print 'La funcio ha tardat %0.3f ms' % temp1
                elif (tem1 > 1) and (tem1 < 60):
                    temp1 = ((t2-t1))
                    print 'La funcio ha tardat %0.3f s' % temp1
                else:
                    temp1 = ((t2-t1)/60.0)                
                    print 'La funcio ha tardat %0.3f min' % temp1

                print cl1
            else:
                tri1 = int(tr1)
                if tri1 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    if pes == False:
                        t1 = time.time()
                        cl1 = arllegit.community_spinglass(spins=tri1)
                        t2 = time.time()
                        print 'algorisme spinglass SENSE pesos'
                    else:
                        t1 = time.time()
                        cl1 = arllegit.community_spinglass(weights=pesos,spins=tri1)
                        t2 = time.time()
                        print 'algorisme spinglass AMB pesos'

                    tem1 = (t2-t1)
                    if (tem1 < 1):
                        temp1 = ((t2-t1)*1000.0)
                        print 'La funcio ha tardat %0.3f ms' % temp1
                    elif (tem1 > 1) and (tem1 < 60):
                        temp1 = ((t2-t1))
                        print 'La funcio ha tardat %0.3f s' % temp1
                    else:
                        temp1 = ((t2-t1)/60.0)                
                        print 'La funcio ha tardat %0.3f min' % temp1

                    print cl1            
            

            gr.dibuixar(pos,layout,cl1,unmm)
            llistacomuni.append('spinglass')
            llistacomuni.append(cl1)
            modu1 = modularitat(arllegit,cl1) #funcio de calcular la modularitat del graf respecte el clustering donat            
            ##############################            
            llistalgori.append('spinglass')
            llistalgori.append(cl1)            
            llistalgori.append(temp1)
            llistalgori.append(modu1)
            ##############################

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl1,unmm)
            
        elif sel[i] == "multilevel":
            print "funcio multilevel \n"

            if pes == False:
                t1 = time.time()
                cl2 = arllegit.community_multilevel()
                t2 = time.time()
                print 'algorisme multilevel SENSE pesos'
            else:
                t1 = time.time()
                cl2 = arllegit.community_multilevel(weights=pesos)
                t2 = time.time()
                print 'algorisme multilevel AMB pesos' 

            tem2 = (t2-t1)
            if (tem2 < 1):
               temp2 = ((t2-t1)*1000.0)
               print 'La funcio ha tardat %0.3f ms' % temp2
            elif (tem2 > 1) and (tem2 < 60):
               temp2 = ((t2-t1))
               print 'La funcio ha tardat %0.3f s' % temp2
            else:
               temp2 = ((t2-t1)/60.0)                
               print 'La funcio ha tardat %0.3f min' % temp2
            
            print cl2
            gr.dibuixar(pos,layout,cl2,unmm)
            llistacomuni.append('multilevel')
            llistacomuni.append(cl2)
            modu2 = modularitat(arllegit,cl2) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('multilevel')
            llistalgori.append(cl2)            
            llistalgori.append(temp2)
            llistalgori.append(modu2)
            ##############################
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl2,unmm)
            
        elif sel[i] == "edgebetweenness":
            print "funcio edgebettweenness\n"
            
            print "Especificar numero de clusters"
            tr3 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr3 == '':
                #L'algorisme no admet pesos(?)
                t1 = time.time()
                cl3 = arllegit.community_edge_betweenness().as_clustering()
                t2 = time.time()

                tem3 = (t2-t1)
                
                if (tem3 < 1):
                    temp3 = ((t2-t1)*1000.0)
                    print 'La funcio ha tardat %0.3f ms' % temp3
                elif (tem3 > 1) and (tem3 < 60):
                    temp3 = ((t2-t1))
                    print 'La funcio ha tardat %0.3f s' % temp3
                else:
                    temp3 = ((t2-t1)/60.0)                
                    print 'La funcio ha tardat %0.3f min' % temp3

                
                print cl3

            else:
                tri3 = int(tr3)
                if tri3 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    t1 = time.time()
                    cl3 = arllegit.community_edge_betweenness(clusters=tri3).as_clustering()
                    t2 = time.time()
                    
                    tem3 = (t2-t1)
                    if (tem3 < 1):
                        temp3 = ((t2-t1)*1000.0)
                        print 'La funcio ha tardat %0.3f ms' % temp3
                    elif (tem3 > 1) and (tem3 < 60):
                        temp3 = ((t2-t1))
                        print 'La funcio ha tardat %0.3f s' % temp3
                    else:
                        temp3 = ((t2-t1)/60.0)                
                        print 'La funcio ha tardat %0.3f min' % temp3

                    print cl3
            
            gr.dibuixar(pos,layout,cl3,unmm)
            llistacomuni.append('edgebetweenness')
            llistacomuni.append(cl3)
            modu3 = modularitat(arllegit,cl3) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('edgebetweenness')
            llistalgori.append(cl3)            
            llistalgori.append(temp3)
            llistalgori.append(modu3)
            ##############################
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl3,unmm)
            
        elif sel[i] == "fastgreedy":
            print "funcio fastgreedy \n"
            arllegit.simplify()
            #pprint (vars(arllegit))# comprovar variables de objecte
            #print inspect.getmembers(arllegit)# inspecionar objecte

            if pes == False:
                t1 = time.time()
                cl4 = arllegit.community_fastgreedy().as_clustering() # Maximitza la modularitat
                t2 = time.time()
                print 'algorisme fastgreedy SENSE pesos'
            else:
                t1 = time.time()
                cl4 = arllegit.community_fastgreedy(weights=pesos).as_clustering()
                t2 = time.time()
                print 'algorisme fastgreedy AMB pesos'
            
            tem4 = (t2-t1)
            if (tem4 < 1):
               temp4 = ((t2-t1)*1000.0)
               print 'La funcio ha tardat %0.3f ms' % temp4
            elif (tem4 > 1) and (tem4 < 60):
               temp4 = ((t2-t1))
               print 'La funcio ha tardat %0.3f s' % temp4
            else:
               temp4 = ((t2-t1)/60.0)                
               print 'La funcio ha tardat %0.3f min' % temp4

            print cl4

            colors = ["red", "green", "blue", "yellow", "magenta"]
            gr.dibuixar(pos,layout,cl4,unmm)
            llistacomuni.append('fastgreedy')
            llistacomuni.append(cl4)
            modu4 = modularitat(arllegit,cl4) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('fastgreedy')
            llistalgori.append(cl4)            
            llistalgori.append(temp4)
            llistalgori.append(modu4)
            ##############################
            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl4,unmm)
            
        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"

            print "L'algorisme 'labelpropagation' en cada execusio dona un resultat diferent a causa de la aleatorietat dels calculs que realitza"
            print "Veure: 'Near linear time algorithm to detect community structures in large-scale networks' U. N. Raghavan, R. Albert, S. Kumara. Sep. 2007"
            print "Per aixo es pot escollir si es vol realitzar una sola iteracio o varies"
            vega = raw_input("Esciu la opcio: 'una' o 'varies'\n")
            
            if vega == 'una':
                
                if pes == False:
                    t1 = time.time()
                    cl5 = arllegit.community_label_propagation()
                    t2 = time.time()
                    print 'algorisme labelpropagation SENSE pesos'
                else:
                    t1 = time.time()
                    cl5 = arllegit.community_label_propagation(weights=pesos)
                    t2 = time.time()
                    print 'algorisme labelpropagation AMB pesos'                 
                
                tem5 = (t2-t1)
                if (tem5 < 1):
                   temp5 = ((t2-t1)*1000.0)
                   print 'La funcio ha tardat %0.3f ms' % temp5
                elif (tem5 > 1) and (tem5 < 60):
                   temp5 = ((t2-t1))
                   print 'La funcio ha tardat %0.3f s' % temp5
                else:
                   temp5 = ((t2-t1)/60.0)                
                   print 'La funcio ha tardat %0.3f min' % temp5

                print cl5
                
                gr.dibuixar(pos,layout,cl5,unmm)
                llistacomuni.append('labelpropagation')
                llistacomuni.append(cl5)
                modu5 = modularitat(arllegit,cl5) #funcio de calcular la modularitat del graf respecte el clustering donat
                ##############################            
                llistalgori.append('labelpropagation')
                llistalgori.append(cl5)            
                llistalgori.append(temp5)
                llistalgori.append(modu5)
                ##############################                
                
                
            elif vega == 'varies':
                print "\nIntrodueix el nombre de vegades que vols que s'executi l'algorisme"
                print "Automaticament s'escullira el resultat que maximitzi el valor de modularitat\n"
                vegavar = raw_input("Escriu el nombre de iteracions:")
                contt = 0
                modu5 = 0
                temp5 = 0
                cl5 = 0
                limitv = int(vegavar)
                print limitv
                while contt != limitv:
                    if pes == False:
                        t1 = time.time()
                        clmod = arllegit.community_label_propagation()
                        t2 = time.time()
                        #print 'algorisme labelpropagation SENSE pesos'
                    else:
                        t1 = time.time()
                        clmod = arllegit.community_label_propagation(weights=pesos)
                        t2 = time.time()
                        #print 'algorisme labelpropagation AMB pesos'
                    tempmod = ((t2-t1)*1000.0)
 

                    modular = modularitat(arllegit,clmod) #Calculo la modularitat
                    #print "modular:"+str(modular)+"modu5:"+str(modu5)
                    if modular > modu5: #Afagare la iteracio amb major modularitat
                        modu5 = modular
                        cl5 = clmod
                        temp5 = tempmod
                    contt+=1

                if modu5 == 0:
                    print "\nLa modularitat es zero, aixo vol dir que no m'ha trobat cap comunitat"
                else:    
                    if (temp5 < 1):
                       temp5 = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % temp5
                    elif (temp5 > 1) and (temp5 < 60):
                       temp5 = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % temp5
                    else:
                       temp5 = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % temp5
    
                    print cl5
    
                    gr.dibuixar(pos,layout,cl5,unmm)
                    llistacomuni.append('labelpropagation')
                    llistacomuni.append(cl5)
                    modu5 = modularitat(arllegit,cl5) #funcio de calcular la modularitat del graf respecte el clustering donat
                    ##############################            
                    llistalgori.append('labelpropagation')
                    llistalgori.append(cl5)            
                    llistalgori.append(temp5)
                    llistalgori.append(modu5)
                    ##############################                



            else:
                print "\nError, entrada no valida"
                return llistacomuni,llistalgori
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl5,unmm)
            
        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            
            print "Especificar numero de comunitats"
            tr6 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr6 == '':
                #No admet pesos
                t1 = time.time()
                cl6 = arllegit.community_leading_eigenvector()
                t2 = time.time()

                tem6 = (t2-t1)
                if (tem6 < 1):
                   temp6 = ((t2-t1)*1000.0)
                   print 'La funcio ha tardat %0.3f ms' % temp6
                elif (tem6 > 1) and (tem6 < 60):
                   temp6 = ((t2-t1))
                   print 'La funcio ha tardat %0.3f s' % temp6
                else:
                   temp6 = ((t2-t1)/60.0)                
                   print 'La funcio ha tardat %0.3f min' % temp6

                print cl6

            else:
                tri6 = int(tr6)
                if tri6 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    t1 = time.time()
                    cl6 = arllegit.community_leading_eigenvector(clusters=tri6)
                    t2 = time.time()

                    tem6 = (t2-t1)
                    if (tem6 < 1):
                       temp6 = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % temp6
                    elif (tem6 > 1) and (tem6 < 60):
                       temp6 = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % temp6
                    else:
                       temp6 = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % temp6

                    print cl6
            
            gr.dibuixar(pos,layout,cl6,unmm)
            llistacomuni.append('leadingeigenvector')
            llistacomuni.append(cl6)
            modu6 = modularitat(arllegit,cl6) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('leadingeigenvector')
            llistalgori.append(cl6)            
            llistalgori.append(temp6)
            llistalgori.append(modu6)
            ##############################
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl6,unmm)

        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            
            print "Especificar numero de pasos (steps)"
            tr8 = raw_input("Per defecte el numero de steps es 4, premer enter per defecte\n:")
            if tr8 == '':
                
                if pes == False:
                    t1 = time.time()
                    cl8 = arllegit.community_walktrap().as_clustering()
                    t2 = time.time()
                    print 'algorisme walktrap SENSE pesos'
                else:
                    t1 = time.time()
                    cl8 = arllegit.community_walktrap(weights=pesos).as_clustering()
                    t2 = time.time()
                    print 'algorisme walktrap AMB pesos'                  
                
                tem8 = (t2-t1)
                if (tem8 < 1):
                   temp8 = ((t2-t1)*1000.0)
                   print 'La funcio ha tardat %0.3f ms' % temp8
                elif (tem8 > 1) and (tem8 < 60):
                   temp8 = ((t2-t1))
                   print 'La funcio ha tardat %0.3f s' % temp8
                else:
                   temp8 = ((t2-t1)/60.0)                
                   print 'La funcio ha tardat %0.3f min' % temp8

                print cl8

            else:
                tri8 = int(tr8)
                if tri8 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    
                    if pes == False:
                        t1 = time.time()
                        cl8 = arllegit.community_walktrap(steps=tri8).as_clustering()
                        t2 = time.time()
                        print 'algorisme walktrap SENSE pesos'
                    else:
                        t1 = time.time()
                        cl8 = arllegit.community_walktrap(weights=pesos,steps=tri8).as_clustering()
                        t2 = time.time()
                        print 'algorisme walktrap AMB pesos'                     

                    tem8 = (t2-t1)
                    if (tem8 < 1):
                       temp8 = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % temp8
                    elif (tem8 > 1) and (tem8 < 60):
                       temp8 = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % temp8
                    else:
                       temp8 = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % temp8

                    print cl8
            
            gr.dibuixar(pos,layout,cl8,unmm)
            llistacomuni.append('walktrap')
            llistacomuni.append(cl8)
            modu8 = modularitat(arllegit,cl8) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('walktrap')
            llistalgori.append(cl8)            
            llistalgori.append(temp8)
            llistalgori.append(modu8)
            ##############################
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl8,unmm)
            
        elif sel[i] == "CFinder":
            #arx = arllegit.write_edgelist("./cfinder/arxiu.dat")
            #os.popen("./cfinder/CFinder_commandline_mac -i arxiu.dat")
            print "funcio CFinder\n"
            
            arx = arllegit.write_edgelist("./cfinder/"+nomar+".dat")
            #print "\nL'arxiu de la xarxa que llegira el cfinder es dira: "+nomar+".dat\n"
            
            t1 = time.time()
            
            p = subprocess.Popen("./cfinder/CFinder_commandline_mac -i ./cfinder/"+nomar+".dat -l ./cfinder/licence.txt", shell=True)
            p.communicate()

            t2 = time.time()

            temcf = (t2-t1)
            if (temcf < 1):
               tempcf = ((t2-t1)*1000.0)
               print 'La funcio ha tardat %0.3f ms' % tempcf
            elif (temcf > 1) and (temcf < 60):
               tempcf = ((t2-t1))
               print 'La funcio ha tardat %0.3f s' % tempcf
            else:
               tempcf = ((t2-t1)/60.0)                
               print 'La funcio ha tardat %0.3f min' % tempcf

            rutacf = glob.glob("./cfinder/"+nomar+".dat_files/*") 

            llistanum = []
            varis = False

            for i in range(len(rutacf)):
                stemp = rutacf[i].split('/')
                semp = stemp[3].split('=')
                #print semp
                if len(semp) > 1:
                    sem = semp[1]
                    #print sem
                    llistanum.append(sem)
                    varis = True
            if varis == True:
                print "\nK disponibles:"
                #contnum = 0
                for i in range(len(llistanum)):
                    numaro = llistanum[i]
                    print numaro
                    #contnum+=1

                knum = raw_input('\nEscull una de les k\n')
                #print numaro
                #print int(knum)
                #if int(knum) > numaro  or int(knum) < 1:
                #    "\nError, especifica un dels numeros disponibles\n"
                #    return
            else:
                knum = 3

            try:
                cfx = open("./cfinder/"+nomar+".dat_files/k="+knum+"/communities", "r")
            except IOError:
                print "L'algorisme no ha trobat cap comunitat\n"
                return llistacomuni,llistalgori
            
            #print "despres del return"
            member = cf.convertir(cfx,unmv)
            particiocf = VertexClustering(arllegit, member)
            
            gr.dibuixar(pos,layout,particiocf,unmm)
            llistacomuni.append('cfinder')
            llistacomuni.append(particiocf)
            moducf = modularitat(arllegit,particiocf) #funcio de calcular la modularitat del graf respecte el clustering donat
            ##############################            
            llistalgori.append('cfinder')
            llistalgori.append(particiocf)            
            llistalgori.append(tempcf)
            llistalgori.append(moducf)
            ##############################
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,particiocf,unmm)

        elif sel[i] == "netcarto":
            #Nomes em funciona per Linux, macosx no deixa compilar i tampoc executar el binari.
            
            
            #netcarto_cl es l'executable
            #> netcarto_cl net_file_name seed T_ini iteration_factor cooling_factor
            ##_randomizations
            #
            #T_ini, iteration_factor, and cooling_factor can be set to -1 to use
            #the defaults (2/size_of_network, 1.0, and 0.995, respectively).
            if sys.platform == 'linux2':
                
                try: #Conversio a format que enten el netcarto
                    re = Graph.write_ncol(arllegit,nomar+".ncol")
                    #re = Graph.write_edgelist(arllegit,nomar+".edgelist")
                except IOError:
                    print 'Error', re
                else:
                    print 'ok\n'  
                
                print "Cal especificar els seguents parametres:"
                llavor = raw_input("La llavor per el generador de nombre aleatori (cal que sigui un enter positiu).\n")
                if llavor < 0:
                    print "Error el nombre ha de ser positiu"
                else:
                    print "\nAra especifica els parametres 'temperatura inicial', 'factor de iteracio' i 'factor de refredament'\n"
                    print "\t default= 2/mida_de_la_xarxa, 1.0 i 0.995\n"
                    pararg = raw_input("Introduexi els nombres dividits per comes. Si vol usar els elements per defecte escrigui 'default'\n")                
                    
                    if pararg == "default":
                        try:
                            t1 = time.time()                            
                            p = subprocess.Popen("./rgraph-1.0.0/netcarto/netcarto_cl ./"+nomar+".edgelist "+llavor+" -1 -1 -1 0", shell=True)
                            p.communicate()
                            t2 = time.time()
                        except IOError:
                            print "Error en l'execusio de l'algorisme netcarto\n"
                    else:
                        parrg = pararg.split(',')
                        try:
                            t1 = time.time()
                            p = subprocess.Popen("./rgraph-1.0.0/netcarto/netcarto_cl ./"+nomar+".edgelist "+llavor+" "+parrg[0]+" "+parrg[1]+" "+parrg[2]+" 0 ", shell=True)
                            p.communicate()
                            t2 = time.time()
                        except IOError:
                            print "Error en l'execusio de l'algorisme netcarto\n"

                    temnc = (t2-t1)
                    if (temnc < 1):
                       tempnc = ((t2-t1)*1000.0)
                       print 'La funcio ha tardat %0.3f ms' % tempnc
                    elif (temnc > 1) and (temnc < 60):
                       tempnc = ((t2-t1))
                       print 'La funcio ha tardat %0.3f s' % tempnc
                    else:
                       tempnc = ((t2-t1)/60.0)                
                       print 'La funcio ha tardat %0.3f min' % tempnc

                    try:
                        arxt = open("./modules.clu", "r")
                    except IOError:
                        print "Error l'arxiu de particions del netcarto no s'ha trobat\n"
                        return llistacomuni,llistalgori
                    
                    mebr = nt.convertir(arxt)
                    
                    particionc = VertexClustering(arllegit, mebr)

                    gr.dibuixar(pos,layout,particionc,unmm)
                    llistacomuni.append('netcarto')
                    llistacomuni.append(particionc)
                    modunc = modularitat(arllegit,particionc) #funcio de calcular la modularitat del graf respecte el clustering donat
                    ##############################            
                    llistalgori.append('netcarto')
                    llistalgori.append(particionc)            
                    llistalgori.append(tempnc)
                    llistalgori.append(modunc)
            else:
                print "\nAquest algorisme no esta disponible en aquest sistema\n"


        else:
            print "\nL'algorisme especificat no existeix\n"


    return llistacomuni,llistalgori
