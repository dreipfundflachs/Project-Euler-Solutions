# PROJECT EULER - PROBLEM 061
import time

start = time.time()
m = 10_000
figurates = []
for k in range(0, 9):
    figurates.append([])

for n in range(1, m):
    triangle = n * (n + 1) // 2
    figurates[3].append(triangle)
for n in range(1, m):
    square = n ** 2
    figurates[4].append(square)
for n in range(1, m):
    pent = n * (3*n - 1) // 2
    figurates[5].append(pent)
for n in range(1, m):
    hexagonal = n * (2*n - 1)
    figurates[6].append(hexagonal)
for n in range(1, m):
    hept = n * (5*n - 3) // 2
    figurates[7].append(hept)
for n in range(1, m):
    octogonal = n * (3*n - 2)
    figurates[8].append(octogonal)

for k in range(3, 9):
    figurates[k] = [n for n in (figurates[k]) if (1000 <= n < 10_000)]
for k in range(3, 9):
    print(figurates[k][0:10])

numbers = list(range(10, 100))
polygons = [8]
ran = range(3, 8)
for n1 in figurates[8]:
    s1 = str(n1)
    p1 = int(str(n1)[:2])
    p2 = int(str(n1)[-2:])
    for p3 in numbers:
        n2 = int(str(p2) + str(p3))
        for i1 in ran:
            if n2 != n1 and n2 in figurates[i1]:
                gen = [k for k in ran if k != i1]
                for p4 in numbers:
                    n3 = int(str(p3) + str(p4))
                    for i2 in gen:
                        if n3 in figurates[i2]:
                            gen = [k for k in ran if k != i1 and k != i2]
                            for p5 in numbers:
                                n4 = int(str(p4) + str(p5))
                                for i3 in gen:
                                    if n4 in figurates[i3]:
                                        gen = [k for k in ran if k != i1 and k
                                               != i2 and k != i3]
                                        for p6 in numbers:
                                            n5 = int(str(p5) + str(p6))
                                            n6 = int(str(p6) + str(p1))
                                            for i4 in gen:
                                                if n5 in figurates[i4]:
                                                    gen = [k for k in ran if
                                                           k != i1 and
                                                           k != i2 and
                                                           k != i3 and
                                                           k != i4]
                                                    for i5 in gen:
                                                        if n6 in figurates[i5]:
                                                            answer =\
                                                                sum([n1, n2,
                                                                    n3, n4, n5,
                                                                    n6])

                                                            print((n1, 8),
                                                                  (n2, i1),
                                                                  (n3, i2),
                                                                  (n4, i3),
                                                                  (n5, i4),
                                                                  (n6, i5))
                                                            print(answer)


end = time.time()
print(f"Program runtime: {end - start} seconds")
