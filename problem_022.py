# PROJECT EULER PROBLEM 022
import time


def name_score(name, score_of_each_letter):
    """ Calculates the score of a name. """
    score = 0
    for char in name:
        score += score_of_each_letter[char]
    return score


start = time.time()

letter_values = {}
initial = ord('A')
diff = ord('Z')
for k in range(initial, diff + 1):
    score = k - initial + 1
    letter_values[chr(k)] = score

with open('p022_names.txt') as file_object:
    content = (file_object.read()).strip()
    names = content.split('","')

new_names = [name.replace('"', '') for name in names]
names = new_names

names.sort()
n = len(names)
print(n)
total = 0
print(name_score(names[937], letter_values) * (938))

for k in range(0, n):
    current = name_score(names[k], letter_values)
    total += (k + 1) * current

print(total)
end = time.time()
print(f"Program runtime is: {end - start} seconds")
