#################################
#  PROJECT EULER - PROBLEM 047  #
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


def number_of_prime_factors(n: int) -> int:
    """ Returns the number of distinct prime factors of n . """
    prime_factors = set()
    for p in PRIMES:
        while n % p == 0:
            prime_factors.add(p)
            n = n // p
        if n == 1:
            break
    return len(prime_factors)


start = time.time()

N = 1000
PRIMES = get_primes_up_to(N)

# Starting with n = 1, if we check whether the number of prime factors of
# n, n + 1, n + 2, n + 3 are all equal to 4, then the number of prime factors
# of, say, n + 3, will be calculated four times. To avoid repeated
# computations, we can proceed in steps of four instead of 1, that is, consider
# 4 * n instead of n, and inspect the most appropriate chain of four
# consecutive numbers containing 4 * n accordingly.

found_solution = False
n = 0
while not found_solution:
    n += 1
    if number_of_prime_factors(4 * n) == 4:
        if number_of_prime_factors(4 * n - 2) == 4:
            if number_of_prime_factors(4 * n - 1) == 4:
                if number_of_prime_factors(4 * n - 3) == 4:
                    solution = 4 * n - 3
                    found_solution = True
                elif number_of_prime_factors(4 * n + 1) == 4:
                    solution = 4 * n - 2
                    found_solution = True
        else:
            if number_of_prime_factors(4 * n + 2) == 4:
                if number_of_prime_factors(4 * n + 1) == 4:
                    if number_of_prime_factors(4 * n - 1) == 4:
                        solution = 4 * n - 1
                        found_solution = True
                    elif number_of_prime_factors(4 * n + 3) == 4:
                        solution = 4 * n
                        found_solution = True

print(solution)

end = time.time()
print(f"Program runtime: {end - start} seconds")
