#################################
#  PROJECT EULER - PROBLEM 096  #
#################################
import time
from copy import deepcopy


def solve_grids(grids: list[list[list[int]]]) -> list[list[list[int]]]:
    """ Given a list of grids of Su Doku, returns a list comprising their
    solutions (in the same order). """
    return [solve(grid) for grid in grids]


def get_sum(grids: list[list[list[int]]]) -> int:
    solved_grids = solve_grids(grids)
    total = 0
    for grid in solved_grids:
        for j in range(3):
            total += grid[0][j]
    return total


def solve(grid: list[list[int]]) -> list[list[int]]:
    for i in range(9):
        grid = fill_rows_or_cols(grid)
    return grid


def fill_rows_or_cols(grid: list[list[int]]) -> list[list[int]]:
    grid = fill_rows(grid)
    return fill_columns(grid)


def fill_rows(grid: list[list[int]]) -> list[list[int]]:
    """ Given a Su Doku grid, returns the solution (as another grid). """
    easiest_rows = find_minimizing_rows(grid)
    if easiest_rows != []:
        same_rows_as_before = False
    else:
        same_rows_as_before = True
    while not same_rows_as_before:
        # Perform one pass through all of the easiest the rows:
        same_rows_as_before = True
        for i in easiest_rows:
            new_grid = fill_row(grid, i)
            if new_grid and new_grid != grid:
                grid = new_grid
                same_rows_as_before = False
    return grid


def fill_columns(grid: list[list[int]]) -> list[list[int]]:
    columns = transpose(grid)
    return transpose(fill_rows(columns))


def count_blanks(line: list[int]) -> int:
    """ Count the number of blanks (or, in our case, '0's) in a given row or
    column of a grid. """
    return line.count(0)


def get_missing_numbers(line: list[int]) -> list[int]:
    """ Given a row or column of a grid, returns a new list comprising all
    numbers which do not appear in it. """
    return [d for d in range(1, 10) if d not in line]


def get_blanks(line: list[int]) -> list[int]:
    """ Given a row or column of a grid, returns a list of the indices of the
    entries equal to 0. """
    return [j for j in range(9) if line[j] == 0]


def transpose(A: list[list[int]]) -> list[list[int]]:
    """ Transposes a (not necessarily square nor numeric) matrix (list of
    lists, each of the same size) """
    m = len(A)
    n = len(A[0])
    # Initialize the transpose
    B = []
    for j in range(0, n):
        column = []
        for i in range(0, m):
            column.append(A[i][j])
        B.append(column)
    return B


def get_min_blanks(grid: list[list[int]]) -> int:
    """ Given a grid, returns the smallest number of blank entries among all
    rows and all columns of the grid. """
    minimum = 10
    columns = transpose(grid)
    for i in range(9):
        row = grid[i]
        column = columns[i]
        minimum = min(count_blanks(row), count_blanks(column), minimum)
    return minimum


def find_minimizing_rows(grid: list[list[int]]) -> list[int]:
    """ Given a grid, finds the indices of the rows which have the smallest
    number of blank entries (or, in our case, entries equal to '0'). """
    minimum = get_min_blanks(grid)
    if minimum == 0:
        return []
    else:
        minimizing_rows = []
        for i in range(9):
            if count_blanks(grid[i]) == minimum:
                minimizing_rows.append(i)
        return minimizing_rows


def find_minimizing_columns(grid: list[list[int]]) -> list[int]:
    """ Given a grid, finds the indices of the rows which have the smallest
    number of blank entries (or, in our case, entries equal to '0'). """
    columns = transpose(grid)
    return find_minimizing_rows(columns)


def fill_row(grid: list[list[int]], i: int) -> list[list[int]]:
    """ Fills the blanks of the i-th row of the grid with a given list of
    numbers. If this is impossible, then it returns the empty list []. """
    columns = transpose(grid)
    row = grid[i]
    missing_numbers = get_missing_numbers(row)
    if missing_numbers:
        j = get_blanks(row)[0]
        for k in missing_numbers:
            if k in columns[j]:
                continue
            else:
                new_grid = deepcopy(grid)
                new_grid[i][j] = k
                filled_new_grid = fill_row(new_grid, i)
                if filled_new_grid:
                    return filled_new_grid
                else:
                    continue
        return None
    else:
        if 0 not in grid[i]:
            return grid


def fill_column(grid: list[list[int]], j: int) -> list[list[int]]:
    """ Fills the blanks of the j-th column of the grid with a given list of
    numbers. If this is impossible, then it returns the empty list []. """
    columns = transpose(grid)
    return transpose(fill_row(columns, j))


start = time.time()

grids: list[list[list[int]]] = []

with open('p096_sudoku.txt') as file_object:
    for i, line in enumerate(file_object):
        if i % 10 == 0:
            current_grid = []
        else:
            current_row = [int(d) for d in line.strip()]
            current_grid.append(current_row)
            if i % 10 == 9:
                grids.append(current_grid)

N = len(grids)

gr = grids[0]
tr_gr = transpose(gr)
print(get_min_blanks(gr))
print(find_minimizing_rows(gr))
print(find_minimizing_columns(gr))
print(tr_gr)
print(get_blanks(tr_gr[2]))
row = gr[0]
print(row)
print(get_missing_numbers(row))
print(get_blanks(row))
print(fill_row(gr, 0))
print()
print(solve(gr))
print(find_minimizing_columns(gr))
# print((fill_column(tr_gr, 6))[6])

# for i in range(9):
#     new_grid = fill_row(grid, i)
#     if new_grid and new_grid != grid:
#         row = grid[i]
#         new_row = new_grid[i]
#         print(row)
#         print(new_row)

# for i in range(1, 2):
#     new_grid = fill_row(grid, i)
#     print(new_grid)
#     if new_grid:
#         print(grid[i])
#         print(new_grid[i])
#         print()
#         grid = new_grid

end = time.time()
print(f"Program runtime: {end - start} seconds")
