#!/usr/bin/python

import sys
import collections

wordsIndex = collections.defaultdict(list)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    word = data_mapped[0].lower()
    wordsIndex[word].append(data_mapped[1])

for word in wordsIndex:
    print "{0}\t{1}".format(word, len(wordsIndex[word]))
