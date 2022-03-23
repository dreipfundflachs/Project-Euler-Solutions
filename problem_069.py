# PROJECT EULER PROBLEM 069
import time
from project_euler import prime_sieve
from functools import reduce

# The key fact is that phi is a multiplicative function in the sense that
# phi(ab) = phi(a) * phi(b) provided that a, b are relatively prime. This
# follows from the Chinese Remainder Theorem, which says that Z/(ab) is
# isomorphic to Z/(a) x Z/(b), and in particular their respective sets of
# _invertible_ elements (under multiplication) are in bijection.

# Now the set of invertible elements in Z/(ab) corresponds to those numbers <
# ab which are relatively prime to ab. Similarly, those in Z/(a) x Z/(b)
# correspond to products p * q where p is rel. prime to a and q is rel. prime
# to q. Therefore phi(ab) = phi(a) * phi(b).

# It follows that if n = p_1^(k_1) * ... * p_m^(k_m), then 
# phi(n) = phi(p_1^(k_1)) * ... * phi(p_m^(k_m)). If p is prime and m > 0, it
# is easy to see directly that phi(p^m) = p^m - p^(m-1) = p^m (1 - 1/p). Thus
# in general, for n as above,
# phi(n) = n * (1 - 1/p_1) * ... * (1 - 1/p_m).
# Finally, n / phi(n) = [(1 - 1/p_1) * ... * (1 - 1/p_m)]^(-1). To maximize
# this quantity, one needs to make the product in brackets as large as
# possible, by choosing as many primes as possible, and choosing them as small
# as possible. Thus to solve the problem, one just needs to take n equal to the
# maximum product of prime numbers (in increasing order) which is still less
# than 10**6.

start = time.time()
primes = prime_sieve(1000)
prod = 1
bound = 1

# Find the last first m for which p_0 * ... * p_m > 10**6.
for m, p in enumerate(primes):
    prod *= p
    if prod > 10**6:
        bound = m
        break

# Compute the product p_0 * ... * p_(m-1).
print(reduce(lambda x, y: x * y, primes[:bound]))
print(primes[:bound])

end = time.time()
print(f"Program runtime is: {end - start} seconds")
