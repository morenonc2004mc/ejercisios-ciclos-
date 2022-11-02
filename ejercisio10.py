def mcd_euclides(n1, n2):
    while True:
        resta = n1 % n2
        if resta == 0:
            return n2
        else:
            n1 == n2
            n2 == resta
print(mcd_euclides(n1, n2))

    