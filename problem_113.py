# PROJECT EULER PROBLEM 113
import time

# We begin by initializing two lists of lists, increasing and decreasing,
# where, e.g., increasing[n][d] will equal the total number of numbers having
# n digits and whose trailing digit is d. The key idea is that to compute it,
# it suffices to determine increasing[n - 1][i] for each i <= d, because each
# such number is obtained from an increasing number of (n - 1) digits by
# appending a d at the end. In other words, the key property is that
# 'increasing' and 'decreasing' are inherited by substrings.

start = time.time()
N = 100
# There are no numbers having 0 digits, so we begin by setting:
increasing = [[]]
decreasing = [[]]

# Append the list which counts increasing (resp. decreasing) numbers having 1
# digit only:
increasing.append([0] + [1] * 9)
decreasing.append([0] + [1] * 9)

# For each 2 <= n <= N, compute the number of increasing (resp. decreasing)
# numbers having n digits as described in the first comment.
for n in range(2, N + 1):
    current_inc = [0] * 10
    current_dec = [0] * 10
    for d in range(10):
        current_inc[d] = sum([increasing[n - 1][i] for i in range(d + 1)])
        current_dec[d] = sum([decreasing[n - 1][i] for i in range(d, 10)])
    increasing.append(current_inc)
    decreasing.append(current_dec)

# Compute the total number of increasing and decreasing numbers below 10**N.
total_increasing = sum(map(sum, increasing))
total_decreasing = sum(map(sum, decreasing))

# The set of 'constant' numbers, i.e., of the form 'dd...d', having a given
# length is always 9. Note that these are exactly the numbers that are
# both increasing and decreasing. They were thus counted twice above.
total_constant = 9 * N
answer = total_increasing + total_decreasing - total_constant
print(answer)

end = time.time()
print(f"Program runtime: {end - start} seconds")
