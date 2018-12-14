#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy

#wrong 20207076 too high

def main( args ):
    b = board()
    print(b)

    state = 0
    num_states = 5
    desired = [5,1,5,8,9]
    desired = [0,1,2,4,5]
    desired = [9,2,5,1,0]
    desired = [5,9,4,1,4]
    num_states = 6
    desired = [8,2,5,4,0,1]

    rev_des = desired[::-1] #reverse
    print('rev_des',rev_des)

    num_to_check = 2
    match = False       
    match_was_second_last = False       
    while not match:
        #print('=============================================')
        #print(b)      
        num_to_check = b.combine()
        #print(b)
        n = b.last
        if num_to_check == 2:
            match = True 
            n = n.prev
            for d in rev_des:
                if n.score != d:
                    match = False
                    break
                else:
                    pass#print('n.score == d', '%d == %d'%(n.score,d))
                n = n.prev
            match_was_second_last = match       
            
        if num_to_check >= 1 and not match:
            match = True       
            n = b.last
            for d in rev_des:
                if n.score != d:
                    match = False
                    break
                else:
                    pass#print('n.score == d', '%d == %d'%(n.score,d))
                n = n.prev
            
    if match_was_second_last:
        print('secondtolast')
        #print(b)
        print( b.size-1-num_states )
    else:
        #print(b)
        print( b.size-num_states )

class board():

    def __init__( self ):
        self.first = recipe( 3 )
        self.last = recipe( 7 )
        self.first.next = self.last
        self.first.prev = self.last
        self.last.next = self.first
        self.last.prev = self.first
        self.elf_cur_1 = self.first
        self.elf_cur_2 = self.last
        self.size = 2
    
    def combine( self ):
        score = self.elf_cur_1.score + self.elf_cur_2.score
        
        if score >= 10:
            num_to_check = 2
            a = recipe( 1 )
            b = recipe( score-10 )
            a.next = b
            b.prev = a
            a.prev = self.last
            self.last.next = a
            self.last = b
            self.last.next = self.first
            self.first.prev = self.last
            self.size +=2
        else:
            a = recipe( score )
            a.prev = self.last
            self.last.next = a
            self.last = a
            self.last.next = self.first
            self.first.prev = self.last
            self.size +=1
            num_to_check = 1
            
        move_1 = self.elf_cur_1.score+1
        for i in range(move_1):
            self.elf_cur_1 = self.elf_cur_1.next

        move_2 = self.elf_cur_2.score+1
        for i in range(move_2):
            self.elf_cur_2 = self.elf_cur_2.next
            
        return num_to_check

    def __str__( self ):
        s = '%d '%self.first.score
        n = self.first.next
        while n != self.first:
            s += '%d '%n.score
            n = n.next
        s += '\n'
        s += 'size: %d'%self.size
        return s

    def print_last_ten( self ):
        n = self.last
        

class recipe():
    def __init__( self, score ):
        self.next = None
        self.score = score

if __name__ == "__main__":
    main(sys.argv)
