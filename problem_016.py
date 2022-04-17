#################################
#  PROJECT EULER - PROBLEM 016  #
#################################
import time


def get_sum_of_digits(n: int) -> int:
    """ Returns the sum of all the digits of the positive integer n. """
    sum_of_digits = 0
    while n > 0:
        last_digit = n % 10
        sum_of_digits += last_digit
        n = (n - last_digit) // 10
    return sum_of_digits


start = time.time()

N = 2 ** 1000
print(get_sum_of_digits(N))

end = time.time()
print(f"Program runtime: {end - start} seconds")
