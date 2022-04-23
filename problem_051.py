#################################
#  PROJECT EULER - PROBLEM 051  #
#################################
import time
from itertools import combinations

start = time.time()


def get_number_of_digits(n: int) -> int:
    """ Determines the number digits of n. """
    d = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        d += 1
    return d


def compare(p: int, q: int) -> bool:
    """ Tells whether a number q can be obtained from a number p by
    replacing some occurrences of the same digit by another digit, e.g.,
    compare(56333, 56443) should return True. """
    string_p = str(p)
    string_q = str(q)
    if len(string_q) != len(string_p):
        return False
    else:
        differing_indices = [i for i in range(string_p)
                             if string_p[i] != string_q[i]]
        set_of_p_digits = {string_p[i] for i in differing_indices}
        set_of_q_digits = {string_q[i] for i in differing_indices}
        if len(set_of_p_digits) == len(set_of_q_digits) == 1:
            return True
        else:
            return False


def convert_to_int(digits: list[int]) -> int:
    """ Converts a list of digits to a single integer, e.g.,
    [1, 2, 3] --> 123. """
    return int(''.join([str(digit) for digit in digits]))


def get_variations(p: int, positions: list[int]) -> list[int]:
    """ Given a number p and a list of positions, starting from 0 (leftmost)
    to n = len(p) - 1 (rightmost), the function returns the list of all 10
    numbers one obtains by replacing each of these digits by 0...9. If the
    digits in the original number p do not match, then it returns [p].
    Example: variations(56333, (2, 3)) returns [56003, 56113, ..., 56993]."""
    list_of_digits_of_p = [int(d) for d in list(str(p))]
    digits_in_positions = {list_of_digits_of_p[i] for i in positions}
    # Test if all the digits of p in positions coincide:
    if len(digits_in_positions) > 1:
        return [p]
    else:
        variations = []
        for k in range(0, 10):
            current_list = list_of_digits_of_p
            for i in positions:
                current_list[i] = k
            variations.append(convert_to_int(current_list))
        return variations


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


MAX_DIGITS = 6
M = 10**(MAX_DIGITS - 1)
N = 10**MAX_DIGITS
PRIME_FLAGS = get_prime_flags_up_to(N)
PRIMES = [p for p in range(M, N) if PRIME_FLAGS[p]]

# The idea is to perform a straightforward search: For each prime p having
# MAX_DIGITS digits, we consider all numbers which can be obtained from it by
# replacing some set of coinciding digits by another digit, and check if the
# resulting variation is also prime. If fewer than 8 of these variations are
# prime, we can proceed to consider the next prime; if we find a solution, we
# can exit the loop.
found_solution = False
for p in PRIMES:
    for positions in list(combinations(range(0, MAX_DIGITS - 1), 3)):
        variations_of_p = get_variations(p, positions)
        # In principle, all 10 variations of p can be prime:
        number_of_prime_candidates = 10
        for q in variations_of_p:
            # If q fails to be prime or if its number of digits is less
            # than MAX_DIGITS, we decrease our counter.
            if not PRIME_FLAGS[q] or len(str(q)) < MAX_DIGITS:
                number_of_prime_candidates -= 1
                if number_of_prime_candidates < 8:
                    break
        # If number_of_prime_candidates == 8, we have found the solution.
        if number_of_prime_candidates == 8:
            print(f"The smallest such prime is {p}.")
            found_solution = True
            break
    if found_solution:
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
