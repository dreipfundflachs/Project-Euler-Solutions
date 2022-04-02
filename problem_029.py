# PROJECT EULER PROBLEM 029
import time
from project_euler import prime_sieve, uniquify
from project_euler import prime_tuples_given_primes as pt


def multiply_second(s, b):
    """ Given a set 's' of tuples,
        multiply the second coordinate of each tuple by b
    """
    new_lst = set([(x, y * b) for (x, y) in s])
    return new_lst


start = time.time()

primes = prime_sieve(100)
powers = []
for a in range(2, 101):
    tuples = pt(a, primes)
    for b in range(2, 101):
        powers.append(multiply_second(tuples, b))

new_powers = uniquify(powers)
print(len(new_powers))

end = time.time()
print(f"Program runtime: {end - start} seconds")
