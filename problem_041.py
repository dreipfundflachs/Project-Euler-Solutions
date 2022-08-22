#################################
#  PROJECT EULER - PROBLEM 041  #
#################################
import time


def get_primes_up_to_greater_than(N: int, M: int) -> list[int]:
    """ Returns a list of all primes p such that M <= p <= N using
    Eratosthenes' sieve.  """
    primes = []
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            if p >= M:
                primes.append(p)
            for multiple in range(p * p, N + 1, p):
                prime_flags[multiple] = False
    return primes


def is_pandigital(n: int) -> bool:
    """ Decides whether an d-digit integer is such that each digit between 1
    and d appears exactly once in the decimal representation of n. """
    assert n >= 0 and type(n) == int
    set_of_digits = set()
    number_of_digits = 0
    while n != 0:
        set_of_digits.add(n % 10)
        n //= 10
        number_of_digits += 1
    number_of_distinct_digits = len(set_of_digits)
    return (number_of_digits == number_of_distinct_digits and
            set_of_digits == {d for d in range(1, number_of_digits + 1)})


# Note that since 10**n = 1 (mod 3) for all n >= 1, a number whose digits are
# d_1, d_2, ..., d_n is divisible by 3 if and only if their sum d_1 + ... + d_n
# is divisible by 3. Thus for the following values of n, if a number is 1-n
# pandigital, then it will be divisible by 3:
# n = 2 (since 1 + 2 = 3);
# n = 3 (since 1 + 2 + 3 = 6);
# n = 5 (since 1 + 2 + 3 + 4 + 5 = 15)
# n = 6 (since 1 + 2 + 3 + 4 + 5 + 6 = 21)
# n = 8 (since 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36)
# n = 9 (since 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45)
# That is, we need only find the largest prime number having 7 digits or, if
# no such prime exists, the largest one having 4 digits.

start = time.time()

D = 7
N = 10**D
M = 10**(D - 1)
PRIMES = get_primes_up_to_greater_than(N, M)

for prime in PRIMES[::-1]:
    if is_pandigital(prime):
        print(prime)
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
