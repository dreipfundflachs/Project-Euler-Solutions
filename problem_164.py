# PROJECT EULER PROBLEM 164
import time

start = time.time()
pairs = []
ending = {}
new_ending = {}

# Create the list of all possible pairs (i, j) with i + j < 10,
pairs = [(i, j) for i in range(0, 10) for j in range(0, 10) if i + j < 10]

# Initializing the dictionaries which will compute the number of r-digit
# numbers --- for variable r in range(1, 21) --- which end in (i,j).
# Watch out for the leading 0.
for (i, j) in pairs:
    if i > 0:
        ending[(i, j)] = 1
    else:
        ending[(i, j)] = 0

# Given (j,k) in 'pairs', r and 'ending', computes the number of r-digit
# numbers which end in (j,k): Take the number of (r-1)-digit numbers ending
# in (i,j), given by ending[(i,j)], and then sum over all i <= 10 - j - k
for r in range(3, 21):
    for (j, k) in pairs:
        new_ending[(j, k)] = 0
        for i in range(0, 10 - j - k):
            new_ending[(j, k)] += ending[(i, j)]

# Make (old) ending = new_ending and reset new_ending
    ending, new_ending = new_ending, {}


# Sum the results for the final pair (j, k) in a 20-digit number
count = 0
for (j, k) in pairs:
    count += ending[(j, k)]
print(count)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
