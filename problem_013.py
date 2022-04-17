#################################
#  PROJECT EULER - PROBLEM 013  #
#################################
import time


start = time.time()

# The numbers were pasted from the problem statement into the file below.
with open('p013_numbers.txt') as file_object:
    numbers = []
    for line in file_object:
        numbers.append(int(line.strip()))

first_ten_digits = str(sum(numbers))[:10]
print(first_ten_digits)

end = time.time()
print(f"Program runtime: {end - start} seconds")
