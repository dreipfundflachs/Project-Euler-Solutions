# PROJECT EULER - PROBLEM 042
import time
import csv
from project_euler import name_score

start = time.time()

triangular = [1, 3]

for n in range(3, 10**3):
    t = n*(n+1)//2
    triangular.append(t)
triangular_set = set(triangular)

filename = 'p042_words.txt'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        names = row
print(names)

count = 0
for name in names:
    if name_score(name) in triangular_set:
        count += 1

print(count)
end = time.time()
print(f"Program runtime: {end - start} seconds")
