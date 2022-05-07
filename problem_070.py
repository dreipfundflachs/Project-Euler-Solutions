#################################
#  PROJECT EULER - PROBLEM 070  #
#################################
import time


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


def get_sorted_digits(n: int) -> list[int]:
    """ Returns a sorted list of all the digits of n. """
    digits = []
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        digits.append(r)
    return sorted(digits)


start = time.time()

M = 10**4
N = 10**7
PRIMES = get_primes_up_to(M)

min_ratio = 10

for p in PRIMES:
    for q in PRIMES:
        if p * q > N:
            break
        else:
            n = p * q
            phi_n = (p - 1) * (q - 1)
            ratio = n / phi_n
            if (get_sorted_digits(n) == get_sorted_digits(phi_n)
                    and ratio < min_ratio):
                min_ratio = ratio
                min_n = n

print(min_n)

end = time.time()
print(f"Program runtime: {end - start} seconds")
