# PROJECT EULER - PROBLEM 077
import time
from project_euler import prime_sieve

start = time.time()

# Initialize the list of ways; for the math to work out, we consider it
# possible to write 0 as a sum of primes in 1 way, so that whenever p is prime,
# we include the sum p = p + 0 as a valid combination (for p prime, this would
# later need to be subtracted as an option, since the problem statement asks
# for a sum of at least *two* primes).
N = 10**3
primes = prime_sieve(N)
ways = [1] + [0] * (N + 1)

# For increasing prime p, to compute the number of ways to write some integer n
# as a sum of primes in which the largest prime is exactly p, we just subtract
# p from n and look at the number of ways to write (n - p) as a sum of primes,
# none of which is greater than p.
for largest_p in primes:
    for n in range(largest_p, N + 1):
        ways[n] += ways[n - largest_p]

# Look for the first number for which the number of ways to write it as a sum
# of primes is greater than 5_000.
for n in range(N):
    if ways[n] > 5_000:
        print(n, ways[n])
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
