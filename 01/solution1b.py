#!/usr/bin/env python

sum = 0
vals = []
sums = [ 0 ]

with open( 'input1.txt', 'r' ) as f:
    for line in f:
        vals.append( int(line.rstrip()) )

#vals = [ 1, -2, 3, 1  ]

iters = 0
not_done = True
while not_done:
    iters +=1
    if iters%2==0:
        print( iters, sum )
    for v in vals:
        sum += v
        #print( sum, sums )
        if sum in sums:
            print( 'Repeated: %d'%(sum) )
            not_done = False
            break
        sums.append(sum)