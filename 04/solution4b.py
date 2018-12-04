#!/usr/bin/env python
import re

lines = []

#too high 138099
#too low 117???
#with open( 'input_test.txt', 'r' ) as f:
with open( 'input1.txt', 'r' ) as f:
    for line in f:
        lines.append(line.rstrip())

pattern = '\[(?P<year>[0-9]+)-(?P<month>[0-9]+)-(?P<day>[0-9]+) (?P<hour>[0-9]+):(?P<minute>[0-9]+)\] (?P<state>.*)'
pat = re.compile(pattern)

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

data = []

for l in lines:
    m = pat.match(l)

    year = int(m.group('year'))
    month = int(m.group('month'))
    day = int(m.group('day'))
    hour = int(m.group('hour'))
    minute = int(m.group('minute'))
    state = m.group('state')

    #print minute
    time_simp = minute+hour*60+(day-1)*60*24+sum(days_in_months[:month-1])*24*60
    #print( time_simp%60 )

    entry = {'time':time_simp, 'state':state, 'minute':minute, 'line':l }

    data.append( entry )

#print data
#print '---------------------------------'
data = sorted( data, key=lambda e: e['time'])
#print data

class Guard():
    def __init__( self, id ):
        self.sleeps = []
        self.mins_slept_in = []
        for i in range(60):
            self.mins_slept_in.append(0)
        self.total_sleep = 0
        self.id = id
        self.min_slept_most = -1
        self.times_slept_in_min_most_slept_in = 0

    def add_sleep( self, start, end ):
        self.sleeps.append([start,end])
        print( 'id = %s start=%d, stop=%d, delta=%d'%(self.id, start,end, ( end-start) ))
        self.total_sleep += ( end-start)

        time = end-1
        while time >= start:
            self.mins_slept_in[time%60]+=1
            print('adding 1 to minute %d'%(time%60))
            time -=1

    def most_slept_min( self ):
        prev_max_idx = 0
        prev_max = 0
        for i, minu in enumerate(self.mins_slept_in):
            if minu > prev_max:
                prev_max = minu
                prev_max_idx = i
        self.min_slept_most = prev_max_idx
        self.times_slept_in_min_most_slept_in = prev_max

        return prev_max_idx, prev_max

    def __str__( self ):
        s = ''
        s += self.id
        a,b = self.most_slept_min()
        s += ' slept most in minute %d (%d times)'%(a,b)
        s += ' so solution=%d'%(int(self.id)*a)
        return s

guards = []

i=0
for d in data:
    print( d )
    if i >10:
        break


current_guard = None
for entry in data:

    if 'begins shift' in entry['state']:
        guard_id = entry['state'].replace(' begins shift','').replace('Guard #','')
        found = False
        asleep = 0
        awake = 0
        for g in guards:
            if guard_id == g.id:
                current_guard = g
                found = True
                print( 'found current_guard.id', current_guard.id )
                break
        if not found:
            current_guard = Guard(guard_id)
            guards.append(current_guard)
            print( 'add current_guard.id', current_guard.id )
        print( 'new_guard' )

    if 'falls asleep' in entry['state']:
        asleep = entry['time']
        print( 'asleep' )

    if 'wakes up' in entry['state']:
        awake = entry['time']
        current_guard.add_sleep( asleep, awake )
        print( 'awake' )

sleep_totals = {}

for guard in guards:
    guard.most_slept_min()

print '---------------------------------'
sorted_guards = sorted(guards, key=lambda a: a.times_slept_in_min_most_slept_in, reverse=True )

guard_slept_most = sorted_guards[0]

#for g in sorted_guards:
#    print( g )

print( guard_slept_most )




