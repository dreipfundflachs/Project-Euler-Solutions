#################################
#  PROJECT EULER - PROBLEM 072  #
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
            for multiple in range(k * k, n + 1, k):
                prime_flags[multiple] = False
    return primes


def get_prime_tuples_given_primes(n: int, primes: list[int]) -> set[int]:
    """ Returns the set of all prime factors of n in tuple form, given a list
    that includes all primes less than n. Example:
    prime_factors(60, [2, 3, 5, 7, 11]) -> {(2,2), (3,1), (5, 1)}. """
    prime_tuples = set()
    for p in primes:
        if n == 1:
            break
        multiplicity = 0
        while n % p == 0:
            n = n // p
            multiplicity += 1
        if multiplicity > 0:
            prime_tuples.add((p, multiplicity))
    return prime_tuples


def phi(n: int) -> int:
    """ Computes phi(n), where phi is Euler's totient function."""
    prime_factors = get_prime_tuples_given_primes(n, primes)
    totient = 1
    for (p, mult) in prime_factors:
        totient *= p**(mult - 1) * (p - 1)
    return totient


start = time.time()
N = 10**6

primes = get_primes_up_to(N)
total = 0

for n in range(2, N + 1):
    total += phi(n)

print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
