#################################
#  PROJECT EULER - PROBLEM 062  #
#################################
import time


# The main idea of this solution is that two numbers m and n are a permutation
# of one another if and only if for each digit d = 0, ..., 9, the number of
# occurrences of d in m and in n coincide.
start = time.time()

list_of_cube_digits: list[list[int]] = []
n = 0
found_solution = False

while not found_solution:
    cube_string = str(n**3)
    cube_digits = []  # cube_digits[d] = number of occurrences of d in n**3.
    for k in range(10):
        cube_digits.append(cube_string.count(str(k)))
    # Store this list as the value associated with n (not n**3) in
    # list_of_cube_digits.
    list_of_cube_digits.append(cube_digits)
    # Test whether cube_digits has already occurred 5x. If so, stop searching.
    if list_of_cube_digits.count(cube_digits) == 5:
        # To obtain the cubes whose digits are a permutation of those of n**3,
        # search list_of_cube_digits for all occurrences of cube_digits.
        special_cubes = [c**3 for c in range(n + 1)
                         if list_of_cube_digits[c] == cube_digits]
        print(min(special_cubes))
        found_solution = True
    n += 1

end = time.time()
print(f"Program runtime: {end - start} seconds")
