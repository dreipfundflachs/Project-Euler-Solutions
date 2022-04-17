#################################
#  PROJECT EULER - PROBLEM 018  #
#################################
import time


def convert_string_to_int(number_strings: list[str]) -> list[int]:
    """ Takes a list of integers formatted as strings and converts it
    into a list of integers. """
    numbers = [int(number_string) for number_string in number_strings]
    return numbers


start = time.time()

# Create a list, each element of which represents a row.
numbers = []
with open('p018_numbers.txt') as file_object:
    for line in file_object:
        numbers.append(line.split())

# Convert the rows to lists of numbers, instead of strings.
numbers = [convert_string_to_int(row) for row in numbers]
N = len(numbers)

# Modify each row by calculating the best possible sum with the row below.
for k in reversed(range(1, N)):
    current_row = numbers[k - 1]
    row_below = numbers[k]
    size = len(row_below)
    for i in range(0, size - 1):
        sum_1 = current_row[i] + row_below[i]
        sum_2 = current_row[i] + row_below[i + 1]
        current_row[i] = max(sum_1, sum_2)
    del numbers[k]

# At this point the list of lists numbers has only one row, and this row has
# only one entry, which is the answer we seek.
print(numbers[0][0])
end = time.time()
print(f"Program runtime: {end - start} seconds")
