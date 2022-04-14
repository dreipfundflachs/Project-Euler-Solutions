#################################
#  PROJECT EULER - PROBLEM 007  #
#################################
import time


def is_prime(n: int) -> bool:
    """ Verifies directly whether a number is prime. """
    if n % 2 == 0:
        return False
    else:
        d = 3
        # Check whether n is divisible by d; no need to check values of d
        # greater than the square root of n, since if d is a divisor of n, then
        # so is n / d.
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True


start = time.time()

N = 10**4 + 1

k = 1
most_recent_prime = 0
prime_count = 0

while prime_count < N:
    if is_prime(k):
        prime_count += 1
        most_recent_prime = k
    k += 1

print(most_recent_prime)

end = time.time()
print(f"Program runtime: {end - start} seconds")
