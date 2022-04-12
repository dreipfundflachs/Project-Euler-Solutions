#################################
#  PROJECT EULER - PROBLEM 003  #
#################################
import time
from math import isqrt


def get_prime_factors(n: int) -> set[int]:
    """ Returns the list of all prime factors of n. Determines all necessary
    primes on the fly.  """
    factors: set[int] = set()
    square_root = isqrt(n)
    prime_flags: list[bool] = [True] * (square_root + 1)
    prime_flags[0] = False
    prime_flags[1] = False

    for (p, is_prime) in enumerate(prime_flags):
        if n == 1:
            break
        if is_prime:
            for multiple in range(p * p, square_root + 1, p):
                prime_flags[multiple] = False
            while n % p == 0:
                factors.add(p)
                n = n // p

    return factors


start = time.time()

N = 600851475143

print(max(get_prime_factors(N)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
