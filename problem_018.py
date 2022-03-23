# PROJECT EULER PROBLEM 18
import time


def convert_string_to_int(a):
    """
    Takes a list of integers formatted as strings and
    converts it to a list of integers
    """
    b = [int(number_string) for number_string in a]
    return b


start = time.time()

# Create a list, each element of which represents a row
numbers = []
with open('p018_numbers.txt') as file_object:
    for line in file_object:
        numbers.append(
            line.split()
        )

# Convert the rows to lists of numbers, instead of strings
numbers = [convert_string_to_int(nums) for nums in numbers]
print(numbers)
n = len(numbers)

# Modify each row by calculating the best possible sum with row below
for k in range(n - 1, 0, -1):
    current_row = numbers[k - 1]
    row_below = numbers[k]
    size = len(row_below)
    for i in range(0, size - 1):
        s_1 = current_row[i] + row_below[i]
        s_2 = current_row[i] + row_below[i + 1]
        current_row[i] = max(s_1, s_2)
    del numbers[k]

print(numbers)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
