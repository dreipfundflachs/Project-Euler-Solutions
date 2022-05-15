#################################
#  PROJECT EULER - PROBLEM 099  #
#################################
import time
from math import log10


# The idea of the solution is to compare the _logarithms_ of the given numbers,
# instead of the numbers themselves.
start = time.time()

triples = []
count = 1
# Open the file and store line number, base, exponent
with open('p099_base_exp.txt') as f:
    for line in f:
        curr = line.strip().split(',')
        triple = (count, int(curr[0]), int(curr[1]))
        triples.append(triple)
        count += 1

# Initialize the maximum logarithm and the line number which realizes it.
max_logarithm = 1
max_line_number = 1

# Determine max_logarithm and max_line_number by direct comparison.
for (line_number, a, b) in triples:
    if b * log10(a) > max_logarithm:
        max_logarithm = b * log10(a)
        max_line_number = line_number

print(max_line_number)

end = time.time()
print(f"Program runtime: {end - start} seconds")
