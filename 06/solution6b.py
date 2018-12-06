#!/usr/bin/env python
from __future__ import print_function

def main():
    lines = []

    #with open( 'input_test.txt', 'r' ) as f:
    with open( 'input1.txt', 'r' ) as f:
        for line in f:
            lines.append(line.rstrip())

    xs = []
    ys = []

    for l in lines:
        x,y = map(int,l.split(','))
        xs.append(x)
        ys.append(y)

    ids = [chr(i+65) for i in range(26)]+[chr(i+97) for i in range(26)]
    ids = ids[0:len(xs)]
    x_max = max(xs)+1
    y_max = max(ys)+1

    #print( 'dims', x_max, y_max )

    num_points = len(xs)
    grid = make_grid(x_max,y_max)

    #print_grid(grid)

    #fill with summed distances.
    for x in range(x_max):
        for y in range(y_max):
            for p in zip(xs,ys):
                grid[x][y] += manhatan_dist( x, y, p[0], p[1] )

    cnt = 0
    for x in range(x_max):
        for y in range(y_max):
            if grid[x][y] >= 10000:
                grid[x][y] = '.'
            else:
                grid[x][y] = '#'
                cnt += 1
    
    #print_grid(grid)

    print( 'Solution: %d'%cnt )

def print_grid( grid ):
    x_dim = len(grid)
    y_dim = len(grid[0])
    for y in range(y_dim):
        for x in range(x_dim):
            print( grid[x][y], end='')
        print('')
        
def make_grid( x_dim, y_dim ):
    grid = [[0 for y in range(y_dim)] for x in range(x_dim)]
    return grid
    
def manhatan_dist( x1, y1, x2, y2 ):
    return abs(x2-x1)+abs(y2-y1)


if __name__ == "__main__":
    main()

















