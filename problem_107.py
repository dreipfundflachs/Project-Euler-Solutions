# PROJECT EULER PROBLEM 107
# The problem is easily solved by Kruskal's algorithm.
import time

start = time.time()

MATRIX = []
with open('p107_network.txt') as file_object:
    for line in file_object:
        line = (line.strip()).split(',')
        line = [n if n == '-' else int(n) for n in line]
        MATRIX.append(line)

N = len(MATRIX)
forest = {}     # Will hold the forest of trees at each step.
# Initially it consists of one tree for each vertex. 
for i in range(N):
    forest[i] = {i}
# Extract the edges from the matrix. Since the matrix is symmetric, we only
# need to consider the entries below the main diagonal.
edges = [(i, j, MATRIX[i][j]) for i in range(N) for j in range(N)
         if (MATRIX[i][j] != '-' and i < j)]
# Sort the edges by their cost (weight).
edges.sort(key=lambda tup: tup[2])

tree_weight = 0
network_weight = sum([cost for (i, j, cost) in edges])

for (i, j, cost) in edges:
    # For each edge, check whether it joins two vertices which are already
    # connected. If not, this edge will be incorporated into the tree.
    f_i = forest[i].copy()
    f_j = forest[j].copy()
    if f_i != f_j:
        tree_weight += cost
        union_ij = forest[i].union(forest[j])
        # If the tree already contains every vertex, break.
        if len(union_ij) == N:
            break
        # Take the union of forest[i] and forest[j] and assign it to
        # forest[k] for each vertex k in either forest[i] or forest[j].
        for k in f_i:
            forest[k] = forest[k].union(union_ij)
        for k in f_j:
            forest[k] = forest[k].union(union_ij)

answer = network_weight - tree_weight
print(answer)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
