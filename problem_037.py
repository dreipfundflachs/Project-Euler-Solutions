#################################
#  PROJECT EULER - PROBLEM 037  #
#################################
import time


def get_prime_flags_up_to(n: int) -> list[bool]:
    """ Returns a list prime_flags of n + 1 elements such that
    prime_flags[k] = True if and only if k is a prime number."""
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
# Since 2, 3, 5, 7 are not considered truncatable, we start from 11.
PRIMES = [p for p in range(11, N) if PRIME_FLAGS[p]]

truncatable_numbers = []
for p in PRIMES:
    p_string = str(p)
    number_of_digits_of_p = len(p_string)
    is_truncatable = True
    for i in range(1, number_of_digits_of_p):
        # Crop p from the left and from the right by i digits:
        init = int(p_string[:i])
        tail = int(p_string[i:])
        # Check if these cropped numbers are still prime; if not, break.
        if not (PRIME_FLAGS[init] and PRIME_FLAGS[tail]):
            is_truncatable = False
            break
    if is_truncatable:
        truncatable_numbers.append(p)
        if len(truncatable_numbers) == 11:
            break

print(sum(truncatable_numbers))

end = time.time()
print(f"Program runtime: {end - start} seconds")
