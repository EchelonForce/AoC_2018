#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy

def main( args ):
    lines = []

    in_file = 'input1.txt'
    if len(args) > 1:
        in_file = args[1]
    
    with open( in_file, 'r' ) as f:
        for line in f:
            lines.append(line.rstrip())

    dots = []

    pattern = 'position=<(?P<x>[-0-9 ]+), (?P<y>[-0-9 ]+)> velocity=<(?P<vx>[-0-9 ]+), (?P<vy>[-0-9 ]+)>'
    pat = re.compile(pattern)

    for line in lines:
        m = pat.match( line )

        if m:
            x = int(m.group('x'))
            y = int(m.group('y'))
            vx = int(m.group('vx'))
            vy = int(m.group('vy'))
            dots.append(dot(x,y,vx,vy))

        #print( 'x  = %d'%x  )
        #print( 'y  = %d'%y  )
        #print( 'vx = %d'%vx )
        #print( 'vy = %d'%vy )



    while not message_detected(dots):
        for d in dots:
            d.update()

    print( 'dots[0].time = %d'%dots[0].time)

    print( '-------------------------------' )
    print_dots(dots)

def message_detected( dots ):

    xs = []
    ys = []
    for d in dots:
        xs.append( d.x )
        ys.append( d.y )

    max_x = max(xs)
    max_y = max(ys)
    min_x = min(xs)
    min_y = min(ys)

    range_x = max_x-min_x
    range_y = max_y-min_y

    #print( 'range_x = %d'%range_x)
    #print( 'range_y = %d'%range_y)

    area = range_x*range_y
    #print( 'area = %d'%area)

    if area < 1000: # this value found by observation...I just let it run until area stopped decreasing.
        return True
    else:
        return False


def print_dots( dots ):

    xs = []
    ys = []
    for d in dots:
        xs.append( d.x )
        ys.append( d.y )

    max_x = max(xs)
    max_y = max(ys)
    min_x = min(xs)
    min_y = min(ys)

    for y in range( min_y-1,max_y+1 ):
        for x in range( min_x-1,max_x+1):
            found = False
            for d in dots:
                if d.x == x and d.y == y:
                    print('#',end='')
                    found = True
                    break
            if not found:
                print( '.', end='' )
        print('')
    print('')

class dot():
    def __init__(self, x, y, vx, vy):
        self.x  = x 
        self.y  = y 
        self.vx = vx
        self.vy = vy
        self.time = 0

    def update( self, time = 1 ):
        self.time = self.time + time
        self.x = self.x+(self.vx*time)
        self.y = self.y+(self.vy*time)

if __name__ == "__main__":
    main(sys.argv)
