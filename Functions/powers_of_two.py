def powers_of_two( limit ):
    x, n = 0, 1
    while n < limit:
        yield n
        x += 1
        n = 2 ** x