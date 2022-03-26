# PROJECT EULER PROBLEM 062
import time

start = time.time()

dict_of_cube_digits = {}
N = 10**4
for n in range(N):
    cube = n**3
    s = str(cube)
    # For each cube in the range, create a dictionary to store its digits. The
    # value at the key 'k' (for k between 0 and 9) is the number of times that
    # k occurs in the cube.
    cube_digits = {}
    for k in range(10):
        cube_digits[k] = s.count(str(k))
    # Store this dictionary as the value associated with the cube in
    # dict_of_cube_digits.
    dict_of_cube_digits[cube] = cube_digits
    # Test whether cube_digits has already occurred 5 times. If so, we can stop
    # searching.
    if (list(dict_of_cube_digits.values())).count(cube_digits) == 5:
        # To obtain the smallest cube whose digits are a permutation of those
        # stored in cube_digits, we need to search through dict_of_cube_digits
        # for all occurrences of cube_digits.
        special_cubes = [c for c in range(N)\
                if dict_of_cube_digits.get(c**3) == cube_digits]
        # Print all numbers the, digits of whose cubes form a permutation of
        # cube_digits, and then print the minimum among those cubes.
        print(special_cubes, min(special_cubes)**3)
        break

end = time.time()
print(f"Program runtime is: {end - start} seconds")
