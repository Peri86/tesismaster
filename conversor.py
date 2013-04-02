#!/usr/bin/env python
import io
import itertools
import glob
import sys

nom = []
numeron = []
coorde = []
traff = []
capac = []
costt = []


def guardaraarxiu(linia):
    fl.write(linia)
    return


def guardarpajek(numero,nom,coord,capa):
    fl = open("./conversor/"+nom+".net", "w")
    nums = str(numero).strip('[]').strip("'").split(" ")
    fl.write("*Vertices\t"+nums[0])
    
    ids = []
    #print coord
    i=1
    fl.write("\n")
    for a in coord:
        coos = str(a).strip('[]').strip("'").split(" ")
        idd = coos[2].strip()
        #print idd
        fl.write("\t"+str(i)+" \""+str(idd)+"\"\n")
        i+=1
    
    #USO LA CAPACITAT COM ELS EDGES DE LA XARXA
    #fl.write("*Arcs\n")
    fl.write("*Edges\n")
    for c in capa:
        cap = str(c).strip().split("=")
        #print "cap:"
        #print cap
        ##print "primer:"+cap[0]
        primer = int(cap[0])+1
        cap1 = cap[1].split(" ")
        #print "cap1:"
        #print cap1
        ##print "segon:"+cap1[1]
        segon = int(cap1[1])+1
        ##print "tercer:"+cap1[2]
        tercer = cap1[2]
        #print c[0].strip(),c[1],c[2]
        fl.write("\t"+str(primer)+"\t"+str(segon)+"\t"+str(tercer)+"\n")        
    
    fl.close()
    return

def guardargraphml(numero,nom,coo,capa):
    fl = open("./conversor/"+nom+".graphml", "w")
    fl.write("<?xml version="+"\""+"1.0"+"\""+" encoding="+"\""+"UTF-8"+"\""+"?>\n")
    fl.write("<graphml xmlns="+"\""+"http://graphml.graphdrawing.org/xmlns"+"\""+" xmlns:xsi="+"\""+"http://www.w3.org/2001/XMLSchema-instance"+"\""
                 +" xsi:schemaLocation="+"\""+"http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd"+"\""+">\n")    
    
    num = str(numero).strip('[]').strip("'").split(" ")
    fl.write("<graph id="+"\""+nom+"\""+" edgedefault="+"\""+"undirected"+"\""+">\n")
    
    for co in coo:
        coos = str(co).strip('[]').strip("'").split(" ")
        idd = coos[2].strip()
        fl.write("<node id="+"\""+idd+"\""+"/>\n")
    
    e=1
    for c in capa:
        cap = str(c).strip().split("=")    
        primer = int(cap[0])+1
        cap1 = cap[1].split(" ")    
        segon = int(cap1[1])+1
        tercer = cap1[2]
        fl.write("<edge id="+"\""+"E"+str(e)+"\""+" source="+"\""+"N"+str(primer)+"\""+" target="+"\""+"N"+str(segon)+"\""+"/>\n")
        e+=1
    
    fl.write("</graph>\n</graphml>")
    
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

#if __name__ == "__main__":
def main():
    print '\n\tConversor de formats'
    print '\tDe SGF a NET PAJEK o GRAPHML'
    print "Els arxius estan a la carpeta 'conversor'\n"
############################
    ruta = glob.glob('./conversor/*.*') #troba la ruta dels arxius que indiquem
        
    print "\nXarxes en format SGF disponibles:"
        
    llista = []
    
    for i in range(len(ruta)):
        stemp = ruta[i].split('/')
        semp = stemp[2].split('.')
        llista.append(semp)
        #print "[",i,"]", semp[0]
        #print " disponible en format: ", semp[1]
    
    conta = 1
    for y in range(len(llista)):
        if llista[y][1] == 'sgf':
            print '[',conta,']',llista[y][0]
            conta+=1 #per tal de que el numero de xarxa apareixi correcte
    
    if conta == 0:
        print "\nNo hi ha cap xarxa en format sgf disponible\n"
############################




    nomar = raw_input("Escriu el nom de l'arxiu SGF a llegir:\n")

    linia =[]
    try:
        with open ("./conversor/"+nomar+".sgf","r") as f:
            #read_data = f.read()
            lines = f.readlines()
            for line in lines:
                #print line
                linia.append(line)
            #linia.append(lines)
        f.close()
        
    except IOError:
        print 'Error. Arxiu no trobat'
        return
    else:
        print 'Arxiu carregat\n'    

    print("\nSelecciona els formats a convertir l'arxiu:\n")
    print("\t [1] NetPajek")
    print("\t [2] GraphML")
    print("\t [3] Tots")
    print("\t [4] Sortir")
    sel = raw_input("\nEscriu un dels numeros per seleccionar l'opcio\n")
    if sel == '1':
        guarxiu(linia)
        guardarpajek(numeron,nomar,coorde,capac)    
    elif sel == '2':
        guarxiu(linia)
        guardargraphml(numeron,nomar,coorde,capac)
    elif sel == '3':
        guarxiu(linia)
        guardarpajek(numeron,nomar,coorde,capac)
        guardargraphml(numeron,nomar,coorde,capac)
        print "\nConversio realitzada amb exit\n"
    elif sel == '4':
        sys.exit()
    else:
        print "\nError, has d'escriure un dels numeros mostrats\n"
