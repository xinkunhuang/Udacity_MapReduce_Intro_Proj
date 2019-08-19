#!/usr/bin/python

import sys
import csv



reader=csv.reader(sys.stdin,delimiter='\t')
reader.next()


for line in reader:
    data=line[2]
    tags=data.strip().split()

    for i in tags:
        print "{0}\t{1}".format(i, 1)
