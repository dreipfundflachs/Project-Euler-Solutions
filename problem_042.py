#################################
#  PROJECT EULER - PROBLEM 042  #
#################################
import time
import csv


def name_score(name: str) -> int:
    """ Calculates the 'score' of a name written in capital letters. """
    letter_values = {}
    initial = ord('A')
    final = ord('Z')

    for k in range(initial, final + 1):
        letter_value = k - initial + 1
        letter_values[chr(k)] = letter_value

    name_score = 0
    for char in name:
        name_score += letter_values[char]

    return name_score


def generate_triangulars(n: int) -> list[int]:
    """ Generates a list containing all triangular numbers up to the n-th such
    number (notice that this triangular number will be n * (n + 1) // 2). """
    triangulars = []
    for k in range(1, n):
        triangular = k * (k + 1) // 2
        triangulars.append(triangular)

    return triangulars


start = time.time()

N = 10**3
TRIANGULARS = generate_triangulars(N)

# Extract the names from the file.
filename = 'p042_words.txt'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        names = row

# Count the number of triangle words.
number_of_triangle_words = 0
for name in names:
    if name_score(name) in TRIANGULARS:
        number_of_triangle_words += 1

print(number_of_triangle_words)

end = time.time()
print(f"Program runtime: {end - start} seconds")
