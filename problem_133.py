#################################
#  PROJECT EULER - PROBLEM 133  #
#################################
import time
from math import gcd

# Let p be a prime number distinct from 2 and 5.  Suppose that p | R(k) (i.e.,
# p divides R(k)). Then we can write R(2 * k) = 10**k * R(k) + R(k), hence p
# also divides R(2 * k). By induction, using the same argument, one proves:
# (1) If p | R(k), then p | R(m * k) for all m >= 1.
# Let A(p) be the least k such that p | R(k). Then, by (1), p | R(k) for any k
# which is a multiple of A(p). Suppose that p | A(l) for some l which is _not_
# a multiple of A(p), say, l = d * A(p) + r where d, r are integers and
# 1 < r < A(p). Then, since p | R(l) by hypothesis and p | R(d * A(p)), p must
# also divide R(l) - R(d * A(p)) = R(r) * 10**[d * A(p)]. Since p is relatively
# prime to 10 by hypothesis, it divides R(r). This contradicts the minimality
# of A(p), since r < A(p). We thus conclude:
# (2) If p | R(k), then k must be a multiple of A(p).
# And combining (1) and (2):
# (3) p | R(k) if and only if A(p) | k.


def A(n: int) -> int:
    """ Computes the function A described in the problem statement. """
    if gcd(n, 10) != 1:
        return 0
    else:
        k = 1  # number of digits in the repunit
        remainder = 1
        # Note that R(k + 1) = 10 * R(k) + 1, so
        # R(k + 1) % n = (10 * [R(k) % n] + 1) % n, and we can assume that
        # R(k) % n has already been computed. This is efficient because
        # (R(k) % n) is always < n, by definition.
        while remainder != 0:
            k += 1
            remainder = (10 * remainder + 1) % n
    return k


def prime_sieve(N: int) -> list[int]:
    """ Returns a list of all primes <= N using Erasthotenes' sieve """
    primes = []
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, isprime) in enumerate(prime_flags):
        if isprime:
            primes.append(k)
            for multiple in range(k * k, N + 1, k):
                prime_flags[multiple] = False
    return primes


def involves_only(n: int, p: int, q: int) -> bool:
    """ Checks if the prime factors of n all lie in the set {p, q}. """
    while (n % p) == 0:
        n //= p
    while (n % q) == 0:
        n //= q
    if n > 1:
        return False
    else:
        return True


start = time.time()

N = 10**5
PRIMES = prime_sieve(N)
PRIMES.remove(2)
PRIMES.remove(5)

# By the theory above, in particular remark (3), a prime p distinct from 2 and
# 5 will divide R(10**n) for some n if and only if A(p) divides 10**n for some
# n, which in turn occurs if and only if the only prime factors of A(p) are 2
# and 5. Thus, to find the solution we need only check directly for each prime
# (distinct from 2 and 5) if the latter condition fails, and if so we update
# our sum. Finally, we need to add back 2 and 5.
answer = 0
for p in PRIMES:
    if not involves_only(A(p), 2, 5):
        answer += p

print(answer + 2 + 5)
end = time.time()
print(f"Program runtime: {end - start} seconds")
