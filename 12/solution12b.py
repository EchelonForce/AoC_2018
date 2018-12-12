#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy
import math

def main( args ):
    lines = []

    in_file = 'input.txt'
    if len(args) > 1:
        in_file = args[1]
    
    with open( in_file, 'r' ) as f:
        for line in f:
            if 'initial' in line:
                first_line = line.rstrip()
            else:
                if line.rstrip() != '':
                    lines.append(line.rstrip())

    lut = get_lut(lines)

    print( lut)

    init_str = first_line[15:]
    print( init_str )

    
    big_int = 0
    for s in init_str:
        if s == '#':
            big_int = (big_int<<1)+1
        else:   
            big_int = (big_int<<1)

    print( bin(big_int)[2:])

    
    highest_bit_idx = int(math.floor(math.log(big_int, 2)))


    print( 'highest_bit_idx',highest_bit_idx)

    rounds = 2000 #found by observation!

    next_big_int = big_int
    for r in range(rounds):
        big_int = next_big_int<<4
        #print( bin(big_int)[2:])

        next_big_int = 0
        i = 0
        remaining_int = big_int
        small_int = remaining_int&0x01F

        first_alive = None
        while remaining_int>0:
            #print( bin(small_int)[2:])
            if small_int in lut:
                next_big_int = next_big_int | (1<<i)
                if first_alive is None:
                    first_alive = i
                    highest_bit_idx+=(2-i)
                last_alive = i
            i+=1
            remaining_int = remaining_int>>1
            small_int = remaining_int&0x01F
            
        next_big_int = next_big_int >> first_alive
        

        #print( 'first_alive',first_alive)
        #print( 'last_alive',last_alive)
        #print( 'highest_bit_idx',highest_bit_idx)

        #print( bin(next_big_int)[2:])
    


    print( 'rounds=', rounds)
    print( bin(next_big_int)[2:])
    lowest_bit_idx = highest_bit_idx-int(math.floor(math.log(next_big_int, 2)))
    print( 'highest_bit_idx',highest_bit_idx)
    print( 'lowest_bit_idx',lowest_bit_idx)

    #it stabilizes after some large number (less than 2000) and just shifts by one every round
    #so I skip all that and ust figure out what it would be by faking the appropriate number of shifts after that.

    s = 0
    cur_val = highest_bit_idx+(50000000000-rounds)
    lowest_bit_idx = lowest_bit_idx+(50000000000-rounds)
    while cur_val >= lowest_bit_idx:
        if ( next_big_int & 1 ) == 1:
            s+=cur_val
        next_big_int = next_big_int >> 1
        cur_val -=1

    print( 'solution=',s )
    exit()


def get_lut( lines ):
    lut = []
    for line in lines:
        #print(line)
        a,b = line.split(' => ')
        #print((a,b))
        if b == '#':
            a = int(a.replace('#','1').replace('.','0'), 2)
            lut.append(a)
    return lut


if __name__ == "__main__":
    main(sys.argv)
