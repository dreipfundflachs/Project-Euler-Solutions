#################################
#  PROJECT EULER - PROBLEM 046  #
#################################
import time
from math import isqrt


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


def is_square(n: int) -> bool:
    """ Decides whether an integer is the square of another integer. """
    m = isqrt(n)
    if m**2 == n:
        return True
    else:
        return False


start = time.time()

N = 10**4
PRIME_FLAGS = get_prime_flags_up_to(N)
PRIMES = [k for k in range(2, N) if PRIME_FLAGS[k]]
ODD_COMPOSITES = [k for k in range(3, N, 2) if not PRIME_FLAGS[k]]

for n in ODD_COMPOSITES:
    satisfies_conjecture = False
    for p in PRIMES:
        if p > n:
            break
        d = (n - p) // 2
        if is_square(d):
            satisfies_conjecture = True
            break
    if not satisfies_conjecture:
        print(n)
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
