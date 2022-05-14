#################################
#  PROJECT EULER - PROBLEM 087  #
#################################
import time
from math import isqrt


def get_primes_up_to(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Eratosthenes' sieve """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            primes.append(k)
            for multiple in range(k * k, n + 1, k):
                prime_flags[multiple] = False
    return primes


start = time.time()

N = 50 * 10**6
# Compute the maximum possible values of a number which, when raised to the
# powers 2, 3, 4, is still less than N:
MAX_2 = isqrt(N)
MAX_3 = int(N**(1/3))
MAX_4 = int(N**(1/4))

primes = get_primes_up_to(MAX_2)

# Compute the maximum indices N_i such that primes[N_i] < MAX_i for i = 3, 4.
k = 0
while primes[k] < MAX_4:
    k += 1
N_4 = k

k = 0
while primes[k] < MAX_3:
    k += 1
N_3 = k

expressibles = set()  # Set that will hold all expressible numbers.

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
                    expressibles.add(s)
                else:
                    break

print(len(expressibles))

end = time.time()
print(f"Program runtime: {end - start} seconds")
