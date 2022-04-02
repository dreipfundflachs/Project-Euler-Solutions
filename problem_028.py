# PROJECT EULER - PROBLEM 028
import time

start = time.time()
s = 1
c = 1
for k in range(1, 501):
    for i in range(0, 4):
        c += 2*k
        s += c

print(s)
end = time.time()
print(f"Program runtime: {end - start} seconds")
