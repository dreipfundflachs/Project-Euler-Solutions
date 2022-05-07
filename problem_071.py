#################################
#  PROJECT EULER - PROBLEM 071  #
#################################
import time


def gcd(a: int, b:  int) -> int:
    """ Computes the greatest common divisor (gcd) of integers a and b. """
    while b:
        a, b = b, a % b
    return a


start = time.time()

N = 10**6

max_frac = 0

# For each denominator q from 8 to N, obtain the best approximation to the
# solution p of p / q = 3 / 7 from below. Starting from the latter, we
# repeatedly decrease p by 1 if necessary until gcd(p, q) == 1. If the
# resulting fraction exceeds the largest reduced fraction < 3 / 7 obtained so
# far, we store the former as the new largest reduced fraction.

for q in range(8, N + 1):
    p = 3 * q // 7
    while gcd(q, p) != 1:
        p -= 1
    frac = p / q
    if frac > max_frac:
        max_p = p
        max_frac = frac

print(max_p)

end = time.time()
print(f"Program runtime: {end - start} seconds")
