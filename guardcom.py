#!/usr/bin/env python
from igraph import *
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


def guardainfo(arllegit,com,algo,nome,param):
    #print arllegit
    #print com
    #print algo

    info = arllegit.__str__()
    
    nom = raw_input("Escriu el nou nom que tindra l'arxiu:\n")    
    arxiuinfo = open("./information/"+nom+".txt","w")
    arxiuinfo.write("Nom de la xarxa :"+nome+" \n\n")
    arxiuinfo.write(info)

    arxiuinfo.write("\n\nParametres calculats\n\n")
    
    i=0
    y=0
    while(i != len(param)):
        arxiuinfo.write(str(param[i])+"\n")        
        arxiuinfo.write(str(param[i+1])+"\n\n")
        i+=2

    i=0
    y=0
    while(i != len(com)):
        #print "Algorisme :",com[i]
        arxiuinfo.write("\n\nAlgorisme : ")
        arxiuinfo.write(com[i])        
        arxiuinfo.write("\nComunitats : ")
        arxiuinfo.write(str(com[i+1]))
        arxiuinfo.write("\nTemps d'execusio : ")
        arxiuinfo.write(str(algo[y+2]))
        arxiuinfo.write("\nModularitat : ")
        arxiuinfo.write(str(algo[y+3]))
        i+=2
        y+=4
    
    arxiuinfo.close()
    
    return