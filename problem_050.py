#################################
#  PROJECT EULER - PROBLEM 050  #
#################################
import time


def get_prime_flags_up_to(n: int) -> list[bool]:
    """ Returns a list prime_flags of n + 1 elements such that
    prime_flags[k] is True if and only if k is a prime number."""
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(p * p, n + 1, p):
                prime_flags[multiple] = False
    return prime_flags


start = time.time()

N = 10**6
PRIME_FLAGS = get_prime_flags_up_to(N)
PRIMES = [p for p in range(1, N) if PRIME_FLAGS[p]]
L = len(PRIMES)

sums_of_primes: list[(int, int)] = []
# Will hold pairs of the form (sum_of_primes, count) where 'sum_of_primes'
# is a sum of 'count' consecutive primes.

i = 0
for i in range(L - 1):
    j = i + 1
    current_sum = PRIMES[i] + PRIMES[j]
    while j < L and current_sum < N:
        if PRIME_FLAGS[current_sum]:
            sums_of_primes.append((current_sum, j - i + 1))
        # Update j and current_sum:
        j += 1
        current_sum += PRIMES[j]

# Search for the solution inside the list sum_of_primes.
max_count = 0
max_prime = 0
for (p, count) in sums_of_primes:
    if count > max_count:
        max_count = count
        max_prime = p

print("The prime under one million which can be written as the sum "
      f"of the greatest number\nof consecutive primes is {max_prime}, "
      f"which is a sum of {max_count} consecutive primes.")

end = time.time()
print(f"Program runtime: {end - start} seconds")
