# PROJECT EULER PROBLEM 13
import time

start = time.time()
with open('p013_numbers.txt') as file_object:
    numbers = []
    for line in file_object:
        numbers.append(int(line.strip()))
    print(sum(numbers))

end = time.time()
print(f"Program runtime: {end - start} seconds")
