    # getting file from passed arguments
    print(dir_)
for dir_ in get_dirs(path):
def read_list():
path = "/home/telix/"
        wiki_graph.add_node(node)
        print("done")
        read the list of urls and set the titlte of the article as node in the graph
    print('reading from file: ' + filename )
    wiki_graph = nx.DiGraph()
    # opening file 
    '''
    '''
        # for every url get the article name with regex














        # add node to graph
import sys, os
def get_dirs(path):
dirs = os.listdir( path )
    ''' This would print all the files and directories '''
    nx.write_gpickle(wiki_graph, "wiki_graph_data.nx")
    # save graph   
import re
    # graph structure for storing the wikipedia nodes
        # read line from file
    
import sys
import networkx as nx
        node =  re.search('(?=\/)/[^/]*$', line).group()
    for line in content:
        print("adding node : " + node )
import pickle
    return  [f.path for f in os.scandir(path) if f.is_dir()]
        content = f.readlines()
    with open(filename) as f:
import datetime
# A program which 
#!/usr/bin/python
    filename =  sys.argv[1]
