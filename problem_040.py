# PROJECT EULER - PROBLEM
import time


def concatenate_list(strings):
    """ Takes a list of strings
        and returns a string which is the concatenation of all of them.
    """
    result = ''
    for element in strings:
        result += element
    return result


start = time.time()

numbers = list(range(1, 7*10**5))
str_numbers = [str(number) for number in numbers]
# print(str_numbers)
digits = concatenate_list(str_numbers)
# print(digits)
# print(digits[10])
product = 1
for n in range(0, 7):
    index = 10**n - 1
    product *= int(digits[index])
print(product)


end = time.time()
print(f"Program runtime: {end - start} seconds")
