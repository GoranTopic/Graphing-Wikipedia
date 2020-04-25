#!/usr/bin/python

# a script to get all the pages and put them into difrent file of the
# whole wikipedi text file of 72 G in size 
# by goran topic

from bs4 import BeautifulSoup
import re, os 

# open files
read_file = open('enwiki-20200401-pages-articles-multistream.xml')
write_file =  open( '/mnt/enwiki-data.xml', "w+" )    

class Article_Reader:
    ''' article class for saving asticles '''
    # macth open tag
    open_page_regex =  '^ +<page>$'
    # macth close tag
    close_page_regex =  '^ +</page>$'
    # macth title tags
    title_regex =  ' +<title>(.*?)</title>$'
    # macth redirect tags
    redirect_regex =  '^ +<redirect[^/>]*/>'
    # regex which matches a link [[]]
    link_regex = '(?<=\[\[)(?!Category:|Wikipedia:|Help:|:Special:|Special:|Image:|Project:|File:|User:|wikt:|Template:|WP:|talk:|help:|User talk:|:Template:)[^|\]]+'
    
    def __init__(self, writting_file):
        self.writting_file =  writting_file
        self.title = ''
        self.is_reading = False
        self.is_redirect = False
        self.article_number = 0
        self.line_number = 0
        self.title 
        self.edges = []
    
    def reset(self):
        self.title = ''
        self.is_reading = False
        self.is_redirect = False
        self.title 
        self.edges =[]

    def stop_reading(self):
        if not self.is_reading:
            print(" ERROR: found closing tag without a opening tag found first") 
        else:
            self.write_to_file()
            self.reset()
            self.article_number += 1

    def start_reading(self):
        if self.is_reading:
            print(" ERROR: already reading an article") 
        else:
            self.reset()
            self.is_reading = True

    def set_title(self, title):
        if not self.is_reading:
            print(" ERROR: reader got title tag when not reading an article ") 
        else:
            self.title = title
    
    def set_redirect(self):
        if self.is_redirect:
            print(" ERROR: Already set as redirect, cannot se twice") 
        elif not self.is_reading:
            print(" ERROR: it is not readin open page tag not found, cannot set atricle as redirect") 
        else:
            self.is_redirect = True   

    def add_edge(self, edge):
        if not self.is_reading:
            print(" ERROR: reader got link when not reading an article ") 
        else:
            self.edges.append( edge)

    def write_to_file(self):
        if not self.is_redirect: 
            self.writting_file.write('-\n')
            self.writting_file.write( self.title + '\n')
            for edge in self.edges:
                self.writting_file.write(edge + ' | ')
            self.writting_file.write('\n')

    def process_line(self, line):
        # if open page tag found
        if re.match( self.open_page_regex, line ):
            print()           
            print("open article")
            self.start_reading()
        # if close page tag found
        elif re.match( self.close_page_regex, line ):
            print("close article")
            self.stop_reading()  
        # if title tag found
        elif re.match( self.title_regex , line ):
            print("change article")
            self.set_title( re.match( ' +<title>(.*?)</title>$', line ).group(1) )
        # if redirect tag found 
        elif re.match( self.redirect_regex, line ):
            print("got REDIRECT ")
            self.set_redirect()
        # if link is found
        elif re.search(self.link_regex ,line):
            for link in re.findall(self.link_regex, line):
                self.add_edge(link)
        # normal linqe 
        else:
            pass

        self.line_number += 1

# buffer for article
reader = Article_Reader(write_file)
 

for line in read_file: 
# for every line in the file
    try:
        reader.process_line(line)
    except:
        print("panis something happpedn")
        print("saving state")
        f = open("state.txt", 'w+')
        f.write( str(reader.article_number) + " article number\n")
        f.write( str(reader.line_number) + " line number")
        exit()
