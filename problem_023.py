#################################
#  PROJECT EULER - PROBLEM 023  #
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
    result = [prod(t) for t in tuples]
    result.append(1)
    return result


start = time.time()

N = 28123
PRIMES = get_primes_up_to(N)

# Construct the list of all abundant numbers < N.
abundants = []
for k in range(2, N):
    if sum(get_proper_divisors_given_primes(k, PRIMES)) > k:
        abundants.append(k)

# Construct the list of numbers < N which can be written as the sum of two
# abundant numbers.
sums_of_abundants = []
number_of_abundants = len(abundants)
for i in range(0, number_of_abundants):
    for j in range(i, number_of_abundants):
        sum_of_abundants = abundants[i] + abundants[j]
        if sum_of_abundants < N:
            sums_of_abundants.append(sum_of_abundants)
        else:
            break

# Take the difference of the sets {1,..., N} and {k | k is a sum of abundants}
# and compute the sum of its elements.
non_sums = set(range(1, N)).difference(set(sums_of_abundants))
print(sum(non_sums))

end = time.time()
print(f"Program runtime: {end - start} seconds")
