import random;

def scramble( s ):
    temp = list( s )
    result = ''
    while len( temp ) > 0:
        x = random.randint( 0, ( len( temp ) - 1 ) )
        result += temp[ x ]
        temp.pop( x )
    return result