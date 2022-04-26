# PROJECT EULER - PROBLEM 060
import time
from itertools import combinations


def get_prime_flags_up_to(n: int) -> list[bool]:
    """ Returns a list prime_flags of n + 1 elements such that
    prime_flags[k] is True if and only if k is a prime number."""
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(p * p, n + 1, p):
                prime_flags[multiple] = False
    return prime_flags


start = time.time()
N = 10**3
PRIME_FLAGS = get_prime_flags_up_to(N)
PRIMES = [p for p in range(N) if PRIME_FLAGS[p]]

quints = list(combinations(PRIMES, 5))
for sequence in quints:
    pairs = combinations(list(sequence), 2)
    found_solution = True
    for (p, q) in pairs:
        pq = int(str(p) + str(q))
        qp = int(str(q) + str(p))
        if not PRIME_FLAGS[pq] or not PRIME_FLAGS[qp]:
            found_solution = False
            break
    if found_solution:
        print(sequence)

end = time.time()
print(f"Program runtime: {end - start} seconds")
