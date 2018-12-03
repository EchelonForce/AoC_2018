#!/usr/bin/env python

lines = []
#with open( 'input_test.txt', 'r' ) as f:
with open( 'input1.txt', 'r' ) as f:
    for line in f:
        lines.append(line.rstrip())

twos = {}
threes = {}

for line in lines:
    print(line)
    twos_found = False
    threes_found = False
    for i,a in enumerate(line):
        remaining_line = line[i+1:]
        #print( 'looking for %s in %s'%(a,remaining_line) )
        for j,b in enumerate(remaining_line):
            #print( remaining_line )
            if a==b:
                print( '---two %s'%(b))
                if not twos_found:
                    twos_found = True
                    twos[line] = [b]
                else:
                    if b not in twos[line]:
                        twos[line].append(b)
                #print( line[i+j+2:] )

                #exit()
                remaining_line_2 = remaining_line[j+1:]
                #print( 'looking for %s in %s'%(a,remaining_line_2) )
                for k,c in enumerate(remaining_line_2):
                    if c==b:
                        print( '--three %s'%(b))
                        if not threes_found:
                            threes_found = True
                            threes[line] = [c]
                        else:
                            threes[line].append(c)

for line in threes:
    for in_threes in threes[line]:
        print( 'removing %s from %s'%(in_threes,twos[line]))
        twos[line].remove(in_threes)
        if len(twos[line]) == 0:
            twos.pop(line, None)
            

print( 'Twos:   %d'%(len(twos)) )
print( 'Threes: %d'%(len(threes)) )

print( 'Checksum:   %d'%(len(twos)*len(threes)) )


