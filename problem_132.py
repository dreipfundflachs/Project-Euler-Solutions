#################################
#  PROJECT EULER - PROBLEM 132  #
#################################
import time
from math import gcd

# Let p be a prime number distinct from 2 and 5.  Suppose that p | R(k) (i.e.,
# p divides R(k)). Then we can write R(2 * k) = 10**k * R(k) + R(k), hence p
# also divides R(2 * k). By induction, using the same argument, one proves:
# (1) If p | R(k), then p | R(m * k) for all m >= 1.
# Let A(p) be the least k such that p | R(k). Then, by (1), p | R(k) for any k
# which is a multiple of A(p). Suppose that p | R(l) for some l which is _not_
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
        # [R(k) % n] is always < n, by definition.
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


start = time.time()

N = 10**6
PRIMES = prime_sieve(N)
PRIMES.remove(2)
PRIMES.remove(5)

# By remark (3) above, we need only search for the primes distinct from 2, 5
# for which A(p) divides 10**9, then take their sum.
answer = 0
count = 0
for p in PRIMES:
    if (10**9 % A(p)) == 0:
        answer += p
        count += 1
        if count == 40:
            print(answer)
            break

end = time.time()
print(f"Program runtime: {end - start} seconds")