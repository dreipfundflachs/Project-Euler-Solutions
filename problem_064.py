#################################
#  PROJECT EULER - PROBLEM 064  #
#################################

# The efficient algorithm for finding the partial denominators below is taken
# from the section "Canonical form and repetend" of the Wikipedia page:
# https://en.wikipedia.org/wiki/Periodic_continued_fraction
import time
from math import isqrt

start = time.time()

M = 10**2
N = M**2
# We will consider the square root of n only when the latter is not a square.
SQUARES = [n**2 for n in range(M + 1)]
NON_SQUARES = [n for n in range(2, N + 1) if n not in SQUARES]

count = 0
for n in NON_SQUARES:
    a_0 = isqrt(n)

    a = isqrt(n)
    d = 1
    m = 0

    k = 1
    period = 0
    while a != 2 * a_0:
        # The algorithm proceeds by repeated calculation of a (the current
        # partial denominator), d and m, given their previous values according
        # to these formulas and the initial values above (see the Wikipedia
        # article).
        m = d * a - m
        d = (n - m**2) / d
        a = int((a_0 + m) / d)

        period += 1
        k += 1

    if period % 2 == 1:
        count += 1

print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
