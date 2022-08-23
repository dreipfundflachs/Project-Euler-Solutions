#################################
#  PROJECT EULER - PROBLEM 086  #
#################################
import time
from math import isqrt, ceil


def is_square(n: int) -> bool:
    """ Decides whether an integer is the square of another integer. """
    m = isqrt(n)  # Requires module 'math'.
    if m**2 == n:
        return True
    else:
        return False


start = time.time()

# We seek triples (a, b, c) such that a <= b <= c. Notice that the three
# possible shortest paths have lengths
#   sqrt(a**2 + (b + c)**2),
#   sqrt(b**2 + (a + c)**2) and
#   sqrt(c**2 + (a + b)**2).
# Clearly, the shortest among them is the third one. To avoid an extra loop,
# we set d = a + b and first find the pairs (c, d) for which c**2 + d**2 is a
# perfect square. Then we count the pairs (a, b) (with d = a + b) for which
# 1 <= a <= b <= c.

L = 10**2
N = 10**6

total = 0
n = 0

while total < N:
    n += 1
    c = n
    # We begin by finding all Pythagorean pairs (c, d = a + b).  The other
    # pairs, for values of c < n, have already been found. Notice that
    # since a <= b <= c, d = a + b can be at most 2 * c.
    c_squared = c**2
    for d in range(2, 2 * c + 1):
        # Check if the smallest distance is an integer.
        if is_square(c_squared + d**2):
            # b must lie between 1 and c, hence b <= c. Also, b <= d - 1,
            # since a + b = d and a >= 1. Therefore
            #   (1) b <= min(c, d - 1).
            # On the other hand, a = d - b must be <= b. Hence d <= 2b and
            #   (2) b >= ceil(d / 2).
            # There are
            #       min(d - 1, c) - ceil(d / 2) + 1
            # numbers b satisfying these inequalities (1) and (2), and any such
            # number yields a valid solution.
            total += min(d - 1, c) - ceil(d / 2) + 1

print(n)

end = time.time()
print(f"Program runtime: {end - start} seconds")
