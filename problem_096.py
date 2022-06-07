#################################
#  PROJECT EULER - PROBLEM 096  #
#################################
import time
from copy import deepcopy


def get_available(grid: list[list[int]], cell: tuple[int]) -> set[int]:
    """ Given a grid and a cell in it, encoded as a pair of integers, returns a
    set comprising all available numbers to be placed at that position. """
    (i, j) = cell
    if grid[i][j] != 0:
        # Cell is already occupied.
        return set()
    else:
        columns = transpose(grid)
        # Extract all values inside the cells in the same box.
        box_entries = {grid[m][n] for m in box(i) for n in box(j)}
        # Get all available numbers in the same row, column and box.
        available_row = {d for d in NUMBERS if d not in grid[i]}
        available_column = {d for d in NUMBERS if d not in columns[j]}
        available_box = {d for d in NUMBERS if d not in box_entries}
        # Take the intersection of the three preceding sets to find the answer.
        available = ((available_row
                     .intersection(available_column))
                     .intersection(available_box))
    return available


def find_minimizing(grid: list[list[int]]) -> tuple[int]:
    """ Given a grid:
        * If it is not completely filled (solved), find a cell at which the
        number of available entries is as small as possible.
        * If the grid is already filled, return (10, 10).
        * If it cannot be solved, return None. """
    minimizing_cell = (10, 10)
    minimum = 10
    for i in INDICES:
        for j in INDICES:
            if grid[i][j] != 0:
                # If a cell is not blank, no need to consider it.
                continue
            else:
                available = get_available(grid, (i, j))
                number_of_available = len(available)
                if number_of_available == 0:
                    # Failure! Not possible to fill grid.
                    return None
                elif number_of_available < minimum:
                    # Found a new minimum:
                    minimizing_cell = (i, j)
                    minimum = number_of_available
    return minimizing_cell


def solve(grid: list[list[int]]) -> list[list[int]]:
    """ Given a Su Doku grid, returns the solution (as another grid). """
    cell = find_minimizing(grid)
    if cell == (10, 10):
        # Grid is already solved.
        return grid
    elif cell is None:
        # Grid cannot be solved.
        return None
    else:
        (i, j) = cell
        possibilities = get_available(grid, (i, j))
        for k in possibilities:
            new_grid = deepcopy(grid)
            new_grid[i][j] = k
            new_grid = solve(new_grid)
            if new_grid is None:
                # Impossible to solve the new grid.
                continue
            elif new_grid != grid:
                # Solved!
                return new_grid
        # If this point has been reached, all attempted substitutions for the
        # given cell failed: It is impossible to solve original grid!
        return None


def box(i: int) -> set[int]:
    """ Given an index i between 0 and 8, returns the set of all three indices
     which belong to the same box as i in a Su Doku grid (including i)."""
    if i in INDICES_1:
        return INDICES_1
    elif i in INDICES_2:
        return INDICES_2
    else:
        return INDICES_3


def transpose(A: list[list[int]]) -> list[list[int]]:
    """ Transposes a (not necessarily square nor numeric) matrix (list of
    lists, each of the same size) """
    m = len(A)
    n = len(A[0])
    B = []
    for j in range(0, n):
        column = []
        for i in range(0, m):
            column.append(A[i][j])
        B.append(column)
    return B


def solve_several(grids: list[list[list[int]]]) -> list[list[list[int]]]:
    """ Given a list of Su Doku grids in the format of the linked file,
    returns a list comprising their solutions (in the same order). """
    return [solve(grid) for grid in grids]


def get_sum(grids: list[list[list[int]]]) -> int:
    """ Returns the sum of the upper-left three-digit numbers in all of the
    solved grids. """
    solved_grids = solve_several(grids)
    total = 0
    for grid in solved_grids:
        current = ''
        for j in range(3):
            current += str(grid[0][j])
        total += int(current)
    return total


def display_grid(grid: list[list[int]]) -> None:
    """ Displays a Su Doku grid, returns None. This function is not required
    for the solution of the problem. """
    for i in INDICES:
        print('\n', end='')
        if i % 3 == 0 and i != 0:
            print('------+-------+------\n', end='')
        for j in INDICES:
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            print(grid[i][j], end=' ')
    print('\n')
    return None


start = time.time()

INDICES = set(range(0, 9))
INDICES_1 = {0, 1, 2}
INDICES_2 = {3, 4, 5}
INDICES_3 = {6, 7, 8}
NUMBERS = set(range(1, 10))

# Extract the grids in the linked file:
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

# grid = grids[7]
# display_grid(solve(grid))
print(get_sum(grids))

end = time.time()
print(f"Program runtime: {end - start} seconds")
