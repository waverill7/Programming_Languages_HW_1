def powers( base, limit ):
    x, n = 0, 1
    if base > 1:
        while n < limit:
            yield n
            x += 1
            n = base ** x