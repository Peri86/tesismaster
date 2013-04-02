#!/usr/bin/env python
from igraph import *

def convertir(arxiu):
    member = []
    coun=0
    for linies in arxiu:
        #print linies
        if coun >0:
            linia = linies.split('\n')
            #print linia
            member.append(int(linia[0]))
        coun+=1
    return member
