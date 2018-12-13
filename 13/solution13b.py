#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy
import time

def main( args ):
    lines = []

    in_file = 'input.txt'
    if len(args) > 1:
        in_file = args[1]
    
    with open( in_file, 'r' ) as f:
        for line in f:
            if line.rstrip() != '':
                lines.append(line[:-1])

    lens = [len(l) for l in lines]
    x_dim = max(lens)
    y_dim = len(lines)
    print( 'x_dim',x_dim )
    print( 'y_dim',y_dim )

    carts,grid = read_input( lines, x_dim, y_dim )
    print_state( carts, grid, x_dim, y_dim  )

    print( 'num_carts = %d'%len(carts))
    tick = 1
    collided = 0
    while len(carts)-collided > 1:
        move_carts(carts, grid)
        #print_state( carts, grid, x_dim, y_dim  )
        collided = 0
        for c in carts:
            if c.collided:
                collided+=1
        #print_state( carts, grid, x_dim, y_dim  )
        tick+=1

    for c in carts:
        if not c.collided:
            print( 'last cart at %d,%d'%(c.x, c.y ))
    #print_state( carts, grid, x_dim, y_dim  )
        

def move_carts( carts, grid ):
    sorted_carts = sorted(carts, key=lambda c: c.x)
    sorted_carts = sorted(sorted_carts, key=lambda c: c.y )
    
    for c in sorted_carts:
        if not c.collided:
            #print( c.x, c.y)
            x,y = c.move(grid)
            for c2 in sorted_carts:
                if not c2.collided:
                    if c != c2 and c.check_loc(c2.x,c2.y):
                        c.collided = True
                        c2.collided = True

class cart():
    def __init__( self, x,y, dir ):
        self.x = x
        self.y = y
        self.dir = dir
        self.next_turn = 'l'
        self.collided = False
    
    def __str__( self ):
        cart_symbols = {'u':'^','d':'v', 'l':'<', 'r':'>'}
        return cart_symbols[self.dir]

    def check_loc( self, x, y ):
        if x == self.x and y == self.y:
            return True
        else:
            return False

    def move( self, grid ):
        next_turns = { 'r':'l', 'l':'s', 's':'r' }
        if self.dir == 'u':
            if grid[self.x][self.y-1] == 'v':
                self.x = self.x
                self.y = self.y-1
                self.dir = 'u'
            elif grid[self.x][self.y-1] == 'ur':
                self.x = self.x
                self.y = self.y-1
                self.dir = 'l'
            elif grid[self.x][self.y-1] == 'ul':
                self.x = self.x
                self.y = self.y-1
                self.dir = 'r'
            elif grid[self.x][self.y-1] == 'i':
                self.x = self.x
                self.y = self.y-1
                if self.next_turn == 'l': 
                    self.dir = 'l'
                elif self.next_turn == 'r':
                    self.dir = 'r'
                self.next_turn = next_turns[self.next_turn]
                    
        elif self.dir == 'd':
            if grid[self.x][self.y+1] == 'v':
                self.x = self.x
                self.y = self.y+1
                self.dir = 'd'
            elif grid[self.x][self.y+1] == 'lr':
                self.x = self.x
                self.y = self.y+1
                self.dir = 'l'
            elif grid[self.x][self.y+1] == 'll':
                self.x = self.x
                self.y = self.y+1
                self.dir = 'r'
            elif grid[self.x][self.y+1] == 'i':
                self.x = self.x
                self.y = self.y+1
                if self.next_turn == 'l': 
                    self.dir = 'r'
                elif self.next_turn == 'r':
                    self.dir = 'l'
                self.next_turn = next_turns[self.next_turn]
        elif self.dir == 'l':
            if grid[self.x-1][self.y] == 'h':
                self.x = self.x-1
                self.y = self.y
                self.dir = 'l'
            elif grid[self.x-1][self.y] == 'ul':
                self.x = self.x-1
                self.y = self.y
                self.dir = 'd'
            elif grid[self.x-1][self.y] == 'll':
                self.x = self.x-1
                self.y = self.y
                self.dir = 'u'
            elif grid[self.x-1][self.y] == 'i':
                self.x = self.x-1
                self.y = self.y
                if self.next_turn == 'l': 
                    self.dir = 'd'
                elif self.next_turn == 'r':
                    self.dir = 'u'
                self.next_turn = next_turns[self.next_turn]
        elif self.dir == 'r':
            if grid[self.x+1][self.y] == 'h':
                self.x = self.x+1
                self.y = self.y
                self.dir = 'r'
            elif grid[self.x+1][self.y] == 'ur':
                self.x = self.x+1
                self.y = self.y
                self.dir = 'd'
            elif grid[self.x+1][self.y] == 'lr':
                self.x = self.x+1
                self.y = self.y
                self.dir = 'u'
            elif grid[self.x+1][self.y] == 'i':
                self.x = self.x+1
                self.y = self.y
                if self.next_turn == 'l': 
                    self.dir = 'u'
                elif self.next_turn == 'r':
                    self.dir = 'd'
                self.next_turn = next_turns[self.next_turn]

        return self.x, self.y

def print_state( carts, grid, x_dim, y_dim ):
    symbols = {' ':' ','v':'|', 'h':'-', 'll':'\\', 'ur':'\\', 'lr':'/', 'ul':'/', 'i':'+'}
    for y in range(y_dim):
        s = ''
        for x in range(x_dim):
            cart_found = False
            for c in carts:
                if c.check_loc(x,y):
                    s+=c.__str__();
                    cart_found = True
            if not cart_found:
                s+=symbols[grid[x][y]]
        print( s )


def read_input( lines, x_dim, y_dim ):

    grid = []
    carts = []

    for x in range(x_dim):
        col = []
        for y in range(y_dim):
            if lines[y][x] == '|':
                col.append('v')
            elif lines[y][x] == '-':
                col.append('h')
            elif lines[y][x] == '\\' and x+1 < x_dim and lines[y][x+1] in ['-','+','>','<']:
                col.append('ll')
            elif lines[y][x] == '\\' and x-1 > 0 and lines[y][x-1] in ['-','+','>','<']:
                col.append('ur')
            elif lines[y][x] == '/' and x+1 < x_dim and lines[y][x+1] in ['-','+','>','<']:
                col.append('ul')
            elif lines[y][x] == '/' and x-1 > 0 and lines[y][x-1] in ['-','+','>','<']:
                col.append('lr')
            elif lines[y][x] == '+':
                col.append('i')
            elif lines[y][x] == ' ':
                col.append(' ')
            elif lines[y][x] == '^':
                col.append('v')
                carts.append(cart(x,y,'u'))
            elif lines[y][x] == 'v':
                col.append('v')
                carts.append(cart(x,y,'d'))
            elif lines[y][x] == '>':
                col.append('h')
                carts.append(cart(x,y,'r'))
            elif lines[y][x] == '<':
                col.append('h')
                carts.append(cart(x,y,'l'))
            else:
                print('dont know',lines[y][x],ord(lines[y][x]), x, y)
                exit()
        grid.append(col)

    return carts, grid


if __name__ == "__main__":
    main(sys.argv)
