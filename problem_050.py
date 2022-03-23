# PROJECT EULER PROBLEM 050
import time
from project_euler import prime_sieve

start = time.time()
n = 10**6
primes = prime_sieve(n)
m = len(primes)
sum_of_primes = []
set_of_primes = set(primes)

i = 0
for i in range(m):
    j = i + 1
    s = primes[i]
    while j < m and s < n:
        s += primes[j]
        if s in set_of_primes:
            sum_of_primes.append((s, j - i + 1))
        j += 1

max_count = 1
max_prime = 0
for (p, c) in sum_of_primes:
    if c > max_count:
        max_count = c
        max_prime = p
# print(sum_of_primes)

message = f"""
The prime under one million which can be written as the sum of
the greatest number of consecutive primes is {max_prime}, which can
be written as the sum of {max_count} primes.
"""
print(message)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
