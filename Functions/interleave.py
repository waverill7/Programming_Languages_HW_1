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
