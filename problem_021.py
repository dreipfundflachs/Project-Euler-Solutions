#################################
#  PROJECT EULER - PROBLEM 021  #
#################################
import time
from itertools import combinations
from math import prod


def get_primes_up_to(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Eratosthenes' sieve """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            primes.append(k)
            for m in range(k * k, n + 1, k):
                prime_flags[m] = False
    return primes


def get_prime_factors_given_primes(n: int, primes: list[int]) -> list[int]:
    """ Returns the list of all prime factors of n, each prime appearing the
    same number of times as its multiplicity, given a list that includes all
    primes less than n. Example:
    get_prime_factors_given_primes(60, [2, 3, 5, 7, 11]) -> [2, 2, 3, 5]. """
    prime_factors = []
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            prime_factors.append(p)
            n = n // p
    return prime_factors


def get_proper_divisors_given_primes(n: int, primes: list[int]) -> list[int]:
    """ Returns the list of all proper divisors of n (i.e., < n) given a list
    that includes all primes less than n """
    list_of_prime_factors = get_prime_factors_given_primes(n, primes)
    m = len(list_of_prime_factors)
    tuples = set()
    for k in range(1, m):
        new_tuples = set(combinations(list_of_prime_factors, k))
        tuples = tuples.union(new_tuples)
    proper_divisors = [prod(t) for t in tuples]
    proper_divisors.append(1)
    return proper_divisors


def get_sum_of_proper_divisors(n: int, primes: list[int]) -> int:
    """ Returns the sum of all proper divisors of n
    given a list that includes all primes less than n. """
    return sum(get_proper_divisors_given_primes(n, primes))


start = time.time()

N = 10**4
PRIMES = get_primes_up_to(N)

sum_of_amicables = 0
for n in range(1, N):
    m = get_sum_of_proper_divisors(n, PRIMES)
    # m is the only candidate for forming an amicable pair with n.
    if m > n and n == get_sum_of_proper_divisors(m, PRIMES):
        sum_of_amicables += n + m

print(sum_of_amicables)

end = time.time()
print(f"Program runtime: {end - start} seconds")
