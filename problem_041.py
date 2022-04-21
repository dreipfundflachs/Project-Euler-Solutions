#################################
#  PROJECT EULER - PROBLEM 041  #
#################################
import time


def get_primes_up_to_greater_than(n: int, m: int) -> list[int]:
    """ Returns a list of all primes >= m and <= n using Eratosthenes' sieve.
    """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            if k >= m:
                primes.append(k)
            for multiple in range(k * k, n + 1, k):
                prime_flags[multiple] = False
    return primes


def is_pandigital(n: int) -> bool:
    """ Decides whether an integer is pandigital. """
    n_string = str(n)
    set_of_digits = {int(digit) for digit in n_string}
    number_of_digits = len(set_of_digits)
    return (len(n_string) == number_of_digits and
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

N = 7
PRIMES = get_primes_up_to_greater_than(10**N, 10**(N - 1))

for prime in PRIMES[::-1]:
    if is_pandigital(prime):
        print(prime)
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
