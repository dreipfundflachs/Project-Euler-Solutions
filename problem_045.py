# PROJECT EULER PROBLEM 045
import time


start = time.time()

triangular = [1, 3]
pentagonal = [1, 5]
hexagonal = [1, 6]

for n in range(3, 10**5):
    t = n*(n+1)//2
    triangular.append(t)
    p = pentagonal[-1]
    h = hexagonal[-1]
    while t > p:
        m = len(pentagonal) + 1
        p = m*(3*m-1)//2
        pentagonal.append(p)
    while t > h:
        k = len(hexagonal) + 1
        h = k*(2*k-1)
        hexagonal.append(h)
    if t == p and t == h and t != 40755:
        print(t)
        break
print(triangular)
print(pentagonal)
print(hexagonal)

end = time.time()
print(f"Program runtime is: {end - start} seconds")
