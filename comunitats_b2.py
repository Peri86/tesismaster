#!/usr/bin/env python
from igraph import *
import networkx as nx

import inspect
import itertools
import glob

def benchmark(xarxa,llistacomunitats):
    #Per tal de comparar les comunitats calculades ho tenim de fer a partir d'una 
    #particio de referencia o particio que es consideri com a real o "bona".
    #Com que no es pot fer de forma "automatica" farem que l'usuari determini quina es la referent
    print "\nEsculli la particio que s'utilitzara com a referent"
    print "o carregui la particio d'un arxiu que vulgui utilitzar com a referent\n"
    print '\nParticions disponibles dels algorismes calculats:'
    con=0
    i=0
    while(i != len(llistacomunitats)):
        print '[',i,']', llistacomunitats[i]
        i+=2
        con+=1
    
    referent = '' # string de l'algorisme referent
    
    ca = raw_input("\nEscriu el numero de l'algorisme o escriu 'arxiu' per carregar un arxiu dels disponibles:\n")
    if ca == 'arxiu':
        print "\nSeleccioni un dels arxius a carregar"
        print "S'ha de tenir en compte la xarxa actual carregada, no carregar una particio d'una altre xarxa\n"
        print "Els arxius es busquen a la carpeta anomenada 'comunitats':\n"
        
        ruta = glob.glob('./comunitats/*.*') #troba la ruta dels arxius que indiquem
            
        print "\nParticions disponibles a la carpeta comunitats:"
            
        llista = []
            
        for i in range(len(ruta)):
            stemp = ruta[i].split('/')
            #print stemp
            semp = stemp[2].split('.')
            #print semp
            print semp[0]
            llista.append(semp[0])
        conta = 1
        #for y in range(len(llista)):
        #    if llista[y][0]!=llista[y-1][0]:
        #        print '[',conta,']',llista[y][0]
        #        #print 'disponible en format: ',llista[y][1]
        #        conta+=1 #per tal de que el numero de xarxa apareixi correcte
        #    else:
        #        print '                      ',llista[y][1]
        #    
        nb = raw_input("\nEscriu el nom de la xarxa a llegir\n")
        linia =[]
        member = []
        with open ('./comunitats/'+nb+'.txt','r') as f:
            read_line = f.readline()
            #print read_line
            #lines = f.readlines()
            #for line in lines:
            #    linia.append(line)
            #linia.append(lines)
        f.close()
        #print read_line
        
        llista = eval(read_line) #aixo es el membership de la comunitat
        #print llista
        #novalist = [int(n) for n in read_line.split(',')]
        #print novalist
        
        #for i in range(len(linia)):
        #    if linia[i]!="[" or linia[i]!="]" or linia[i]!="'" or linia[i]!="," or linia[i]!=' ':
        #        member.append(linia[i])
        #
        #print member
        vc = VertexClustering(xarxa,llista)
        print vc
    
    elif ca == 'tornar':
        return
    elif(len(ca)!=1):
        print "S'ha d'escriure un numero dels algorismes o 'arxiu' per cargar un arxiu o 'tornar' per sortir al menu"
    else:
        referent = ca
    
    return

def comparador(llistacomunitats):
    print '\nEsculli dos algorismes dels de la llista per a realitzar la comparacio\n'
    print '\nAlgorismes disponibles:'
    con=0
    i=0
    while(i != len(llistacomunitats)):
        print '[',i,']', llistacomunitats[i]
        i+=2
        con+=1
    
    se = raw_input("\nIndiqui els dos algorismes amb els numeros que es corresponen separats per una coma:\nO escriu 'tornar' per tornar al menu principal\n")
    sel = se.split(',')
    
    if(len(sel)!=2):
        print '\nHas de seleccionar dos algorismes.\n'
    elif(len(sel)!=2 and se =='tornar'):
        return
    else:
        mesurador(sel,llistacomunitats)

    return

def mesurador(sel,llistacomunitats):
    print '\nEstem comparant la comunitat trobada amb',sel[0],' amb la',sel[1]
    print '\nEsculli la metrica que usar per realitzar la comparacio:\n'
    print '[1] Variation of information metric of Meila (2003)\n'
    #VI(X;Y)=H(X)+H(Y)-2I(X,Y) . H = entropy, I = mutual information.
    
    print '[2] Normalized mutual information as defined by Danon et al (2005)\n'
    #Funciona com un %
    
    print '[3] Split-join distance of van Dongen (2000)\n'
    #http://lists.gnu.org/archive/html/igraph-help/2010-07/msg00088.html
    #d(A,B) = 2n - Pa(B) - Pb(A
    #Performance Criteria for Graph Clustering and Markov Cluster Experiments (2000)
    
    #The split/join distance is easily interpretable as the number of
    #nodes that need changing to obtain one clustering from the other, and
    #fragmentation is in practice uncommon.    
    
    print '[4] Rand index of Rand (1971)\n'    
    #http://en.wikipedia.org/wiki/Rand_index
    #Paper no disponible gratis
    #The Rand index has a value between 0 and 1, with 0 indicating
    #that the two data clusters do not agree on any pair of points and 1 indicating that the data clusters are exactly the same.    
    
    print '[5] Adjusted Rand index of Hubert and Arabie (1985)\n'
    #http://en.wikipedia.org/wiki/Rand_index#Adjusted_Rand_index
    #ARI=(RI-E)/(1-E)
    #1 es el maxim de igual, 0 es totalment diferent
    #Paper no disponible gratis
    
    ce = raw_input('Escriu els numeros dels parametres que vulguis amb una coma entre mig:\n')
    cel = ce.split(',')
    
    n0 = int(sel[0])
    n1 = int(sel[1])    
    
    for y in range(len(cel)):
        if cel[y] == "1":
            print '\n\tVariation of information metric of Meila :'
            print compare_communities(llistacomunitats[n0+1],llistacomunitats[n1+1],)
        if cel[y] == "2":
            print '\n\tNormalized mutual information as defined by Danon et al :'
            print compare_communities(llistacomunitats[n0+1],llistacomunitats[n1+1],"dannon")            
        if cel[y] == "3":
            print '\n\tSplit-join distance of van Dongen :'
            print compare_communities(llistacomunitats[n0+1],llistacomunitats[n1+1],"split-join")
        if cel[y] == "4":
            print '\n\tIndex of Rand :'
            print compare_communities(llistacomunitats[n0+1],llistacomunitats[n1+1],"rand")
        if cel[y] == "5":
            print '\n\tAdjusted Rand index of Hubert and Arabie :'
            print compare_communities(llistacomunitats[n0+1],llistacomunitats[n1+1],"adjusted_rand")    
    
    
    return
