#!/usr/bin/env python
#Per forcar el python a 32bits: defaults write com.apple.versioner.python Prefer-32-Bit -bool yes

from igraph import *
import networkx as nx
#import community as cp
#import community_jolleycraig as cj

import glob
import cairo as cai
import matplotlib.pyplot as plt
import graph as gra
#from nodebox import *

from pprint import pprint
import inspect
import io

import itertools

############Funcio guardar graf################
def guardargraf(pos,layout,com):
    nom = raw_input('Escriu el nom del graf:')
    plot(com,nom+".pdf",vertex_label=pos,layout=layout)
    return
############Funcio dibuixar################
def dibuixar(pos,layout,com,num):
    #surface = cai.ImageSurface().create_from_png('prova.png')
    #nom = 'hola.png'
    #plot(com,target=nom,vertex_label=pos,layout=layout)
    if num < 100:
        plot(com,vertex_label=pos,layout=layout)
    elif 101 < num < 500:
        plot(com,vertex_label=pos,bbox=(0, 0, 1500, 1500),layout=layout)
    elif 1000 < num:
        plot(com,vertex_label=pos,bbox=(0, 0, 3500, 3500),layout=layout)
    return 

############Funcio dibuixar networkx################
def nxdibuixar(G1,pos,p):
    #pos = nx.spring_layout(G1)
    dmin=1
    ncenter=0
    for n in pos:
        x,y=pos[n]
        d=(x-0.5)**2+(y-0.5)**2
        if d<dmin:
            ncenter=n
            dmin=d
    
    
    plt.figure(figsize=(8,8))
    nx.draw_networkx_edges(G1,pos,nodelist=[ncenter],alpha=0.4)
    nx.draw_networkx_nodes(G1,pos,nodelist=p.keys(),
                           node_size=80,
                           node_color=p.values(),
                           cmap=plt.cm.Reds_r)
    
    
    nx.draw_networkx_labels(G1,pos)
    
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    plt.axis('off')
    plt.savefig('prova.png')
    plt.show()
    return 
###################################################
def dibuixargraph():
    #graph =  ximport("graph")
    g = gra.create(iterations=500, distance=0.8)
    print g
    g.add_node("NodeBox")
    g.add_node("Core Image", category="library")
    g.add_edge("Core Image", "NodeBox")
    g.solve()
    g.draw()
    return