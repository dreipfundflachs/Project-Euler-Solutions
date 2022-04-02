# PROJECT EULER - PROBLEM 17
import time


def count_teens(n):
    """ Counts the number of letters of an integer between 0 and 19 """
    if n < 20:
        if n == 0:
            return 0
        elif n == 1 or n == 2 or n == 6 or n == 10:
            return 3
        elif n == 4 or n == 5 or n == 9:
            return 4
        elif n == 3 or n == 7 or n == 8:
            return 5
        elif n == 12 or n == 11:
            return 6
        elif n == 15 or n == 16:
            return 7
        elif n == 13 or n == 14 or n == 18 or n == 19:
            return 8
        elif n == 17:
            return 9
    elif n >= 20 or n < 0:
        raise ValueError("Number is greater than 20 or less than 0")


def count_ties(d):
    """ Counts the number of letters of d0 for d = 2, 3, ..., 9 """
    if d < 2 or d > 9:
        raise ValueError("Digit is greater than 9 or less than 2")
    else:
        if d == 4 or d == 5 or d == 6:
            return 5
        elif d == 2 or d == 3 or d == 8 or d == 9:
            return 6
        elif d == 7:
            return 7


def count_small(n):
    """ Counts the number of letters of a number between 1 and 99 """
    if n < 1 or n > 99:
        raise ValueError("Digit is greater than 999 or less than 1")
    elif n < 20:
        number_of_letters = count_teens(n)
    else:
        d_0 = n % 10
        d_1 = (n - d_0) // 10
        number_of_letters = count_ties(d_1) + count_teens(d_0)
    return number_of_letters


def count_letters(n):
    """ Counts the number of letters in a number between 1 and 999 """
    if n < 1 or n > 999:
        raise ValueError("Digit is greater than 999 or less than 1")
    elif n > 99:
        r = n % 100
        d_2 = (n - r) // 100
        if r == 0:
            number_of_letters = count_teens(d_2) + 7
        else:
            number_of_letters = count_teens(d_2) + 10 + count_small(r)
    else:
        number_of_letters = count_small(n)
    return number_of_letters


start = time.time()

numbers = list(range(1, 1000))
list_of_counts = [count_letters(n) for n in numbers]

s = sum(list_of_counts) + 3 + 8
print(s)

end = time.time()
print(f"Program runtime: {end - start} seconds")
