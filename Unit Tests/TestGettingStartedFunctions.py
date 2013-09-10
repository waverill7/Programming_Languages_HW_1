from pythonwarmup import ( change, strip_vowels, scramble, powers_of_two, powers, interleave, stutter )
import unittest

def anagram( s, t ):
    return sorted( s ) == sorted( t )

def listPowersOfTwo( limit ):
    return [ x for x in powers_of_two( limit ) ]

def listPowers( base, limit ):
    return [ x for x in powers( base, limit ) ]

class TestGettingStartedFunctions( unittest.TestCase ):

    def test_change( self ):
        self.assertEqual( ( 3, 2, 0, 2 ), change( 97 ) )
        self.assertEqual( ( 0, 0, 1, 3 ), change( 8 ) )
        self.assertEqual( ( 10, 0, 0, 0 ), change( 250 ) )
        self.assertEqual( ( 0, 0, 0, 0 ), change( 0 ) )
        self.assertEqual( ( 0, 0, 0, 1 ), change( 1 ) )
        self.assertEqual( ( 0, 0, 1, 0 ), change( 5 ) )
        self.assertEqual( ( 0, 1, 0, 0 ), change( 10 ) )
        self.assertEqual( ( 1, 0, 0, 0 ), change( 25 ) )
        self.assertEqual( ( 39, 2, 0, 4 ), change( 999 ) )
        self.assertEqual( ( 402, 1, 1, 3 ), change( 10068 ) )

    def test_strip_vowels( self ):
        self.assertEqual( 'Hll, wrld', strip_vowels( 'Hello, world' ) )
        self.assertEqual( '', strip_vowels( 'aeiouAEIOU' ) )
        self.assertEqual( 'LL YR BS R BLNG T S', strip_vowels( 'ALL YOUR BASE ARE BELONG TO US' ) )
        self.assertEqual( 'Msssspp', strip_vowels( 'Mississippi' ) )
        self.assertEqual( 'nmtp', strip_vowels( 'onomatopoeia' ) )
        self.assertEqual( '`~1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:,<.>/?', strip_vowels( '`~1!2@3#4$5%6^7&8*9(0)-_=+[{]}\|;:,<.>/?' ) )

    def test_scramble( self ):
        data = [ "a", "rat", "BSOD", "BDFL", "Python testing" ]
        for s in data:
            self.assertTrue( anagram( s, scramble( s ) ) )

    def test_powers_of_two( self ):
        self.assertEqual( [], listPowersOfTwo( 0 ) )
        self.assertEqual( [], listPowersOfTwo( 1 ) )
        self.assertEqual( [ 1 ], listPowersOfTwo( 2 ) )
        self.assertEqual( [], listPowersOfTwo( -10 ) )
        self.assertEqual( [ 1, 2, 4, 8, 16, 32, 64 ], listPowersOfTwo( 70 ) )
        self.assertEqual( [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 ], listPowersOfTwo( 2000 ) )

    def test_powers( self ):
        self.assertEqual( [], listPowers( 0, 1000 ) )
        self.assertEqual( [], listPowers( 1, 1000 ) )
        self.assertEqual( [], listPowers( 1000, 0 ) )
        self.assertEqual( [ 1 ], listPowers( 1000, 1000 ) )
        self.assertEqual( [ 1, 3, 9, 27, 81, 243 ], listPowers( 3, 400 ) )
        self.assertEqual( [], listPowers( -2, 2000 ) )
        self.assertEqual( [], listPowers( -2, -2000 ) )
        self.assertEqual( [], listPowers( 2, -2000 ) )

    def test_interleave( self ):
        self.assertEqual( [], interleave( [], [] ) )
        self.assertEqual( [ 1, 'a', [ 1, 'a' ], ( 1, 'a' ) ], interleave( [ 1, 'a', [ 1, 'a' ], ( 1, 'a' ) ], [] ) )
        self.assertEqual( [ 1, 'a', [ 1, 'a' ], ( 1, 'a' ) ], interleave( [], [ 1, 'a', [ 1, 'a' ], ( 1, 'a' ) ] ) )
        self.assertEqual( [ 0, 1, 2, 3, 4, 5, 6, 7 ], interleave( [ 0, 2, 4, 6 ], [ 1, 3, 5, 7 ] ) )
        self.assertEqual( [ 'a', 1, 'b', 2, True, None ], interleave( [ 'a', 'b' ], [ 1, 2, True, None ] ) )
        self.assertEqual( [ 1, 'a', 2, 'b', True, None ], interleave( [ 1, 2, True, None ], [ 'a', 'b' ] ) )

    def test_stutter( self ):
        self.assertEqual( [ 5, 5, 4, 4, [ 3 ], [ 3 ], 9, 9 ], stutter( [ 5, 4, [ 3 ], 9 ] ) )
        self.assertEqual( [], stutter( [] ) )
        self.assertEqual( [ [], [] ], stutter( [ [] ] ) )
        self.assertEqual( [ [ 'Hello', [ 'World', [ 'Again' ] ] ], [ 'Hello', [ 'World', [ 'Again' ] ] ] ], stutter( [ [ 'Hello', [ 'World', [ 'Again' ] ] ] ] ) )
        self.assertEqual( [  ( 2, 2 ), ( 2, 2 ), [ 2 ], [ 2 ], 2, 2, 2.0, 2.0, '2', '2', { 'two': 2 }, { 'two': 2 }, 2.0j, 2.0j ], stutter( [ ( 2, 2 ), [ 2 ], 2, 2.0, '2', { 'two': 2 }, 2.0j ] ) )

if __name__ == '__main__':
    unittest.main()
