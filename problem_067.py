# PROJECT EULER - PROBLEM 067
import time

start = time.time()

rows = []
# Open the file and create a list of rows, each row consisting of integers
with open('p067_triangle.txt', encoding='utf-8') as file_object:
    for row in file_object:
        new_row = [int(n) for n in row.split()]
        rows.append(new_row)

# Use dynamic programming. From bottom to top, for each number in a given row,
# update the number to be the sum of itself with the maximum of the two
# neighboring elements below it.
m = len(rows)
for k in reversed(range(0, m - 1)):
    r = len(rows[k])
    for i in range(0, r):
        rows[k][i] += max(rows[k + 1][i], rows[k + 1][i + 1])

# Print the answer.
print(rows[0])
end = time.time()
print(f"Program runtime: {end - start} seconds")
