#################################
#  PROJECT EULER - PROBLEM 003  #
#################################
import time
from math import isqrt


def get_prime_factors(n: int) -> list[int]:
    """ Returns the list of all prime factors of n, each prime appearing as
    many times as its multiplicity indicates.  Determines all necessary primes
    on the fly. Requires 'isqrt' from module 'math'. """
    assert n >= 1
    prime_factors = []
    N = isqrt(n)
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if n == 1:
            break
        if is_prime:
            for multiple in range(p * p, N + 1, p):
                prime_flags[multiple] = False
            while n % p == 0:
                prime_factors.append(p)
                n = n // p
    if n != 1:
        prime_factors.append(n)

    return prime_factors


start = time.time()

N = 600851475143

print(max(get_prime_factors(N)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
