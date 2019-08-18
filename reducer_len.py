import sys

sum_ans=0
count_ans=0
prev_topid=None
len_top=0

for line in sys.stdin:
    data=line.strip().split("\t")
    if len(data) == 3:
        cur_topid=data[0]

        if prev_topid and cur_topid != prev_topid:
            if count_ans ==0:
                avg=0
            else:
                avg=sum_ans/count_ans
            print "{0}\t{1}\t{2}".format(prev_topid, len_top,avg)
            sum_ans=0
            count_ans=0

        #if the line is for the post
        if int(data[2])==1:
            len_top=int(data[1])
        else:
            count_ans=count_ans+1
            sum_ans=sum_ans+float(data[1])

        prev_topid=cur_topid

if prev_topid != None:
    if count_ans ==0:
        avg=0
    else:
        avg=sum_ans/count_ans
    print "{0}\t{1}\t{2}".format(prev_topid, len_top,avg)
