# PROJECT EULER PROBLEM 087
import time
from project_euler import prime_sieve
from math import isqrt

start = time.time()

N = 50 * 10**6
# Compute the maximum possible values of a number which, when raised to the
# powers 2, 3, 4, is still less than N.
MAX_2 = isqrt(N)
MAX_3 = int(N**(1/3))
MAX_4 = int(N**(1/4))

primes = prime_sieve(MAX_2)

# Compute the maximum indices N_i such that primes[N_i] < MAX_i for i = 3, 4.
k = 0
while primes[k] < MAX_4:
    k += 1
N_4 = k

k = 0
while primes[k] < MAX_3:
    k += 1
N_3 = k

# Initialize a set to hold all expressible numbers.
expressible = set()

for k in range(N_4 + 1):
    c = primes[k]
    for j in range(N_3 + 1):
        b = primes[j]
        r = b**3 + c**4
        # If r >= N, then break from the j-loop and increase k.
        if r >= N:
            break
        # Otherwise, there may still be room to add the square of a prime.
        else:
            for a in primes:
                s = a**2 + r
                if s < N:
                    expressible.add(s)
                else:
                    break
# Print answer.
print(len(expressible))

end = time.time()
print(f"Program runtime is: {end - start} seconds")
