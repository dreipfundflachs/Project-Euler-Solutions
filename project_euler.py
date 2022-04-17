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


def gcd(a: int, b: int) -> int:
    """ Computes the g.c.d. (also known as h.c.f.) of the integers a and b."""
    if b == 0 or a == b:
        return a
    elif a == 0:
        return b
    elif a > b:
        return gcd(b, a % b)
    elif b > a:
        return gcd(a, b % a)


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


def powmod(base: int, exp: int, m: int) -> int:
    """ Computes base**exp (mod m) efficiently (in O(log(exp)) time). """
    if exp == 1:
        return base % m
    elif exp % 2 == 0:
        return (powmod(base, exp // 2, m)**2) % m
    else:
        return ((base * powmod(base, (exp - 1)//2, m)**2) % m)


def get_primes_up_to(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Eratosthenes' sieve """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            primes.append(k)
            for m in range(k * k, n + 1, k):
                prime_flags[m] = False
    return primes


def prime_sieve_flags(n: int) -> list[bool]:
    """ Returns a 'prime_flags' of primes <=n, such that prime_flags[p] = True
    if and only if p is a prime number."""
    prime_flags = [True] * (n+1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            for m in range(k*k, n+1, k):
                prime_flags[m] = False
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
    """ Returns the list of all prime factors of n.  Determines all necessary
    primes on the fly.  """
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


def prime_tuples_given_primes(n: int, primes: list[int]) -> int:
    """ Returns the set of all prime factors of n in tuple form, given a list
    that includes all primes less than n Ex.: prime_factors(60, [2, 3, 5, 7,
    11]) -> {(2,2), (3,1), (5, 1)} """
    prime_tuples = set()
    for p in primes:
        if n == 1:
            break
        mult = 0
        while n % p == 0:
            n = n // p
            mult += 1
        if mult > 0:
            prime_tuples.add((p, mult))
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


def number_of_digits(n: int) -> int:
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


def sum_of_digits(n: int) -> int:
    """ Returns the sum of all the digits of n """
    sum = 0
    while n > 0:
        last = n % 10
        sum += last
        n = (n - last) // 10
    return sum


def swap(lst: list, i: int, j: int) -> list:
    """ Swaps elements i and j of list lst """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


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


def uniquify(lst: list) -> list:
    """ Given a list 'lst', returns a new list with all duplicates removed. """
    new_lst = []
    for x in lst:
        if x not in new_lst:
            new_lst.append(x)
    return new_lst


################################################
#  FUNCTIONS INVOLVING STRINGS AND CHARACTERS  #
################################################


def convert_list_to_int(lst: list[int]) -> int:
    return int(''.join(str(i) for i in lst))


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


def flatten(t: list[list]) -> list:
    """ Converts a list of lists into a single list by joining all sublists,
    e.g., flatten([[1, 2], [2, 3]]) --> [1, 2, 2, 3] """
    return [item for sublist in t for item in sublist]
