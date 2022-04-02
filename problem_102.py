# PROJECT EULER - PROBLEM 102
import time

start = time.time()
# Extract the coordinates of the vertices of each triangle ABC.
with open('p102_triangles.txt', 'r') as file_object:
    triangles = []
    for line in file_object:
        coordinates = [int(k) for k in line.split(',')]
        A = (coordinates[0], coordinates[1])
        B = (coordinates[2], coordinates[3])
        C = (coordinates[4], coordinates[5])
        triangle = [A, B, C]
        triangles.append(triangle)

# Initialize the total number of triangles which contain the origin.
total = 0
for triangle in triangles:
    # For each triangle, store the three vertices in a list.
    P = [triangle[0], triangle[1], triangle[2]]
    contains_origin = True
    for k in range(3):
        # For each pair of vertices, compute the difference v between them,
        # take the product with i to obtain a vector iv orthogonal to v, and
        # consider the differences from the origin and from the remaining
        # vertex to the first vertex in the pair.
        v = (P[(k - 1) % 3][0] - P[k][0], P[(k - 1) % 3][1] - P[k][1])
        iv = (-v[1], v[0])
        diff = (P[(k + 1) % 3][0] - P[k][0], P[(k + 1) % 3][1] - P[k][1])
        diff_origin = (0 - P[k][0], 0 - P[k][1])
        # Take the inner product of each difference with iv.
        inner_product_diff = diff[0] * iv[0] + diff[1] * iv[1]
        inner_product_origin = diff_origin[0] * iv[0] + diff_origin[1] * iv[1]
        # If the inner products do not have the same sign, then the origin and
        # the remaining vertex cannot lie on the same half-plane determined by
        # the chosen side.
        if inner_product_diff * inner_product_origin <= 0:
            contains_origin = False
            break
    if contains_origin == True:
        total += 1
# Print the answer.
print(total)

end = time.time()
print(f"Program runtime: {end - start} seconds")
