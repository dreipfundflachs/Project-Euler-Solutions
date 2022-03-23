# PROJECT EULER PROBLEM 076

import time

# Initialize the number of ways in which all integers <= N can be written as a
# sum of positive integers (possibly a single integer). For the math to work
# out, we also set ways[0] = 1. Later on we need to subtract 1 from ways[n] for
# all n since the problem statement explicitly excludes the case where there is
# a single summand.
start = time.time()
N = 100
ways = [1] * (N + 1)

# For increasing k and n >= k, compute the number of ways that n can be written
# as a sum of positive integers in which the largest summand is exactly k by
# subtracting k from n and referring to the number of ways to write (n - k) as
# a sum of integers, none of which is larger than k (which has been calculated
# previously).
for largest_k in range(2, N + 1):
    for n in range(largest_k, N + 1):
        ways[n] += ways[n - largest_k]

# Subtract 1 from the number of ways to discard the sum 100 = 0 + 100.
print(ways[100] - 1)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
