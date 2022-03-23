fibonacci = [1, 2]
for n in range(2, 10**4, 1):
    current = fibonacci[n - 1]
    previous = fibonacci[n - 2]
    next_element = previous + current
    if next_element < 4*10**6:
        fibonacci.append(next_element)
    else:
        break

size = len(fibonacci)
s = 0
for i in range(1, size + 1, 3):
    s += fibonacci[i]
print(s)
