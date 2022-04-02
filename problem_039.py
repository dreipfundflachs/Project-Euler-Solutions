# PROJECT EULER PROBLEM 039
import time
from math import isqrt

start = time.time()

perimeters = {}
for k in range(1, 3001):
    perimeters[k] = 0

for a in range(1, 500):
    for b in range(a + 1, 1000):
        s = a**2 + b**2
        c = isqrt(s)
        if c**2 == s:
            p = a + b + c
            perimeters[p] += 1

pmax = 0
maxp = 0
for k in range(1, 1001):
    p = perimeters[k]
    if p > pmax:
        maxp = k
        pmax = p

print(pmax)
print(maxp)
end = time.time()
print(f"Program runtime: {end - start} seconds")
