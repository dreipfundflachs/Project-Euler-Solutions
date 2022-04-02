###############################
#  PROJECT EULER - PROBLEM 123  #
###############################
import time


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


start = time.time()

N = 10**6
M = 10**10
primes = [-1] + prime_sieve(N)   # We count from the 1st (not 0th) prime

n = 1
# A simple computation using binomial expansion shows that the remainder is
# of (p - 1)**n + (p + 1)**n upon division by p**2 is given by:
# 2 * p if n is odd or 2 if n is even. Thus we need only to consider odd values
# of n. The solution is a straightforward search.

while True:
    remainder = (2 * n * primes[n]) % (primes[n])**2
    if remainder > M:
        print(n)
        break
    n += 2

end = time.time()
print(f"Program runtime: {end - start} seconds")
