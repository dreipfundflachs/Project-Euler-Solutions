#################################
#  PROJECT EULER - PROBLEM 129  #
#################################
import time
from math import gcd

# We will prove the assertion that given n with gcd(n, 10) == 1, there always
# exists k such that R(k) is divisible by n. More importantly, the proof will
# also show that A(n) < n for all n, a fact which is essential to speed up the
# computation below.

# The set of possible remainders of R(k) upon division by n is restricted to
# 0, 1, ..., n - 1. Therefore, as we increase k starting from 1, eventually we
# will obtain the same remainder twice. Let this occur for the first time for
# k = k_1, i.e., suppose that for any k != k' < k_1, (R(k) % n) != (R(k') % n);
# but that (R(k_0) % n) = (R(k_1) % n) for some k_0 < k_1. Notice that k_1 <= n
# by the pigeonhole principle. Then
# (1)  [R(k_1) - R(k_0)] % n = 0.
# Moreover,
# (2)  [R(k_1) - R(k_0)] = (10**k_0) * R(k_1 - k_0),
# and since 10 is a unit in the ring Z_n (because gcd(n, 10) = 1 by
# hypothesis), it follows from (1) and (2) that
# (3) R(k_1 - k_0) % n = 0
# as well. We conclude that for some k < n (_strictly_ less than n!), R(k) is
# divisible by n. This proves our claim and also establishes that A(n) < n.


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
# all n (as proved above), if n <= 10**6 + 1, then A(n) <= 10**6.
n = N + 2
while True:
    if A(n) > N:
        print(n)
        break
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
