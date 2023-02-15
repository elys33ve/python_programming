# Programming challenge 1
from fractions import Fraction
from math import ceil


# calculates and returns fraction (n/d) as string of integer reciprocals 
def egypt(n, d):        # numerator, denominator
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """
    x = []

    while (n > 0):
            nxt = ceil(d/n)
            x.append(str(Fraction(1,nxt)))

            # remaining fraction
            n = n * nxt - d
            d = d * nxt

            f = Fraction(n,d)
            n = f.numerator
            d = f.denominator

            # check if last fraction
            if n == 1:
                x.append(str(Fraction(1,d)))
                break

    return ' + '.join(x)


import doctest
if __name__ == "__main__":
    #print(egypt(103,104))
    doctest.testmod(verbose=True)
