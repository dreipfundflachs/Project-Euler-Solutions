###############################
#  PROJECT EULER PROBLEM 114  #
###############################

import time

start = time.time()
N = 50
# ways[n] will count the number of configurations of a row of length n. We
# begin by initializing every entry to 1 to account for the case where every
# square is grey.
ways = [1] * (N + 1)

# The idea is to proceed by induction. Supposing we have already computed
# ways[n - 1], ways[n] will be 1 (all squares are red) plus
# ways[n - 1] (initial square grey, fill the remaining n - 1 squares) plus
# the sum, for each size between 3 and (n - 1), of the configurations
# which begin with a red block of this size (in addition to a subsequent grey
# square, as required). The remaining (n - size - 1) squares can then be filled
# in ways[n - size - 1] ways.
for n in range(3, N + 1):
    ways[n] = ways[n - 1]   # Initial square is grey
    ways[n] += 1    # All n squares are red
    # Start with a block of size initial_block_size, then fill the rest.
    for initial_block_size in range(3, n):
        ways[n] += ways[n - initial_block_size - 1]

print(ways[N])

end = time.time()
print(f"Program runtime: {end - start} seconds")

# Below is a previous attempt using dynamic programming. The idea was to
# consider increasing maximum block sizes of variable initial position, and to
# fill what remains from the row to its left and right independently. It does
# not work because certain configurations involving two blocks of the same
# maximum size are counted more than once.

# for max_block_size in range(3, N + 1):
#     for n in range(max_block_size, N + 1):
#         for init_position in range(1, n - max_block_size + 2):
#             if (init_position - 2) < 0:
#                 left_ways = 1
#             else:
#                 left_ways = ways[init_position - 2]
#             if (n - init_position - max_block_size) < 0:
#                 right_ways = 1
#             else:
#                 right_ways = ways[n - init_position - max_block_size]
#             ways[n] += left_ways * right_ways
#
# print(ways[50])
