import random;

#Problem 1:
def change( cents ):
    coins = [ 25, 10, 5, 1 ]
    for x in range( 0, 4 ):
        y = divmod( cents, coins[ x ] )
        coins[ x ] = y[ 0 ]
        cents = y[ 1 ]
    return tuple( coins )

#Problem 2:
def strip_vowels( s ):
    vowels = 'aeiou'
    vowels += vowels.upper()
    result = ''
    for c in s:
        if c not in vowels:
            result += c
    return result

#Problem 3:
def scramble( s ):
    temp = list( s )
    result = ''
    while len( temp ) > 0:
        x = random.randint( 0, ( len( temp ) - 1 ) )
        result += temp[ x ]
        temp.pop( x )
    return result

#Problem 4:
def powers_of_two( limit ):
    x, n = 0, 1
    while n < limit:
        yield n
        x += 1
        n = 2 ** x

#Problem 5:
def powers( base, limit ):
    x, n = 0, 1
    if base > 1:
        while n < limit:
            yield n
            x += 1
            n = base ** x

#Problem 6:
def interleave( a1, a2 ):
    result = []
    if len( a1 ) == len( a2 ):
        for x in range( 0, len( a1 ) ):
            result.append( a1[ x ] )
            result.append( a2[ x ] )
    elif len( a1 ) > len( a2 ):
        for x in range( 0, len( a2 ) ):
            result.append( a1[ x ] )
            result.append( a2[ x ] )
        for y in range( len( a2 ), len( a1 ) ):
            result.append( a1[ y ] )
    else:
        for x in range( 0, len( a1 ) ):
            result.append( a1[ x ] )
            result.append( a2[ x ] )
        for y in range( len( a1 ), len( a2 ) ):
            result.append( a2[ y ] )
    return result

#Problem 7:
def stutter( a ):
    result = []
    for x in a:
        for i in range( 0, 2 ):
            result.append( x )
    return result