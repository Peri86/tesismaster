#!/usr/bin/env python
from igraph import *
import networkx as nx
#from networkx.readwrite import json_graph
#import json 

def arxiucom(xarxa,nom,cl): #arxiu llistant els nodes i amb quina comunitat pertanyen
    ##########
    arllegit['attrname'] = 'comunitat'
    atributs = arllegit['attrname']
    print atributs
    ##########
    n = xarxa.vcount()
    un=0
    for v in arllegit.vs:
        attr = v.attributes()
        com = cl[un]
        arllegit['comunitat'] = 22
        un+=1
    
    print arllegit
    
    try:
        re = Graph.write_graphml(xarxanova,+nom+".graphml")
    except IOError:
        print 'Error', re
    else:
        print 'ok\n'    

    return

def add_vertex_with_attrs(graph, attrs):
    n = graph.vcount()
    for key, value in attrs.iteritems():
        graph.vs[n][key] = value
#
#def compropiet(): #arxiu amb propeitat representativa de comunitat
#    return

def save_jsonfile():
    G=nx.Graph([(1,2),(2,3)])
    g_json = json_graph.node_link_data(G) # node-link format to serialize
    json.dump(g_json, open('prova','w'))

def save_to_jsonfile(filename, graph):
    ''' 
    Save graph object to filename 
    '''
    #g = graph
    g_json = json_graph.node_link_data(graph) # node-link format to serialize
    json.dump(g_json, open(filename,'w'))