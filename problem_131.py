# PROJECT EULER PROBLEM 131
import time

# This is more of a math problem than a programming problem. The original
# equation n**3 + n**2 * p = m**3 is equivalent to n**3 * ((n + p) / n) = m**3.
# Taking cube roots we deduce that the cube root of (n + p) / n must be
# rational. This can happen if and only if (n + p) / n is the cube of a
# rational number. If n + p and n have no common prime factors, then the only
# way that this can happen is for both n + p and n to be cubes. If n + p and n
# do have common prime factors, then the only possible such factor is p itself
# (indeed, if a prime q != p divides n, it cannot divide n + p, since it does
# not divide q). After clearing this common factor p we deduce by the first
# case that both (n / p + 1) and n / p have to be cubes, which is impossible.
# In conclusion, both n + p and n have to be cubes, that is, p is a difference
# of two cubes.

# Now given positive integers a and r,
# (a + r)**3 - a**3 = 3 * r * a**2 + 3 * r**2 * a + r**3 can be written as a
# product r * (3 * a**2 + 3 * r * a + r**2), , so if this is to be prime, we
# must have r = 1 (since the second factor is clearly > 1). We have thus
# narrowed our search to primes which can be expressed as the difference of two
# _consecutive_ cubes. A direct search will now find all of them below 10**6.


def is_prime(n):
    """ Verifies directly whether a number is prime. """
    if n % 2 == 0:
        return False
    else:
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True


start = time.time()

N = 10**6
count = 0
n = 1
while True:
    delta = (n + 1)**3 - n**3
    if is_prime(delta):
        count += 1
    if delta > N:
        break
    n += 1

print(count)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
