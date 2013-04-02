#!/usr/bin/env python
import io
import itertools

nom = []
numeron = []
coorde = []
traff = []
capac = []
costt = []


def guardaraarxiu(linia):
    fl.write(linia)
    return


def guardarpajek(numero,coord):
    fl = open("arxiu.net", "w")
    nums = str(numero).strip('[]').strip("'").split(" ")
    fl.write("*Vertices\t"+nums[0])
    print coord
    for a in coord:
        print coord[a]
    coos = str(coord).strip('[]').strip("'").split(" ")
    print coos
    fl.close()
    return

def guardargraphml():
    fl = open("arxiu.graphml", "w")
    fl.close()
    return

def guarxiu (linia):
    ################
    actguar = False #boolea per saber quant tinc de guardar 
    
    netname = "[netname]"
    nodenum = "[nodenum]"
    coordinates = "[coordinates]"
    capacity = "[capacity]"
    traffic = "[traffic]"
    cost = "[cost]"
    
    infosgf = []
    #coorde = []
    #traff = []
    #capac = []
    #costt = []
    ################
    for i in range(len(linia)):
        #print linia[i]
        if actguar == False:
            if netname in linia[i]:
                actguar = True
                part = netname
            if nodenum in linia[i]:
                actguar = True
                part = nodenum
            if coordinates in linia[i]:
                actguar = True
                part = coordinates
            if traffic in linia[i]:
                actguar = True
                part = traffic
            if capacity in linia[i]:
                actguar = True
                part = capacity
            if cost in linia[i]:
                actguar = True
                part = cost
        else:
            tros = linia[i]
            if tros.isspace():
                actguar = False
            elif part == netname:
                nom.append(tros)
            elif part == nodenum:
                numeron.append(tros)
            elif part == coordinates:
                coorde.append(tros)
            elif part == traffic:
                traff.append(tros)
            elif part == capacity:
                capac.append(tros)
            elif part == cost:
                costt.append(tros)
    
    #print numeron,costt
    
    return

if __name__ == "__main__":
    print 'Conversor de formats'
    print 'De SGF a NET PAJEK o GRAPHML'

    nomar = raw_input("Escriu el nom de l'arxiu SGF a llegir:\n")

    linia =[]
    
    with open (nomar+'.sgf','r') as f:
        #read_data = f.read()
        lines = f.readlines()
        for line in lines:
            #print line
            linia.append(line)
        #linia.append(lines)
    f.close()
    
    guarxiu(linia)
    #print numeron,coorde
    guardarpajek(numeron,coorde)