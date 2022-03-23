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


# Problem 7

def nthprime(n):
    """ Returns list containing first to nth prime number  """
    list_of_primes = [2, ]
    k = 3
    while k >= 1 and len(list_of_primes) < n:
        prime = True
        for p in list_of_primes:
            if k % p == 0:
                prime = False
                k += 1
                break
        if prime is True:
            list_of_primes.append(k)
            k += 1
    return list_of_primes


problem_7 = nthprime(10001)
print(problem_7[-1])
