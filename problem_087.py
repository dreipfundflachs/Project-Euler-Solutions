# PROJECT EULER PROBLEM 087
import time
from project_euler import prime_sieve
from math import isqrt

start = time.time()

N = 50 * 10**6
MAX_4 = int(N**(1/4))
MAX_3 = int(N**(1/3))
MAX_2 = isqrt(N)
primes = prime_sieve(MAX_2)

k = 0
while primes[k] < MAX_4:
    k += 1
N_4 = k

k = 0
while primes[k] < MAX_3:
    k += 1
N_3 = k

expressible = set()

for k in range(N_4 + 1):
    c = primes[k]
    for j in range(N_3 + 1):
        b = primes[j]
        r = b**3 + c**4
        if r < N:
            for a in primes:
                s = a**2 + r
                if s < N:
                    expressible.add(s)
                else:
                    break
        else:
            break

print(len(expressible))

end = time.time()
print(f"Program runtime is: {end - start} seconds")
