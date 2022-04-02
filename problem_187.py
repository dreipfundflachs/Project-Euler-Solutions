# PROJECT EULER PROBLEM 187
import time


def prime_sieve(n):
    """ Returns a list of all primes <= n using Erasthotenes' sieve """
    primes = []
    flags = [True] * (n+1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if isprime:
            primes.append(k)
            for m in range(k*k, n+1, k):
                flags[m] = False
    return primes


def number_of_digits(n):
    """ Determines the number digits of n. """
    d = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        d += 1
    return d


# Obtain the list of all primes under m
start = time.time()
m = 10**8
primes = prime_sieve(m)
count = 0

# Whenever two primes in the list have product under m, increment the count
for i in range(len(primes) + 1):
    for j in range(i, len(primes)):
        if number_of_digits(primes[i] * primes[j]) < 9:
            count += 1
        else:
            break

print(count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
