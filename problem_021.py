# PROJECT EULER PROBLEM 21
import time
import itertools
import math


def prime_sieve(n):
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


def prime_factors(n, primes):
    """
    Returns the list of all prime factors of n,
    each prime appearing the same number of times as its multiplicity,
    given a list that includes all primes less than n
    Ex.: prime_factors(60, [2, 3, 5, 7, 11]) -> [2, 2, 3, 5]
    """
    prime_factors = []
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            prime_factors.append(p)
            n = n // p
    return prime_factors


def proper_divisors(n, primes):
    """
    Returns the list of all divisors of n
    given a list that includes all primes less than n
    """
    list_of_prime_factors = prime_factors(n, primes)
    m = len(list_of_prime_factors)
    tuples = set()
    for k in range(1, m):
        new_tuples = set(itertools.combinations(list_of_prime_factors, k))
        tuples = tuples.union(new_tuples)
    result = [math.prod(t) for t in tuples]
    result.append(1)
    return result


def sum_of_proper_divisors(n, primes):
    """
    Returns the sum of all proper divisors of n
    given a list that includes all primes less than n
    """
    return(sum(proper_divisors(n, primes)))


start = time.time()
list_of_primes = prime_sieve(10_000)
amicable = 0
print(sum_of_proper_divisors(220, list_of_primes))
print(sum_of_proper_divisors(284, list_of_primes))
for n in range(1, 10_000):
    m = sum_of_proper_divisors(n, list_of_primes)
    if m > n:
        s = sum_of_proper_divisors(m, list_of_primes)
        if s == n:
            amicable += n + m
print(amicable)
end = time.time()
print(f"Program runtime: {end - start} seconds")
