# PROJECT EULER - PROBLEM 023
import time
from project_euler import prime_sieve
from project_euler import proper_divisors_given_primes as pd


start = time.time()

n = 28123
primes = prime_sieve(n)
abundant = []

for k in range(2, n):
    if sum(pd(k, primes)) > k:
        abundant.append(k)

abundant_sums = []
m = len(abundant)
for i in range(0, m):
    for j in range(i, m):
        current = abundant[i] + abundant[j]
        abundant_sums.append(current)

B = set(abundant_sums)
A = set(range(1, n))
diff = A.difference(B)

print(sum(diff))

end = time.time()
print(f"Program runtime: {end - start} seconds")
