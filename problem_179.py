# PROJECT EULER PROBLEM 179
import time

start = time.time()

# For each integer in the given range, add 1 to the count of divisors of all
# of its multiples
m = 10**7
divisors = [0] + [1]*m
for n in range(2, m):
    r = m // n
    for k in range(1, r + 1):
        divisors[k * n] += 1

# Check which of the numbers in the given range have the same number of
# divisors as one of its neighbors
count = 0
for n in range(2, m, 2):
    d = divisors[n]
    if divisors[n - 1] == d:
        count += 1
    if divisors[n + 1] == d:
        count += 1

print(count)
end = time.time()
print(f"Program runtime: {end - start} seconds")
