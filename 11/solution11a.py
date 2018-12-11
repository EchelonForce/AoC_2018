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

    max_x,max_y = 0,0
    biggest = 0

    for x in range(297):
        for y in range(297):
            s = sum(sum( grid[x:x+3,y:y+3] ))
            if biggest < s:
                biggest = s
                max_x = x
                max_y = y
    
    print( 'Solution: %d, %d, %d'%(max_x+1, max_y+1, biggest))
            
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
