###############################
#  PROJECT EULER - PROBLEM 115  #
###############################

import time

# The solution is essentially the same as that of problem 114.
start = time.time()
B = 50
M = 10**6
# ways[n] will count the number of configurations of a row of length n. We
# begin by initializing every entry to 1 to account for the case where every
# square is grey (black).
ways = [1] * (500 + 1)

# The idea is to proceed by induction. Supposing we have already computed
# ways[n - 1], ways[n] will be 1 (all squares are red) plus
# ways[n - 1] (initial square grey, fill the remaining n - 1 squares) plus
# the sum, for each size between 50 and (n - 1), of the configurations
# which begin with a red block of this size (in addition to a subsequent grey
# square, as required). The remaining (n - size - 1) squares can then be filled
# in ways[n - size - 1] ways.

n = B
while True:
    ways[n] = ways[n - 1]   # Initial square is grey
    ways[n] += 1    # All n squares are red
    # Start with a block of size initial_block_size, then fill the rest.
    for initial_block_size in range(B, n):
        ways[n] += ways[n - initial_block_size - 1]
    if ways[n] > M:
        print(n, ways[n])
        break
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
