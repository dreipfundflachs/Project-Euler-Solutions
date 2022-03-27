# PROJECT EULER PROBLEM 206
import time
from math import isqrt

# If the square of a number a ends in 0, then a must also end in 0. Hence a can
# be written as 10 * b for some b. Then a**2 = 100 * b**2, so that a**2 ends in
# 00 and we are reduced to finding a natural number b such that b**2 is a**2
# (whose form was given), truncated at the last the two digits. That is, it
# suffices to search for b such that b**2 has the form 1x2x3x4x5x6x7x8x9 and,
# after b has been found, to multiply it by 10 to obtain the solution a.


def check(k: int) -> bool:
    """ Check if the string s (thought to represent the number b)
    has the required form. """
    s = str(k)
    for d in range(9):
        if s[2 * d] != str(d + 1):
            return False
    return True


start = time.time()

N = isqrt(19293949596979899)
# The number inside parentheses is the largest number that can be the square
# of b, in the above notation.

for b in reversed(range(1, N + 1, 2)):
    if check(b**2):
        print(10 * b)
        break

end = time.time()
print(f"Program runtime is: {end - start} seconds")
