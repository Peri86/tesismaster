#!/usr/bin/env python
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

def betweenness_centralization(G):
    vnum = G.vcount()
    if vnum < 3:
        raise ValueError("graph must have at least three vertices")
    denom = (vnum-1)*(vnum-2)
 
    temparr = [2*i/denom for i in G.betweenness()]
    max_temparr = max(temparr)
    return sum(max_temparr-i for i in temparr)/(vnum-1)

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