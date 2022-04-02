# PROJECT EULER PROBLEM 035
import time
from project_euler import prime_sieve


start = time.time()

primes = prime_sieve(10**6)
set_of_primes = set(primes)
count = 0

for p in primes:
    p_string = str(p)
    p_string_rotations = []
    for k in range(0, len(p_string)):
        p_string_rotations.append(p_string[k:] + p_string[:k])
    p_rotations = [int(q) for q in p_string_rotations]
    flag = True
    for q in p_rotations:
        if q not in set_of_primes:
            flag = False
            break
    if flag:
        count += 1
        print(p_rotations)
print(count)


end = time.time()
print(f"Program runtime: {end - start} seconds")
