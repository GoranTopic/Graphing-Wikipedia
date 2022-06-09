#!/usr/bin/python
# A program which 

import networkx as nx
import pickle
import datetime
import sys
import re
import sys, os


path = "/home/telix/"
dirs = os.listdir( path )

def get_dirs(path):
    ''' This would print all the files and directories '''
    return  [f.path for f in os.scandir(path) if f.is_dir()]


for dir_ in get_dirs(path):
    print(dir_)




def read_list():
    '''
        read the list of urls and set the titlte of the article as node in the graph
    '''
    # getting file from passed arguments
    filename =  sys.argv[1]
    print('reading from file: ' + filename )

    # graph structure for storing the wikipedia nodes
    wiki_graph = nx.DiGraph()

    # opening file 
    with open(filename) as f:
        # read line from file
        content = f.readlines()
    
    for line in content:
        # for every url get the article name with regex
        node =  re.search('(?=\/)/[^/]*$', line).group()
        print("adding node : " + node )
        # add node to graph
        wiki_graph.add_node(node)
        print("done")

    # save graph   
    nx.write_gpickle(wiki_graph, "wiki_graph_data.nx")

