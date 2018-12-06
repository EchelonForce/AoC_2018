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

    #place points
    for i in range(num_points):
        x = xs[i]
        y = ys[i]
        #print( x, y )
        grid[x][y]=ids[i]


    #print_grid(grid)

    #place owned points
    for x in range(x_max):
        for y in range(y_max):
            idx=min_point( x, y, xs, ys )
            if idx == -1:
                grid[x][y] = ':'
            else:
                grid[x][y] = ids[idx]
            #like example...
            #elif grid[x][y] != ids[idx]:
            #    grid[x][y] = ids2[idx]

    #print_grid(grid)

    #determine non-edge ids
    non_edge = []
    for id in ids:
        if id not in grid[0] and id not in grid[-1]:
            found = False
            for col in grid:
                if id == col[0] or id == col[-1]:
                    found= True
                    break
            if not found:
                non_edge.append(id)

    #print( non_edge )
    non_edge_cnts = []
    for id in non_edge:
        cnt = 0
        for col in grid:
            for a in col:
                if a == id:
                    cnt += 1
        non_edge_cnts.append(cnt)
    #print( zip( non_edge_cnts, non_edge ) )
    print( 'Solution: %d'%max( non_edge_cnts ) )

    

def min_point( x, y, xs, ys ):
    min_idx = -1
    min_val = 100000
    dup_found = True
    for i in range(len(xs)):
        m = manhatan_dist( x,y,xs[i],ys[i])
        if m < min_val:
            min_val = m
            dup_found = False
            min_idx = i
        elif m == min_val:
            dup_found = True
    if dup_found:
        return -1
    else:
        return min_idx
        

def print_grid( grid ):
    x_dim = len(grid)
    y_dim = len(grid[0])
    for y in range(y_dim):
        for x in range(x_dim):
            print( grid[x][y], end='')
        print('')
        
def make_grid( x_dim, y_dim ):
    grid = [['.' for y in range(y_dim)] for x in range(x_dim)]
    return grid
    
def manhatan_dist( x1, y1, x2, y2 ):
    return abs(x2-x1)+abs(y2-y1)


if __name__ == "__main__":
    main()

















