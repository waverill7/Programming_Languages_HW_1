def strip_vowels( s ):
    vowels = 'aeiou'
    vowels += vowels.upper()
    result = ''
    for c in s:
        if c not in vowels:
            result += c
    return result