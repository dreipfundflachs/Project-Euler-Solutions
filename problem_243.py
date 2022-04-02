#################################
#  PROJECT EULER - PROBLEM 243  #
#################################
import time
from functools import reduce
from itertools import product


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


start = time.time()
N = 10**5
C = 15499 / 94744
primes = prime_sieve(N)

# Given n, the number of irreducible proper fraction having n as denominator is
# given by phi(n), since this counts the number of integers < n which are
# relatively prime to n. We also know that phi(n) / n = PROD (1 - 1/p), where p
# ranges over the set of all primes dividing n. We want to find the smallest n
# for which (phi(n) / n) * (n / (n - 1)) is smaller than a certain constant C.

# It is easy to find some n such that phi(n) / (n - 1) < C. Indeed, n / (n - 1)
# converges to 1 as n -> infinity and to satisfy phi(n) / n < C, we only need
# to select distinct primes p_1, ..., p_r such that PROD_i (1 - 1/p_i) < C, and
# then take n to be their product. Moreover, as p increases, so does (1 - 1/p),
# so the smallest solution to the latter inequality _among numbers of this
# type_ is obtained by taking the primes involved as small as possible. That
# is, a reasonable first guess would be to take n = p_1 * ...  * p_r to be the
# product of the first r primes such that phi(n) / (n - 1) is smaller than C.
# The following piece of code shows that r = 9 (and p_r = 29) works.
prod = 1
phi = 1
for i in range(100):
    prod *= primes[i]
    phi *= (primes[i] - 1)
    if phi / (prod - 1) < C:
        print(i, primes[i])
        break

# We now know that the solution must be at most equal to S = 2 * ... * 29. We
# proceed to analyze if it would be possible to obtain an even smaller solution
# to the inequality phi(n) / (n - 1) < C.

# If n < S is another solution and if it is divisible by q**e for some prime q
# > 29 and e > 0, then at least one of the primes 2, 3, ..., 29, call it p,
# must be missing from the prime factorization of n (otherwise n would be
# greater than S).  But then n' = (p**e/q**e) * n is smaller than n and
# phi(n') / n' = (phi(n) / n) * ((1 - 1/p) / (1 - 1/q)) is also smaller than
# phi(n). On the other hand, (n' / (n' - 1)) / (n / (n - 1)) =
# = ((p**e)/(q**e)) * ((q**e - 1)/(p**e - 1)) = (1 - 1/q**e) / (1 - 1/p**e).
# That is, even though n' / (n' - 1) is greater than n / (n - 1), their
# quotient is at most (1 - 1/q) / (1 - 1/p), so it does not exceed the
# decrease from phi(n) / n to phi(n') / n'. In conclusion, the smallest
# solution cannot by divisible by a prime q > 29 (if it were, we could just
# replace q by a prime p < 29 to reduce n and thereby also reduce or at least
# keep the same ratio phi(n) / (n - 1)).

# Similarly, if some solution n < S does not include a prime q between 2 and 29
# in its factorization, then:
# (i)  It must include all other primes between 2 and 29, otherwise it would
#      fail to be a solution, since phi(n) / n > C;
# (ii) If 29**e is the greatest power of 29 dividing n, with e > 0, then we
#      could find an even smaller solution n' = (q**e / 29**e) * n, by the same
#      argument as above.
# We thus narrow our search for a smaller solution than S to numbers n having
# the form (2 * 3 * ... * 23) * (2**e_2 * 3**e_3 * ... * 23**e_23) for some
# exponents e_2, ..., e_23 >= 0. The factor on the left we will call the
# 'base'.

i_max = i - 1   # i_max is the index of 23 in primes, i.e., i_max = 8
factors = [(p - 1) for p in primes[:i_max + 1]]
base = reduce(lambda x, y: x * y, primes[:i_max + 1])   # base = 2 * ... * 23
phi_base = reduce(lambda x, y: x * y, factors)   # phi_base = phi(base)

# We search for new solutions. They must be smaller than S = base * 29.
least = base * 29
# If n = base * (2**e_2 * 3**e_3 * ... * 23**e_23) < S = base * 29 is a
# solution, then the we must e_2 <= 4, e_3 <= 3, e_5 <= 2 and e_7, ..., e_23 <=
# 1. Let exponents = (e_2, e_3, ..., e_23). We test all possible combinations
# of exponents satisfying these inequalities to see if any of them yields a
# smaller solution.
for exponents in product(range(5), range(4), range(3), range(2), range(2),
                         range(2), range(2), range(2), range(2)):
    n = base
    new_phi = phi_base
    for i in range(i_max + 1):
        n *= primes[i]**exponents[i]
        new_phi *= primes[i]**exponents[i]
    new_resilience = new_phi / (n - 1)
    if new_resilience < C and n < least:
        least = n

print(least)
end = time.time()
print(f"Program runtime: {end - start} seconds")
