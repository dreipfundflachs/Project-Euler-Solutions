# PROJECT EULER PROBLEM 027
import time
from project_euler import prime_sieve

start = time.time()

primes = prime_sieve(10**4)
set_of_primes = set(primes)
max_a = -79
max_b = 1601
max_count = 40

for a in range(-999, 1000, 2):
    for b in primes[22:168]:
        n = 1
        p = 1 + a + b
        count = 1
        while p in set_of_primes:
            n += 1
            count += 1
            p = n**2 + a*n + b
        if count > max_count:
            max_count = count
            max_a = a
            max_b = b

print(max_a)
print(max_b)
print(max_count)
# lst = []
# for n in range(0, max_count):
#     lst.append(n**2 + max_a*n + max_b)
print(max_a*max_b)
# print(lst)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
