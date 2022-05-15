#################################
#  PROJECT EULER - PROBLEM 100  #
#################################
import time
from math import isqrt


def gcd(a: int, b:  int) -> int:
    """ Computes the greatest common divisor (gcd) of integers a and b. """
    while b:
        a, b = b, a % b
    return a


# Let b (resp. n) be the number of blue (resp. total) balls. Then we need to
# find solutions to the equation b(b - 1) / (n(n - 1)) = 1 / 2. Given n, this
# is a quadratic equation in b. The solution b will be a positive integer if
# and only if n is such that (1 + 2 * n**2 -2 * n) = (n - 1)**2 + n**2
# is a perfect square. Thus, we have reduced the problem to finding natural
# numbers n such that (n - 1, n) will yield a primitive Pythagorean triple. We
# know that any such triple is given by Euclid's formula:
# a = p**2 - q**2, b = 2 * p * q and c = p**2 + q**2, where p > q have gcd = 1
# and exactly one of them is even. Thus we look for integers p, q satisfying
# all of those conditions and for which in addition either a = b - 1 or
# a = b + 1. Again, solving this for given q yields a quadratic equation in p,
# which can thus easily be solved. For p to be an integer, we must have that
# either 2 * q**2 + 1 or 2 * q**2 - 1 is a perfect square, respectively. Once
# we find the first pair (p, q) satisfying these conditions for which
# n = max(2 * p * q, p**2 - q**2) is larger than the given bound, we are done
# and b is given by the solution of the original quadratic equation.

start = time.time()

N = 10**12

# Since p > q and n or n - 1 = 2 * p * q, it suffices to let q range from 1 to
# isqrt(N), say.
for q in range(1, isqrt(N)):
    delta_1 = 2 * q**2 - 1
    delta_2 = 2 * q**2 + 1
    r_1 = isqrt(delta_1)
    r_2 = isqrt(delta_2)
    # These correspond to the case where a = b - 1 or a = b + 1, respectively.
    # We need to check if one of them is a square.
    if r_1**2 == delta_1:
        p = q + r_1
        is_valid = True
    elif r_2**2 == delta_2:
        p = q + r_2
        is_valid = True
    # If so, and if the other conditions for a primitive Pythagorean triple are
    # satisfied, we compute n.
    if is_valid and gcd(p, q) == 1:
        n = max(2 * p * q, p**2 - q**2)
        # And check if it is greater than N.
        if n > N:
            blues = (2 + isqrt(4 + 8 * n * (n - 1))) // 4
            print(blues)
            break

end = time.time()
print(f"Program runtime: {end - start} seconds")
