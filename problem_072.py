#################################
#  PROJECT EULER - PROBLEM 072  #
#################################
import time

# The number of reduced proper fractions with denominator d > 1 is equal to the
# count of numbers n between 1 and d - 1 which are relatively prime to d. That
# is, it is given by phi(d), where phi is Euler's totient function. It is easy
# to show that:
#   (1) If p is prime, then phi(p) = p - 1.
#   (2) More generally, if p is prime, then
#           phi(p^k) = p^(k - 1) * (p - 1) for any k >= 1.
#   (3) If m and n are relatively prime, then phi(m * n) = phi(m) * phi(n),
#       that is, phi is a multiplicative function.
# From (2) and (3) it follows that
#   (4) If n = p_1^(k_1) ... p_r^(k_r) is the prime factorization of n, then
#           phi(n) = p_1^(k_1 - 1) ... p_r^(k_r - 1) (p_1 - 1) ... (p_r - 1)
#                  = n * product(p - 1 for p prime dividing n)
#                    // product(p for p prime dividing n)
#       where both products are over the _distinct_ prime factors of n, i.e.,
#       without regard to their multiplicities.
#
# Therefore, the idea of the solution is to compute the distinct prime factors
# of all integers n below N = one million, then use the formula in (4) to
# compute the value of phi(n) for such n, and finally take the sum of the
# latter values. We combine the first of these two steps in a single function
# to speed up the computation.


def sieve_phis(N: int) -> list[int]:
    """ Uses sieving to compute phi(n) for all n <= N. Returns the list
        [phi(n) for n in range(N + 1)]. """

    prime_flags = [True for _ in range(N + 1)]
    prime_flags[0], prime_flags[1] = False, False
    phis = [n for n in range(N + 1)]
    phis[1] = 0

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for n in range(p, N + 1, p):
                phis[n] = (phis[n] // p) * (p - 1)
                prime_flags[n] = False
    return phis


start = time.time()

N = 10**6

answer = sum(sieve_phis(N))
print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
