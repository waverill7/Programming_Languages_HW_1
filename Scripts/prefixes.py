import sys;

result = ''
s =  sys.argv[ 1 ]

for x in range( 0, len( s ) + 1 ):
    print result
    if x < len( s ):
        result += s[ x ]
