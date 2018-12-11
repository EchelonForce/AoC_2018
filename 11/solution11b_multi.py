#!/usr/bin/env python
from __future__ import print_function
import sys
import numpy
from multiprocessing import Pool

dim = 300
serial = 7511

def main( args ):

    pool = Pool(processes=12)

    results = pool.map( do_x, range(dim) )

    print(get_grid())

    max_x,max_y,max_s = 0,0,0
    biggest = 0
    for r in results:
        if biggest < r[0]:
                biggest = r[0]
                max_x = r[1]
                max_y = r[2]
                max_s = r[3]

    print( 'Solution: %d,%d,%d,%d'%(max_x+1, max_y+1, max_s, biggest))
      
def do_x(x):      
    grid = get_grid()

    max_x,max_y,max_s = 0,0,0
    biggest = 0

    for y in range(dim):
        max_size = dim+1-(max(x,y))
        for s in range(1,max_size):
            power = sum(sum( grid[x:x+s,y:y+s] ))
            if biggest < power:
                biggest = power
                max_x = x
                max_y = y
                max_s = s

    return [biggest, max_x, max_y, max_s]

def get_grid():
    grid = []
    for i in range(dim):
        grid.append(range(dim))
    

    for x in range(dim):
        for y in range(dim):
            grid[x][y] = p(x,y,serial)

    grid = numpy.array(grid)
    return grid

            
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
