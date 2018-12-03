#!/usr/bin/env python
import re

lines = []
#with open( 'input_test.txt', 'r' ) as f:
with open( 'input1.txt', 'r' ) as f:
    for line in f:
        lines.append(line.rstrip())

pattern = '#(?P<id>[0-9]+) @ (?P<x>[0-9]+),(?P<y>[0-9]+): (?P<w>[0-9]+)x(?P<h>[0-9]+)'
pat = re.compile(pattern)

the_grid = []
size = 1000
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    the_grid.append( row )

#for r in the_grid:
#    print r

for l in lines:
    m = pat.match(l)
    
    id = m.group('id')
    x = int(m.group('x'))
    y = int(m.group('y'))
    w = int(m.group('w'))
    h = int(m.group('h'))

    for i in range( x, x+w ):
        for j in range( y, y+h):
            the_grid[i][j]+=1

print( '-------------------------------')
print( '-------------------------------')

#for r in the_grid:
#    print r

overlaps=0
for row in the_grid:
    for val in row:
        if val > 1:
            overlaps+=1

print( 'Overlaps: %d'%overlaps )
 