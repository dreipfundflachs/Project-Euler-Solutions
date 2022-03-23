# PROJECT EULER PROBLEM 075
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

N = 15 * 10**5
perimeters = {}
# Euclid's formula for Pythagorean triples states that any _primitive_
# Pythagorean triple has the form:
# a = m**2 - n**2, b = 2 * m * n and c = m**2 + n**2, where
# (i) 0 < n < m; (ii) exactly one of m, n is even; (iii) gcd(m, n) = 1.
# Thus we begin by generating all of these triples and, in case the resulting
# perimeter is less than the given bound, we take all possible multiples of the
# triple (still under the condition that the resulting perimeter satisfies the
# bound). 

# Notice that since c = m**2 + n**2 must be <= N,
# m must be <= the square root of N.
for m in range(isqrt(N) + 1):
    for n in range(1, m):
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            p = a + b + c
            if p <= N:
                for q in range(p, N + 1, p):
                    if q in perimeters:
                        perimeters[q] += 1
                    else:
                        perimeters[q] = 1

total = 0
# Filter those perimeters which occur exactly once.
for p in perimeters:
    if perimeters[p] == 1:
        total += 1

print(total)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
