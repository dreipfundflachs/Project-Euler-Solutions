#################################
#  PROJECT EULER - PROBLEM 028  #
#################################
import time


start = time.time()

N = 500

sum_of_numbers = 1
current_number = 1

for k in range(1, N + 1):
    for i in range(0, 4):
        current_number += 2 * k
        sum_of_numbers += current_number

print(sum_of_numbers)

end = time.time()
print(f"Program runtime: {end - start} seconds")
