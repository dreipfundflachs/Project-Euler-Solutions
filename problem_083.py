# PROJECT EULER PROBLEM 083
import time


def extract(line):
    """ Given a string ending in a newline character and containing various
    integers separated by commas, return a list of those integers.
    Ex.: extract('13,49,732,5\n') -> [13, 49, 732, 5] """
    new_line = (line.strip()).split(',')
    return [int(entry) for entry in new_line]


start = time.time()
# Initialize the matrix A by extracting each line in turn.
A = []
with open('p083_matrix.txt') as file_object:
    for line in file_object:
        A.append(extract(line))

# N = dimension of the matrix
N = len(A)
C = 1_000_000

best = [([C] * N) for i in range(N)]
best[0][0] = A[0][0]

while True:
    previous_best = best[N - 1][N - 1]
    for i in range(N):
        for j in range(N):
            current_min = C
            if i > 0:
                current_min = min(current_min, best[i - 1][j])
            if i < 79:
                current_min = min(current_min, best[i + 1][j])
            if j > 0:
                current_min = min(current_min, best[i][j - 1])
            if j < 79:
                current_min = min(current_min, best[i][j + 1])

            best[i][j] = min(best[i][j], A[i][j] + current_min)

    if best[N - 1][N - 1] < C and best[N - 1][N - 1] == previous_best:
        break

print(best[N - 1][N - 1])
