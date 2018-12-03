#!/usr/bin/env python

lines = []
#with open( 'input_test.txt', 'r' ) as f:
with open( 'input1.txt', 'r' ) as f:
    for line in f:
        lines.append(line.rstrip())

for i,a in enumerate(lines):
    for j,b in enumerate(lines[i+1:]):
        
        cnt=0
        for q,w in enumerate(a):
            if a[q] != b[q]:
                cnt+=1
        if cnt == 1:
            print( a )
            print( b )

            print( 'Manual diff!' )


            