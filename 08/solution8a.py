#!/usr/bin/env python
from __future__ import print_function
import re
import sys

def main( args ):
    lines = []

    in_file = 'input.txt'
    if len(args) > 1:
        in_file = args[1]
    
    with open( in_file, 'r' ) as f:
        for line in f:
            lines.append(line.rstrip())

    node = tree_node()
    node.parse(map(int,lines[0].split(' ')))
    print('metsum: %d'%(node.meta_sum()))
    
class tree_node():
    def __init__( self ):
        self.children = []
        self.num_children = 0
        self.meta_data = []
        self.num_meta_data = 0
        
    def parse( self, data ):
        #print('data',data)
        read_nums = 0
        self.num_children = data[0]
        self.num_meta_data = data[1]
        read_nums = 2
        if self.num_children > 0:
            for d in range(self.num_children):
                node = tree_node()
                read_nums += node.parse(data[read_nums:])
                self.children.append(node)
        self.meta_data = data[read_nums:read_nums+self.num_meta_data]
        read_nums += self.num_meta_data
        #print('meta_data',self.meta_data)
        return read_nums

    def meta_sum(self):
        temp = sum(self.meta_data)
        for c in self.children:
            temp+=c.meta_sum()
        return temp

if __name__ == "__main__":
    main(sys.argv)
