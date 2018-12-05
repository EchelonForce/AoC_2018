#!/usr/bin/env python

def main():
    lines = []

    #with open( 'input_test.txt', 'r' ) as f:
    with open( 'input1.txt', 'r' ) as f:
        for line in f:
            lines.append(line.rstrip())

    input = lines[0]
    #input = 'abBcCDdAd'
    idx = 0
    done = False
    while not done:
        #print( idx, 'idx' )
        #print input[ idx:idx+2 ]
        if same_char(input[ idx:idx+2 ]):
            #print('matches' )
            input = input[0:idx]+input[idx+2:]
            #print( 'i:', input)
            
            if idx != 0:
                idx=idx-1
        else:
            idx=idx+1
        if idx == len(input):
            done = True
    
    print( 'Length Remaining: %d'%len(input) )

def same_char( a ):
    if len(a) < 2:
        return False
    b = ord(a[0])
    c = ord(a[1])
    if b<c and b+32==c:
        return True
    elif c<b and c+32==b:
        return True
    else:
        return False
        
if __name__ == "__main__":
    main()

















