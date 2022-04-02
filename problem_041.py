# PROJECT EULER PROBLEM 041
import time
from project_euler import prime_sieve, is_prime, convert_list_to_int
from itertools import permutations

start = time.time()
primes = prime_sieve(10**4)

# No need to check 9-digit pandigital numbers, because all of them
# are divisible by 3
pandigital = list(permutations(list(range(1, 8))))
pan = list(convert_list_to_int(n) for n in pandigital)
pan_primes = []
print(pan)

for n in pan:
    if is_prime(n, primes):
        pan_primes.append(n)

print(max(pan_primes))

end = time.time()
print(f"Program runtime: {end - start} seconds")
