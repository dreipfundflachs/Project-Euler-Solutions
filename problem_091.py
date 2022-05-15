#################################
#  PROJECT EULER - PROBLEM 091  #
#################################
import time

start = time.time()

N = 50
total = 0
# Let O = (0, 0), P = (x_1, y_1) and Q = (x_2, y_2). We consider the following
# cases separately:
#   (i) x_1 < x_2 and the triangle has a right angle at either P or Q;
#   (ii) x_1 == x_2 and the triangle has a right angle at either P or Q;
#   (iii) The triangle has a right angle at O.

# The number of solutions of type (i) is computed in the loop below.
for x_1 in range(N + 1):
    for y_1 in range(N + 1):
        # Note that x_2 > x_1 by hypothesis.
        for x_2 in range(x_1 + 1, N + 1):
            for y_2 in range(y_1 + 1):
                # We can consider only those values of y_2 <= y_1 because this
                # condition must hold if the triangle has a right angle at P or
                # Q; see the two equality tests below, observing that
                # x_2 - x_1 > 0 by hypothesis.
                if x_1 * y_2 != x_2 * y_1:
                    # Test if the angle at P = (x_1, y_1) is right.
                    if x_1 * (x_2 - x_1) == y_1 * (y_1 - y_2):
                        total += 1
                    # Test if the angle at Q = (x_2, y_2) is right.
                    elif x_2 * (x_2 - x_1) == y_2 * (y_1 - y_2):
                        total += 1

# Now add to this the number of solutions of type (ii). There are N choices for
# the common x-coordinate x_1 = x_2 (since it must be different from 0).
# Moreover, one of the vertices must have y-coordinate zero and for the
# y-coordinate of the other we have N choices (any y between 1 and N).
total += N**2

# Finally, in case (iii) one of the vertices lies along the positive x-axis and
# the other along the positive y-axis. There are again N**2 possible choices,
# since neither vertex can coincide with the origin.
total += N**2

print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
