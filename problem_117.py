###############################
#  PROJECT EULER PROBLEM 116  #
###############################

import time

start = time.time()
N = 50
# ways[n] will count the number of configurations of a row of length n. We
# begin by initializing every entry to 1 to account for the case where every
# square is grey.
ways = [1] * (N + 1)
ways[2] = 2
ways[3] = 1 + 2 + 1

# The idea is to proceed by induction. Supposing we have already computed
# ways[n - 1], ways[n] will be 1 (all squares are red) plus
# ways[n - 1] (initial square grey, fill the remaining n - 1 squares) plus
# the sum, for each size between 3 and (n - 1), of the configurations
# which begin with a red block of this size (in addition to a subsequent grey
# square, as required). The remaining (n - size - 1) squares can be filled in
# ways[n - size - 1] ways.

for n in range(4, N + 1):
    ways[n] = ways[n - 1]   # Initial square is grey
    for initial_block_size in range(2, 5):
        ways[n] += ways[n - initial_block_size]

print(ways[N])
end = time.time()
print(f"Program runtime: {end - start} seconds")
