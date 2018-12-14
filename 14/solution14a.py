#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy

def main( args ):
    b = board()
    print(b)

    desired = 825401
    additional = 10
        
    while b.size < desired:
        b.combine()
    #print(b)
    nth = b.last
    while b.size < desired+additional:
        b.combine()
    #print(b)
   
    nth = b.first
    for i in range(desired):
        nth = nth.next
            
    s = ''
    for i in range(additional):
        s+='%d'%nth.score
        nth = nth.next
    print( s )

class board():

    def __init__( self ):
        self.first = recipe( 3 )
        self.last = recipe( 7 )
        self.first.next = self.last
        self.last.next = self.first
        self.elf_cur_1 = self.first
        self.elf_cur_2 = self.last
        self.size = 2
    
    def combine( self ):
        score = self.elf_cur_1.score + self.elf_cur_2.score
        
        if score >= 10:
            a = recipe( 1 )
            b = recipe( score-10 )
            a.next = b
            b.next = self.first
            self.last.next = a
            self.last = b
            self.size +=2
        else:
            a = recipe( score )
            a.next = self.first
            self.last.next = a
            self.last = a
            self.size +=1
            
        move_1 = self.elf_cur_1.score+1
        for i in range(move_1):
            self.elf_cur_1 = self.elf_cur_1.next

        move_2 = self.elf_cur_2.score+1
        for i in range(move_2):
            self.elf_cur_2 = self.elf_cur_2.next
            
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
