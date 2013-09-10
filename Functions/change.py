def change( cents ):
    coins = [ 25, 10, 5, 1 ]
    for x in range( 0, 4 ):
        y = divmod( cents, coins[ x ] )
        coins[ x ] = y[ 0 ]
        cents = y[ 1 ]
    return tuple( coins )