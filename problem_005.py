# Problem 5


def primes(n):
    """ Return a list of all primes less than or equal to n """
    list_of_primes = [2, 3]
    list_of_nonprimes = [1, 4]
    for k in range(4, n+1):
        for p in list_of_primes:
            if k % p == 0:
                list_of_nonprimes.append(k)
                break
        if list_of_nonprimes[-1] != k:
            list_of_primes.append(k)
    return list_of_primes


def factors(n):
    """ Obtains the list of all prime factors of n """
    list_of_primes = []
    list_of_nonprimes = [1, ]
    factors = []
    k = 2
    while k <= n:
        for p in list_of_primes:
            if k % p == 0:
                list_of_nonprimes.append(k)
                k += 1
                break
        if list_of_nonprimes[-1] != k:
            list_of_primes.append(k)
            while n % k == 0:
                factors.append(k)
                n = n / k
            k += 1
    return factors


multiplicities = []
for p in primes(20):
    max_mult = 1
    for n in range(1, 21):
        m = factors(n).count(p)
        if max_mult < m:
            max_mult = m
    multiplicities.append(max_mult)

print(primes(20))
print(multiplicities)
highest = [p**m for p, m in zip(primes(20), multiplicities)]
print(highest)
number = 1
for n in highest:
    number = number * n
print(number)
