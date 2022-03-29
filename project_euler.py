from math import prod, isqrt
import itertools


# %%%%% Functions involving primes, factorization, etc. %%%%%% #
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
    """ Computes the g.c.d. (a.k.a. h.c.f.) of the integers a and b."""
    if b == 0 or a == b:
        return a
    elif a == 0:
        return b
    elif a > b:
        return gcd(b, a % b)
    elif b > a:
        return gcd(a, b % a)


def powmod(base: int, exp: int, m: int) -> int:
    """ Computes base**exp (mod m) efficiently (log(exp) time). """
    if exp == 1:
        return base % m
    elif exp % 2 == 0:
        return (powmod(base, exp // 2, m)**2) % m
    else:
        return ((base * powmod(base, (exp - 1)//2, m)**2) % m)


def prime_sieve(n: int) -> list(int):
    """ Returns a list of all primes <= n using Erasthotenes' sieve """
    primes = []
    flags = [True] * (n+1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if isprime:
            primes.append(k)
            for m in range(k*k, n+1, k):
                flags[m] = False
    return primes


def prime_sieve_flags(n: int) -> list(bool):
    """ Returns a 'flags' of primes <=n, such that
    flags[p] = True if and only if p is a prime number."""
    flags = [True] * (n+1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if isprime:
            for m in range(k*k, n+1, k):
                flags[m] = False
    return flags


def is_prime_given_primes(n: int, primes: list(int)) -> bool:
    """ Tells whether a number n is prime,
    given a list of all primes from 2 to the square root of n
    """
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


def integer_product(list_of_integers: list(int)) -> int:
    """ Takes a list of integers and returns their product """
    p = 1
    for k in list_of_integers:
        p *= int(k)
    return p


def prime_factors(n: int) -> list(int):
    """ Returns the list of all prime factors of n.
        Determines all necessary primes on the fly.
    """
    number = n
    primes = []
    factors = []
    flags = [True] * (n + 1)
    flags[0] = False
    flags[1] = False
    for (k, isprime) in enumerate(flags):
        if number == 1:
            break
        if isprime:
            primes.append(k)
            for m in range(k * k, n + 1, k):
                flags[m] = False
            while number % k == 0:
                factors.append(k)
                number = number // k
    return factors


def divisor_count(n: int) -> int:
    """ Counts the number of divisors of n,
        including 1 and the number itself.
    """
    list_of_factors = prime_factors(n)
    set_of_factors = set(list_of_factors)
    prod = 1
    for prime in set_of_factors:
        multiplicity = 1 + list_of_factors.count(prime)
        prod *= multiplicity
    return prod


def prime_factors_given_primes(n: int, primes: list(int)) -> int:
    """
    Returns the list of all prime factors of n,
    each prime appearing the same number of times as its multiplicity,
    given a list that includes all primes less than n
    Ex.: prime_factors(60, [2, 3, 5, 7, 11]) -> [2, 2, 3, 5]
    """
    prime_factors = []
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            prime_factors.append(p)
            n = n // p
    return prime_factors


def prime_tuples_given_primes(n: int, primes: list(int)) -> int:
    """
    Returns the set of all prime factors of n in tuple form,
    given a list that includes all primes less than n
    Ex.: prime_factors(60, [2, 3, 5, 7, 11]) -> {(2,2), (3,1), (5, 1)}
    """
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


def proper_divisors_given_primes(n: int, primes: list(int)) -> list(int):
    """
    Returns the list of all proper divisors of n (i.e., < n)
    given a list that includes all primes less than n
    """
    list_of_prime_factors = prime_factors_given_primes(n, primes)
    m = len(list_of_prime_factors)
    tuples = set()
    for k in range(1, m):
        new_tuples = set(itertools.combinations(list_of_prime_factors, k))
        tuples = tuples.union(new_tuples)
    result = [prod(t) for t in tuples]
    result.append(1)
    return result


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


# %%%%% Functions involving matrices and arrays %%%%% #
def transpose(A: list) -> list:
    """
    Transposes a (not necessarily square nor numeric) matrix
    (list of lists, each of the same size)
    """
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


def proper_divisors(n: int, primes: list(int)) -> list(int):
    """
    Returns the list of all divisors of n distinct from n
    given a list that includes all primes less than n
    """
    list_of_prime_factors = prime_factors_given_primes(n, primes)
    m = len(list_of_prime_factors)
    tuples = set()
    for k in range(1, m):
        new_tuples = set(itertools.combinations(list_of_prime_factors, k))
        tuples = tuples.union(new_tuples)
    result = [prod(t) for t in tuples]
    result.append(1)
    return result


def sum_of_proper_divisors(n: int, primes: list(int)) -> int:
    """
    Returns the sum of all proper divisors of n
    given a list that includes all primes less than n
    """
    return(sum(proper_divisors(n, primes)))


# %%%%% Miscellanea %%%%% #

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


def palindromes(n: int) -> list(int):
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

# %%%%% Characters and strings %%%%% #

def convert_list_to_int(lst: list(int)) -> int:
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


def flatten(t: list(list)) -> list:
    """ Converts a list of lists into a single list by joining all sublists,
    e.g., flatten([[1, 2], [2, 3]]) --> [1, 2, 2, 3]
    """
    return [item for sublist in t for item in sublist]
