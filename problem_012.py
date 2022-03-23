# PROJECT EULER PROBLEM 12
def prime_factors(n):
    """ Returns the list of all prime factors of n """
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


print(prime_factors(30))


def divisor_count(n):
    """ Counts the number of divisors of n """
    list_of_factors = prime_factors(n)
    set_of_factors = set(list_of_factors)
    prod = 1
    for prime in set_of_factors:
        multiplicity = 1 + list_of_factors.count(prime)
        prod *= multiplicity
    return prod


flag = True
k = 2
while flag:
    d_1 = divisor_count(k) * divisor_count(2*k - 1)
    d_2 = divisor_count(k) * divisor_count(2*k + 1)
    if d_1 > 500:
        triangular_number = k * (2*k - 1)
        flag = False
    if d_2 > 500:
        triangular_number = k * (2*k + 1)
        flag = False
    k += 1
print(triangular_number)

#
#
# print(divisor_count(16*9))
#
# n = 1
# while n >= 1:
#     t = n*(n+1) / 2
#     if divisor_count(t) > 500:
#         print(t)
#         break
