#################################
#  PROJECT EULER - PROBLEM 011  #
#################################
import time


def convert_strings_to_int(strings: [str]) -> int:
    """ Takes a list of integers formatted as strings and converts it to a
    list of integers.  """
    integers = [int(number_string) for number_string in strings]
    return integers


def get_max_product_along_rows(A: list[list[int]]) -> int:
    """ Calculates the maximum product of four entries
    along the rows of matrix A (whose entries are integers).  """
    m = len(A)
    n = len(A[0])
    max_product = 1
    for i in range(0, m):
        row = A[i]
        for j in range(3, n):
            product = row[j - 3] * row[j - 2] * row[j - 1] * row[j]
            max_product = max(product, max_product)
    return max_product


def transpose(A: list[list]) -> list[list]:
    """ Transposes a (not necessarily square nor numeric) matrix (list of
    lists, each of the same size)."""
    m = len(A)
    n = len(A[0])
#   A = [[A[i][j] for j in range(n)] for i in range(m)], so its transpose is:
    B = [[A[i][j] for i in range(m)] for j in range(n)]
    return B


start = time.time()
# Import grid from file and store it as a matrix.
A = []
with open('p011_numbers.txt') as file_object:
    for line in file_object:
        A.append(line.split())
A = [convert_strings_to_int(nums) for nums in A]
B = transpose(A)
N = len(A)

# Calculate the maximum product along rows and columns.
max_row_product = get_max_product_along_rows(A)
max_column_product = get_max_product_along_rows(B)

# Calculate the maximum product along the diagonal.
max_diagonal_product = 1
for i in range(0, N - 4):
    for j in range(0, N - 4):
        prod = A[i][j] * A[i + 1][j + 1]
        prod *= A[i + 2][j + 2] * A[i + 3][j + 3]
        max_diagonal_product = max(prod, max_diagonal_product)

# Calculate the maximum product along the anti-diagonal.
max_anti_diagonal_product = 1
for i in range(0, N - 4):
    for j in range(4, N):
        prod = A[i][j] * A[i + 1][j - 1]
        prod *= A[i + 2][j - 2] * A[i + 3][j - 3]
        max_anti_diagonal_product = max(prod, max_anti_diagonal_product)

# Print the answer.
print(max(max_row_product, max_column_product,
          max_diagonal_product, max_anti_diagonal_product))

end = time.time()
print(f"Program runtime: {end - start} seconds")
