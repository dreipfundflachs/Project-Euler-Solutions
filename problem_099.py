# PROJECT EULER PROBLEM 099
import time
from math import log10


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
m = 1
ml = 1

# Determine m and ml, then print ml.
for (l, a, b) in triples:
    if b*log10(a) > m:
        m = b*log10(a)
        ml = l
print(ml)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
