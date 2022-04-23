#################################
#  PROJECT EULER - PROBLEM 049  #
#################################
import time
from itertools import permutations, combinations


def get_prime_flags_up_to(n: int) -> list[bool]:
    """ Returns a list prime_flags of n + 1 elements such that
    prime_flags[k] = True if and only if k is a prime number."""
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(p * p, n + 1, p):
                prime_flags[multiple] = False
    return prime_flags


start = time.time()

M = 10**3
N = 10**4
PRIME_FLAGS = get_prime_flags_up_to(N)
PRIMES = [p for p in range(M, N) if PRIME_FLAGS[p]]

found_solution = False
for p in PRIMES:
    permutations_of_p = [int(''.join(perm)) for perm in permutations(str(p))]
    for n in permutations_of_p[:]:
        if not PRIME_FLAGS[n] or n < M:
            permutations_of_p.remove(n)
    # Remove duplicates from the list of permutations of the digits of p:
    permutations_of_p = list(set(permutations_of_p))
    # If there are at least three prime numbers obtained by permuting the
    # digits of p:
    if len(permutations_of_p) >= 3:
        # Sort them and extract all possible triples we can form using them:
        permutations_of_p.sort()
        triples = set(combinations(permutations_of_p, 3))
        # If one of these triples is in arithmetic progression, and if the
        # smallest of the three numbers is != 1487, we have found the solution.
        for (k, m, n) in triples:
            if k != 1487:
                diff_1 = n - m
                diff_2 = m - k
                if diff_1 == diff_2:
                    print(f"{k} and {m} and {n}")
                    found_solution = True
    if found_solution:
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
