#################################
#  PROJECT EULER - PROBLEM 081  #
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
with open('p081_matrix.txt') as file_object:
    for line in file_object:
        A.append(extract(line))

N = len(A)  # dimension of the matrix A

# We will use dynamic programming to compute the minimal path. Begin by
# initializing the bottom row (i = N - 1) and right column (j = N - 1),
# which are exceptional because they are at the boundary.
for j in reversed(range(N - 1)):
    A[N - 1][j] += A[N - 1][j + 1]
    A[j][N - 1] += A[j + 1][N - 1]

# Now for each j between 0 and N - 2, update the cost of reaching the target
# from A[j][j] by adding to it the minimum of the costs of reaching the target
# from A[j + 1][j]  and A[j][j + 1] (the entries below and to the right of
# A[j][j], respectively). Then in reverse order we do the same for the
# remaining entries in row j and in column j.
for j in reversed(range(N - 1)):
    A[j][j] += min(A[j + 1][j], A[j][j + 1])
    for i in reversed(range(j)):
        A[i][j] += min(A[i + 1][j], A[i][j + 1])
        A[j][i] += min(A[j + 1][i], A[j][i + 1])

# At the end, A[0][0] stores the cost of reaching the entry at (N - 1, N - 1)
# from that at (0, 0), which is what we are looking for.
print(A[0][0])

end = time.time()
print(f"Program runtime: {end - start} seconds")
