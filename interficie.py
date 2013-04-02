#!/usr/bin/env python

#Imports del programa
import conversor as cvs
import algorismes as alg
import parametres as para
import comunitats as comu
import gephi as ge
import fitxers as ft
######################################
from Tkinter import *
from tkFileDialog import askopenfilename

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
    
    if comunitats == False:
        def parametres():
            num = para.parametres(arllegit,nllegit)
        def algorisme():
            com = alg.escollir(arllegit,nllegit)
            comunitats = True #Tinc comunitats disponibles
        def carregar():
            main()
        def gephi():
            ge.obrir(nom)#obrir el gephi amb l'arxiu cargat
        def sortir():
            sys.exit()
        
        # create a toplevel menu
        menubar = Menu(root)
        menubar.add_command(label="Calcular parametres de la xarxa", command=parametres)
        menubar.add_command(label="Aplicar algorisme de deteccio de comunitats", command=algorisme)    
        menubar.add_command(label="Carregar una xarxa diferent", command=carregar)
        menubar.add_command(label="Obrir l'arxiu amb el Gephi", command=gephi)
        menubar.add_command(label="Sortir del programa", command=sortir)
        # display the menu
        root.config(menu=menubar)       
    else:
        def parametres():
            num = para.parametres(arllegit,nllegit)
        def algorisme():
            com = alg.escollir(arllegit,nllegit)
            comunitats = True #Tinc comunitats disponibles
        def comparar():
            comu.benchmark(arllegit,com) #afegir nllegit???
        def guardarc():
            guardarcom(com)
        def carregar():
            main()
        def gephicom():
            ge.escriuregraf(arllegit,com)
        def sortir():
            sys.exit()
        
        # create a toplevel menu
        menubar = Menu(root)
        menubar.add_command(label="Calcular parametres de la xarxa", command=parametres)
        menubar.add_command(label="Aplicar algorisme de deteccio de comunitats", command=algorisme)    
        menubar.add_command(label="Comparar les comunitats calculades", command=comparar)
        menubar.add_command(label="Guardar en fitxer les comunitats calculades", command=guardarc)
        menubar.add_command(label="Carregar una xarxa diferent", command=carregar)
        menubar.add_command(label="Guardar les comunitats amb graphml i obrir-les amb el Gephi", command=gephicom)
        menubar.add_command(label="Sortir del programa", command=sortir)
        # display the menu
        root.config(menu=menubar)

#def menugraphml(arllegit,nllegit):
#    sortida = False
#    comunitats = False
#    com = []
#    while(sortida != True):
#        if comunitats == False:
#            print '\n Escull una de les opcions:'
#            print "\n [1] Calcular parametres de la xarxa\n"
#            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
#            print "\n [3] Carregar una xarxa diferent\n"
#            print "\n [4] Obrir l'arxiu amb el Gephi\n"
#            print "\n [5] Sortir del programa\n"
#            
#            op = raw_input("Escriu el numero de la opcio: \n")
#            
#            if op == '1':
#                num = para.parametres(arllegit,nllegit)
#            elif op == '2':
#                com = alg.escollir(arllegit,nllegit)
#                comunitats = True #Tinc comunitats disponibles
#            elif op == '3':
#                main()
#            elif op == '4':
#                ge.obrir(nom)#obrir el gephi amb l'arxiu cargat
#            elif op == '5':
#                sys.exit()
#        else:
#            print '\n Escull una de les opcions:'
#            print "\n [1] Calcular parametres de la xarxa\n"
#            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
#            print "\n [3] Comparar les comunitats calculades\n"
#            print "\n [4] Guardar en fitxer les comunitats calculades\n"
#            print "\n [5] Guardar les comunitats amb graphml i obrir-les amb el Gephi\n"
#            print "\n [6] Carregar una xarxa diferent\n"
#            print "\n [7] Sortir del programa\n"
#            
#            op = raw_input("Escriu el numero de la opcio: \n")
#            
#            if op == '1':
#                num = para.parametres(arllegit,nllegit)
#            elif op == '2':
#                com = alg.escollir(arllegit,nllegit)
#            elif op == '3':
#                comu.benchmark(arllegit,com) #afegir nllegit???
#                #comu.comparador(com)
#            elif op == '4':
#                guardarcom(com)
#            elif op == '5':
#                ge.escriuregraf(arllegit,com)
#            elif op == '6':
#                main()
#            elif op == '7':
#                sys.exit()               
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
    #root = Tk()
    
    #print glob.glob('./networks/*.*')
    ruta = glob.glob('./networks/*.*') #troba la ruta dels arxius que indiquem
        
    print "\nXarxes disponibles a la carpeta networks:"
        
    llista = []
    filename = askopenfilename(initialdir=("./networks/"))
    #print filename
    ftemp = filename.split('/')
    #print ftemp
    ful = ftemp[-1]
    #print ful

    nb = ful.split('.')
    ######  cargar el graf depenent del format de l'arxiu #####
    if nb[1] == 'graphml':
        try:
            #print 'estic dins del graphml'
            arllegit = Graph.Read_GraphML("./networks/"+nb[0]+".graphml") #llegit per igraph
            nllegit = nx.read_graphml("./networks/"+nb[0]+".graphml") #llegit per networkx
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
      
    elif nb[1] == 'net':
        try:
            #print 'estic dins del net'
            arllegitnet = Graph.Read_Pajek("./networks/"+nb[0]+".net") #llegit per igraph
            nllegitnet = nx.read_pajek("./networks/"+nb[0]+".net") #llegit per networkx
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
   
   #print 'estic al final'

if __name__ == "__main__":
    root = Tk()
    main()
    root.mainloop()