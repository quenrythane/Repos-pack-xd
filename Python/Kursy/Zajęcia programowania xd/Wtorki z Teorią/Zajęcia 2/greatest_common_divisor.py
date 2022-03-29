# Jak znaleźć największy wspólny dzielnik 2 liczb? -> Algorytm Euklidesa
"""
https://pl.wikipedia.org/wiki/Algorytm_Euklidesa
"""


def euklides(a, b):
    # a, b = max(a, b), min(a, b)  # set a as bigger number, b as smaller  # it's not necessary  cause they will change positions if a > b
    r = 1
    while r != 0:
        r = a % b
        a, b = b, r
    return a


print(euklides(105, 252))
