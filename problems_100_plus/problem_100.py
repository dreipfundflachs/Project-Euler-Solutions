# PROJECT EULER PROBLEM 100
import time
from math import isqrt


def gcd(a, b):
    """ Computes the gcd of two integers a and b. """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


start = time.time()
N = 10**12

# Let b (resp. n) be the number of blue (resp. total) balls. Then we need to
# find solutions to the equation b(b - 1) / (n(n - 1)) = 1 / 2. Given n, this
# is a quadratic equation in b. The solution b will be a positive integer if
# and only if n is such that (1 + 2 * n**2 -2 * n) = (n - 1)**2 + n**2 
# is a perfect square. Thus, we have reduced the problem to finding natural
# numbers n such that (n - 1, n) will yield a primitive Pythagorean triple. We
# know that any such triple is given by Euclid's formula:
# a = p**2 - q**2, b = 2 * p * q and c = p**2 + q**2 where p > q have gcd = 1
# and exactly one of them is even. Thus we look for integers p, q satisfying
# all of those conditions and for which in addition either a = b - 1 or 
# a = b + 1. Again, solving this for given q yields a quadratic equation in p,
# which can thus easily be solved. For p to be an integer, we must have that
# either 2 * q**2 + 1 or 2 * q**2 - 1 is a perfect square, respectively. Once
# we find the first pair (p, q) satisfying these conditions for which 
# n = max(2 * p * q, p**2 - q**2) is larger than the given bound, we are done
# and b is given by the solution of the original quadratic equation.

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
        valid = True
    elif r_2**2 == delta_2:
        p = q + r_2
        valid = True
    # If so, and if the other conditions for a primitive Pythagorean triple are
    # satisfied, we compute n.
    if gcd(p, q) == 1 and valid == True:
        n = max(2 * p * q, p**2 - q**2)
        # And check if it is greater than N.
        if n > N:
            blue = (2 + isqrt(4 + 8 * n * (n - 1))) // 4
            print(
            f"{blue} blue balls among {n} total balls, "
            + f"with probability {blue * (blue - 1) / ((n -1) * n)}"
            )
            break

end = time.time()
print(f"Program runtime is: {end - start} seconds")
