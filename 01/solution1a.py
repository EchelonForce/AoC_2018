#!/usr/bin/env python

sum = 0
with open( 'input1.txt', 'r' ) as f:
    for line in f:
        sum += int(line.rstrip())

print( 'Sum: %d'%(sum) )
