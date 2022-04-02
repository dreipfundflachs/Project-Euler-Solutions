# PROJECT EULER - PROBLEM 037
import time
from project_euler import prime_sieve

start = time.time()
primes = prime_sieve(10**6)
set_of_primes = set(primes)
special = []

for p in primes:
    s = str(p)
    m = len(s)
    active = True
    for i in range(1, m):
        q = int(s[i:])
        if q not in set_of_primes:
            active = False
            break
    if active:
        for i in range(1, m):
            q = int(s[:i])
            if q not in set_of_primes:
                active = False
                break
    if active:
        special.append(p)

print(special)
print(sum(special) - 17)


end = time.time()
print(f"Program runtime: {end - start} seconds")
