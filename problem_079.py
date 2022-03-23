# PROJECT EULER PROBLEM 079
import time


start = time.time()

# Get the numbers from the file.
numbers = []
filename = 'p079_keylog.txt'
with open(filename) as f:
    for line in f:
        numbers.append(line.strip())
print(numbers)

# Obtain the set of all digits involved and create a set of pairs (m, n) where
# m is to the left of n.
digits = set()
pairs = set()

for number in numbers:
    first = int(number[0])
    second = int(number[1])
    third = int(number[2])
    pairs.add((first, second))
    pairs.add((second, third))
    pairs.add((first, third))
    digits.add(first)
    digits.add(second)
    digits.add(third)

# Count the number of ocurrences of each digit a smaller of the two numbers in
# a given pair.

count = {}
for d in digits:
    count[d] = 0

for d in digits:
    for pair in pairs:
        if pair[0] == d:
            count[d] += 1

# Sort the digits by their counts, in decreasing order.
for d in sorted(count, key=count.get, reverse=True):
    print(d, count[d])

end = time.time()
print(f"Program runtime is: {end - start} seconds")
