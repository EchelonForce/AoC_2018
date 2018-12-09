#!/usr/bin/env python
from __future__ import print_function
import sys
import time

def main( args ):
    #solve( 9, 25 ) == 32
    #solve( 10, 1618 ) == 8317
    #solve( 13, 7999 ) == 146373
    #solve( 17, 1104 ) == 2764
    #solve( 21, 6111 ) == 54718
    #solve( 30, 5807 ) == 37305
    solve( 465, 71498 )

def solve( players, last ):
    start_time = time.time()
    player_scores = []
    for p in range(players):
        player_scores.append([])
    
    player = 0
    circ_buf = [0]
    cur_marb = 0
    prev_time = start_time
    
    for p in range(1,last+1):
        if p % (last/100) == 0:
            print( 'Completed %f '%(p/(last/100)))
            end_time = time.time()
            print( 'Total_time %f '%(end_time-start_time) )
            print( 'Part_time %f '%(end_time-prev_time) )
            prev_time = end_time
        
        #print( 'marble %d'%p )
        #print( 'player+1= %d'%(player+1) )
        if p % 23 == 0:

            #print( 'dealing with 23')
            player_scores[player].append( p )
            #print( 'cur_marb %d'%cur_marb )
            #print( 'circ_buf[cur_marb]=%d'%circ_buf[cur_marb] )
            #print( 'Moving 7 counter clock')
            cur_marb = cur_marb-7
            if cur_marb < 0:
                cur_marb = cur_marb+len(circ_buf)
            #print( 'cur_marb %d'%cur_marb )
            #print( 'circ_buf[cur_marb]=%d'%circ_buf[cur_marb] )
            player_scores[player].append( circ_buf[cur_marb] )
            circ_buf.remove(circ_buf[cur_marb])

        else:
            cur_marb=cur_marb+2
            #print( 'cur_marb %d'%cur_marb )

            if cur_marb == len(circ_buf):
                circ_buf.append(p)
            elif cur_marb > len(circ_buf):
                cur_marb = cur_marb-len(circ_buf)
                circ_buf.insert(cur_marb,p)
            else:
                circ_buf.insert(cur_marb,p)

            #print( 'circ_buf',circ_buf )

        player = (player+1 )%players

    scores = []
    for p in player_scores:
        scores.append( sum(p))
    
    max_score = max(scores)
    print( 'Winning score: %d'%max_score)

if __name__ == "__main__":
    main(sys.argv)
