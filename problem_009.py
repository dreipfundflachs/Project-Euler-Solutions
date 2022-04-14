#################################
#  PROJECT EULER - PROBLEM 009  #
#################################
import time


start = time.time()

found_triplet = False

for b in range(250, 1000):
    if found_triplet:
        break
    for a in range(1, b):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f"Triplet: a = {a},  b = {b},  c = {c}")
            print(f"Product: {a*b*c}")
            found_triplet = True
            break

end = time.time()
print(f"Program runtime: {end - start} seconds")
