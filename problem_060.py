# PROJECT EULER PROBLEM 060
import time
from project_euler import prime_sieve, is_prime_simple
from itertools import combinations


start = time.time()
n = 10_000
primes = prime_sieve(n)

quints = list(combinations(primes, 5))
for sequence in quints:
    pairs = list(combinations(list(sequence), 2))
    active = True
    for (p, q) in pairs:
        pq = int(str(p) + str(q))
        qp = int(str(q) + str(p))
        if not(is_prime_simple(pq) and is_prime_simple(qp)):
            active = False
            break
    if active == True:
        print(pairs)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
