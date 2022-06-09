    filename =  sys.argv[1]
        # for every url get the article name with regex
    # getting file from passed arguments
def get_dirs(path):
    # save graph   
        print("adding node : " + node )
    nx.write_gpickle(wiki_graph, "wiki_graph_data.nx")
        wiki_graph.add_node(node)
import pickle
    # opening file 
    ''' This would print all the files and directories '''
import sys, os
    # graph structure for storing the wikipedia nodes
def read_list():
    '''
    '''
path = "/home/telix/"
    














import networkx as nx
for dir_ in get_dirs(path):
    wiki_graph = nx.DiGraph()
    with open(filename) as f:
        # read line from file
dirs = os.listdir( path )
    print('reading from file: ' + filename )
        print("done")
#!/usr/bin/python
        # add node to graph
        read the list of urls and set the titlte of the article as node in the graph
        node =  re.search('(?=\/)/[^/]*$', line).group()
import datetime
        content = f.readlines()
# A program which 
    return  [f.path for f in os.scandir(path) if f.is_dir()]
    print(dir_)
    for line in content:
import sys
import re
