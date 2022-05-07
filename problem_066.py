#################################
#  PROJECT EULER - PROBLEM 066  #
#################################
import time
from math import isqrt
# The efficient algorithm for finding the partial denominators below is taken
# from the section "Canonical form and repetend" of the Wikipedia page:
# https://en.wikipedia.org/wiki/Periodic_continued_fraction


start = time.time()

M = 10**2
N = 10**3
SQUARES = [n**2 for n in range(M + 1)]
NON_SQUARES = [n for n in range(2, N + 1) if n not in SQUARES]

max_n = 0
max_solution = 0

for n in NON_SQUARES:
    p = []  # p[k] will be the numerator of the k-th convergent
    q = []  # q[k] will be the denominatro of the k-th convergent
    # We compute p[0], p[1], q[0] and q[1] outside of the loop to avoid
    # negative indices in our list.
    p.append(isqrt(n))
    q.append(1)

    a_0 = isqrt(n)
    a = isqrt(n)
    m = isqrt(n)
    d = (n - m**2)
    a = int(2 * a / d)
    p.append(a * a_0 + 1)
    q.append(a)

    # For k >= 2, we calculate p[k] and q[k] according to the formulas:
    # p[k] = a_k * p[k - 1] + p[k - 2] and q[k] = a_j * q[k - 1] + q[k - 2]
    k = 2
    period = 1
    while p[k - 1]**2 - n * q[k - 1]**2 != 1:
        # The algorithm to find a = a_k proceeds by repeatedly updating the
        # values a, d and m, given their previous values according to the
        # three formulas immediately below (cf. the Wikipedia article).
        m = d * a - m
        d = (n - m**2) / d
        a = int((a_0 + m) / d)

        p.append(a * p[k - 1] + p[k - 2])
        q.append(a * q[k - 1] + q[k - 2])
        period += 1
        k += 1
    if p[k - 1] > max_solution:
        max_solution = p[k - 1]
        max_n = n

print(max_n)

end = time.time()
print(f"Program runtime: {end - start} seconds")
