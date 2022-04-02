# PROJECT EULER PROBLEM 071
import time


def gcd(a, b):
    """ Computes the greatest common divisor (gcd) of integers a and b. """
    if b == 0:
        return a
    if a == 0:
        return b
    try:
        if a >= b:
            return gcd(b, a % b)
        else:
            return gcd(a, b % a)
    except ValueError:
        print(f"The arguments must be integers!")


start = time.time()
C = 10**6
max_p = 2
max_q = 5
max_frac = max_p / max_q

# For each denominator q from 8 to C, obtain the best approximation to the
# solution p of p / q = 3 / 7 from below. Starting from the latter, we
# repeatedly decrease p by 1 if necessary until gcd(p, q) == 1. Then we compare
# the resulting fraction to the previous greatest reduced fraction < 3 / 7. If
# it exceeds this previous fraction, we record it.
for q in range(8, C + 1):
    p = 3 * q // 7
    while gcd(q, p) != 1:
        p -= 1
    frac = p / q
    if frac > max_frac:
        max_p = p
        max_q = q
        max_frac = frac

print(max_p, max_q, max_frac)

end = time.time()
print(f"Program runtime: {end - start} seconds")
