#!/usr/bin/python

#   A script which takes a list of urls to read to, makes a it's know file to keep track
#   if it find the file frist it does not read from the passed parameter, and 
#   by Goran Topic

from urllib.request import urlopen 
from bs4 import BeautifulSoup
from multiprocessing import Queue
import networkx as nx
import pickle
import datetime
import random
import collections
import re
import os

# url list file
filename = 'sorted_list_urls.txt'

# Basic besite url for wikipedia
wikipedia_base_url = 'https://en.wikipedia.org/wiki' 


def get_links( url ):
    ''' Get all the unvisited links form the given url '''
    links = []
    # get html page
    page_html = urlopen(url)
    # make soup....hmmm yummi =) lxml to make it fast 
    soup = BeautifulSoup( page_html, 'lxml' )
    # for a tag found to have a tribute href which starts with 'wiki'
    return soup('a', href=re.compile('^(\/wiki\/(?!File|Portal:|Wikipedia:|Special:|Help:|Talk:|Template:|Category:))'))

def panic_save_everything(queued_pages, visited_pages, WG):
    ''' PANIC and save all the python objects to disk '''
    print("PANIC!! saving data")
    # make a file indicating that the previous try has encounted an error
    #f = open(".exited_on_error","w+") 
    #data = (queued_pages, visited_pages, WG)
    #data_file = open("graph_data.pyo", 'wb')
    #pickle.dump( data , data_file )
    # Save queued web pages into file
    queue_file = open('queue.pyo', 'wb')
    pickle.dump( queued_pages, queue_file )
    # Save the visited pages file
    visited_file = open('visited.pyo', 'wb')
    pickle.dump( visited_pages , visited_file )
    # Save graph object
    nx.write_gpickle(WG, "graph_data.nx")
    print("data saved")



def print_status( current_page, queued_pages, visited_pages, WG):
    ''' prints the status of the search '''
    print()
    #print(  "queue size: "        +  str(queued_pages.qsize())    )
    #print(  "visited pages: "     +  str(len(visited_pages))      )
    print(  "current page: "      +  current_page                 )
    print(  "number of nodes: "   +  str(WG.number_of_nodes())    )
    print(  "number of edges: "   +  str(WG.number_of_edges())    )




# get file
f = open(filename)
# read urls in file
urls = f.readlines()
print("got list")
wiki_graph = nx.read_gpickle("wiki_graph_data.nx")
print("got graph")



# look for passed file with list of urls
#   process file and save list
# else exit


# look for grap save object 
# else exit
percentage = 0.0
position = 0;

for url in  urls:
    #getlist of nodes in urls 
    #try:
    #
    links =  get_links(url)
    #except:
    #    print("could not get links")
    #    save 
    #    exit

    current =  re.search('(?=\/)/[^/]*$', url).group() 
    print(current)
    print(position)
    print(percentage)

    for link in links:
        node =  re.search('(?=\/)/[^/]*$', link['href']).group() 
        #add edge to the graph 
        wiki_graph.add_edge( current,  node )
        #print(node)
    #delete urls 
    position+=1
    percentage += 0.00001
'''
def start_crawler( start_page, target_page, wikipedia_base_url ):
    # a dictionary  of visited pages, has to be a dict
    # so that time complexity is kept at o(1)
    visited_pages = {}
    # queue of pages to visit 
    queued_pages = collections.deque()
    # graph structure for storing the wikipedia nodes
    WG = nx.Graph()
    # current page is starting pages 
    current_page = start_page
    # check if there is error file
    # check if there are files
    if os.path.isfile(".exited_on_error"):
        print(" reading from file left behind in previus seccion...")
        # delete errror file 
        os.remove(".exited_on_error")
    else:
        #staring the scrawler 
        print("Starting crawler...")
        
    while current_page is not target_page:
        # Add current node to the graph
        WG.add_node(current_page)
        try:
        # try to get the links for the current url
            pages = get_links( wikipedia_base_url + current_page )
        except:
        # if it failed, PANIC! saved everything, and bait! 
            print("Error getting: " + wikipedia_base_url + current_page)
            panic_save_everything(queued_pages, visited_pages, WG)       
            return 0
        # mange to ge the page
        print("done loading")
        for page in pages: 
            if page not in visited_pages:
                # if it is a new page
                print("add node and edge")
                WG.add_node( page['href'] )
                WG.add_edge( current_page,  page['href'] )
                print("appedin queue")
                queued_pages.append( page['href'] )
        # add current page a visited
        visited_pages[current_page] = True
        # get new current page
        current_page = queued_pages.popleft()
        # print staus
        print_status(current_page, queued_pages, visited_pages, WG)
'''
