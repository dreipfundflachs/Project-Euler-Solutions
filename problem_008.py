#################################
#  PROJECT EULER - PROBLEM 008  #
#################################
import time


def get_list_product(numbers: list[int]) -> int:
    """ Takes a list of integers and returns their product """
    product = 1
    for k in numbers:
        product *= int(k)
    return product


start = time.time()

# The number in the problem statement was pasted into the file below.
number = ''
with open('p008_number.txt') as file_object:
    for line in file_object:
        number += line.strip()

N = 1000  # Total number of digits in the given number.

max_product = 1

for k in range(12, N):
    current_product = get_list_product(number[k - 12: k + 1])
    max_product = max(max_product, current_product)

print(max_product)

end = time.time()
print(f"Program runtime: {end - start} seconds")
