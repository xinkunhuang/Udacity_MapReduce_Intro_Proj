#!/usr/bin/python

import sys

author_list=[]
last_top=None


for line in sys.stdin:
    data=line.strip().split('\t')
    if len(data) ==3:
        topID,authorID,topPost=data

        if last_top and last_top != topID:
            print "{0}\t{1}".format(last_top,author_list)
            author_list=[]

        last_top=topID
        author_list.append(authorID)

if last_top != None:
    print "{0}\t{1}".format(last_top,author_list)
