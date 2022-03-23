# PROJECT EULER PROBLEM 47
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


def prime_factors(n):
    """ Returns the list of all prime factors of n """
    number = n
    factors = []
    for p in primes:
        while number % p == 0:
            factors.append(p)
            number = number // p
        if number == 1:
            break
    return factors


def set_of_prime_factors(n):
    """ Returns the *set* of all prime factors of n """
    number = n
    set_of_factors = set()
    for p in primes:
        if number % p == 0:
            set_of_factors.add(p)
            number = number // p
        while number % p == 0:
            number = number // p
        if number == 1:
            break
    return set_of_factors


def number_of_prime_factors(n):
    """ Returns the number of distinct prime factors of n """
    return len(set_of_prime_factors(n))


def remove_prime(n, p):
    """
    If p divides n, return the quotient of n
    by the highest power of p that divides n
    """
    while n % p == 0:
        n = n // p
    return n


start = time.time()

primes = prime_sieve(700)

flag = True
n = 0
while flag:
    n += 1
    p_0 = 1 + number_of_prime_factors(remove_prime(n, 2))
    if p_0 == 4:
        p_m2 = 1 + number_of_prime_factors(2*n - 1)
        if p_m2 == 4:
            p_m1 = number_of_prime_factors(4*n - 1)
            if p_m1 == 4:
                p_1 = number_of_prime_factors(4*n + 1)
                p_m3 = number_of_prime_factors(4*n - 3)
                if p_m3 == 4:
                    flag = False
                    number = 4*n - 3
                elif p_1 == 4:
                    flag = False
                    number = 4*n - 2
        else:
            p_2 = 1 + number_of_prime_factors(2*n + 1)
            if p_2 == 4:
                p_1 = number_of_prime_factors(4*n + 1)
                if p_1 == 4:
                    p_3 = number_of_prime_factors(4*n + 3)
                    p_m1 = number_of_prime_factors(4*n - 1)
                    if p_m1 == 4:
                        flag = False
                        number = 4*n - 1
                    elif p_3 == 4:
                        flag = False
                        number = 4*n

print(number)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
