#################################
#  PROJECT EULER - PROBLEM 127  #
#################################
import time
from functools import reduce
from math import gcd


def radical(n: int, primes: list[int]) -> int:
    """ Computes the radical of an integer n (the product of each of its prime
    factors), given a list of primes which includes all prime factors of n. """
    prime_factors = {1}
    for p in primes:
        if n == 1:
            break
        while (n % p) == 0:
            n //= p
            prime_factors.add(p)
    return reduce(lambda x, y: x * y, prime_factors)


def radical_set_sieve(N: int) -> list[int]:
    """ Returns a set whose n-th element is the set of all prime factors of n,
    for each n <= N.  """
    primes = []
    flags = [True] * (N + 1)
    flags[0] = False
    flags[1] = False
    radicals = [set() for n in range(N + 1)]
    radicals[0] = {1}
    radicals[1] = {1}
    for (k, isprime) in enumerate(flags):
        if isprime:
            primes.append(k)
            for multiple in range(k * k, N + 1, k):
                flags[multiple] = False
            for multiple in range(k, N + 1, k):
                (radicals[multiple]).add(k)
    return radicals


def radical_sieve(N: int) -> list[int]:
    """ Returns a list whose n-th element is the radical of n for each n <= N.
    """
    flags = [True] * (N + 1)
    flags[0] = False
    flags[1] = False
    radicals = [1] * (N + 1)
    for (k, isprime) in enumerate(flags):
        if isprime:
            for multiple in range(k * k, N + 1, k):
                flags[multiple] = False
            for multiple in range(k, N + 1, k):
                radicals[multiple] *= k
    return radicals


def product(set_of_integers: set[int]) -> int:
    """ Takes a set of integers and returns their product """
    product = 1
    for k in set_of_integers:
        product *= k
    return product


start = time.time()

N = 120_000
radicals = radical_sieve(N)
sorted_radicals = sorted([(n, radicals[n]) for n in range(1, N + 1)],
                         key=lambda tup: tup[1])
total = 0
for c in range(3, N + 1):
    for (a, rad_a) in sorted_radicals:
        rad = rad_a * radicals[c]
        if rad >= c:
            break
        else:
            b = c - a
            rad_b = radicals[b]
            if a < b and rad * rad_b < c and gcd(rad_a, rad_b) == 1:
                total += c

print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
