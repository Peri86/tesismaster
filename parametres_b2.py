#!/usr/bin/env python
from igraph import *
import networkx as nx
#import community as cp
#import community_jolleycraig as cj
import glob
import cairo
import matplotlib.pyplot as plt
from pprint import pprint
import inspect
import itertools

param = []

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
    print "\t[1] Betweenness Centralization\n" #Aguanta xarxes inconectes
    #The network betweenness centralization score is calculated based on the betweenness centrality for each individual in the network.
    #Betweenness centrality examines the number of times one person lies on the shortest path between two others    
    print "\t[2] Average path length\n" 
    #La longitud de cami mitjana
    print "\t[3] Assortativity degree\n" 
    #This coefficient is basically the correlation between the actual connectivity patterns of the vertices and the pattern expected from the
    #disribution of the vertex types.
    print "\t[4] Diameter\n" 
    print "\t[5] Density\n" 
    print "\t[6] Cohesion\n" 
    #The vertex connectivity between two given vertices is the number of vertices
    #that have to be removed in order to disconnect the two vertices into two
    #separate components. This is also the number of vertex disjoint directed
    #paths between the vertices (apart from the source and target vertices of
    #course). The vertex connectivity of the graph is the minimal vertex
    #connectivity over all vertex pairs.
    #
    #This method calculates the vertex connectivity of a given vertex pair if both
    #the source and target vertices are given. If none of them is given (or they
    #are both negative), the overall vertex connectivity is returned.
    
    print "\t[7] Radius\n" #No funciona amb xarxes inconectes
    #The radius of a graph is defined as the minimum eccentricity of its vertices
    #The eccentricity of a vertex is calculated by measuring the shortest distance from (or to) the vertex, to (or from) all other
    #vertices in the graph, and taking the maximum.
    print "\tParametres per cada node de la xarxa: \n"
    print "\t[11] Betweenness\n"
    #Mostra per cada node el seu valor de betweenness, gran = centric.
    print "\t[12] Pagerank\n"
    #Calcula algorisme de google, es una variant del eigenvector centratily, canviar posicio
    print "\t[13] EigenVectorCentrality\n"
    #It assigns relative scores to all nodes in the network based on the concept that connections to high-scoring nodes
    #contribute more to the score of the node in question than equal connections to low-scoring nodes.
    print "\t[14] Average degree connectivity\n"
    #The average degree connectivity is the average nearest neighbor degree ofnodes with degree k. 
    print "\t[15] Periphery\n" #No funciona amb xarxes inconectes
    #The periphery is the set of nodes with eccentricity equal to the diameter. 
    print "\t[16] Eccentricity\n"#No funciona amb xarxes inconectes
    #The eccentricity of a node v is the maximum distance from v to all other nodes in G.
    
    print "\t[17] Center nodes\n"#No funciona amb xarxes inconectes
    #The center is the set of nodes with eccentricity equal to radius. 

    print "\t[18] Degree Distribution\n"
    #Grau de distribucio del graf
    print "\t[19] Count the number of Motif\n"
    #Counts the total number of motifs in the graph
    #Motifs are small subgraphs of a given structure in a graph.
    #This function counts the total number of motifs in a graph without
    #assigning isomorphism classes to them.
    print "\t[20] Similarity Jaccard\n"
    #The Jaccard similarity coefficient of two vertices is the number of their
    #common neighbors divided by the number of vertices that are adjacent to
    #at least one of them.
    
    se = raw_input('Escriu els numeros dels parametres que vulguis amb una coma entre mig:\n')
    secom = se.split(',')
    
    for i in range(len(secom)):
        if secom[i] == "1":
                print "\nBetweenness Centralization:"
                p1 = betweenness_centralization(G)
                print p1
                param.append("Betweenness Centralization")
                param.append(p1)
        elif secom[i] == "2":
                print "\nAverage path length:"
                p2 = G.average_path_length()            
                print p2
                param.append("Average path length")
                param.append(p2)
        elif secom[i] == "3":
                print "\nAssortativity degree:"
                p3 = G.assortativity_degree()            
                print p3
                param.append("Assortativity degree")
                param.append(p3)
        elif secom[i] == "4":
                print "\nDiameter:"
                p4 = G.diameter()          
                print p4
                param.append("Diameter")
                param.append(p4)
        elif secom[i] == "5":
                print "\nDensity:"
                p5 = G.density()            
                print p5
                param.append("Density")
                param.append(p5)
        elif secom[i] == "6":
                print "\nCohesion:"
                p6 = G.cohesion()            
                print p6
                param.append("Cohesion")
                param.append(p6)
        elif secom[i] == "7":
                print("\nRadius:")
                p7 = nx.radius(nG)
                print p7
                param.append("Radius")
                param.append(p7)
    ###################################
        elif secom[i] == "11":
                print "\nBetweenness:"
                p11 = G.betweenness(directed=False, cutoff=16)            
                print p11
                param.append("Betweenness")
                param.append(p11)
        elif secom[i] == "12":
                print "\nPagerank:"
                p12 = G.pagerank()           
                print p12
                param.append("Pagerank")
                param.append(p12)
        elif secom[i] == "13":
                print "\nEigenVectorCentrality:"
                p13 = G.eigenvector_centrality()            
                print p13
                param.append("EigenVectorCentrality")
                param.append(p13)
        elif secom[i] == "14":
                print "\nAverage degree connectivity:"
                p14 = nx.average_degree_connectivity(nG)            
                print p14
                param.append("Average degree connectivity")
                param.append(p14)
        elif secom[i] == "15":
                print "\nPeriphery:"
                p15 = nx.periphery(nG)            
                print p15
                param.append("Periphery")
                param.append(p15)
        elif secom[i] == "16":
                print("\nEccentricity:")
                p16 = nx.eccentricity(nG)            
                print p16
                param.append("Eccentricity")
                param.append(p16)
        elif secom[i] == "17":
                print("\nCenter:")
                p17 = nx.center(nG)            
                print p17
                param.append("Center")
                param.append(p17)
        elif secom[i] == "18":
                print("\nDegree Distribution:")
                p18 = G.degree_distribution()    
                print p18
                param.append("Degree Distribution")
                param.append(p18)
        elif secom[i] == "19":
                print("\nTotal number of Motif:")
                p19 = G.motifs_randesu_no()
                print p19
                param.append("Total number of Motif")
                param.append(p19)
        elif secom[i] == "20":
                print("\nSimilarity Jaccard:")
                p20 = G.similarity_jaccard()
                print p20
                param.append("Similarity Jaccard")
                param.append(p20)

    #####Parametres exclosos#####
    #print "Assortativity meu:" # es el mateix que el degree?
    #print assortativitymeu(G)  
    #print("diameter: %d" % nx.diameter(nG))
    #print("density: %s" % nx.density(nG))
    #print("richclub coefficient: %s" % nx.rich_club_coefficient(nG.to_undirected()))
    #print("richclub coefficient: %s" % nx.rich_club_coefficient(nG))
    
    return param