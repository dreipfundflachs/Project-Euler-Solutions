#################################
#  PROJECT EULER - PROBLEM 010  #
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
            for m in range(k*k, n+1, k):
                prime_flags[m] = False

    return primes


start = time.time()

N = 2 * 10**6

print(sum(get_primes_up_to(N)))

end = time.time()
print(f"Program runtime: {end - start} seconds")
