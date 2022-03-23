# PROJECT EULER PROBLEM 095
import time
from functools import reduce

start = time.time()
N = 10**6

# Initialize a dictionary listing the proper divisors of all integers <= N.
proper_divisors = {0: [], }
for n in range(N + 1):
    proper_divisors[n] = [1]

# Use a sieve method to obtain the proper divisors of each number.
for d in range(2, N):
    for n in range(2*d, N + 1, d):
    # Start from 2 * d instead of d, because we want only _proper_ divisors.
        (proper_divisors[n]).append(d)

# Obtain the _sum_ of proper divisors of each number.  If a number is such that
# the sum of its proper divisors exceeds N, then set this sum to 0.
sum_of_proper_divisors = [sum(proper_divisors[n]) for n in range(N + 1)]
for n in range(N + 1):
    if sum_of_proper_divisors[n] > N:
        sum_of_proper_divisors[n] = 0

max_chain = [1]
max_length = 1
# For each n, determine the chain starting at n.
for n in range(N + 1):
    current_chain = []
    k = n
    while k not in current_chain:
        current_chain.append(k)
        k = sum_of_proper_divisors[k]
    # Flag the chain and its length if the first (= n) and last (= k) of its
    # members coincide and if its length is greater than the current maximum.
    if k == n and len(current_chain) > max_length:
        max_length = len(current_chain)
        max_chain = current_chain
        print(n, current_chain)

# Print the answer.
print(min(max_chain))

end = time.time()
print(f"Program runtime is: {end - start} seconds")
