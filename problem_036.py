# PROJECT EULER - PROBLEM 036
import time
from project_euler import dec_to_bin, palindromic


start = time.time()

s = 0
for n in range(1, 10**6):
    dec_str = str(n)
    binary = dec_to_bin(n)
    bin_str = str(binary)
    if palindromic(dec_str):
        if palindromic(bin_str):
            s += n
print(s)

end = time.time()
print(f"Program runtime: {end - start} seconds")
