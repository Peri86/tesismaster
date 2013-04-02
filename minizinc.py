#!/usr/bin/env python
from igraph import *

def escriuread(matriu):
    nom = 'prova'
    try:
        bet = Graph.edge_betweenness(matriu)
        print bet
        re = Graph.write_adjacency(matriu,"./minizinc/"+nom+".dzn")
    except IOError:
        print 'Error', re
    else:
        print 'ok\n'   
    return
