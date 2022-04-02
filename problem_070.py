# PROJECT EULER PROBLEM 070
import time
from project_euler import prime_sieve


def get_digits(n):
    """ Returns a list of all the digits of n. """
    digits = []
    d = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        digits.append(r)
    return digits


start = time.time()
m = 10**7
primes = prime_sieve(m)
minp = 0
minq = 0
minratio = 10
for p in primes:
    for q in primes:
        if p * q > m:
            break
        else:
            n = p * q
            phin = (p - 1) * (q - 1)
            ratio = n / phin
            if (sorted(get_digits(n)) == sorted(get_digits((phin)))
                    and ratio < minratio):
                minratio = ratio
                minp = p
                minq = q
                print(p, q, p * q, minratio)
end = time.time()
print(f"Program runtime: {end - start} seconds")
