#################################
#  PROJECT EULER - PROBLEM 060  #
#################################
import time
from random import randrange


def get_primes_up_to(n: int) -> list[bool]:
    """ Returns a list all primes from 3 to n, converted to strings. Uses
    Erathostenes' sieve. """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            primes.append(str(p))
            for multiple in range(p * p, n + 1, p):
                prime_flags[multiple] = False
    return primes[1:]


def cannot_combine(p: str, q: str) -> bool:
    return not (miller_rabin(int(p + q)) and miller_rabin(int(q + p)))


def miller_rabin(n: int, k: int = 40) -> bool:
    """ Verifies whether a number n is prime using by using k random
    numbers between 2 and n - 1. Requires 'randrange' from the module 'random'.
    A good value for k in general is k = 40.
    """
    # The only even prime is 2:
    assert n >= 2
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


start = time.time()
N = 10**4
PRIME_STRINGS = get_primes_up_to(N)
M = len(PRIME_STRINGS)

for i_1 in range(M):
    p_1 = PRIME_STRINGS[i_1]
    for i_2 in range(i_1 + 1, M):
        p_2 = PRIME_STRINGS[i_2]
        if cannot_combine(p_1, p_2):
            continue
        else:
            for i_3 in range(i_2 + 1, M):
                p_3 = PRIME_STRINGS[i_3]
                if cannot_combine(p_1, p_3) or cannot_combine(p_2, p_3):
                    continue
                else:
                    for i_4 in range(i_3 + 1, M):
                        p_4 = PRIME_STRINGS[i_4]
                        if (cannot_combine(p_1, p_4) or
                           cannot_combine(p_2, p_4) or
                           cannot_combine(p_3, p_4)):
                            continue
                        else:
                            for i_5 in range(i_4 + 1, M):
                                p_5 = PRIME_STRINGS[i_5]
                                if (cannot_combine(p_1, p_5) or
                                   cannot_combine(p_2, p_5) or
                                   cannot_combine(p_3, p_5) or
                                   cannot_combine(p_4, p_5)):
                                    continue
                                else:
                                    answer = (int(p_1) + int(p_2) + int(p_3)
                                              + int(p_4) + int(p_5))
                                    print(answer)
                                    end = time.time()
                                    print("Program runtime: "
                                          f"{end - start} seconds")
                                    quit()
