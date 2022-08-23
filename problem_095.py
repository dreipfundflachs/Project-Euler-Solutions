#################################
#  PROJECT EULER - PROBLEM 095  #
#################################
import time


start = time.time()
N = 10**6

# Use a sieving method to obtain the sum of proper divisors of each number.
sum_of_proper_divisors = [1 for k in range(N + 1)]
for d in range(2, N + 1):
    for n in range(2 * d, N + 1, d):
        # Starting from 2 * d because we want only _proper_ divisors.
        sum_of_proper_divisors[n] += d

# If a number is such that the sum of its proper divisors exceeds N, then set
# this sum to 0.
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
    # Store the chain and its length if the first (= n) and last (= k) of its
    # members coincide and its length is greater than the current maximum.
    if k == n and len(current_chain) > max_length:
        max_length = len(current_chain)
        max_chain = current_chain

print(min(max_chain))

end = time.time()
print(f"Program runtime: {end - start} seconds")
