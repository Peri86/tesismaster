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
# Conversor amb python [X]
# Comparador multiple[X]
# El lector del net pajek i graphml no funciona amb tots els arxius [/]
# El Gephi pot carregar els arxiu de xarxes pero no directament els de comunitats. El mes sembla es afegir atribut extra, nomes graphml.[X]
# El grafic de finestra igraph del MCL no funciona [/] De moment esta eliminat
# Afegir comparador amb una particio com a referent [X]
# Treure llibreria networkx [/] (errors en la lectura de netpajek implementacions duplicades)
# Amb linux les xarxes per llegir surten esparades del format [X]
# Similarity Jacardd mostra matriu similitud?
# Afegir Commfind esta en C 
# Afegir CFinder fent servir el command_linemac [/]
# Opcio veure grafs amb svg [X]
# Canviar el layout del plot [/] He adaptat les mides millor
# Guardar format de comunitats per com es veuen per consola [/]
# mirar perque infomap no troba comunitats be amb grafs de 1000 nodes, tambe falla amb menys
# Adjuntar conversor amb comparador [X]
# Veure utilitat de parametres [/]
# Canviar nom per defecte a l'hora de guardar comunitat a xarxa+algorisme i canviar format .txt a .com?
# Afegir temps que tarden els algorismes per la comparativa [X]
# Posar opcio de mostar numero de nodes o membership de comunitats en els dibuixos? [/]
# Opcio de parametres per els algorismes [/]
# Implementar Algorisme Jerarca nomes per linux o windows
# Falla al comparar les comunitats [/]
# Afegir opcio de nodes amb numero de posicio o de comunitat al dibuixar-les.
#
# Algorisme de R Guimera i Amaral, netcarto.
# Amb linux he pogut compilar el netcarto, si s'ha de agregar al programa hi ha el netcarto_cl
#
# Comprovar que les comunitats mostrades amb el gephi (graphml) i les de l'arxiu netpajek son iguals
# Gephi de linux no visualitza les xarxes
# Afegir paramatres per l'arxiu de informacio
# Buscar possibles problemes de inputs
# Arreclar guardarinfo (afegir opcio de que em guardi nomes les variables que em passa)
# En xarxes directes (nomes????) dona errors al calcular paramtres com el Radius i Periphery
# En indirectes el Cohesion tarda molt o no acaba
# Afegir OSLOM
# Possiblitat d'afegir la variacio de la Mesura de MI anomenada "mutual3" (esta a la carpeta de baixades)
# A l'hora de mostrar les etiquetes dels benchmarks la primera no em surt be.
# (PRIORITARI) Implementar algorismes amb pesos i tot amb pesos [\]
# Incloure ms,min o seg als informes.
# Error a portein_ al tornar a tirar algorismes???

#Imports del programa
import conversor as cvs
import algorismes as alg
import parametres as para
import comunitats as comu
import gephi as ge
import fitxers as ft
import minizinc as mz
import guardcom as gdc
import conversor as con
######################################
#import Tkinter #llibreria grafica

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
#def guardarcom(com):
#    i=0
#    while(i != len(com)):
#        print "L'arxiu es guardara amb el nom "+com[i]+".Vol canviar el nom de l'arxiu?"
#        sino = raw_input('si,no:\n')
#        if sino == 'si':
#            nom = raw_input("Escriu el nou nom de l'arxiu:\n")
#        else:
#            nom = com[i]
#        
#        arxiucom = open("./comunitats/"+nom+".txt","w")
#        #for component in com[i+1]:
#        #    print component
#        #print com[i+1].membership
#        arxiucom.write(str(com[i+1].membership))
#        arxiucom.close()
#        
#        i+=2
#    
#    return
######################################

def menugraphml(arllegit,nllegit,pes):
    sortida = False
    comunitats = False
    com = []
    param = []
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
                param = para.parametres(arllegit,nllegit)
            elif op == '2':
                com,algo = alg.escollir(arllegit,nllegit,nom,pes)
                if com: # si he trobat alguna comunitat que es vegi el menu extes
                    comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                ge.obrir(nom)#obrir el gephi amb l'arxiu cargat
            elif op == '5':
                #mz.escriuread(arllegit) ######################## minizinc
                sys.exit()
            else:
                print "Parametre incorrecte, escriu un dels nombres disponibles"
        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Guardar en fitxer les comunitats calculades\n"
            print "\n [5] Guardar les comunitats amb graphml i obrir-les amb el Gephi\n"
            print "\n [6] Guardar la infomacio dels procediments\n"
            print "\n [7] Carregar una xarxa diferent\n"
            print "\n [8] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                param = para.parametres(arllegit,nllegit)
            elif op == '2':
                com,algo = alg.escollir(arllegit,nllegit,nom,pes)
            elif op == '3':
                compa = comu.benchmark(arllegit,com) #afegir nllegit???
            elif op == '4':
                gdc.guardarcom(com)
            elif op == '5':
                ge.escriuregraf(arllegit,com)
            elif op == '6':
                gdc.guardainfo(arllegit,com,algo,nom,param)
            elif op == '7':
                main()
            elif op == '8':
                sys.exit()
            else:
                print "Parametre incorrecte, escriu un dels nombres disponibles"
 ####################################################################

def menunet(arllegitnet,nllegitnet,pes):
    sortida = False
    comunitats = False
    com = []
    compa = []
    param = []
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
                param = para.parametres(arllegitnet,nllegitnet)
            elif op == '2':
                com,algo = alg.netescollir(arllegitnet,nllegitnet,nom,pes)
                if com:
                    comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                ge.obrirnet(nom)#obrir el gephi amb l'arxiu cargat
            elif op == '5':
                sys.exit()
            else:
                print "Parametre incorrecte, escriu un dels nombres disponibles"

        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Guardar en fitxer les comunitats calculades\n"
            print "\n [5] Guardar les comunitats amb graphml i obrir-les amb el Gephi\n"
            print "\n [6] Guardar la infomacio dels procediments\n"
            print "\n [7] Carregar una xarxa diferent\n"
            print "\n [8] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                param = para.parametres(arllegitnet,nllegitnet)
            elif op == '2':
                com,algo = alg.netescollir(arllegitnet,nllegitnet,nom,pes)
            elif op == '3':
                compa = comu.benchmark(arllegitnet,com)
            elif op == '4':
                gdc.guardarcom(com)
            elif op == '5':
                ge.escriuregraf(arllegitnet,com)
            elif op == '6':
                gdc.guardainfo(arllegitnet,com,algo,nom,param)
            elif op == '7':
                main()
            elif op == '8':
                sys.exit()
            else:
                print "Parametre incorrecte, escriu un dels nombres disponibles"
 ####################################################################

def menugml(arllegitgml,nllegitgml,pes):
    sortida = False
    comunitats = False
    com = []
    compa = []
    param = []    
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
                param = para.parametres(arllegitgml,nllegitgml)
            elif op == '2':
                com,algo = alg.netescollir(arllegitgml,nllegitgml,nom,pes)
                if com:
                    comunitats = True #Tinc comunitats disponibles
            elif op == '3':
                main()
            elif op == '4':
                ge.obrir(nom)#obrir el gephi amb l'arxiu cargat
            elif op == '5':
                sys.exit()
            else:
                print "Parametre incorrecte, escriu un dels nombres disponibles"

        else:
            print '\n Escull una de les opcions:'
            print "\n [1] Calcular parametres de la xarxa\n"
            print "\n [2] Aplicar algorisme de deteccio de comunitats\n"
            print "\n [3] Comparar les comunitats calculades\n"
            print "\n [4] Guardar en fitxer les comunitats calculades\n"
            print "\n [5] Guardar les comunitats amb graphml i obrir-les amb el Gephi\n"
            print "\n [6] Guardar la infomacio dels procediments\n"
            print "\n [7] Carregar una xarxa diferent\n"
            print "\n [8] Sortir del programa\n"
            
            op = raw_input("Escriu el numero de la opcio: \n")
            
            if op == '1':
                param = para.parametres(arllegitgml,nllegitgml)
            elif op == '2':
                com,algo = alg.escollir(arllegitgml,nllegitgml,nom,pes)
            elif op == '3':
                compa = comu.benchmark(arllegitgml,com)
            elif op == '4':
                gdc.guardarcom(com)
            elif op == '5':
                ge.escriuregraf(arllegitgml,com)
            elif op == '6':
                gdc.guardainfo(arllegitgml,com,algo,nom,param)
            elif op == '7':
                main()
            elif op == '8':
                sys.exit()
            else:
                print "Parametre incorrecte, escriu un dels nombres disponibles"

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
        llista.sort() #Afegit per linux, ja que no ordena la llista per defecte
    conta = 1
    for y in range(len(llista)):
        if llista[y][0]!=llista[y-1][0]:
            print '[',conta,']',llista[y][0]
            print 'disponible en format: ',llista[y][1]
            conta+=1 #per tal de que el numero de xarxa apareixi correcte
        else:
            print '                      ',llista[y][1]
        
    nb = raw_input("\nEscriu el nom de la xarxa a llegir, 'conversor' per entrar al conversor o 'sortir' per tancar el programa\n")

    if nb == 'sortir':
        sys.exit()

    elif nb == 'conversor':
        con.main()
        main()
    
    global nom
    nom = nb #per passar-ho al gephi
    #print ('Xarxa %s' % (nb))
    print "\n"
    formats = list() #llista dels formats disponibles buida
    conex = False #inicialment no sabem si el nom es correcte 
    pes = False # Variable per saber si la xarxa es amb pesos o sense
    
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
            if infor[7] == 'U' and infor[9] == '-':
                print "La xarxa carregada es indirecte i sense pesos"
            elif infor[7] == 'D' and infor[9] == '-':
                print "La xarxa carregada es directe i sense pesos"
            elif infor[7] == 'U' and infor[9] == 'W':
                print "La xarxa carregada es indirecte i amb pesos"
                pes = True
            elif infor[7] == 'D' and infor[9] == 'W':
                print "La xarxa carregada es directe i amb pesos"
                pes = True
            
        except IOError:
            print 'Error', arllegit
        else:
            print 'Arxiu carregat\n'
       
        
        menugraphml(arllegit,nllegit,pes)
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
            #de moment aquesta opcio de amb o sense pesos nomes esta implementada aqui
            if infor[7] == 'U' and infor[9] == '-':
                print "La xarxa carregada es indirecte i sense pesos"
            elif infor[7] == 'D' and infor[9] == '-':
                print "La xarxa carregada es directe i sense pesos"
            elif infor[7] == 'U' and infor[9] == 'W':
                print "La xarxa carregada es indirecte i amb pesos"
                pes = True
            elif infor[7] == 'D' and infor[9] == 'W':
                print "La xarxa carregada es directe i amb pesos"
                pes = True


        except IOError:
            print 'Error', arllegitnet
        else:
           print 'Arxiu carregat\n'
        
        menunet(arllegitnet,nllegitnet,pes)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER NET PAJEK###
        #num = escollir(arllegitnet,nllegitnet)
        #num =  netescollir(arllegitnet,nllegitnet)
        #print num
   
    elif fm == 'gml':
        try:
            #print 'estic dins del graphml'
            arllegitgml = Graph.Read_GML("./networks/"+nb+".gml") #llegit per igraph
            nllegitgml = nx.read_gml("./networks/"+nb+".gml") #llegit per networkx
            
            info = GraphSummary(arllegitgml)
            infor = info.__str__()
            if infor[7] == 'U' and infor[9] == '-':
                print "La xarxa carregada es indirecte i sense pesos"
            elif infor[7] == 'D' and infor[9] == '-':
                print "La xarxa carregada es directe i sense pesos"
            elif infor[7] == 'U' and infor[9] == 'W':
                print "La xarxa carregada es indirecte i amb pesos"
                pes = True
            elif infor[7] == 'D' and infor[9] == 'W':
                print "La xarxa carregada es directe i amb pesos"
                pes = True
            
        except IOError:
            print 'Error', arllegitgml
        else:
            print 'Arxiu carregat\n'
       
        
        menugml(arllegitgml,nllegitgml,pes)
        ####CRIDO FUNCIO DE ESCOLLIR L'ALGORISME PER GRAPHML###
        #num = escollir(arllegit,nllegit)
        #print num

    else:
        print "El format especificat no existeix\n"
        main()
   #print 'estic al final'

if __name__ == "__main__":
    main()