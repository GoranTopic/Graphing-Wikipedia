        #print(node)
    # queue of pages to visit 
    print(percentage)
            pages = get_links( wikipedia_base_url + current_page )
        # try to get the links for the current url
    # for a tag found to have a tribute href which starts with 'wiki'
        print(" reading from file left behind in previus seccion...")
            if page not in visited_pages:
# else exit
# else exit
    pickle.dump( visited_pages , visited_file )
    print(  "number of edges: "   +  str(WG.number_of_edges())    )
                print("appedin queue")
        try:
    #    save 
    print("data saved")
import networkx as nx
urls = f.readlines()
        # print staus
    print(position)
        # Add current node to the graph
    print("PANIC!! saving data")
    return soup('a', href=re.compile('^(\/wiki\/(?!File|Portal:|Wikipedia:|Special:|Help:|Talk:|Template:|Category:))'))
for url in  urls:
        # add current page a visited
                print("add node and edge")
        #add edge to the graph 
        #staring the scrawler 
f = open(filename)
import re
import collections
    print(  "number of nodes: "   +  str(WG.number_of_nodes())    )
    ''' prints the status of the search '''
        wiki_graph.add_edge( current,  node )
    # Save queued web pages into file
#   by Goran Topic
    else:
    for link in links:
import pickle
import os
    #except:
        visited_pages[current_page] = True
def start_crawler( start_page, target_page, wikipedia_base_url ):
    current_page = start_page
import random
    soup = BeautifulSoup( page_html, 'lxml' )
    while current_page is not target_page:
        # if it failed, PANIC! saved everything, and bait! 
                WG.add_node( page['href'] )
print("got list")
def panic_save_everything(queued_pages, visited_pages, WG):
    # get html page
# Basic besite url for wikipedia
    print()
filename = 'sorted_list_urls.txt'
    # check if there is error file
'''
'''
        node =  re.search('(?=\/)/[^/]*$', link['href']).group() 
from urllib.request import urlopen 
    #    print("could not get links")
    nx.write_gpickle(WG, "graph_data.nx")
    WG = nx.Graph()
    if os.path.isfile(".exited_on_error"):
# get file
print("got graph")
    pickle.dump( queued_pages, queue_file )
    page_html = urlopen(url)
    #data = (queued_pages, visited_pages, WG)
    # check if there are files
            panic_save_everything(queued_pages, visited_pages, WG)       
    ''' PANIC and save all the python objects to disk '''
# look for grap save object 
from bs4 import BeautifulSoup
    #    exit
    # so that time complexity is kept at o(1)
    print(current)
        # delete errror file 
    ''' Get all the unvisited links form the given url '''
        except:
        WG.add_node(current_page)
        current_page = queued_pages.popleft()
    # a dictionary  of visited pages, has to be a dict
        print("Starting crawler...")
percentage = 0.0
    #data_file = open("graph_data.pyo", 'wb')
    # current page is starting pages 
    #f = open(".exited_on_error","w+") 






















wikipedia_base_url = 'https://en.wikipedia.org/wiki' 
            return 0
#!/usr/bin/python
        os.remove(".exited_on_error")
#   A script which takes a list of urls to read to, makes a it's know file to keep track
                # if it is a new page
    #getlist of nodes in urls 
    # make a file indicating that the previous try has encounted an error
    percentage += 0.00001
    current =  re.search('(?=\/)/[^/]*$', url).group() 
                queued_pages.append( page['href'] )
# read urls in file
    links = []
    visited_file = open('visited.pyo', 'wb')
    # make soup....hmmm yummi =) lxml to make it fast 
        # get new current page
    #print(  "visited pages: "     +  str(len(visited_pages))      )
position = 0;
                WG.add_edge( current_page,  page['href'] )
    links =  get_links(url)
# url list file
    print(  "current page: "      +  current_page                 )
def print_status( current_page, queued_pages, visited_pages, WG):
    # graph structure for storing the wikipedia nodes
    #try:
        print("done loading")
    #
    # Save the visited pages file
    position+=1
    queued_pages = collections.deque()
    #pickle.dump( data , data_file )
        # mange to ge the page
    #print(  "queue size: "        +  str(queued_pages.qsize())    )
        
#   if it find the file frist it does not read from the passed parameter, and 
#   process file and save list
        print_status(current_page, queued_pages, visited_pages, WG)
def get_links( url ):
    queue_file = open('queue.pyo', 'wb')
        for page in pages: 
    # Save graph object
            print("Error getting: " + wikipedia_base_url + current_page)
wiki_graph = nx.read_gpickle("wiki_graph_data.nx")
import datetime
    visited_pages = {}
# look for passed file with list of urls
    #delete urls 
from multiprocessing import Queue
