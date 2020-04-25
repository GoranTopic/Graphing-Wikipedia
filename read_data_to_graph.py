#!/usr/bin/python
# by goran topic


import networkx as nx
from bs4 import BeautifulSoup
import re, os 


# open files

# wrtting file 
file_path = 'enwiki-data.txt'

class Reader:
    ''' article class for saving asticles '''
    # start of article
    start_regex = '^-$'  
    seperator_str = ' | '
    node_list = []

    def __init__(self ):
        # graph structure for storing the wikipedia nodes
        self.graph = nx.DiGraph()
        self.title = ''
        self.edges = []
        self.reading_node = False
        self.reading_edges = False
        self.article_number = 0
        self.line_number = 0
    
    def reset(self):
        self.title = ''
        self.reading_node = False
        self.reading_edges = False
        self.edges = []

    def start_reading(self):
        self.reset()
        self.reading_node = True

    def read_title(self, title):
        print("got title: " + title)
        self.title = title
        # add node to graph
        self.graph.add_node(title)
        self.reading_node = False
        self.reading_edges = True

    def read_edges(self, edges):
        self.edges = edges
        for edge in edges:
            print( edge, end='')
            # add edge
            self.graph.add_edge( self.title, edge )
        self.reset()
        self.article_number += 1
        print()

    def panic_and_save(self):
        # save graph   
        f = open("state.txt", 'w+')
        nx.write_gpickle( self.graph, "wiki_graph_data.nx" )
        f.write( str(self.article_number) + " article number\n")
        f.write( str(self.line_number) + " line number\n")
        f.write( str(self.title) + " title")

    def done(self):
        # save graph   
        print("finished reading ")
        f = open("state.txt", 'w+')
        nx.write_gpickle( self.graph, "wiki_graph_data.nx" )
        f.write( str(self.article_number) + " article number\n")
        f.write( str(self.line_number) + " line number\n")
        f.write( str(self.title) + " title")

    def process_line(self, line):
        # reading node set
        if self.reading_node:
            self.read_title(line) 

        # reading node set
        elif self.reading_edges:
            edges = line.split( self.seperator_str )

            self.read_edges(edges)

        # if open page tag found
        elif re.match( self.start_regex, line ):
            self.start_reading()


        #line read
        self.line_number += 1


# open file
reading_file = open( file_path )

# buffer for article
reader = Reader()
 

for line in reading_file: 
# for every line in the file
    try:
        reader.process_line(line)
    except:
        print("panic something happpend")
        print("saving state")
        reader.panic_and_save()
        exit()
        
reader.done()







