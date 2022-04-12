# Problem 5

# multiplicities = []
# for p in primes(20):
#     max_mult = 1
#     for n in range(1, 21):
#         m = factors(n).count(p)
#         if max_mult < m:
#             max_mult = m
#     multiplicities.append(max_mult)
#
# print(primes(20))
# print(multiplicities)
# highest = [p**m for p, m in zip(primes(20), multiplicities)]
# print(highest)
# number = 1
# for n in highest:
#     number = number * n
# print(number)


# Problem 7


# def nthprime(n):
#     """ Returns list containing first to nth prime number  """
#     list_of_primes = [2, ]
#     k = 3
#     while k >= 1 and len(list_of_primes) < n:
#         prime = True
#         for p in list_of_primes:
#             if k % p == 0:
#                 prime = False
#                 k += 1
#                 break
#         if prime is True:
#             list_of_primes.append(k)
#             k += 1
#     return list_of_primes
#
#
# problem_7 = nthprime(10001)
# print(problem_7[-1])


# Problem 10


def problem_10(n):
    """ Calculate the sum of all primes less than or equal to n """
    list_of_primes = [2, 3]
#    list_of_nonprimes = [1, 4]
    s = 0
    for k in range(4, n+1):
        is_prime = True
        for p in list_of_primes:
            if k % p == 0:
                is_prime = False
                break
        if is_prime is True:
            list_of_primes.append(k)
            s += k
    return s


print(problem_10(10**5))
