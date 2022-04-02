# PROJECT EULER PROBLEM
import time
from project_euler import prime_sieve
from itertools import permutations, combinations

start = time.time()
primes = prime_sieve(10**4)
set_of_primes = set(primes)
for p in set_of_primes:
    perms_string = [''.join(perm) for perm in permutations(str(p))]
    perms = [int(number) for number in perms_string]
    for n in perms[:]:
        if n not in set_of_primes:
            perms.remove(n)
    perms = set(perms)
    if len(perms) >= 3:
        perms = list(perms)
        perms.sort()
        triples = list(combinations(perms, 3))
        sorted_triples = [tuple(sorted((k, m, n))) for (k, m, n) in triples]
        set_of_triples = set(sorted_triples)
        for (k, m, n) in set_of_triples:
            d_1 = n - m
            d_2 = m - k
            if d_1 == d_2:
                print(f"{k} and {m} and {n}")


end = time.time()
print(f"Program runtime: {end - start} seconds")
