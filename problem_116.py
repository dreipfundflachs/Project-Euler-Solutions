###############################
#  PROJECT EULER - PROBLEM 116  #
###############################

import time

start = time.time()
N = 50
# ways[n] will count the number of configurations of a row of length n. We
# begin by initializing every entry to 1 to account for the case where every
# square is grey.
red_ways, green_ways, blue_ways = [1] * (N + 1), [1] * (N + 1), [1] * (N + 1)

# The idea is to proceed by induction. Supposing we have already computed
# ways[n - 1], ways[n] will be 1 (all squares are red) plus
# ways[n - 1] (initial square grey, fill the remaining n - 1 squares) plus
# the sum, for each size between 3 and (n - 1), of the configurations
# which begin with a red block of this size (in addition to a subsequent grey
# square, as required). The remaining (n - size - 1) squares can be filled in
# ways[n - size - 1] ways.
for n in range(2, N + 1):
    red_ways[n] = red_ways[n - 1]   # Initial square is grey
    red_ways[n] += red_ways[n - 2]  # Start with a red block of length 2

for n in range(3, N + 1):
    green_ways[n] = green_ways[n - 1]   # Initial square is grey
    green_ways[n] += green_ways[n - 3]  # Start with a green block of length 3

for n in range(4, N + 1):
    blue_ways[n] = blue_ways[n - 1]   # Initial square is grey
    blue_ways[n] += blue_ways[n - 4]  # Start with a blue block of length 4

print(red_ways[N] + green_ways[N] + blue_ways[N] - 3)

end = time.time()
print(f"Program runtime: {end - start} seconds")
