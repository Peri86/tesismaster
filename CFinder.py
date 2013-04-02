#!/usr/bin/env python
import re
from igraph import *

def convertir(filex,nume):
    #print filex
    lines = filex.readlines()
    linia = []
    ix = 0
    
    for line in lines:
        if ix >= 7:
            line = line[:-2]
            re.split(r'(\D)',line)
            linia.append(line)
       #print line
        ix+=1
    print linia

    num=0
    conta=0
    
    #member=[]
    member = [0]*nume
    
    for line in linia:
        num=line[0]
        line = line[3:]

        for un in line.split(' '):
            try:
                #print 'un : '
                #print un
                member.pop(int(un)) #eliminio el zero per posar-hi el nou element
                member.insert(int(un),int(num)+1) # + 1 per evitar la comunitat 0 que es la que no s'ha trobat res
                conta+=1
            except ValueError:
                pass
    
    #print 'mida de la membership: '
    #print len(member)
    #contt = 0
    #if member is None: #Si no he trobat cap comunitat ho empleno amb zeros
    #    zero = 0
    #    [member for zero in xrange(nume)]
    #else:
    #    while(contt != nume):
    #        print 'contt : '
    #        print contt
    #        
    #        if member[contt] is None:
    #            member.insert(contt,0)
    #            print 'estaba buit'
    #        
    #        print 'member[contt] : '
    #        print member[contt]
    #        #if member[contt]:
    #        #    print 'Found element!'
    #        #else:
    #        #    member[contt]=0
    #        #    print 'Empty element.'
    #        
    #        contt+=1
    print "\nCal tenir en compte que la comunitat 0 s'utilitza per agrupar els nodes que no han estat assignats a cap comunitat\n"
    print member
    
    return member