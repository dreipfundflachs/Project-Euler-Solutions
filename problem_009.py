# PROJECT EULER PROBLEM 9

flag = False
for b in range(250, 1000, 1):
    if flag:
        break
    for a in range(1, b, 1):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f"a={a}\tb={b}\tc={c}")
            print(a**2 + b**2)
            print(c**2)
            print(a*b*c)
            flag = True
            break
