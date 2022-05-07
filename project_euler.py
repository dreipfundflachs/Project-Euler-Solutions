##############################################################
#  SOME USEFUL FUNCTIONS FOR SOLVING PROJECT EULER PROBLEMS  #
##############################################################

from math import prod, isqrt
from itertools import combinations
from functools import reduce


#################################################################
#  FUNCTIONS INVOLVING PRIMES, FACTORIZATION, DIVISORS, ETC...  #
#################################################################


def even(n: int) -> bool:
    """ Decides whether a number is even """
    if n % 2 == 0:
        return True
    else:
        return False


def is_square(n: int) -> bool:
    """ Decides whether an integer is the square of another integer. """
    m = isqrt(n)
    if m**2 == n:
        return True
    else:
        return False


def gcd(a: int, b:  int) -> int:
    """ Computes the greatest common divisor (gcd) of integers a and b. """
    while b:
        a, b = b, a % b
    return a


def involves_only(n: int, p: int, q: int) -> bool:
    """ Checks if the prime factors of n all lie in the set {p, q}. """
    while (n % p) == 0:
        n //= p
    while (n % q) == 0:
        n //= q
    if n > 1:
        return False
    else:
        return True


def powmod(base: int, exponent: int, m: int) -> int:
    """ Computes base**exp (mod m) efficiently (in O(log(exp)) time). """
    if exponent == 1:
        return base % m
    elif exponent % 2 == 0:
        return (powmod(base, exponent // 2, m)**2) % m
    else:
        return ((base * powmod(base, (exponent - 1)//2, m)**2) % m)


def get_primes_up_to(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Eratosthenes' sieve """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            primes.append(k)
            for multiple in range(k * k, n + 1, k):
                prime_flags[multiple] = False
    return primes


def get_primes_up_to_greater_than(n: int, m: int) -> list[int]:
    """ Returns a list of all primes p such that m <= p <= n using
    Eratosthenes' sieve. """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            if k >= m:
                primes.append(k)
            for multiple in range(k * k, n + 1, k):
                prime_flags[multiple] = False
    return primes


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


def composite_sieve(N: int) -> list[int]:
    """ Returns a list of all composite numbers <= N, computed using
    Eratosthenes' sieve """
    flags = [True] * (N + 1)
    flags[0] = False
    flags[1] = False
    for (k, is_prime) in enumerate(flags):
        if is_prime:
            for multiple in range(2 * k, N + 1, k):
                flags[multiple] = False
    composite = [n for n in range(N + 1) if n > 1 and flags[n] is False]
    return composite


def is_prime_given_primes(n: int, primes: list[int]) -> bool:
    """ Tells whether a number n is prime, given a list of all primes from 2 to
    the square root of n """
    for p in primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    return True


def is_prime(n: int) -> bool:
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


def product(set_of_integers: set[int]) -> int:
    """ Takes a set of integers and returns their product """
    product = 1
    for k in set_of_integers:
        product *= k
    return product


def integer_product(list_of_integers: list[int]) -> int:
    """ Takes a list of integers and returns their product """
    p = 1
    for k in list_of_integers:
        p *= int(k)
    return p


def get_prime_factors(n: int) -> list[int]:
    """ Returns the list of all prime factors of n, each prime appearing as
    many times as its multiplicity indicates.  Determines all necessary primes
    on the fly.  """
    factors = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if n == 1:
            break
        if is_prime:
            for multiple in range(p * p, n + 1, p):
                prime_flags[multiple] = False
            while n % p == 0:
                factors.append(p)
                n = n // p
    return factors


def divisor_count(n: int) -> int:
    """ Counts the number of divisors of n, including 1 and the number itself.
    """
    list_of_factors = get_prime_factors(n)
    set_of_factors = set(list_of_factors)
    prod = 1
    for prime in set_of_factors:
        multiplicity = 1 + list_of_factors.count(prime)
        prod *= multiplicity
    return prod


def divisor_count_given_primes(n: int, primes: list[int]) -> int:
    """ Counts the number of divisors of n, including 1 and the number itself.
    """
    prod = 1
    for p in primes:
        if n == 1:
            break
        multiplicity = 0
        while (n % p) == 0:
            multiplicity += 1
            n //= p
        prod *= multiplicity + 1
    return prod


def radical(n: int, primes: list[int]) -> int:
    """ Computes the radical of an integer n (the product of each of its prime
    factors), given a list of primes which includes all prime factors of n. """
    prime_factors = {1}
    for p in primes:
        if n == 1:
            break
        while (n % p) == 0:
            n //= p
            prime_factors.add(p)
    return reduce(lambda x, y: x * y, prime_factors)


def radical_sieve(N: int) -> list[int]:
    """ Returns a list whose n-th element is the radical of n for each n <= N.
    """
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    radicals = [1] * (N + 1)
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(k * k, N + 1, k):
                prime_flags[multiple] = False
            for multiple in range(k, N + 1, k):
                radicals[multiple] *= k
    return radicals


def radical_set_sieve(N: int) -> list[int]:
    """ Returns a set whose n-th element is the set of all prime factors of n,
    for each n <= N.  """
    primes = []
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    radicals = [set() for n in range(N + 1)]
    radicals[0] = {1}
    radicals[1] = {1}
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            primes.append(k)
            for multiple in range(k * k, N + 1, k):
                prime_flags[multiple] = False
            for multiple in range(k, N + 1, k):
                (radicals[multiple]).add(k)
    return radicals


def get_prime_factors_given_primes(n: int, primes: list[int]) -> list[int]:
    """ Returns the list of all prime factors of n, each prime appearing the
    same number of times as its multiplicity, given a list that includes all
    primes less than n. Example:
    get_prime_factors_given_primes(60, [2, 3, 5, 7, 11]) -> [2, 2, 3, 5]. """
    prime_factors = []
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            prime_factors.append(p)
            n = n // p
    return prime_factors


def get_prime_tuples_given_primes(n: int, primes: list[int]) -> set[int]:
    """ Returns the set of all prime factors of n in tuple form, given a list
    that includes all primes less than n. Example:
    prime_factors(60, [2, 3, 5, 7, 11]) -> {(2,2), (3,1), (5, 1)}. """
    prime_tuples = set()
    for p in primes:
        if n == 1:
            break
        multiplicity = 0
        while n % p == 0:
            n = n // p
            multiplicity += 1
        if multiplicity > 0:
            prime_tuples.add((p, multiplicity))
    return prime_tuples


def get_proper_divisors_given_primes(n: int, primes: list[int]) -> list[int]:
    """ Returns the list of all proper divisors of n (i.e., < n) given a list
    that includes all primes less than n """
    list_of_prime_factors = get_prime_factors_given_primes(n, primes)
    m = len(list_of_prime_factors)
    tuples = set()
    for k in range(1, m):
        new_tuples = set(combinations(list_of_prime_factors, k))
        tuples = tuples.union(new_tuples)
    result = [prod(t) for t in tuples]
    result.append(1)
    return result


def sum_of_proper_divisors(n: int, primes: list[int]) -> int:
    """ Returns the sum of all proper divisors of n given a list that includes
    all primes less than n """
    return sum(get_proper_divisors_given_primes(n, primes))


def get_number_of_digits(n: int) -> int:
    """ Determines the number digits of n. """
    d = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        d += 1
    return d


def get_digital_sum(n: int) -> int:
    """ Determines the sum of all digits of n. """
    s = 0
    while n != 0:
        r = n % 10
        n = (n - r) // 10
        s += r
    return s


#############################################
#  FUNCTIONS INVOLVING MATRICES AND ARRAYS  #
#############################################


def transpose(A: list) -> list:
    """ Transposes a (not necessarily square nor numeric) matrix (list of
    lists, each of the same size) """
    m = len(A)
    n = len(A[0])
    # Initialize the transpose
    B = [[0 for i in range(m)] for j in range(n)]
    for j in range(0, n):
        column = []
        for i in range(0, m):
            column.append(A[i][j])
        B[j] = column
    return B


#################
#  MISCELLANEA  #
#################


def binary_search(target: int, numbers: list[int]) -> True:
    """ Given a _sorted_ list of integers 'numbers', uses a binary search to
    decide whether 'target' lies in it. """
    first = 0
    last = len(numbers) - 1
    middle = 0

    while first <= last:
        middle = (first + last) // 2
        if numbers[middle] == target:
            return True
        elif target < numbers[middle]:
            last = middle - 1
        else:
            first = middle + 1

    return False


def get_powerset(ns: set[int]) -> list[iter]:
    """ Returns the power set of 'ns' as a list, e.g., get_powerset([1,2,3])
    yields [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]. """
    return [tup for n in range(0, len(ns) + 1) for tup in combinations(ns, n)]


def get_sum_of_digits(n: int) -> int:
    """ Returns the sum of all the digits of n """
    sum = 0
    while n > 0:
        last = n % 10
        sum += last
        n = (n - last) // 10
    return sum


def swap(lst: list, i: int, j: int) -> list:
    """ Swaps elements i and j of list lst """
    lst[i], lst[j] = lst[j], lst[i]


def dec_to_bin(n: int) -> int:
    """ Converts a decimal integer to binary """
    return(int(bin(n)[2:]))


def palindromic(string: str) -> bool:
    """ Checks if the given string is palindromic. """
    return (string == string[::-1])


def palindromes(n: int) -> list[int]:
    """ Produces a list of all palindromic numbers having at most n digits."""
    palindromes = [False] * (10**n)
    half = n // 2
    for k in range(0, 10):
        palindromes[k] = True
    if n % 2 == 1:
        for d in range(1, half + 1):
            for k in range(10**(d - 1), 10**d):
                palindrome = int(str(k)+str(k)[::-1])
                palindromes[palindrome] = True
                for r in range(0, 10):
                    palindrome = int(str(k) + str(r) + str(k)[::-1])
                    palindromes[palindrome] = True
    elif n % 2 == 0:
        for d in range(1, half):
            for k in range(10**(d - 1), 10**d):
                palindrome = int(str(k)+str(k)[::-1])
                palindromes[palindrome] = True
                for r in range(0, 10):
                    palindrome = int(str(k) + str(r) + str(k)[::-1])
                    palindromes[palindrome] = True
        for k in range(10**(half - 1), 10**half):
            palindrome = int(str(k)+str(k)[::-1])
            palindromes[palindrome] = True
    return palindromes


def get_decimal_representation(n: int, d: int, precision: int) -> list[int]:
    """ Given integers n < d, computes the decimal part of n / d up to the
    'precision'-th digit of its decimal part or until there is a recurring
    cycle. The function does not determine the cycle. 'r' indicates a
    recurring cycle from that position on. Example: since 1 / 7 = 0.(142857),
    we have: int_division(1, 7, 10) = [1, 4, 2, 8, 5, 7, 'r']. To obtain the
    decimal representation, the function simply emulates long division. """
    decimals = []
    remainders = [n]
    decimal = -1
    count = 0
    while n != 0 and count < precision:
        n *= 10
        while n < d:
            n *= 10
            decimals.append(0)
            count += 1
            remainders.append(n)
        decimal = n // d
        decimals.append(decimal)
        n = n % d
        count += 1
        if n not in remainders:
            remainders.append(n)
        else:
            decimals.append('r')
            break
    return decimals


################################################
#  FUNCTIONS INVOLVING STRINGS AND CHARACTERS  #
################################################


def convert_to_int(digits: list[int]) -> int:
    """ Converts a list of digits to a single integer, e.g.,
    [1, 2, 3] --> 123. """
    return int(''.join([str(digit) for digit in digits]))


def name_score(name: str) -> int:
    """ Calculates the 'score' of a name written in capital letters. """
    letter_values = {}
    initial = ord('A')
    diff = ord('Z')
    for k in range(initial, diff + 1):
        score = k - initial + 1
        letter_values[chr(k)] = score
    score = 0
    for char in name:
        score += letter_values[char]
    return score


def flatten(list_of_lists: list[list[int]]) -> list[int]:
    """ Converts a list of lists into a single list by joining all sublists,
    e.g., flatten([[1, 2], [2, 3]]) --> [1, 2, 2, 3]. """
    return [item for sublist in list_of_lists for item in sublist]


def generate_palindromes(letters: list[str], length: int) -> list[str]:
    """ Returns a list containing all palindromes of the specified length using
    the letters (or strings) in the given list of strings. """
    # Base cases:
    if length <= 0:
        palindromes = []
    elif length == 1:
        palindromes = letters
    elif length == 2:
        palindromes = [string + string for string in letters]
    # General case:
    else:
        palindromes = []
        # Choose an initial/final letter and make a recursive call using
        # (length - 2) to generate the central string.
        for letter in letters:
            for palindrome in generate_palindromes(letters, length - 2):
                new_palindrome = letter + palindrome + letter
                palindromes.append(new_palindrome)
    return palindromes


def generate_palindromic_integers(length: int) -> list[int]:
    """ Returns a list of all integers having at most 'length' digits
    which are palindromic when written in base 10. """
    DIGITS = [str(d) for d in range(0, 10)]

    palindromic_strings = generate_palindromes(DIGITS, length)
    palindromic_integers = [int(string) for string in palindromic_strings
                            if string[0] != '0']
    return palindromic_integers


def is_palindromic_base_2(n: int) -> bool:
    """ Determines whether the positive integer n is palindromic when expressed
    as a binary string. """
    if n <= 0:
        return False
    else:
        binary_string = str(bin(n))[2:]
        return binary_string == binary_string[::-1]
