#################################
#  PROJECT EULER - PROBLEM 026  #
#################################
import time


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


start = time.time()

N = 1000

max_length = 0
max_d = 0
for d in range(2, N):
    length = len(get_decimal_representation(1, d, N)) - 1
    if length > max_length:
        max_length = length
        max_d = d

print(max_d)

end = time.time()
print(f"Program runtime: {end - start} seconds")
