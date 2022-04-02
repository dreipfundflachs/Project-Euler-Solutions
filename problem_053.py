# PROJECT EULER PROBLEM 053
import time
from scipy.special import comb

start = time.time()

count = 0
for n in range(23, 101):
    k = 1
    while comb(n, k) <= 10**6:
        k += 1
    count += n - 2 * k + 1
print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
