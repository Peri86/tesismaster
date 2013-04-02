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

import grafics as gr
import gephi as gp

global cl,cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8

def modularitat(xarxa,comun):
    print "Modularity:"
    print xarxa.modularity(comun)
    return

#####Funcio escollir algoritmes######
def escollir(arllegit,nllegit):

    #### El numero de nodes que conte la xarxa, per passar el dibuixar ####
    unmm = arllegit.ecount()    
    pos = arllegit.vs["id"]
    #mida = arllegit.vs["size"]
    
    ###layout de la xarxa###
    layout =  arllegit.layout("kk")
    
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
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    #Modularity Based > Modifications of modularity. Amb Pesos.
    
    print 'labelpropagation\n'
    print "\tNear linear time algorithm to detect community structures in large-scale networks.\n\t Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"
    #Alternative Methods > Label Propagation. Amb Pesos.
    
    print 'infomap\n'    
    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    #Methods based on statistical inference > Blockmodeling. Amb Pesos als vertex i als enllacos.
    
    print 'edgebettweenness\n'
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    #Divisive algorithms > Girvan and Newman. Sense Pesos.

    print 'CFinder\n'
    print "\tUncovering the overlapping community structure of complex networks in nature and society. Palla et. al., Nature 435, 814-818 (2005)\n"    
    #Overlapping Communities > Clique percolation
    
    ######## externs al igraph ##########
    #####################################
    #print '\nPer sortir del programa escriu: sortir\n'
    
    esc = raw_input()
    sel = esc.split(',')
    
    llistacomuni = []
    
    for i in range(len(sel)):
        if sel[i] == "infomap":
            print "funcio infomap \n"
            
            print "Especificar numero de iteracions (trials)"
            tr = raw_input("Per defecte (son 10) premer enter\n:")
            if tr == '':
                cl = arllegit.community_infomap()
                print cl
            else:
                tri = int(tr)
                if tri <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl = arllegit.community_infomap(trials=tri)
                    print cl
            
            
            gr.dibuixar(pos,layout,cl,unmm)
            llistacomuni.append('infomap') #inserto el nom de la funcio i el calcul de comunitat per saberho a comunitats.py
            llistacomuni.append(cl)
            ####
            modularitat(arllegit,cl) #funcio de calcular la modularitat del graf respecte el clustering donat
            ####
            #gp.escriuregraf(arllegit,cl)############
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl,unmm)
            

        elif sel[i] == "spinglass":
            print "funcio spinglass \n"
            
            print "Especificar numero de iteracions (spins)"
            tr1 = raw_input("Per defecte (son 25) premer enter\n:")
            if tr1 == '':
                cl1 = arllegit.community_spinglass()
                print cl1
            else:
                tri1 = int(tr1)
                if tri1 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl1 = arllegit.community_spinglass(spins=tri1)
                    print cl1            
            
            
            gr.dibuixar(pos,layout,cl1,unmm)
            llistacomuni.append('spinglass')
            llistacomuni.append(cl1)
            modularitat(arllegit,cl1) #funcio de calcular la modularitat del graf respecte el clustering donat

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl1,unmm)

        elif sel[i] == "multilevel":
            print "funcio multilevel \n"
            cl2 = arllegit.community_multilevel()
            print cl2
            
            gr.dibuixar(pos,layout,cl2,unmm)
            llistacomuni.append('multilevel')
            llistacomuni.append(cl2)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl2,unmm)

        elif sel[i] == "edgebettweenness":
            print "funcio edgebettweenness\n"
            
            print "Especificar numero de clusters"
            tr3 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr3 == '':
                cl3 = arllegit.community_edge_betweenness().as_clustering()
                print cl3
            else:
                tri3 = int(tr3)
                if tri3 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl3 = arllegit.community_edge_betweenness(clusters=tri3).as_clustering()
                    print cl3            
            
            gr.dibuixar(pos,layout,cl3,unmm)
            llistacomuni.append('edgebettweenness')
            llistacomuni.append(cl3)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl3,unmm)

        elif sel[i] == "fastgreedy":
            print "funcio fastgreedy \n"
            arllegit.simplify()
            #pprint (vars(arllegit))# comprovar variables de objecte
            #print inspect.getmembers(arllegit)# inspecionar objecte
            cl4 = arllegit.community_fastgreedy().as_clustering() # Maximitza la modularitat
            #cl4.__plot__()
            print cl4
            #pprint (vars(cl4))#
            colors = ["red", "green", "blue", "yellow", "magenta"]
            gr.dibuixar(pos,layout,cl4,unmm)
            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
            llistacomuni.append('fastgreedy')
            llistacomuni.append(cl4)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl4,unmm)

        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"
            cl5 = arllegit.community_label_propagation()
            print cl5
            gr.dibuixar(pos,layout,cl5,unmm)
            llistacomuni.append('labelpropagation')
            llistacomuni.append(cl5)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl5,unmm)

        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            
            print "Especificar numero de comunitats"
            tr6 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr6 == '':
                cl6 = arllegit.community_edge_betweenness().as_clustering()
                print cl6
            else:
                tri6 = int(tr6)
                if tri6 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl6 = arllegit.community_edge_betweenness(clusters=tri6).as_clustering()
                    print cl6                   
            
            
            gr.dibuixar(pos,layout,cl6,unmm)
            llistacomuni.append('leadingeigenvector')
            llistacomuni.append(cl6)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl6,unmm)

        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            
            print "Especificar numero de pasos (steps)"
            tr8 = raw_input("Per defecte el numero de steps es 4, premer enter per defecte\n:")
            if tr8 == '':
                cl8 = arllegit.community_edge_betweenness().as_clustering()
                print cl8
            else:
                tri8 = int(tr8)
                if tri8 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl8 = arllegit.community_edge_betweenness(clusters=tri8).as_clustering()
                    print cl8
            
            gr.dibuixar(pos,layout,cl8,unmm)
            llistacomuni.append('walktrap')
            llistacomuni.append(cl8)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl8,unmm)

        elif sel[i] == "CFinder":
            #arx = arllegit.write_edgelist("./cfinder/arxiu.dat")
            #os.popen("./cfinder/CFinder_commandline_mac -i arxiu.dat")
            ###
            ### Afegir al menu graphml i net opcio per mac i linux
            ### amb linux em fa mostra errors pero dona el resultat be
            ###
            arx = arllegit.write_edgelist("./cfinder/arxiu.dat")
            print arx
            print "l'arxiu que genera el cfinder es dira"
            
            p = subprocess.Popen("./cfinder/CFinder_commandline_mac -i ./cfinder/arxiu.dat -l ./cfinder/licence.txt", shell=True)
            p.communicate()
            cfx = open("./cfinder/arxiu.dat_files/k=3/communities", "r")
            member = cf.convertir(cfx)
            particiocf = VertexClustering(arllegit, member)
            
            gr.dibuixar(pos,layout,particiocf,unmm)
            llistacomuni.append('cfinder')
            llistacomuni.append(particiocf)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,particiocf,unmm)

        elif sel[i] == "commfind":
            nuigen = 10
            
            p = subprocess.Popen("./commfind/commfind ./commfind/"++".graphml"+nuigen, shell=True)
            p.communicate()
            #cfx = open("./cfinder/arxiu.dat_files/k=3/communities", "r")
            #member = cf.convertir(cfx)
            #particiocf = VertexClustering(arllegit, member)
            #
            #gr.dibuixar(pos,layout,particiocf,unmm)
            #llistacomuni.append('cfinder')
            #llistacomuni.append(particiocf)
            #
            #print 'Vols guardar la imatge?\n'
            #sino = raw_input('si,no:\n')
            #if sino == 'si':
            #    gr.guardargraf(pos,layout,particiocf,unmm)


    return llistacomuni   
####################################

#####Funcio escollir algoritmes NET PAJEK ######
def netescollir(arllegit,nllegit):
    
    ###layout de la xarxa sera igual per tots els algoritmes##
    layout =  arllegit.layout()
    #### El numero de nodes que conte la xarxa, per passar el dibuixar ####
    unmm = arllegit.ecount()

    print arllegit.vs()
    pos = arllegit.vs["id"]
    #####
    #####
    ############ DIVIDIR PER TIPUS DE ALGORISMES ############
    print 'Escull un o varis algorismes per la deteccio de comunitats'
    print "Si son varis, els algorismes han d'estar separats per comes\n"
    print "Algorismes disponibles:\n\n"
    
    #Methods based on statistical inference > Blockmodeling. Amb Pesos als vertex i als enllacos.
    print 'infomap\n'    
    print "\tMaps of random walks on complex networks reveal community structure.\n\t Martin Rosvall, Carl T. Bergstrom. 2007.\n"
    
    #Modularity Based > Modifications of modularity. Amb Pesos.
    print 'spinglass\n'
    print "\tStatistical Mechanics of Community Detection.\n\t Joerg Reichardt, Stefan Bornholdt. 2006.\n"
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    
    #Modularity > Modularity optimitzation > Greedy Techniques. Amb Pesos.
    print 'multilevel\n'
    print "\tFast unfolding of communities in large networks.\n\t V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. 2008\n"
    
    #Divisive algorithms > Girvan and Newman. Sense Pesos.    
    print 'edgebettweenness\n'
    print "\tFinding and evaluating community structure in networks.\n\t M.E.J. Newman, M. Girvan. 2004.\n"
    
    #Modularity > Modularity optimitzation > Greedy Techniques. Amb Pesos.    
    print 'fastgreedy\n'
    print "\tFinding community structure in very large networks.\n\t A Clauset, MEJ Newman, C Moore. 2004.\n"
    
    #Alternative Methods > Label Propagation. Amb Pesos.    
    print 'labelpropagation\n'
    print "\tNear linear time algorithm to detect community structures in large-scale networks.\n\t Usha Nandini Raghavan, Reka Albert, Soundar Kumara. 2007.\n"    
    
    #Modularity Based > Modularity optimitzation > Spectral optimitzation. Sense Pesos.    
    print 'leadingeigenvector\n'
    print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    
    #Modularity Based > Modularity optimitzation > Spectral optimitzation. Sense Pesos.    
    #print 'leadingeigenvectornaive\n'
    #print "\tFinding community structure in networks using the eigenvectors of matrices.\n\t M. E. J. Newman. 2006.\n"
    
    #Dynamic algorithms > Random Walk. Amb Pesos.    
    print 'walktrap\n'
    print "\tComputing communities in large networks using random walks.\n\t Pascal Pons, Matthieu Latapy. 2005.\n"
    
    #Overlapping Communities > Clique percolation
    print 'CFinder\n'
    print "\tUncovering the overlapping community structure of complex networks in nature and society. Palla et. al., Nature 435, 814-818 (2005)\n"    
    
    
    ######## externs al igraph ##########
    #####################################
    esc = raw_input()
    sel = esc.split(',')
    
    for i in range(len(sel)):
        if sel[i] == "infomap":
            print "funcio infomap \n"
            
            print "Especificar numero de iteracions (trials)"
            tr = raw_input("Per defecte (son 10) premer enter\n:")
            if tr == '':
                cl = arllegit.community_infomap()
                print cl
            else:
                tri = int(tr)
                if tri <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl = arllegit.community_infomap(trials=tri)
                    print cl
            
            gr.dibuixar(pos,layout,cl,unmm)
            llistacomuni.append('infomap')
            llistacomuni.append(cl)
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl,unmm)
            
        elif sel[i] == "spinglass":
            print "funcio spinglass \n"

            print "Especificar numero de iteracions (spins)"
            tr1 = raw_input("Per defecte (son 25) premer enter\n:")
            if tr1 == '':
                cl1 = arllegit.community_spinglass()
                print cl1
            else:
                tri1 = int(tr1)
                if tri1 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl1 = arllegit.community_spinglass(spins=tri1)
                    print cl1            
            

            gr.dibuixar(pos,layout,cl1,unmm)
            llistacomuni.append('spinglass')
            llistacomuni.append(cl1)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl1,unmm)
            
        elif sel[i] == "multilevel":
            print "funcio multilevel \n"
            cl2 = arllegit.community_multilevel()
            print cl2
            gr.dibuixar(pos,layout,cl2,unmm)
            llistacomuni.append('multilevel')
            llistacomuni.append(cl2)

            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl2,unmm)
            
        elif sel[i] == "edgebettweenness":
            print "funcio edgebettweenness\n"
            
            print "Especificar numero de clusters"
            tr3 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr3 == '':
                cl3 = arllegit.community_edge_betweenness().as_clustering()
                print cl3
            else:
                tri3 = int(tr3)
                if tri3 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl3 = arllegit.community_edge_betweenness(clusters=tri3).as_clustering()
                    print cl3
            
            gr.dibuixar(pos,layout,cl3,unmm)
            llistacomuni.append('edgebettweenness')
            llistacomuni.append(cl3)

            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl3,unmm)
            
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
            gr.dibuixar(pos,layout,cl4,unmm)
            llistacomuni.append('fastgreedy')
            llistacomuni.append(cl4)

            #plot(arllegit, vertex_color=[colors[i] for i in cl4.membership]) #
            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl4,unmm)
            
        elif sel[i] == "labelpropagation":
            print "funcio labelpropagation\n"
            cl5 = arllegit.community_label_propagation()
            print cl5
            gr.dibuixar(pos,layout,cl5,unmm)
            llistacomuni.append('labelpropagation')
            llistacomuni.append(cl5)

            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl5,unmm)
            
        elif sel[i] == "leadingeigenvector":
            print "funcio leadingeigenvector\n"
            
            print "Especificar numero de comunitats"
            tr6 = raw_input("Per defecte s'estableix un nivell que maximitza la modularitat, premer enter per defecte\n:")
            if tr6 == '':
                cl6 = arllegit.community_edge_betweenness().as_clustering()
                print cl6
            else:
                tri6 = int(tr6)
                if tri6 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl6 = arllegit.community_edge_betweenness(clusters=tri6).as_clustering()
                    print cl6
            
            gr.dibuixar(pos,layout,cl6,unmm)
            llistacomuni.append('leadingeigenvector')
            llistacomuni.append(cl6)

            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl6,unmm)

        elif sel[i] == "walktrap":
            print "funcio walktrap\n"
            
            print "Especificar numero de pasos (steps)"
            tr8 = raw_input("Per defecte el numero de steps es 4, premer enter per defecte\n:")
            if tr8 == '':
                cl8 = arllegit.community_edge_betweenness().as_clustering()
                print cl8
            else:
                tri8 = int(tr8)
                if tri8 <= 0:
                    print "Nombre no acceptat"
                    return
                else:
                    cl8 = arllegit.community_edge_betweenness(clusters=tri8).as_clustering()
                    print cl8
            
            gr.dibuixar(pos,layout,cl8,unmm)
            llistacomuni.append('walktrap')
            llistacomuni.append(cl8)

            
            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,cl8,unmm)
            
        elif sel[i] == "CFinder":
            #arx = arllegit.write_edgelist("./cfinder/arxiu.dat")
            #os.popen("./cfinder/CFinder_commandline_mac -i arxiu.dat")
            p = subprocess.Popen("./cfinder/CFinder_commandline_mac -i ./cfinder/arxiu.dat -l ./cfinder/licence.txt", shell=True)
            p.communicate()
            cfx = open("./cfinder/arxiu.dat_files/k=3/communities", "r")
            member = cf.convertir(cfx)
            particiocf = VertexClustering(arllegit, member)
            
            gr.dibuixar(pos,layout,particiocf,unmm)
            llistacomuni.append('cfinder')
            llistacomuni.append(particiocf)

            print 'Vols guardar la imatge?\n'
            sino = raw_input('si,no:\n')
            if sino == 'si':
                gr.guardargraf(pos,layout,particiocf,unmm)

    return llistacomuni
