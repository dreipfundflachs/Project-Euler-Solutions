#################################
#  PROJECT EULER - PROBLEM 014  #
#################################

import time

start = time.time()

collatz = {1: 1, 2: 2}
max_count = 1
max_number = 1
for n in range(1, 10**6):
    if n in collatz:
        continue
    else:
        if n % 2 == 0:
            m = n//2
            count = collatz[m] + 1
            collatz[n] = count
        else:
            p = (3*n + 1) // 2
            if p % 2 == 0:
                q = p // 2
                count = collatz[q] + 3
                collatz[n] = count
                collatz[3*n+1] = count - 1
                collatz[p] = count - 2
            else:
                numbers = [n]
                k = n
                count = 0
                while k not in collatz:
                    if k % 2 == 0:
                        k = k // 2
                    else:
                        k = 3*k + 1
                    count += 1
                    numbers.append(k)
                count += collatz[k]
                temp_count = count
                for number in numbers:
                    collatz[number] = temp_count
                    temp_count -= 1
    if count > max_count:
        max_count = count
        max_number = n

print(max_number, max_count)

end = time.time()
print(f"Program runtime: {end - start} seconds")
