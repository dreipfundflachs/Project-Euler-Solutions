# PROJECT EULER - PROBLEM 032
import time

start = time.time()
pandigital = []
for m in range(1, 1001):
    for n in range(m, 10001):
        p = m * n
        s = str(m) + str(n) + str(p)
        if len(set(s)) == 9 and len(s) == 9 and '0' not in s:
            pandigital.append(p)
            print(f"{m} x {n} = {p}")

print(pandigital)
panset = set(pandigital)
print(sum(panset))
end = time.time()
print(f"Program runtime: {end - start} seconds")
