#################################
#  PROJECT EULER - PROBLEM 011  #
#################################
import time


def convert_strings_to_int(strings: [str]) -> int:
    """ Takes a list of integers formatted as strings and converts it to a
    list of integers.  """
    integers = [int(number_string) for number_string in strings]
    return integers


def get_max_prod_rows(A: list[list[int]]) -> int:
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


def get_max_prod_diags(A: list[list[int]]) -> int:
    """ Calculates the maximum product of four entries along the diagonals of a
    _square_ matrix A (whose entries are integers). """
    m = len(A)
    max_diagonal_product = 1
    for i in range(0, m - 4):
        for j in range(0, m - 4):
            product = A[i][j] * A[i + 1][j + 1]\
                      * A[i + 2][j + 2] * A[i + 3][j + 3]
            max_diagonal_product = max(product, max_diagonal_product)
    return max_diagonal_product


def get_max_prod_skew_diags(A: list[list[int]]) -> int:
    """ Calculates the maximum product of four entries along the skew-diagonals
    of a _square_ matrix A (whose entries are integers). """
    m = len(A)
    max_skew_diag_product = 1
    for i in range(0, m - 4):
        for j in range(4, m):
            product = A[i][j] * A[i + 1][j - 1]\
                   * A[i + 2][j - 2] * A[i + 3][j - 3]
            max_skew_diag_product = max(product, max_skew_diag_product)
    return max_skew_diag_product


start = time.time()
# Import grid from file and store it as a matrix.
A = []
with open('p011_numbers.txt') as file_object:
    for line in file_object:
        A.append(line.split())
A = [convert_strings_to_int(nums) for nums in A]

max_product_rows = get_max_prod_rows(A)
max_product_columns = get_max_prod_rows(transpose(A))
max_product_diagonals = get_max_prod_diags(A)
max_product_skew_diagonals = get_max_prod_skew_diags(A)

print(max(max_product_rows, max_product_columns,
          max_product_diagonals, max_product_skew_diagonals))

end = time.time()
print(f"Program runtime: {end - start} seconds")
