#!/usr/bin/python

import sys
import csv

reader=csv.reader(sys.stdin,delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        if(line[7]=='\N'):
            top_id=line[0]
            post=1
        else:
            top_id=line[7]
            post=0

        author_id=line[3]

        print "{0}\t{1}\t{2}".format(top_id,author_id,post)
