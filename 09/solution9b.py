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
    #solve( 465, 71498 )
    solve( 465, 7149800 )

class link():
    def __init__( self, ccw, cw, val ):
        self.ccw = ccw
        self.cw = cw
        self.val = val

    def __str__( self ):
        s = '%d'%self.val
        return s

class llist():
    def __init__( self, link ):
        self.origin = link
        self.cur_link = link
        self.cur_link.ccw = self.cur_link
        self.cur_link.cw = self.cur_link
        self.cnt = 1

    def insert_cw( self, next_val ):
        self.cur_link = self.cur_link.cw #move cw before insert.
        next_link = link( self.cur_link, self.cur_link.cw, next_val )
        self.cur_link.cw.ccw = next_link
        self.cur_link.cw = next_link
        self.cur_link = next_link
        self.cnt = self.cnt+1

    def remove_cur( self ):
        self.cur_link.cw.ccw = self.cur_link.ccw
        self.cur_link.ccw.cw = self.cur_link.cw
        ret = self.cur_link.val
        self.cur_link = self.cur_link.cw
        self.cnt -= 1
        return ret

    def move_ccw( self, cnt ):
        for c in range(cnt):
            self.cur_link = self.cur_link.ccw

    def __str__( self ):
        s = ''
        n = self.origin
        c = 0
        while c < self.cnt:
            if n == self.cur_link:
                s+= ' ('+n.__str__()+')'
            else:
                s+= ' '+n.__str__()
            
            n = n.cw
            c +=1
        return s

def solve( players, last ):
    start_time = time.time()
    player_scores = []
    for p in range(players):
        player_scores.append(0)

    player = 0
    circ_buf = llist( link( None, None, 0 ) )
    prev_time = start_time

    print(circ_buf)
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
            player_scores[player]+= p
            circ_buf.move_ccw(7)
            player_scores[player]+= circ_buf.remove_cur()
        else:
            circ_buf.insert_cw(p)
            #print( 'circ_buf',circ_buf )

        #print(circ_buf)
        player = (player+1 )%players


    max_score = max(player_scores)
    print( 'Winning score: %d'%max_score)

if __name__ == "__main__":
    main(sys.argv)
