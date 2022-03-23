# PROJECT EULER PROBLEM 11
import time


def convert_string_to_int(a):
    """
    Takes a list of integers formatted as strings and
    converts it to a list of integers
    """
    b = [int(number_string) for number_string in a]
    return b


def max_rows(A):
    """ Calculates the maximum product of four entries
    along the rows of matrix A (whose entries are integers)
    """
    m = len(A)
    n = len(A[0])
    prod = 1
    max_prod = 1
    for i in range(0, m):
        row = A[i]
        for j in range(3, n):
            prod = row[j-3]*row[j-2]*row[j-1]*row[j]
            if prod > max_prod:
                max_prod = prod
    return max_prod


def transpose(A):
    """
    Transposes a (not necessarily square nor numeric) matrix
    (list of lists, each of the same size)
    """
    m = len(A)
    n = len(A[0])
    # Initialize the transpose
    B = [[0 for i in range(m)] for j in range(n)]
    for j in range(0, n):
        column = []
        for i in range(0, m):
            column.append(A[i][j])
        B[j] = column
    return B


start = time.time()
# Import grid from file and store it as a matrix
A = []
with open('p011_numbers.txt') as file_object:
    for line in file_object:
        A.append(
            line.split()
        )
A = [convert_string_to_int(nums) for nums in A]
B = transpose(A)

# Calculate the maximum product along rows and columns (p_1 and p_2 resp.)
p_1 = max_rows(A)
p_2 = max_rows(B)
p_3 = 1
p_4 = 1

# Calculate the maximum product p_3 along diagonals
for i in range(0, 16):
    for j in range(0, 16):
        prod = A[i][j] * A[i + 1][j + 1]
        prod *= A[i + 2][j + 2] * A[i + 3][j + 3]
        if prod > p_3:
            p_3 = prod

# Calculate the maximum product p_4 along anti-diagonals
for i in range(0, 16):
    for j in range(4, 20):
        prod = A[i][j] * A[i + 1][j - 1]
        prod *= A[i + 2][j - 2] * A[i + 3][j - 3]
        if prod > p_3:
            p_4 = prod

print(p_1)
print(p_2)
print(p_3)
print(p_4)
print(max(p_1, p_2, p_3, p_4))


end = time.time()
print(f"Program runtime is: {end - start} seconds")
