#!/usr/bin/env python
from __future__ import print_function
import re
import sys

def main( args ):
    lines = []

    in_file = 'input1.txt'
    if len(args) > 1:
        in_file = args[1]
    
    with open( in_file, 'r' ) as f:
        for line in f:
            lines.append(line.rstrip())

    deps = []

    pattern = 'Step (?P<a>[A-Z]) must be finished before step (?P<b>[A-Z]) can begin.'
    pat = re.compile(pattern)

    for line in lines:
        m = pat.match( line )
        deps.append([m.group('b'),m.group('a')])

    #print( deps )
    
    nodes = {}
    for d in deps:
        if d[0] not in nodes:
            nodes[d[0]] = []
        if d[1] not in nodes:
            nodes[d[1]] = []
        
    #print( nodes )
    
    for d in deps:
        nodes[d[0]].append(d[1])
    print( nodes )
        
    resolve( nodes )
    
def resolve( nodes ):
    no_deps = []
    for n in nodes:
        if len(nodes[n]) == 0:
            no_deps.append(n)

    #print( no_deps )

    no_deps = sorted(no_deps)

    while len( no_deps ) > 0:
        #print( nodes )
        cur_node = no_deps[0]
        no_deps.remove(cur_node)
        if cur_node in nodes:
            nodes.pop(cur_node)
            print( cur_node, end='' );
        for n in nodes:
            if cur_node in nodes[n]:
                nodes[n].remove(cur_node)
            if len(nodes[n]) == 0:
                no_deps.append(n)
                
        no_deps = sorted(no_deps)
                

if __name__ == "__main__":
    main(sys.argv)
