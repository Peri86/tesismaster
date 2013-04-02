#!/usr/bin/env python
from igraph import *
import networkx as nx

def comparador(llistacomunitats):

    numero = len(llistacomunitats)/2
    #numero = len(llistacomunitats)
    #print 'Estem comparant la comunitat trobada amb',llistacomunitats[0],' amb la',llistacomunitats[2]
    print 'llistacomunitat/2:'
    print numero
    print 'elevat:'
    print numero**2
    Tn = (((numero)**2)/2)-(numero/2)
    print 'Tn:'
    print Tn
    #for i in range(len(llistacomunitats)-1):
    for i in range(Tn):
        if i%2 ==0:
            if i == len(llistacomunitats)-2:
                print '\nEstem comparant la comunitat trobada amb',llistacomunitats[i],' amb la',llistacomunitats[0]
                
                print '\nEsculli la metrica que usar per realitzar la comparacio:\n'
                print '[1] Variation of information metric of Meila (2003)\n'
                print '[2] Normalized mutual information as defined by Danon et al (2005)\n'
                print '[3] Split-join distance of van Dongen (2000)\n'
                print '[4] Rand index of Rand (1971)\n'    
                print '[5] Adjusted Rand index of Hubert and Arabie (1985)\n'
                
                se = raw_input('Escriu els numeros dels parametres que vulguis amb una coma entre mig:\n')
                sel = se.split(',')
                
                for y in range(len(sel)):
                    if sel[y] == "1":
                        print '\n\tVariation of information metric of Meila :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[1],)
                    if sel[y] == "2":
                        print '\n\tNormalized mutual information as defined by Danon et al :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[1],"dannon")            
                    if sel[y] == "3":
                        print '\n\tSplit-join distance of van Dongen :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[1],"split-join")
                    if sel[y] == "4":
                        print '\n\tIndex of Rand :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[1],"rand")
                    if sel[y] == "5":
                        print '\n\tAdjusted Rand index of Hubert and Arabie :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[1],"adjusted_rand")
            else:    
                print '\nEstem comparant la comunitat trobada amb',llistacomunitats[i],' amb la',llistacomunitats[i+2]
                
                print '\nEsculli la metrica que usar per realitzar la comparacio:\n'
                print '[1] Variation of information metric of Meila (2003)\n'
                print '[2] Normalized mutual information as defined by Danon et al (2005)\n'
                print '[3] Split-join distance of van Dongen (2000)\n'
                print '[4] Rand index of Rand (1971)\n'    
                print '[5] Adjusted Rand index of Hubert and Arabie (1985)\n'
                
                se = raw_input('Escriu els numeros dels parametres que vulguis amb una coma entre mig:\n')
                sel = se.split(',')
                
                for y in range(len(sel)):
                    if sel[y] == "1":
                        print '\n\tVariation of information metric of Meila :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[i+3],)
                    if sel[y] == "2":
                        print '\n\tNormalized mutual information as defined by Danon et al :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[i+3],"dannon")            
                    if sel[y] == "3":
                        print '\n\tSplit-join distance of van Dongen :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[i+3],"split-join")
                    if sel[y] == "4":
                        print '\n\tIndex of Rand :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[i+3],"rand")
                    if sel[y] == "5":
                        print '\n\tAdjusted Rand index of Hubert and Arabie :'
                        print compare_communities(llistacomunitats[i+1],llistacomunitats[i+3],"adjusted_rand")

    #print compare_communities(llistacomunitats[0],llistacomunitats[1])
    #
    #print '\nEsculli la metrica que usar per realitzar la comparacio:\n'
    #print '[1] Variation of information metric of Meila (2003)\n'
    #print '[2] Normalized mutual information as defined by Danon et al (2005)\n'
    #print '[3] Split-join distance of van Dongen (2000)\n'
    #print '[4] Rand index of Rand (1971)\n'    
    #print '[5] Adjusted Rand index of Hubert and Arabie (1985)\n'
    #
    
    
    return
