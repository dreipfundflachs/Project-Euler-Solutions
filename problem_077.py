#################################
#  PROJECT EULER - PROBLEM 077  #
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


start = time.time()

N = 10**3
C = 5 * 10**3
PRIMES = get_primes_up_to(N)

# Begin by initializing a list to hold the number of ways in which all integers
# <= N can be written as a sum of primes (possibly a single prime). For the
# math to work out, we also set ways[0] = 1.

ways = [1] + [0] * (N + 1)
# For increasing prime p, to compute the number of ways to write some integer n
# as a sum of primes in which the largest prime is exactly p, we just subtract
# p from n and consider the number of ways to write (n - p) as a sum of primes,
# none of which is greater than p.
for largest_p in PRIMES:
    for n in range(largest_p, N + 1):
        ways[n] += ways[n - largest_p]

# Look for the first number for which the number of ways to write it as a sum
# of primes is greater than C.
for n in range(N):
    if ways[n] > C:
        print(n)
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
