##############################################################
#  SOME USEFUL FUNCTIONS FOR SOLVING PROJECT EULER PROBLEMS  #
##############################################################

from math import prod, isqrt
from itertools import combinations
from functools import reduce
from typing import Callable
from scipy.special import comb


#############
#  CLASSES  #
#############

class Memoize:
    """ Provides memoization for functions through the use of the @Memoize
    decorator. Also consider using @functools.cache. """
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
            # Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]


class Die:
    """ Models a balanced die. """
    def __init__(self, sides=4):
        self.sides = sides

    def roll(self) -> int:
        from random import randint
        return randint(1, self.sides)  # Requires randint from module random


#################################################################
#  FUNCTIONS INVOLVING PRIMES, FACTORIZATION, DIVISORS, ETC...  #
#################################################################

def is_power_of_2(n: int) -> bool:
    """ Decides whether the positive integer n is a power of 2 in O(log_2(n))
    time. """
    assert n >= 1
    return n & (n - 1) == 0


def is_even(n: int) -> bool:
    """ Decides whether a number is even """
    if n % 2 == 0:
        return True
    else:
        return False


def gcd(a: int, b:  int) -> int:
    """ Computes the greatest common divisor (gcd) of integers a and b. """
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> list[int]:
    """
    Returns a list 'result' of size 3 where, referring to the equation
    ax + by = gcd(a, b):
        result[0] = gcd(a, b)
        result[1] = x
        result[2] = y.
    The Euclidean algorithm proceeds by finding q_n, r_n such that:
        a = q_0 b + r_1
        b = q_1 r_1 + r_2
        r_1 = q_2 r_2 + r_3
        ...
        r_{n - 1} = q_n r_n + r_{n + 1}
    Suppose that we have already computed that:
        r_{n - 1} = (old_s a + old_t b) and that r_n = (s a + t b).
    Then it follows that:
        r_{n + 1} = (old_s - q_n s) a + (old_t - q_n t) b.
    """
    if a > b:
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = b, a

        while r:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
        return [old_r, old_s, old_t]

    else:
        d, y, x = extended_gcd(b, a)
        return [d, x, y]


def get_inverse_mod(n: int, m: int) -> int:
    """ Returns the inverse of n modulo m, for m > 0 and n relatively prime to
    n. Also consider using pow(n, -1, m). """
    d, x, y = extended_gcd(n, m)
    if d != 1:
        raise ValueError("""The two arguments of 'get_inverse_mod' must be
                         relatively prime positive integers.""")
    else:
        return x % m


def chinese_remainder(remainders: list[int], modulos: list[int]) -> int:
    """ Given a list of remainders and a list of modulos, of the same length,
    where the modulos are relatively prime (i.e., the g.c.d. of all of them is
    1), returns the unique integer x modulo m, where m is the product of all
    the remainders, such that for each i
        x = remainders[i] mod modulos[i] """
    assert len(remainders) == len(modulos)
    result = 0
    # Let m be the product of the modulos:
    m = reduce(lambda a, b: a * b, modulos)
    # We want x to be congruent to a mod p, where
    # a = remainders[i] and p = modulos[i], for each i:
    for (a, p) in [(remainders[i], modulos[i]) for i in range(len(modulos))]:
        n = m // p
        result += a * pow(n, -1, p) * n
    return result % m


def binomial_mod_p(m: int, n: int, p: int) -> int:
    """ Computes the binomial coefficient m choose n modulo p, using Lucas'
    theorem. Requires the function 'get_b_ary_representation'. """
    digits_m = get_b_ary_representation(m, p)
    digits_n = get_b_ary_representation(n, p)
    J = min(len(digits_m), len(digits_n))
    binomial = 1
    for j in range(J):
        binomial = (binomial * comb(digits_m[j], digits_n[j], exact=True)) % p
    return binomial


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


def fast_power(base: int, exponent: int) -> int:
    """ Computes base**exp (mod m) efficiently (in O(log(exp)) time). """
    if exponent == 1:
        return base
    elif exponent % 2 == 0:
        return fast_power(base, exponent // 2)**2
    else:
        return base * fast_power(base, exponent - 1)


def power_mod(base: int, exponent: int, m: int) -> int:
    """ Computes base**exp (mod m) efficiently (in O(log(exp)) time). """
    if exponent == 1:
        return base % m
    elif exponent % 2 == 0:
        return (power_mod(base, exponent // 2, m)**2) % m
    else:
        return ((base * power_mod(base, (exponent - 1)//2, m)**2) % m)


def hyper_exp(base: int, exponent: int, m: int) -> int:
    """ Computes the result of hyperexponentiating the given base to the given
    exponent (>= 0) modulo m. """
    current_exponent = 1
    for k in range(1, exponent + 2):
        current_exponent = power_mod(base, current_exponent, m)
    return current_exponent


def get_primes_up_to(n: int) -> list[int]:
    """ Returns a list of all primes <= n using Eratosthenes' sieve """
    prime_flags = [True for _ in range(n + 1)]
    prime_flags[0] = False
    prime_flags[1] = False
    for (k, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(k * k, n + 1, k):
                prime_flags[multiple] = False
    return [p for p in range(2, n + 1) if prime_flags[p]]


def get_primes_up_to_greater_than(N: int, M: int) -> list[int]:
    """ Returns a list of all primes p such that M <= p <= N using
    Eratosthenes' sieve.  """
    primes = []
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            if p >= M:
                primes.append(p)
            for multiple in range(p * p, N + 1, p):
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


def get_smallest_prime_factor(N: int) -> list[int]:
    """ Using a sieving method, returns a list whose n-th entry is the smallest
    prime factor of n, for each n <= N. Takes O(N log(N)) time and O(N) memory.
    """
    assert N >= 1
    S = isqrt(N)
    prime_flags = [True for _ in range(S + 1)]
    smallest = [n for n in range(N + 1)]
    prime_flags[0], smallest[0] = False, 0
    prime_flags[1], smallest[1] = False, 1

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(p * p, S + 1, p):
                prime_flags[multiple] = False
            for multiple in range(p, N + 1, p):
                if smallest[multiple] == multiple:
                    smallest[multiple] = p
    return smallest


def sieve_prime_factors(N: int) -> list[list[int]]:
    """ For each integer n <= N, uses a sieving method to compute the list of
    all prime factors of n, each prime being repeated as many times as its
    multiplicity. For example:
        sieve_prime_factors(6) = [[], [], [2], [3], [2, 2], [5], [2, 3]]
    """
    prime_flags = [True for _ in range(N + 1)]
    prime_flags[0], prime_flags[1] = False, False
    prime_factors = [[] for _ in range(N + 1)]

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for m in range(p, N + 1, p):
                prime_factors[m].append(p)
                prime_flags[m] = False
            k = 2
            while (q := p**k) <= N:
                for m in range(q, N + 1, q):
                    prime_factors[m].append(p)
                k += 1
    return prime_factors


def sieve_distinct_prime_factors(N: int) -> list[list[int]]:
    """ For each integer n <= N, uses a sieving method to compute the list of
    all _distinct_ prime factors of n. For example:
        sieve_prime_factors(8) = [[], [], [2], [3], [2], [5], [2, 3], [7], [2]]
    """
    prime_flags = [True for _ in range(N + 1)]
    prime_flags[0], prime_flags[1] = False, False
    prime_factors = [[] for _ in range(N + 1)]

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for m in range(p, N + 1, p):
                prime_factors[m].append(p)
                prime_flags[m] = False
    return prime_factors


def sieve_proper_divisors(N: int) -> list[list[int]]:
    """ For each integer n <= N, computes the list of all _proper_ divisors of
    n, i.e., including 1 but excluding n. Requires the function
    'sieve_prime_factors'. For example:
        f(6) = [[[], [1], [1], [1], [1, 2], [1], [3, 1, 2]]
    Note that the divisors are not necessarily listed in increasing order. """
    list_of_prime_factors = sieve_prime_factors(N)
    list_of_divisors = [[] for _ in range(N + 1)]
    list_of_divisors[1] = [1]
    for n in range(2, N + 1):
        m = len(list_of_prime_factors[n])
        tuples = set()
        for k in range(0, m):
            new_tuples = set(combinations(list_of_prime_factors[n], k))
            tuples = tuples.union(new_tuples)
        divisors_of_n = [prod(t) for t in tuples]
        list_of_divisors[n] = divisors_of_n
    return list_of_divisors


def sieve_divisors(N: int) -> list[list[int]]:
    """ For each integer n <= N, computes the list of all divisors of n
    (including 1 and n). Requires the function 'sieve_prime_factors'. Example:
        f(6) = [[], [1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6]]
    """
    list_of_prime_factors = sieve_prime_factors(N)
    list_of_divisors = [[] for _ in range(N + 1)]
    list_of_divisors[1] = [1]
    for n in range(2, N + 1):
        m = len(list_of_prime_factors[n])
        tuples = set()
        for k in range(0, m):
            new_tuples = set(combinations(list_of_prime_factors[n], k))
            tuples = tuples.union(new_tuples)
        divisors_of_n = [prod(t) for t in tuples]
        divisors_of_n.append(n)
        list_of_divisors[n] = divisors_of_n
    return list_of_divisors


def sieve_coprime_decomposition(N: int) -> list[list[int]]:
    """ For each integer n <= N, uses a sieving method to compute the (unique)
    decomposition of n as a product of prime _powers_, given as a list. Returns
    a list of such decompositions for all n ranging from 0 to N. For example:
        f(9)        = [[0], [1], [2], [3], [4], [5], [2, 3], [7], [8], [9]]
        f(17)[17]   = [17]
        f(30)[30]   = [2, 3, 5]
        f(40)[40]   = [8, 5]
        f(60)[60]   = [4, 3, 5]
    where f denotes the present function. """

    assert N >= 1
    prime_flags = [True for _ in range(N + 1)]
    decompositions = [[] for _ in range(N + 1)]
    prime_flags[0], decompositions[0] = False, [0]
    prime_flags[1], decompositions[1] = False, [1]

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for multiple in range(p, N + 1, p):
                prime_flags[multiple] = False
                decompositions[multiple].append(p)
            k = 2
            while (q := p**k) <= N:
                for multiple in range(q, N + 1, q):
                    decompositions[multiple][-1] *= p
                k += 1
    return decompositions


def sieve_composite(N: int) -> list[int]:
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


def sieve_phis(N: int) -> list[int]:
    """ Uses a sieving method to compute phi(n) for all n <= N, where phi
    denotes Euler's totient function. Returns the list
    [phi(n) for n in range(N + 1)]. """

    prime_flags = [True for _ in range(N + 1)]
    prime_flags[0], prime_flags[1] = False, False
    phis = [n for n in range(N + 1)]
    phis[1] = 0

    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            for n in range(p, N + 1, p):
                phis[n] = (phis[n] // p) * (p - 1)
                prime_flags[n] = False
    return phis


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
    if n <= 1 or (n % 2 == 0 and n != 2):
        return False
    else:
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True


def miller_rabin(n: int, k: int = 40) -> bool:
    """ Verifies whether a number n is prime using by using k random
    numbers between 2 and n - 1. A good value for k in general is k = 40.
    """
    from random import randrange
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


def moebius(n: int) -> int:
    """ Given a positive integer n, returns mu(n), the value of the Moebius
    function at n, computed directly by finding all prime factors of n.
    Requires O(sqrt(n)) memory and O(sqrt(n) * log(n)) time. """
    assert n >= 1
    N = isqrt(n)
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    product = 1
    for (p, is_prime) in enumerate(prime_flags):
        if n == 1:
            break
        if is_prime:
            for multiple in range(p * p, N + 1, p):
                prime_flags[multiple] = False
            if n % p == 0:
                n = n // p
                product *= -1
                if n % p == 0:
                    product = 0
                    break
    if n != 1:
        product *= -1
    return product


def moebius_sieve(n: int) -> list[int]:
    """ Given a positive integer n, returns a list mu such that mu[n] = mu(n),
    the value of the Moebius function at k, for each 1 <= k <= n.  Uses a
    sieving method to compute these values. """
    assert n >= 1
    mu = [1 for _ in range(n + 1)]
    mu[0] = 0
    prime_flags = [True for _ in range(n + 1)]
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if is_prime:
            mu[p] = -1
            for i in range(2, n // p + 1):
                prime_flags[p * i] = False
                if i % p == 0:
                    mu[p * i] = 0
                else:
                    mu[p * i] *= -1
    return mu


def has_prime_factors_taken_from(n: int, primes: list[int]) -> bool:
    """ Decides whether all prime factors of n are elements of the given list
    'primes'. """
    assert n >= 1
    for p in primes:
        if n == 1:
            return True
        while n % p == 0:
            n //= p

    return n == 1


def get_prime_factors(n: int) -> list[int]:
    """ Returns the list of all prime factors of n, each prime appearing as
    many times as its multiplicity indicates.  Determines all necessary primes
    on the fly. """
    from math import isqrt
    assert n >= 1
    prime_factors = []
    N = isqrt(n)
    prime_flags = [True] * (N + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if n == 1:
            break
        if is_prime:
            for multiple in range(p * p, N + 1, p):
                prime_flags[multiple] = False
            while n % p == 0:
                prime_factors.append(p)
                n = n // p
    if n != 1:
        prime_factors.append(n)

    return prime_factors


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
    return reduce(lambda x, y: x * y, prime_factors)  # requires functools


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


def has_two_prime_factors(n: int, primes: list[int]) -> bool:
    """ Decides whether a number has exactly two distinct prime factors. """
    number_of_prime_factors = 0
    for p in primes:
        if n == 1:
            break
        # If n /= 1 and the number of prime factors is >= 2, then it must be at
        # least 3.
        if number_of_prime_factors == 2:
            number_of_prime_factors = 3
            break
        if n % p == 0:
            n = n // p
            number_of_prime_factors += 1
            while n % p == 0:
                n = n // p
    if number_of_prime_factors == 2:
        return True
    else:
        return False


def get_highest_power(m: int, n: int) -> int:
    """ Returns the largest e >= 0 such that m**e divides n. """
    if n == 0:
        raise ValueError("Second argument cannot be 0.")
    else:
        e = 0
        while n % m == 0:
            e += 1
            n //= m
        return e


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


def get_proper_divisors(n: int) -> list[int]:
    """ Given n > 0, returns all divisors of n smaller than n as a list. """
    if n <= 0:
        return []
    divisors = [1]
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            divisors.append(k)
    return divisors


def get_divisors(n: int) -> set[int]:
    """ Given n > 1, returns the set of all divisors of n, incl. 1 and n. """
    divisors = {1, n}
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            divisors.add(k)
            divisors.add(n // k)
    return divisors


def list_divisors(n: int) -> list[int]:
    """ Given n > 1, returns the set of all divisors of n, incl. 1 and n. """
    small_divisors = [1]
    large_divisors = [n]
    for k in range(2, isqrt(n) + 1):
        if n % k == 0:
            small_divisors.append(k)
            large_divisors.append(n // k)
    return small_divisors + reversed(large_divisors)


def get_proper_divisors_given_primes(n: int, primes: list[int]) -> list[int]:
    """ Returns the list of all proper divisors of n (i.e., < n) given a list
    that includes all primes less than n. Requires 'combinations' from
    module 'itertools'.  """
    list_of_prime_factors = get_prime_factors_given_primes(n, primes)
    m = len(list_of_prime_factors)
    tuples = set()
    for k in range(1, m):
        new_tuples = set(combinations(list_of_prime_factors, k))
        tuples = tuples.union(new_tuples)
    result = [prod(t) for t in tuples]  # Requires module 'math'.
    result.append(1)
    return result


def sum_of_proper_divisors(n: int, primes: list[int]) -> int:
    """ Returns the sum of all proper divisors of n given a list that includes
    all primes less than n """
    return sum(get_proper_divisors_given_primes(n, primes))


def get_b_ary_representation(n: int, b: int) -> list[int]:
    """ Computes the b-ary representation of n >= 1 in base b >= 2. Returns the
    digits as a list, from least significant to most significant, e.g.,
        (10, 2) -> [0, 1, 0, 1] since 10 = 2^1 + 2^3. """
    assert n >= 1 and b >= 2
    digits = []
    while n != 0:
        digits.append(n % b)
        n //= b
    return digits


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


def get_highest_power_in_fact(n: int, p: int) -> int:
    """ Returns the largest power of a _prime_ number p dividing the factorial
    n! of n. This is given by:
        n // p + n // p**2 + n // p**3 + ... + n // p**K
    where K is the largest (integer) power of p that does not exceed n. """
    largest_power = 0
    while n > 1:
        n //= p
        largest_power += n
    return largest_power


def smallest_factorial_divisible_by_prime_power(p: int, e: int) -> int:
    """ Given a prime p and e >= 0, returns the smallest m such that m! is
    divisible by p**e. Note that m must be a multiple of p, say, m = k * p. To
    find it, we start from the upper bound k = e and sequentially test
    decreasing values of k until (k * p)! is no longer divisible by p**e.
    Requires the function 'get_highest_power_in_fact'. """
    for k in reversed(range(e)):
        if get_highest_power_in_fact(k * p, p) < e:
            break
    return (k + 1) * p


def get_highest_power_in_binom(n: int, k: int, p: int) -> int:
    """ Returns the largest power of a _prime_ number p dividing the binomial
    coefficient (n, k) (a.k.a. 'n choose k'). """
    return (get_highest_power_in_fact(n, p)
            - get_highest_power_in_fact(k, p)
            - get_highest_power_in_fact(n - k, p))


#########################################################
#  FUNCTIONS INVOLVING SQUARES AND PYTHAGOREAN TRIPLES  #
#########################################################


def is_square(n: int) -> bool:
    """ Decides whether an integer is the square of another integer. """
    return pow(n, 0.5) % 1 == 0


def get_primitive_pythagorean_triples(N: int) -> set[int]:
    """ Returns a set containing all _primitive_ Pythagorean triples (a, b, c)
    with a <= b <= c <= N.

    Euclid's formula for Pythagorean triples states that any _primitive_
    Pythagorean triple (a, b, c) has the form:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
    where
        (i) 0 < n < m.
        (ii) Exactly one of m, n is even.
        (iii) gcd(m, n) = 1.
    """
    triples = set()
    for m in range(2, isqrt(N - 1) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a > b:
                    a, b = b, a
                triples.add((a, b, c))
    return triples


def get_pythagorean_triples(N: int) -> set[int]:
    """ Returns a set containing all (not necessarily primitive) Pythagorean
    triples (a, b, c) with a <= b <= c <= N.

    Euclid's formula for Pythagorean triples states that any _primitive_
    Pythagorean triple (a, b, c) has the form:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
    where
        (i) 0 < n < m.
        (ii) Exactly one of m, n is even.
        (iii) gcd(m, n) = 1.
    """
    triples = set()
    for m in range(2, isqrt(N - 1) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a > b:
                    a, b = b, a
                k = 1
                while k * c <= N:
                    triples.add((k * a, k * b, k * c))
                    k += 1
    return triples


###############################
#  FUNCTIONS INVOLVING LISTS  #
###############################


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


def get_frequencies(lst: list[int]) -> list[int]:
    """ Given a list, returns a new list consisting of all the frequency counts
    of its unique elements. """
    return sorted([lst.count(x) for x in set(lst)])


def insert_in_ascending(n: int, a: list[int]) -> list[int]:
    """ Given an integer or float and an ascending list of numbers of the
    same type, inserts the number in the list. Also take a look at 'insort'
    from the 'bisect' module. """
    if a == []:
        return [n]
    else:
        m = len(a) // 2
        if a[m] == n:
            return a[:m + 1] + [n] + a[m + 1:]
        elif a[m] < n:
            return a[:m + 1] + insert_in_ascending(a[m + 1:], n)
        else:
            return insert_in_ascending(a[:m], n) + a[m:]


def insert_in_descending(n: int, a: list[int]) -> list[int]:
    """ Given an integer or float and a descending list of numbers of the
    same type, inserts the number in the list. Also take a look at 'insort'
    from the 'bisect' module."""
    if a == []:
        return [n]
    else:
        m = len(a) // 2
        if a[m] == n:
            return a[:m + 1] + [n] + a[m + 1:]
        elif a[m] > n:
            return a[:m + 1] + insert_in_descending(a[m + 1:], n)
        else:
            return insert_in_descending(a[:m], n) + a[m:]


def get_maximum_sublist_sum(numbers: list[int]) -> int:
    """ Given a list [n_0, n_1, ..., n_{m-1}] of (possibly negative) integers,
    returns the maximum sum
        n_i + n_{i+1} + ... + n_{j-1} + n_j
    among all sublists with 1 <= i <= j <= m - 1.
    This is known as "Kadane's algorithm" and takes O(n) time and O(1) memory.
    Note that if the list is empty or if all of its elements are negative, then
    the function returns 0 (which is the sum of an empty sublist). """
    maximum_sum = 0
    current_sum = 0
    for n in numbers:
        current_sum = max(0, current_sum + n)
        maximum_sum = max(current_sum, maximum_sum)
    return maximum_sum


#############################################
#  FUNCTIONS INVOLVING MATRICES AND ARRAYS  #
#############################################

def transpose(A: list) -> list:
    """ Transposes a (not necessarily square nor numeric) matrix (list of
    lists, each of the same size) """
    m = len(A)
    n = len(A[0])
    B = []
    for j in range(0, n):
        column = []
        for i in range(0, m):
            column.append(A[i][j])
        B.append(column)
    return B


#################
#  MISCELLANEA  #
#################

def number_to_base(n: int, b: int) -> list[int]:
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    return digits[::-1]


def precise_partitions(target: int, bound: int, summands: int) -> [tuple[int]]:
    """ Computes the unique ways (as a list of tuples) in which one can
    partition the integer 'target' using numbers in the range from 1 to 'bound'
    (inclusive) in exactly the given number of summands. For example:
        get_partitions(8, 5, 3) = [(2, 3, 3), (2, 2, 4), (1, 3, 4), (1, 2, 5)]
    """
    partitions = []
    if summands < 0 or target < summands:
        return []
    elif target == 0:
        return [()]
    else:
        for k in range(1, bound + 1):
            partitions += [p + (k,) for p in
                           precise_partitions(target - k, k, summands - 1)]
    return partitions


def get_partitions(target: int) -> [tuple[int]]:
    """ Computes the unique ways (as a list of increasing tuples) in which one
    can partition the integer 'target' using numbers from 1 to target
    (inclusive). For example:
        get_partitions(4) = [(4,), (2, 2), (1, 3), (1, 1, 2), (1, 1, 1, 1)]
    """
    assert target >= 1
    partitions = []
    for number_of_summands in range(1, target + 1):
        partitions += precise_partitions(target, target, number_of_summands)
    return partitions


def get_number_of_partitions(target: int, bound: int, summands: int)\
        -> [tuple[int]]:
    """ Computes the number of unique ways (as a list of tuples) in which one
    can partition the integer 'target' using numbers in the range from 1 to
    'bound' (inclusive) in exactly the given number of summands. For example:
        get_number_of_partitions(8, 5, 3) = 4 """
    if summands < 0 or target < summands:
        return 0
    elif target == 0:
        return 1
    else:
        partitions = 0
        for k in range(1, bound + 1):
            partitions += get_number_of_partitions(target - k, k, summands - 1)
    return partitions


def get_ordered_partitions(n: int) -> list[list[int]]:
    """ Determines all the ordered partitions of n, each partition being
    represented by a list. For example, the ordered partitions of 4 are:
        [1, 1, 1, 1],
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1],
        [2, 2],
        [1, 3],
        [3, 1],
        [4].
    The total number of such partitions is 2**(n - 1) if n >= 1 (see the
    function 'count_ordered_partitions').
    """
    if n == 0:
        return 0
    else:
        partitions = [[] for k in range(n + 1)]
        partitions[0] = [[]]
        for k in range(1, n + 1):
            # Determine the ordered partitions of k and store them, as follows.
            # Any partition of k can be obtained from a partition of k - i by
            # appending i, for some i between 1 and k.
            for i in range(1, k + 1):
                for p in partitions[k - i]:
                    partitions[k].append(p + [i])
        return partitions[n]


def count_ordered_partitions(n: int) -> int:
    """ Counts the number of ordered partitions of an integer n. This is given
    simply by 2**(n - 1) if n >= 1.

    The proof is by induction: Except for the partition [n], the remaining
    ordered partitions of n can be obtained from the partitions of n - k, for k
    between 1 and n - 1 (inclusive), by appending k.  Hence there are
        1 + 2**0 + 2**1 + ... + 2**(n - 2)
        = 1 + [2**(n - 1) - 1]
        = 2**(n - 1)
    total ordered partitions of n.
    """
    if n <= 0:
        return 0
    else:
        return 2**(n - 1)


def multinomial(*coefficients: list[int]) -> int:
    """ Given a list k_1, ..., k_r, computes the multinomial coefficient
        n! / (k_1)! * (k_2)! * ... * (k_r)! where n = k_1 + ... + k_r. """
    result = 1
    m = 1  # Will run through the values of n!.
    for k in coefficients:
        for j in range(1, k + 1):
            result *= m
            result //= j
            m += 1
    return result


def get_powerset(ns: set[int]) -> list[iter]:
    """ Returns the power set of 'ns' as a list, e.g., get_powerset([1,2,3])
    yields [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)].
    Requires 'combinations' from module 'itertools'. """
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


def is_terminating_decimal(n: int, d: int) -> bool:
    """ Given integers n and d, decides whether the decimal part of n / d is
    terminating (finite) or non-terminating/repeating (infinite).
    Examples:
        Since 1 / 7 = 0.(142857), is_terminating_decimal(1, 7) is False.
        Since 11 / 4 = 2.75, is_terminating_decimal(11, 4) is True.
    To decide whether the decimal part is finite, the function performs long
    division, recording each possible remainder < d along the way. If a
    remainder has already appeared, then the decimal is non-terminating.
    Otherwise, eventually the remainder will be zero and we can break. """
    n = n % d
    remainders = [n]
    while n != 0:
        n *= 10
        while n < d:
            remainders.append(n)
            n *= 10
        n = n % d
        if n in remainders:
            return False
        else:
            remainders.append(n)
    return True


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


def generate_lagged_Fibonacci(N: int) -> list[int]:
    """ Generates the lagged Fibonacci sequence. Returns a list 'sequence'
    where sequence[0] = 0 for completeness (even though in the description, the
    index usually starts at 1). """
    L = 56
    H = 24
    A = 100003
    B = 200003
    C = 300007
    D = 500000
    MOD = 1000000
    sequence = [0]
    for n in range(1, L):
        sequence.append((A -
                        (n * (B - (C * (n**2 % MOD) % MOD)) % MOD)
                        % MOD - D))
    for n in range(L, N + 1):
        sequence.append((sequence[n - H] + sequence[n - L + 1]) % MOD - D)
    return sequence


def fib_iter(n: int, a: int = 0, b: int = 1) -> int:
    """ Computes the n-th Fibonacci number in O(n) time. """
    if n < 0:
        raise ValueError(""" The argument of 'log_fib'
                         must be a positive integer.""")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib_iter(n - 1, b, a + b)


def log_fib(n: int) -> int:
    """ Computes the n-th Fibonacci number in O(log n) time. """
    if n < 0:
        raise ValueError(""" The argument of 'log_fib'
                         must be a positive integer.""")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        m = n // 2
        return log_fib(m) * (2 * log_fib(m - 1) + log_fib(m))
    else:
        m = (n + 1) // 2
        return log_fib(m)**2 + log_fib(m - 1)**2


def is_tail_pandigital(n: int) -> bool:
    """ Decides whether the last 9 digits of an integer are 1-9 pandigital. """
    if {int(d) for d in str(n)[-9:]} == set(range(1, 10)):
        return True
    else:
        return False


################################################
#  FUNCTIONS INVOLVING STRINGS AND CHARACTERS  #
################################################


def is_palindromic(string: str) -> bool:
    """ Checks if the given string is palindromic. """
    return (string == string[::-1])


def is_pandigital(n: int) -> bool:
    """ Decides whether an d-digit integer is such that each digit between 1
    and d appears exactly once in the decimal representation of n. """
    assert n >= 0 and type(n) == int
    set_of_digits = set()
    number_of_digits = 0
    while n != 0:
        set_of_digits.add(n % 10)
        n //= 10
        number_of_digits += 1
    number_of_distinct_digits = len(set_of_digits)
    return (number_of_digits == number_of_distinct_digits and
            set_of_digits == {d for d in range(1, number_of_digits + 1)})


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


def convert_to_dec(digits: list[int]) -> int:
    """ Converts a list of the digits '0' and '1' to the corresponding decimal,
    e.g.,
        [0, 0, 0, 1, 0, 1, 1, 1] -> 23.  """
    if not digits:
        return 0
    else:
        return digits[-1] + 2 * convert_to_dec(digits[:-1])


def convert_to_int(digits: list[int]) -> int:
    """ Converts a list of digits to a single integer, e.g.,
        [1, 2, 3] --> 123. """
    return int(''.join([str(digit) for digit in digits]))


def convert_to_list(n: int) -> list[int]:
    """ Converts an integer to the list of its digits, e.g.,
        1234 -> [1, 2, 3, 4]. """
    if n // 10 > 0:
        init = convert_to_list(n // 10)
    else:
        init = []
    last = n % 10
    return init + [last]


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


def are_equal_strings(string_1: str, string_2: str) -> bool:
    """ Decides if two strings are equal. """
    n_1, n_2 = len(string_1), len(string_2)
    if n_1 != n_2:
        return False
    elif n_1 == n_2 == 0:
        return True
    else:
        if string_1[0] == string_2[0]:
            return are_equal_strings(string_1[1:], string_2[1:])
        else:
            return False


def string_type(string: str) -> tuple[int]:
    """ Given a string, returns a tuple consisting of the frequencies of each
    of its letters, sorted in decreasing order. For example:
        string_type("representation") -> (3, 2, 2, 2, 1, 1, 1, 1, 1)
            corresponding to the letters (e, r, n, t, p, s, a, i, o) """
    return tuple(reversed(sorted(string.count(letter) for letter in
                 set(string))))


def are_anagrams(string_1: str, string_2: str) -> bool:
    """ Decides if two given strings are anagrams of each other. To this end,
    the function searches the second string for the presence of the first
    character of the first string. If it is not found, then False is returned.
    Otherwise, (one instance of) this character is removed from both strings
    and a recursive call on the resulting smaller strings is performed. """
    n_1, n_2 = len(string_1), len(string_2)
    if n_1 != n_2:
        return False
    elif n_1 == n_2 == 0:
        return True
    else:
        i = string_2.find(string_1[0])
        if i == -1:
            return False
        else:
            return are_anagrams(string_1[1:], string_2[:i] + string_2[i + 1:])


def strings_match(str_1: str, str_2: str) -> bool:
    """ Given two strings, decides if one can be transformed into the other by
    applying a bijection of the set of letters of the first to the set of
    letters of the second one. """
    n = len(str_1)
    if len(str_2) != n:
        return False
    else:
        for char in set(str_1):
            char_indices = [k for k in range(n) if str_1[k] == char]
            matching_char = str_2[char_indices[0]]  # Matching char in str_2.
            mchar_indices = [k for k in range(n) if str_2[k] == matching_char]
            if char_indices != mchar_indices:
                return False
    return True


#######################
#  GENERIC UTILITIES  #
#######################


def bisection(f: Callable[[float], float], a: float, b: float,
              eps: float, max_iter: int) -> float:
    """ Uses the bisection method to find a root of the real function f of a
    real variable, within a tolerance of eps. Note that it is _not_ necessary
    that the inputs a and b satisfy:
        (a) a < b; nor
        (b) f(a) < 0 < f(b).
    However, if f(a)f(b) >= 0, then an error is returned.  Requires 'Callable'
    from the 'typing' module for the type annotation.  """

    def search(f: Callable[[float], float], neg_point: float, pos_point: float,
               eps: float, max_iter: int) -> float:
        """ Relying on the intermediate value theorem, uses interval halving
        to find an approximation to a zero of f within the interval joining
        neg_point and pos_point. It is assumed that
            f(neg_point) < 0 < f(pos_point).
        This condition is enforced before 'search' is called. """
        midpoint = (neg_point + pos_point) / 2
        f_mid = f(midpoint)
        if max_iter == 0 or f_mid == 0 or abs(pos_point - midpoint) < eps:
            print(f"Found the approximate zero {midpoint} where the", end=' ')
            print(f"function takes the value {f_mid}.")
            return midpoint
        elif f_mid > 0:
            return search(f, neg_point, midpoint, eps, max_iter - 1)
        else:
            return search(f, midpoint, pos_point, eps, max_iter - 1)

    assert (eps > 0 and max_iter > 0)
    f_a, f_b = f(a), f(b)
    # Check the signs of f(a) and f(b), and call 'search' accordingly:
    if f_a < 0 < f_b:
        return search(f, a, b, eps, max_iter)
    elif f_b < 0 < f_a:
        return search(f, b, a, eps, max_iter)
    else:
        error_message = "The values of the function at the given arguments "
        error_message += f"a = {a} and b = {b} do not have opposite signs; "
        error_message += f"they are f(a) = {f(a)} and f(b) = {f(b)}."
        raise ValueError(error_message)


def dampening(f: Callable[[float], float]) -> Callable[[float], float]:
    """ Given a function f of a real variable x, returns the function
    f_dampened which maps x to the midpoint of x and f(x). Requires 'Callable'
    from the 'typing' module for the type annotation. """
    return lambda x: ((f(x) + x) / 2.0)


def general_loop(indices: list[int],
                 reset_condition: Callable[[list[int]], bool]) -> any:
    """ A prototype for a procedure that loops through an arbitrary number of
    indices, performing some useful computation in the process (to be
    implemented by the user). The return type is not fixed. The arguments are:
        (a) An initial value 'indices' for all the indices, provided as a list
            of integers.
        (b) A 'reset_condition', that is, a function on a list of indices which
            determines whether to increment the _previous_ (instead of the
            current) index and to reset every index thereafter.

    The intuitive idea is to visualize the loop as being controlled by a moving
    head modifying a list of indices. The head begins at the last index. The
    default action is to increment the last index by 1. However, while the
    reset condition is satisfied, the head instead moves from the current
    index to the one preceding it (i.e., to its left), increments the latter by
    1 and resets all of the indices to the right. The iteration ends when the
    head is at (the invalid) position -1. In the simplest situation where the
    indices (i_0, ..., i_{m-1}) run through the product [0, N] x ... x [0, N],
    the reset condition would be that one of the indices exceeds N. """

    def reset_condition(indices: list[int]) -> bool:
        # TODO: Implement the reset condition as nedeed.
        return False

    m = len(indices)
    head = m - 1

    while head != -1:
        head = m - 1
        required_resetting = False

        while reset_condition(indices):
            required_resetting = True
            head -= 1
            if head == -1:
                break
            else:
                indices[head] += 1
                for j in range(head + 1, m):
                    indices[j] = 0
                    # TODO: Depending on the task at hand, one might instead
                    # wish to modify the preceding line to set all indices to
                    # the right of the head to indices[head], for example.

        else:
            if not required_resetting:
                # TODO:
                # Apply the relevant process to the indices here, like adding
                # the value of some function on them to a running total.
                indices[head] += 1
    # TODO:
    # return answer
