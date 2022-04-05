#################################
#  PROJECT EULER - PROBLEM 129  #
#################################
import time
from math import gcd

# We will prove the assertion that given n with gcd(n, 10) = 1, there always
# exists k such that R(k) is divisible by n. More importantly, the proof will
# actually show that A(n) < n for all n, a fact which is essential to speed up
# the computation below.

# The set of possible remainders of R(k) upon division by n is restricted to
# 0, 1, ..., n - 1. Suppose that, as we increase k from 1 to n, the remainder
# [R(k) % n] is never 0. Then by the pigeonhole principle, as we increase k
# starting from 1, we will obtain the same (non-zero) remainder twice after at
# most n steps.  Let this occur for the first time for k_1 <= n, i.e., suppose
# that for any
# k != k' < k_1, [R(k) % n] != [R(k') % n]; but that
# (R(k_0) % n) = [R(k_1) % n] for some 1 <= k_0 < k_1 <= n. Then
# (1)  [R(k_1) - R(k_0)] % n = 0.
# Moreover,
# (2)  [R(k_1) - R(k_0)] = (10**k_0) * R(k_1 - k_0),
# and since gcd(n, 10) = 1 by hypothesis, it follows from (1) and (2) that
# (3) R(k_1 - k_0) % n = 0
# as well. We conclude that for some k < n (_strictly_ less than n), R(k) is
# divisible by n. This proves the claim in the statement of the problem and
# also establishes that A(n) < n.


def A(n: int) -> int:
    """ Computes the function A described in the problem statement. """
    if gcd(n, 10) != 1:
        return 0
    else:
        k = 1  # number of digits in the repunit
        remainder = 1
        # Note that R(k + 1) = 10 * R(k) + 1, so
        # R(k + 1) % n = (10 * [R(k) % n] + 1) % n, and we can assume that
        # R(k) % n has already been computed. This is efficient because
        # (R(k) % n) is always < n, by definition.
        while remainder != 0:
            k += 1
            remainder = (10 * remainder + 1) % n
    return k


start = time.time()

N = 10**6

# Because the computation of A(n) is reasonably fast, we can just use a
# straightforward search, starting from N = 10**6 + 2, since, as A(n) < n for
# all n (established above), if n <= 10**6 + 1, then A(n) <= 10**6.
n = N + 2
while True:
    if A(n) > N:
        print(n)
        break
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
