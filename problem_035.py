#################################
#  PROJECT EULER - PROBLEM 035  #
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
            for m in range(p * p, n + 1, p):
                prime_flags[m] = False
    return prime_flags


start = time.time()

N = 10**6
PRIME_FLAGS = get_prime_flags_up_to(N)
PRIMES = [p for p in range(N) if PRIME_FLAGS[p]]

number_of_circulars = 0
for p in PRIMES:
    p_string = str(p)
    p_string_rotations = []
    for k in range(0, len(p_string)):
        p_string_rotations.append(p_string[k:] + p_string[:k])
    p_rotations = [int(q) for q in p_string_rotations]

    is_circular = True
    for q in p_rotations:
        if not PRIME_FLAGS[q]:
            is_circular = False
            break
    if is_circular:
        number_of_circulars += 1

print(number_of_circulars)

end = time.time()
print(f"Program runtime: {end - start} seconds")
