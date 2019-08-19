#!/usr/bin/python

import sys



N=10
topN_tag = [None] * N
topN_count = [0] * N

last_tag=None
last_count=0

def getMin():
    count = min(topN_count)
    index=topN_count.index(count)
    return count, index

def update_top(index):
    topN_count[index]=last_count
    topN_tag[index]=last_tag


for line in sys.stdin:
    data=line.strip().split('\t')
    tag=data[0]


    if last_tag and last_tag != tag:
        min_count,min_index=getMin()
        if min_count < last_count:
            update_top(min_index)
        last_count=0

    last_tag=tag
    last_count+=1

if last_tag is not None:
    min_count,min_index=getMin()
    if min_count < last_count:
        update_top(min_index)

order=sorted(range(N), key = lambda k: topN_count[k],reverse=True)

for i in range(N):
    print '{0}\t{1}'.format(topN_tag[order[i]],topN_count[order[i]])
