#################################
#  PROJECT EULER - PROBLEM 093  #
#################################
import time
from itertools import combinations, product


def combine(a: int, b: int, operator: str) -> int:
    """ Yields the result of the expression a (operator) b, where 'operator'
    is a binary operator, passed as a string. """
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    # Caution, even if an intermediate division results in a float, the final
    # result may still be an integer, so we cannot discard a float right away.
    if operator == '/':
        try:
            d = a / b
        except ZeroDivisionError:
            return 0
        return d


def combine_list(numbers: list[int], operator: str, i: int, j: int) -> int:
    """ Given a list of numbers, an arithmetic operator and a pair of indices,
    returns a new list of numbers, in which the corresponding pair of elements
    in the list is replaced by the result of operating on them with the
    given operator. """
    numbers_copy = numbers[:]
    a = numbers_copy[i]
    b = numbers_copy[j]
    result = combine(a, b, operator)
    numbers_copy.remove(a)
    numbers_copy.remove(b)
    numbers_copy.append(result)
    return numbers_copy


def find_targets(list_of_digits: list[int]) -> list[int]:
    """ Given a list of four digits, returns a list containing all natural
    numbers (> 0) which can be obtained from the four digits by means of the
    four elementary arithmetic expression, in some combination."""
    targets = set()
    for operator_list in product(OPERATORS, repeat=3):
        for (i_1, j_1) in\
                [(i, j) for (i, j) in product(range(4), repeat=2) if i != j]:
            numbers = list_of_digits[:]
            numbers_1 = combine_list(numbers, operator_list[0], *(i_1, j_1))
            for (i_2, j_2) in [(i, j) for (i, j) in
                               product(range(3), repeat=2) if i != j]:
                numbers_2 = combine_list(numbers_1, operator_list[1],
                                         *(i_2, j_2))
                for (i_3, j_3) in [(i, j) for (i, j) in
                                   product(range(2), repeat=2) if i != j]:
                    numbers_3 = combine_list(numbers_2, operator_list[2],
                                             *(i_3, j_3))
                    result = numbers_3[0]
                    if result > 0 and result == int(result):
                        targets.add(int(result))
    return targets


def chain(set_of_numbers: set) -> int:
    """ Determines the largest integer n such that every number
    between 1 and n (including n) lies in the given set of numbers."""
    list_of_numbers = sorted(list(set_of_numbers))
    length = len(list_of_numbers)
    for k in range(length):
        if list_of_numbers[k] != k + 1:
            break
    return k


start = time.time()

# We also need to include 0 as a valid digit.
DIGITS = list(range(0, 10))
OPERATORS = ['+', '-', '*', '/']

m = 28
max_digits = []

# For each digit combination consisting of four digits...
for digit_combination in combinations(DIGITS, 4):
    list_of_digits = list(digit_combination)
    # Find the largest integer n such that every number between 1 and n can be
    # obtained from the digit combination by means of arithmetic operations.
    n = chain(find_targets(list_of_digits))
    # If this number exceeds the previous largest number, store it as the new
    # maximum, along with the list of digits that gave rise to it.
    if n > m:
        m = n
        max_digits = list_of_digits

print((f"Combining the digits in {max_digits} under all possible "
       f"combinations of the\nelementary arithmetic operations yields each "
       f"natural number between 1 and {m}."))

end = time.time()
print(f"Program runtime: {end - start} seconds")
