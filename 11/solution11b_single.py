#!/usr/bin/env python
from __future__ import print_function
import sys
import numpy

def main( args ):
    grid = []
    for i in range(300):
        grid.append(range(300))
    
    serial = 7511

    for x in range(300):
        for y in range(300):
            grid[x][y] = p(x,y,serial)

    grid = numpy.array(grid)

    max_x,max_y,max_s = 0,0,0
    biggest = 0

    for x in range(300):
        print(x)
        for y in range(300):
            max_size = 301-(max(x,y))
            for s in range(1,max_size):
                power = sum(sum( grid[x:x+s,y:y+s] ))
                if biggest < power:
                    biggest = power
                    max_x = x
                    max_y = y
                    max_s = s
    
    print( 'Solution: %d,%d,%d,%d'%(max_x+1, max_y+1, max_s, biggest))
            
def p(x,y,serial):
    gx = x+1
    gy = y+1
    p1 = (((gx+10)*(gy))+serial)*(gx+10)
    p2 = (p1-(p1%100))
    p2 = p2%1000
    if p2 != 0:
        p2=p2/100
    return p2-5

if __name__ == "__main__":
    main(sys.argv)
