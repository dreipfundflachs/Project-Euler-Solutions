# PROJECT EULER PROBLEM 072
import time
from functools import reduce
from project_euler import prime_sieve


def prime_factors_given_primes(n, primes):
    """
    Given a list including all primes less than n, returns a dictionary
    containing of all prime factors of n and their respective multiplicities.
    Ex.: prime_factors(60, [2, 3, 5, 7, 11]) -> {2: 2, 3: 1, 5: 1}
    """
    prime_factors = []
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            prime_factors.append(p)
            n = n // p
    primes_dict = {}
    for p in set(prime_factors):
        primes_dict[p] = prime_factors.count(p)
    return primes_dict


def phi(n):
    """ Computes phi(n), where phi is Euler's totient function."""
    prime_factors = prime_factors_given_primes(n, primes)
    totient = 1
    for p in prime_factors:
        totient *= p**(prime_factors[p] - 1) * (p - 1)
    return totient


start = time.time()
N = 10**6
primes = prime_sieve(N)
total = 0
for n in range(2, N + 1):
    total += phi(n)

print(total)
end = time.time()
print(f"Program runtime: {end - start} seconds")
