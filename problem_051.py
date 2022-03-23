# PROJECT EULER PROBLEM 051
import time
from project_euler import prime_sieve, number_of_digits
from itertools import combinations

start = time.time()


def flatten(t):
    """ Converts a list of lists into a single list by joining all sublists,
    e.g., flatten([[1, 2], [2, 3]]) --> [1, 2, 2, 3]
    """
    return [item for sublist in t for item in sublist]


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    return list(list(combinations(xs, n)) for n in range(1, len(xs) + 1))


def number_of_digits(n):
    """ Determines the number digits of n. """
    d = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        d += 1
    return d


def compare(p, q):
    """ Tells whether a number q can be obtained from a number p by
    replacing part some occurrences of the same digit by another digit, e.g.,
    compare(56333, 56443) should return True.
    """
    sp = str(p)
    sq = str(q)
    m = len(sp)
    if len(sq) != m:
        return False
    else:
        differing_indices = [ k for k in range(m) if sp[k] != sq[k] ]
        set_of_p_digits = set([sp[k] for k in differing_indices])
        set_of_q_digits = set([sq[k] for k in differing_indices])
        if len(set_of_p_digits) == len(set_of_q_digits) == 1:
            return True
        else:
            return False


def convert_to_number(digits):
    """ Converts a list of digits to a single integer, e.g.,
    [1, 2, 3] --> 123. """
    s = [str(d) for d in digits]
    return int(''.join(s))


def variations(p, positions):
    """ Given a number p and a list of positions, starting from 0 (leftmost)
    to n = len(p) - 1 (rightmost), the function returns the list of all 10
    numbers one obtains by replacing each of these digits by 0...9. If the
    digits in the original number p do not match, then it returns [p].
    Example: variations(56333, (2, 3)) returns [56003, 56113, ..., 56993]."""
    list_of_digits_of_p = [int(c) for c in list(str(p))]
    digits_in_positions = set([list_of_digits_of_p[k] for k in positions])
    # Test if all the digits of p in positions coincide
    if len(digits_in_positions) > 1:
        return [p]
    else:
        result = []
        for i in range(0, 10):
            current_list = list_of_digits_of_p
            for k in positions:
                current_list[k] = i
            result.append(convert_to_number(current_list))
        return result


def first_prime_index(d, primes):
    """ Returns the index of the first prime in the given list of primes having
    d digits."""
    m = len(primes)
    for i in range(m + 1):
        if number_of_digits(primes[i]) == d:
            return i

# Initialize the list and set of primes
dmax = 7
m = 10**dmax
primes = prime_sieve(m)
set_of_primes = set(primes)
active = True

# Separate the search by the number of digits of the primes involved, storing
# them in the list 'relevant_primes'
for d in range(6, dmax):
    imin = first_prime_index(d, primes)
    imax = first_prime_index(d + 1, primes)
    relevant_primes = primes[imin:imax + 1]
    for p in relevant_primes:
#        for positions in flatten(powerset(range(1, d))):
        for positions in list(combinations(range(0, d), 3)):
            related = variations(p, positions)
            count = 10
            special = related
            for q in related:
# If at least three of the related numbers are *not* primes, no need keep
# checking if the other ones are prime
                if q not in set(relevant_primes):
                    count -= 1
                    special.remove(q)
                    if count < 8:
                        break
# If count == 8, we have found the first number, so break out of all loops
            if count == 8:
                print(p, positions, special)
                active = False
                break
        if active == False:
            break
    if active == False:
        break


end = time.time()
print(f"Program runtime is: {end - start} seconds")
