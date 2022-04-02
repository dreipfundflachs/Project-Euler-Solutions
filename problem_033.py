# PROJECT EULER PROBLEM 033
import time
from fractions import Fraction

start = time.time()
s = []
for a in range(10, 100):
    s.append(str(a))

new_s = [a for a in s if '0' not in a]
s = new_s
special = []
for p in s:
    for q in s:
        pint = int(p)
        qint = int(q)
        if pint < qint:
            if p[0] == q[0] and int(p[1]) / int(q[1]) == pint / qint:
                special.append((pint, qint))
            if p[0] == q[1] and int(p[1]) / int(q[0]) == pint / qint:
                special.append((pint, qint))
            if p[1] == q[0] and int(p[0]) / int(q[1]) == pint / qint:
                special.append((pint, qint))
            if p[1] == q[1] and int(p[0]) / int(q[0]) == pint / qint:
                special.append((pint, qint))

print(special)
p = 1
q = 1
for (a, b) in special:
    p *= a
    q *= b
print(p)
print(q)
r = Fraction(p, q)
print(r)
end = time.time()
print(f"Program runtime: {end - start} seconds")
