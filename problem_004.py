#################################
#  PROJECT EULER - PROBLEM 004  #
#################################
import time


def get_largest_palindrome(digits: int) -> int:
    """
    Returns the largest palindromic number that is the product of two numbers
    having 'digits' digits each.
    """
    UPPER = 10**digits
    LOWER = 10**(digits - 1)
    products: list[str] = [str(a * b)
                           for a in range(UPPER, LOWER - 1, -1)
                           for b in range(UPPER, LOWER - 1, -1)
                           ]
    largest = 0

    for number in products:
        rebmun = number[::-1]  # rebnum is the palindrome of number.
        if number == rebmun and int(number) > largest:
            largest = int(number)
    return largest


start = time.time()

D = 3
print(get_largest_palindrome(D))

end = time.time()
print(f"Program runtime: {end - start} seconds")
