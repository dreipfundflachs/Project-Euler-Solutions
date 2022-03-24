# PROJECT EULER PROBLEM 091
import time

start = time.time()

N = 50
total = 0
# Iterate over each possible pair of points (x_1, y_1) and (x_2, y_2). 
for x_1 in range(N + 1):
    for y_1 in range(N + 1):
        for x_2 in range(N + 1):
            for y_2 in range(N + 1):
                # Test if the points are collinear.
                non_collinear = (x_1 * y_2 - x_2 * y_1 != 0)
                # Test if the angle at the origin is right.
                right_O = (x_1 * x_2 + y_1 * y_2 == 0)
                # Test if the angle at P = (x_1, y_1) is right.
                right_P = (x_1 * (x_1 - x_2) + y_1 * (y_1 - y_2) == 0)
                # Test if the angle at Q = (x_2, y_2) is right.
                right_Q = (x_2 * (x_1 - x_2) + y_2 * (y_1 - y_2) == 0)
                if  non_collinear and (right_O or right_P or right_Q):
                    total += 1

# Divide the number of triangles by 2 to get the answer, since triangle OPQ is
# always counted twice: as OPQ and as OQP.
print(total // 2)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
