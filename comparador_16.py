#!/usr/bin/env python
#__author__ = """Pau Pericay Vendrell"""

##################### TO DO #####################
# Formats de arxius per cargar correctes [X]
# Posar nom a les finestres dels grafs
# Arreclar errors - eigenvectornaive
# Afegir algorismes nous
# Mantenir la posicio per tots els grafs [/]
# Classificar algorismes [X]
# Implementar grafs direcionals o no direcionals[/]
# Modificar el menu per fer-lo mes agradable[/]
# Funcio per guardar el dibuix
# Funcio per guardar les comunitats
# Parametres a comparar entre els algorismes escollits a nivell general [X]
# Parametres a comparar entre els algorismes escollits a nivell de node [X]
# Comparar algorismes tinguent en compte els parametres resultants
# Conversor amb python
# Comparador multiple[X]
# El lector del net pajek i graphml no funciona amb tots els arxius [/]
# El Gephi pot carregar els arxiu de xarxes pero no directament els de comunitats. El mes sembla es afegir atribut extra, nomes graphml.

#Imports del programa
import conversor as cvs
import algorismes as alg
import parametres as para
import comunitats as comu
import gephi as ge
######################################
#import Tkinter llibreria grafica

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

######################################
nom = ''
######################################

def menugraphml(arllegit,nllegit):
    sortida = False
    comunitats = False
    com = []
    while(sortida != True):
        if comunitats == False:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Carregar una xarxa diferent\n"
            print "\n [4] Sortir del programa\n"
            print "\n [5] Obrir l'arxiu amb el Gephi NOMES PER GRAPHML\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegit,nllegit)
            elif op == '2':
                com = alg.escollir(arllegit,nllegit)
                comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                sys.exit()
            elif op == '5':
                ge.obrir(nom)#obrir el gephi amb l'arxiu cargat
        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Carregar una xarxa diferent\n"
            print "\n [5] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegit,nllegit)
            elif op == '2':
                num = alg.escollir(arllegit,nllegit)
            elif op == '3':
                comu.comparador(com)
            elif op == '4':
                main()
            elif op == '5':
                sys.exit()

####################################################################

def menunet(arllegitnet,nllegitnet):
    sortida = False
    comunitats = False
    com = []
    while(sortida != True):
        if comunitats == False:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Carregar una xarxa diferent\n"
            print "\n [4] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegitnet,nllegitnet)
            elif op == '2':
                com = alg.escollir(arllegitnet,nllegitnet)
                comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                sys.exit()
        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Carregar una xarxa diferent\n"
            print "\n [5] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegitnet,nllegitnet)
            elif op == '2':
                num = alg.escollir(arllegitnet,nllegitnet)
            elif op == '3':
                comu.comparador(com)
            elif op == '4':
                main()
            elif op == '5':
                sys.exit()

    
####################################
####################################
####################################
def main():
    print "\n\nPrograma per l'analisi de xarxes complexes i la deteccio de comunitats."
   
    #print glob.glob('./networks/*.*')
    ruta = glob.glob('./networks/*.*') #troba la ruta dels arxius que idiquem
        
    print "\nXarxes disponibles a la carpeta networks:"
        
    llista = []
        
    for i in range(len(ruta)):
        stemp = ruta[i].split('/')
        semp = stemp[2].split('.')
        llista.append(semp)
        #print "[",i,"]", semp[0]
        #print " disponible en format: ", semp[1]
    conta = 1
    for y in range(len(llista)):
        if llista[y][0]!=llista[y-1][0]:
            print '[',conta,']',llista[y][0]
            print 'disponible en format: ',llista[y][1]
            conta+=1 #per tal de que el numero de xarxa apareixi correcte
        else:
            print '                      ',llista[y][1]
        
    nb = raw_input("\nEscriu el nom de la xarxa a llegir\n")
    global nom
    nom = nb #per passar-ho al gephi
    #print ('Xarxa %s' % (nb))
    print "\n"
    formats = list() #llista dels formats disponibles buida
    
    for o in range(len(ruta)):
        stemp = ruta[o].split('/')
        semp = stemp[2].split('.')
        if(semp[0] == nb): #comprovo si coincideix amb el nom de l'arxiu
            #print "catch"
            #print semp[1]
            formats.append(semp[1]) #afegeixo format a la llista   
    if len(formats) > 1:
        print "Tria en quin format vols cargar l'arxiu.\n Formats disponibles:"
        print formats
        fm = raw_input("Escriu el nom del format escollit\n")
    else:
        fm = formats
        fm = fm[0] #converteixo de list a string
   
    ######  cargar el graf depenent del format de l'arxiu #####
    if fm == 'graphml':
        try:
            #print 'estic dins del graphml'
            arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml") #llegit per igraph
            nllegit = nx.read_graphml("./networks/"+nb+".graphml") #llegit per networkx
        except IOError:
            print 'Error', arllegit
        else:
            print 'ok\n'
       
        
        menugraphml(arllegit,nllegit)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER GRAPHML###
        #num = escollir(arllegit,nllegit)
        #print num
      
    elif fm == 'net':
        try:
            #print 'estic dins del net'
            arllegitnet = Graph.Read_Pajek("./networks/"+nb+".net") #llegit per igraph
            nllegitnet = nx.read_pajek("./networks/"+nb+".net") #llegit per networkx
        except IOError:
            print 'Error', arllegitnet
        else:
           print 'ok\n'
        
        menunet(arllegitnet,nllegitnet)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER NET PAJEK###
        #num = escollir(arllegitnet,nllegitnet)
        #num =  netescollir(arllegitnet,nllegitnet)
        #print num
   
   #print 'estic al final'

if __name__ == "__main__":
    main()