#################################
#  PROJECT EULER - PROBLEM 130  #
#################################
import time
from math import gcd


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


def composites_rel_prime_to_10(N: int) -> list[int]:
    """ Returns a list of all composite numbers <= N which are relatively prime
    to 10, computed using Erasthotenes' sieve """
    flags = [True] * (N + 1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if isprime:
            for multiple in range(2 * k, N + 1, k):
                flags[multiple] = False
    composite = [n for n in range(2, N + 1)
                 if flags[n] is False and gcd(n, 10) == 1]
    return composite


start = time.time()

N = 10**6
C = 25
CANDIDATES = composites_rel_prime_to_10(N)

count = 0
answer = 0
# Since the bounds involved are low, we can use a straightforward search.
for n in CANDIDATES:
    if (n - 1) % A(n) == 0:
        count += 1
        answer += n
        if count == C:
            break
print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
