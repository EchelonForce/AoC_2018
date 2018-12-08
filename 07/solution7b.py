#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import copy

#1248 To High (forgot to set num_w=5)

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
        
    nodes_copy = copy.deepcopy(nodes)
    res_order = resolve( nodes )
    print( res_order )

    do_work( res_order, nodes_copy )

    
def do_work( order, nodes ):
    num_w = 5
    workers = []
    for a in range(num_w):
        workers.append([0,'.'])

    time_elapsed = 0
    started = []
    finished = []
    ready_but_not_started = []
    for n in nodes:
        if len(nodes[n]) == 0 and n not in ready_but_not_started:
            ready_but_not_started.append(n)

    print( time_elapsed, workers )
    while len(order) != len(finished):
        time_elapsed = time_elapsed+1
        for w in workers:
            if w[1] != '.':
                w[0] = w[0]-1
                if w[0]==0:
                    finished.append(w[1])
                    for n in nodes:
                        if w[1] in nodes[n]:
                            nodes[n].remove(w[1])
                            print('removed %s from %s'%(w[1],n))
                            if len(nodes[n]) == 0 and n not in ready_but_not_started:
                                ready_but_not_started.append(n)
                    w[1]='.'


        for w in workers:
            if w[1] == '.':        
                if len(ready_but_not_started) > 0:
                    next = ready_but_not_started[0]
                    print( 'starting = ', next )
                    started.append(next)
                    w[1] = next
                    w[0] = 60+(ord(next)-ord('A')+1)
                    ready_but_not_started.remove(next)

        print( time_elapsed, workers )
    print( 'Solution: %d s'%(time_elapsed-1))

def resolve( nodes ):
    ordered = []
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
            #print( cur_node, end='' );
            ordered.append(cur_node)
        for n in nodes:
            if cur_node in nodes[n]:
                nodes[n].remove(cur_node)
            if len(nodes[n]) == 0:
                no_deps.append(n)
                
        no_deps = sorted(no_deps)
    return ordered

if __name__ == "__main__":
    main(sys.argv)
