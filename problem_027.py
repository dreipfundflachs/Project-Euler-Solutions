#################################
#  PROJECT EULER - PROBLEM 027  #
#################################
import time


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


def get_prime_flags_up_to(n: int) -> list[bool]:
    """ Returns a list prime_flags of n + 1 elements such that
    prime_flags[k] = True if and only if k is a prime number."""
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for m in range(p * p, n + 1, p):
                prime_flags[m] = False
    return prime_flags


def polynomial(a: int, b: int, n: int) -> int:
    """ Computes n**2 + a * n + b. """
    return n**2 + a * n + b


start = time.time()

T = 10**3
M = 10**6
PRIME_FLAGS = get_prime_flags_up_to(M)

max_a = -79
max_b = 1601
max_number_of_primes = 40

# Note that n**2 + a * n + b is prime for n = 0 if and only if b is prime.
# Thus, it suffices to consider only those coefficients b which are prime.
for b in get_primes_up_to(T):
    for a in range(-T + 1, T):
        n = 0
        while PRIME_FLAGS[polynomial(a, b, n)]:
            n += 1
        if n > max_number_of_primes:
            max_number_of_primes = n
            max_a = a
            max_b = b

print(max_a * max_b)

end = time.time()
print(f"Program runtime: {end - start} seconds")
