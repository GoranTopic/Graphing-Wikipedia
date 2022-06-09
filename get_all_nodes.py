for dir_ in get_dirs(path):
    with open(filename) as f:
    # save graph   
path = "/home/telix/"














dirs = os.listdir( path )
    print(dir_)
    return  [f.path for f in os.scandir(path) if f.is_dir()]
        read the list of urls and set the titlte of the article as node in the graph
        content = f.readlines()
        # add node to graph
    nx.write_gpickle(wiki_graph, "wiki_graph_data.nx")
# A program which 
    ''' This would print all the files and directories '''
    for line in content:
import sys, os
    '''
    '''
import datetime
        print("adding node : " + node )
import re
    # getting file from passed arguments
def get_dirs(path):
    print('reading from file: ' + filename )
    
    # opening file 
    # graph structure for storing the wikipedia nodes
        print("done")
    wiki_graph = nx.DiGraph()
def read_list():
import sys
        node =  re.search('(?=\/)/[^/]*$', line).group()
    filename =  sys.argv[1]
        # for every url get the article name with regex
#!/usr/bin/python
import pickle
import networkx as nx
        wiki_graph.add_node(node)
        # read line from file
