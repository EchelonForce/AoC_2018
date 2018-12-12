#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy

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

    init_str = first_line[15:]
    print( init_str )

    start_len = len(init_str)*4
    zed = start_len/2
    
    plants = ['.:%+03d'%(i-zed) for i in range(start_len)]

    print(print_plants( plants ))
    
    for i,t in enumerate(init_str):
        plants[i+zed] = t+':%+03d'%(i)
    print(print_plants( plants ))

    patterns = []
    for line in lines:
        #print(line)
        a,b = line.split(' => ')
        #print((a,b))
        patterns.append( [a,b] )

    rounds = 20

    for round in range(rounds):
        alive = []
        dead = []
        for i in range(2,len(plants)-2):
            temp = print_plants( plants[i-2:i+3] )
            found = False
            for pat in patterns:
                #print( temp, pat[0], temp in pat[0])
                if pat[0] in temp:
                    if pat[1] == '.':
                        dead.append(i)
                    if pat[1] == '#':
                        alive.append(i)
                    found = True
                    break
            if not found:
                dead.append(i)
        
        for al in alive:
            plants[al] = '#:%+03d'%(al)
        for d in dead:
            plants[d] = '.:%+03d'%(d)

        print(print_plants( plants ), sum([a-zed for a in alive]))
    
def sum_alive( plants ):
    for p in plants:
        pass

def print_plants( plants ):

    ss = ['','','','']
    
    for p in plants:
        ss[0] += p[0] 
        ss[1] += p[2]
        ss[2] += p[3]
        ss[3] += p[4]
    #print(ss[0])
    #print(ss[1])
    #print(ss[2])
    #print(ss[3])

    return ss[0]

    #i = zed
    #for i, p in enumerate(plants):
    #    if i-zed > 0 and i-zed < 
    #    plants[i] = p
    #    for p
    #
    #for p in init_str:

if __name__ == "__main__":
    main(sys.argv)
