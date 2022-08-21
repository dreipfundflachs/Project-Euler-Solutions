#################################
#  PROJECT EULER - PROBLEM 023  #
#################################
import time
from itertools import combinations
from math import prod


def sieve_prime_factors(N: int) -> list[list[int]]:
    """ For each integer n <= N, uses a sieving method to compute the list of
    all prime factors of n, each prime being repeated as many times as its
    multiplicity. For example:
        sieve_prime_factors(6) = [[], [], [2], [3], [2, 2], [5], [2, 3]]
    """
    prime_flags = [True for _ in range(N + 1)]
    prime_flags[0], prime_flags[1] = False, False
    prime_factors = [[] for _ in range(N + 1)]

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for m in range(p, N + 1, p):
                prime_factors[m].append(p)
                prime_flags[m] = False
            k = 2
            while (q := p**k) <= N:
                for m in range(q, N + 1, q):
                    prime_factors[m].append(p)
                k += 1
    return prime_factors


def sieve_proper_divisors(N: int) -> list[list[int]]:
    """ For each integer n <= N, computes the list of all _proper_ divisors of
    n, i.e., including 1 but excluding n. Requires the function
    'sieve_prime_factors'. For example:
        f(6) = [[[], [1], [1], [1], [1, 2], [1], [3, 1, 2]]
    Note that the divisors are not necessarily listed in increasing order. """
    list_of_prime_factors = sieve_prime_factors(N)
    list_of_divisors = [[] for _ in range(N + 1)]
    list_of_divisors[1] = [1]
    for n in range(2, N + 1):
        m = len(list_of_prime_factors[n])
        tuples = set()
        for k in range(0, m):
            new_tuples = set(combinations(list_of_prime_factors[n], k))
            tuples = tuples.union(new_tuples)
        divisors_of_n = [prod(t) for t in tuples]
        list_of_divisors[n] = divisors_of_n
    return list_of_divisors


start = time.time()

N = 28123
LIST_OF_DIVISORS = sieve_proper_divisors(N)

# Construct the list of all abundant numbers < N.
abundants = []
for k in range(2, N):
    if sum(LIST_OF_DIVISORS[k]) > k:
        abundants.append(k)

# Find all numbers < N which can be written as the sum of two abundant numbers
# and record the corresponding flag (T or F) in a list.
sum_of_abundants_flags = [False for k in range(N)]
number_of_abundants = len(abundants)

for i in range(0, number_of_abundants):
    abundants_i = abundants[i]
    for j in range(i, number_of_abundants):
        s = abundants_i + abundants[j]
        if s < N:
            sum_of_abundants_flags[s] = True
        else:
            break

answer = sum(k for k in range(N) if not sum_of_abundants_flags[k])
print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
