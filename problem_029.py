#################################
#  PROJECT EULER - PROBLEM 029  #
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


def multiply_second(set_of_tuples: set[(int, int)], b: int)\
        -> frozenset[(int, int)]:
    """ Given set_of_tuples, multiplies the second coordinate
    of each tuple by b; returns a frozenset to avoid the 'not of a hashable
    type' error. """
    new_set = frozenset([(x, y * b) for (x, y) in set_of_tuples])
    return new_set


# Because the numbers involved can be very large, we can substantially speed up
# the computation by representing them conveniently as follows: Given a > 2,
# let a = p_1**e_1 * ... * p_m**e_m be its prime factorization, represented
# by the set of pairs {(p_1, e_1), ..., (p_m, e_m)}. Then the prime
# factorization of a**b is determined by {(p_1, b * e_1), ..., (p_m, b * e_m)}.
# Clearly, two numbers a**b and c**d are equal if and only if they give rise to
# the same sets of this form.

start = time.time()

N = 100
PRIMES = get_primes_up_to(N)

powers = set()
for a in range(2, N + 1):
    tuples = get_prime_tuples_given_primes(a, PRIMES)
    for b in range(2, N + 1):
        powers.add(multiply_second(tuples, b))

print(len(set(powers)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
