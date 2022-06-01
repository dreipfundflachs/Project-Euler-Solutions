#################################
#  PROJECT EULER - PROBLEM 082  #
#################################
import time


def extract(line: str) -> list[int]:
    """ Given a string ending in a newline character and containing various
    integers separated by commas, return a list of those integers.
    Ex.: extract("13,49,732,5\n") -> [13, 49, 732, 5] """
    new_line = (line.strip()).split(',')
    return [int(entry) for entry in new_line]


start = time.time()
# Initialize the matrix A by extracting each line in turn.
A = []
with open('p082_matrix.txt') as file_object:
    for line in file_object:
        A.append(extract(line))

N = len(A)  # dimension of the matrix A

# As in the preceding (simpler) problem, we use dynamic programming. The idea
# is to proceed from the last column to the first one as follows. We update
# each entry of a given column j so that it reflects the minimum cost to reach
# the last column using the permissible moves and starting from this entry.
# Imagine you are standing at an entry, say, (k, j), in the j-th column. Then
# you can pace up and down this column, but eventually you must move right,
# say, at the i-th line, to the entry (i, j + 1). The most efficient way to
# choose this move, and from there to the last column, is to minimize the sum
# of the costs from (k, j) to (i, j + 1) along the j-th column _plus_ the cost
# recorded at (i, j + 1), which contains the cost to reach the last column from
# the latter entry.

# For the last column (j = N - 1), we do not need to calculate anything.
for j in reversed(range(N - 1)):
    # Initialize a list to hold a copy of the current j-th column. This is
    # necessary because modifying the entries of the j-th column in place would
    # mess up the costs.
    B = [0 for i in range(N)]
    for k in range(N):
        # Compute the list of costs of moving from (k, j) to the last column,
        # as described above. For this we need to compare the cost of moving
        # right at the i-th line, for each i = 0,..., N - 1.
        costs = []
        for i in range(N):
            cost = A[k][j] + A[i][j + 1]
            if i < k:
                cost += sum([A[r][j] for r in range(i, k)])
            elif k < i:
                cost += sum([A[r][j] for r in range(k + 1, i + 1)])
            costs.append(cost)
        B[k] += min(costs)
    # Now copy B back to the j-th column of A.
    for i in range(N):
        A[i][j] = B[i]

print(min([A[i][0] for i in range(N)]))

end = time.time()
print(f"Program runtime: {end - start} seconds")
