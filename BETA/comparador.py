#!/usr/bin/env python
#__author__ = """Pau Pericay Vendrell"""

##################### TO DO #####################
# Formats de arxius per cargar correctes [X]
# Posar nom a les finestres dels grafs 
# Arreclar errors - eigenvectornaive : eliminar??? [X]
# Afegir algorismes nous (MCL no acaba de funcionar)
# Mantenir la posicio per tots els grafs [/]
# Classificar algorismes [/] (afegir per net pajek i visualment)
# Implementar grafs direcionals o no direcionals[/]
# Modificar el menu per fer-lo mes agradable[/]
# Funcio per guardar el dibuix [/]
# Funcio per guardar les comunitats [/]
# Parametres a comparar entre els algorismes escollits a nivell general [X]
# Parametres a comparar entre els algorismes escollits a nivell de node [X]
# Comparar algorismes tinguent en compte els parametres resultants [/]
# Conversor amb python
# Comparador multiple[X]
# El lector del net pajek i graphml no funciona amb tots els arxius [/]
# El Gephi pot carregar els arxiu de xarxes pero no directament els de comunitats. El mes sembla es afegir atribut extra, nomes graphml.
# El grafic de finestra igraph del MCL no funciona
# Afegir comparador amb una particio com a referent [X]
# Treure llibreria networkx [/] (errors en la lectura de netpajek implementacions duplicades)

#Imports del programa
import conversor as cvs
import algorismes as alg
import parametres as para
import comunitats as comu
import gephi as ge
import fitxers as ft
######################################
#import Tkinter llibreria grafica

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

######################################
nom = ''
######################################

###############Funcio guardar comunitats#####################
def guardarcom(com):
    i=0
    while(i != len(com)):
        print "L'arxiu es guardara amb el nom "+com[i]+".Vol canviar el nom de l'arxiu?"
        sino = raw_input('si,no:\n')
        if sino == 'si':
            nom = raw_input("Escriu el nou nom de l'arxiu:\n")
        else:
            nom = com[i]
        
        arxiucom = open("./comunitats/"+nom+".txt","w")
        #for component in com[i+1]:
        #    print component
        #print com[i+1].membership
        arxiucom.write(str(com[i+1].membership))
        arxiucom.close()
        
        i+=2
    
    return
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
            print "\n [4] Obrir l'arxiu amb el Gephi\n"
            print "\n [5] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegit,nllegit)
            elif op == '2':
                com = alg.escollir(arllegit,nllegit)
                comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                ge.obrir(nom)#obrir el gephi amb l'arxiu cargat
            elif op == '5':
                sys.exit()
        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Guardar en fitxer les comunitats calculades\n"
            print "\n [5] Carregar una xarxa diferent\n"
            print "\n [6] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegit,nllegit)
            elif op == '2':
                com = alg.escollir(arllegit,nllegit)
            elif op == '3':
                comu.benchmark(arllegit,com) #afegir nllegit???
                #comu.comparador(com)
            elif op == '4':
                guardarcom(com)
            elif op == '5':
                main()
            elif op == '6':
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
            print "\n [4] Obrir l'arxiu amb el Gephi\n"
            print "\n [5] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegitnet,nllegitnet)
            elif op == '2':
                com = alg.escollir(arllegitnet,nllegitnet)
                comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                ge.obrirnet(nom)#obrir el gephi amb l'arxiu cargat
            elif op == '5':
                sys.exit()

        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Guardar en fitxer les comunitats calculades\n"
            print "\n [5] Carregar una xarxa diferent\n"
            print "\n [6] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                num = para.parametres(arllegitnet,nllegitnet)
            elif op == '2':
                num = alg.escollir(arllegitnet,nllegitnet)
            elif op == '3':
                comu.comparador(com)
            elif op == '4':
                guardarcom(com)
            elif op == '5':
                main()
            elif op == '6':
                sys.exit()

    
####################################
####################################
####################################
def main():
    print "\n\nPrograma per l'analisi de xarxes complexes i la deteccio de comunitats."
   
    #print glob.glob('./networks/*.*')
    ruta = glob.glob('./networks/*.*') #troba la ruta dels arxius que indiquem
        
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
        
    nb = raw_input("\nEscriu el nom de la xarxa a llegir o 'sortir' per tancar el programa\n")
    
    if nb == 'sortir':
        return
    
    global nom
    nom = nb #per passar-ho al gephi
    #print ('Xarxa %s' % (nb))
    print "\n"
    formats = list() #llista dels formats disponibles buida
    conex = False #inicialment no sabem si el nom es correcte 
    
    for o in range(len(ruta)):
        stemp = ruta[o].split('/')
        semp = stemp[2].split('.')
        if(semp[0] == nb): #comprovo si coincideix amb el nom de l'arxiu
            #print "catch"
            #print semp[1]
            formats.append(semp[1]) #afegeixo format a la llista
            conex = True #el nom coincideix
    if len(formats) > 1:
        print "Tria en quin format vols cargar l'arxiu.\n Formats disponibles: ",formats
        #print formats
        fm = raw_input("Escriu el nom del format escollit\n")
    elif conex == False: # si el nom no existeix
        print "Nom de arxiu incorrecte"
        main()
    else:
        fm = formats
        fm = fm[0] #converteixo de list a string
   
    ######  cargar el graf depenent del format de l'arxiu #####
    if fm == 'graphml':
        try:
            #print 'estic dins del graphml'
            arllegit = Graph.Read_GraphML("./networks/"+nb+".graphml") #llegit per igraph
            nllegit = nx.read_graphml("./networks/"+nb+".graphml") #llegit per networkx
            #ft.save_jsonfile()#######
            
            info = GraphSummary(arllegit)
            infor = info.__str__()
            if infor[7] == 'U':
                print "La xarxa carregada es indirecte"
            elif infor[7] == 'D':
                print "La xarxa carregada es directe"
            
        except IOError:
            print 'Error', arllegit
        else:
            print 'Arxiu carregat\n'
       
        
        menugraphml(arllegit,nllegit)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER GRAPHML###
        #num = escollir(arllegit,nllegit)
        #print num
      
    elif fm == 'net':
        try:
            #print 'estic dins del net'
            arllegitnet = Graph.Read_Pajek("./networks/"+nb+".net") #llegit per igraph
            nllegitnet = nx.read_pajek("./networks/"+nb+".net") #llegit per networkx
            info = GraphSummary(arllegitnet)
            infor = info.__str__()
            if infor[7] == 'U':
                print "La xarxa carregada es indirecte"
            elif infor[7] == 'D':
                print "La xarxa carregada es directe"

        except IOError:
            print 'Error', arllegitnet
        else:
           print 'Arxiu carregat\n'
        
        menunet(arllegitnet,nllegitnet)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER NET PAJEK###
        #num = escollir(arllegitnet,nllegitnet)
        #num =  netescollir(arllegitnet,nllegitnet)
        #print num
   
   #print 'estic al final'

if __name__ == "__main__":
    main()