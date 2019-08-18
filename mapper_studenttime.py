# Replace this with your mapper code
# This will actually not get graded at the moment, because it's
# pretty hard to properly simulate a Hadoop cluster in our system :-)
# This will serve as a storage for your code.

#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        author_id = line[3]
        hour = line[8].split(' ')[1].split(':')[0]
        print "{0}\t{1}".format(author_id, hour)
