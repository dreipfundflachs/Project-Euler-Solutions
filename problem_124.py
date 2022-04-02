#################################
#  PROJECT EULER - PROBLEM 124  #
#################################

import time
from functools import reduce


def prime_sieve(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Erasthotenes' sieve """
    primes = []
    flags = [True] * (n+1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if isprime:
            primes.append(k)
            for m in range(k*k, n+1, k):
                flags[m] = False
    return primes


def radical(n: int, primes: set[int]) -> int:
    """
    Returns the radical of n (as described in the statement of problem 124),
    given a list of primes which includes all prime factors of n. """
    prime_factors = set()
    for p in primes:
        if n == 1:
            break
        # If p divides n, keep taking out p until it no longer divides n.
        while n % p == 0:
            prime_factors.add(p)
            n = n // p
    return reduce(lambda x, y: x * y, list(prime_factors))


# The solution is straightforward. We compute
start = time.time()
N = 10**5
primes = prime_sieve(N)
radicals = [(0, 0), (1, 1)]     # Will hold (n, radical(n)) for each n <= N.

for n in range(2, N + 1):
    radicals.append((n, radical(n, primes)))

# Sort the list obtained above by the radicals.
sorted_radicals = sorted(radicals, key=lambda tup: tup[1])
print(sorted_radicals[10**4])

end = time.time()
print(f"Program runtime: {end - start} seconds")
