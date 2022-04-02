###############################
#  PROJECT EULER - PROBLEM 110  #
###############################

# First note that x, y must be greater than n. Hence we can write them in the
# form x = n + a and y = n + b for some integers a, b > 0. The original
# equation is equivalent to (n + a + n + b) / ((n + a) * (n + b)) = 1 / n,
# or n * (2 * n + a + b) = (n + a) * (n + b), or yet
# n ** 2 = a * b. Thus the number of solutions equals the number of pairs of
# divisors (a, b) of n**2 such that a * b = n**2.

# If n = p_1**m_1 * ... * p_r**m_r is the prime factorization of n, then that
# of n**2 is n**2 = p_1**(2 * m_1) * ... * p_r**(2 * m_r), and the total
# number of divisors of n**2 is the product of the number of ways we can choose
# these multiplicities, from 0 to 2 * m_k in the case of p_k. That is, we have
# d = (2 * m_1 + 1) * ... * (2 * m_r + 1) divisors of n**2 (incl. 1 and n**2).
# Each such divisor a has a 'complement' b = n**2 / a, except that the
# complement of n is itself. We are only interested in sets of the form {a, b}
# where a and b are complementary, so the number of such sets is given by
# number_of_sol = d // 2 + 1 = (d + 1) // 2 (note that d is always odd).

# We seek the smallest n for which the number_of_sol is greater than one
# thousand. If we take m_1 = m_2 = ... = m_r = 1, we will have
# 3**r // 2 + 1 solutions. The smallest r for which this number exceeds one
# thousand is r = 7. Thus certainly n_0 = 2 * 3 * 5 * 7 * 11 * 13 * 17 (the
# product of the first 7 primes, all with multiplicity 1) yields more than one
# thousand solutions. There is no advantage in considering numbers whose prime
# factors are not included in {2, 3, 5, 7, 11, 13, 17} and no point in
# considering values of n greater than n_0. This narrows our search
# sufficiently to obtain the answer in reasonable time.

import time


def prime_sieve(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Erasthotenes' sieve """
    primes = []
    flags = [True] * (n+1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if isprime:
            primes.append(k)
            for m in range(k*k, n+1, k):
                flags[m] = False
    return primes


def divisor_count_square(n: int, primes: list[int]) -> int:
    """ Counts the number of divisors of n,
        including 1 and the number itself.
    """
    prod = 1
    for p in primes:
        if n == 1:
            break
        multiplicity = 0
        while (n % p) == 0:
            multiplicity += 1
            n //= p
        prod *= (2 * multiplicity + 1)
    return prod


start = time.time()

P = 17
T = 10**3
primes = prime_sieve(P)
n = 2
while True:
    d = divisor_count_square(n, primes) // 2 + 1
    if d > T:
        print(n)
        break
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
