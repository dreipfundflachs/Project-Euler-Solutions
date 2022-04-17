#################################
#  PROJECT EULER - PROBLEM 022  #
#################################
import time


def get_name_score(name: str, score_of_letter: dict[str, int]) -> int:
    """ Calculates the score of a name. """
    name_score = 0
    for letter in name:
        name_score += score_of_letter[letter]
    return name_score


start = time.time()

# Construct a dictionary to hold the score of each individual letter.
letter_values = {}
initial = ord('A')
diff = ord('Z')
for k in range(initial, diff + 1):
    score = k - initial + 1
    letter_values[chr(k)] = score

# Extract the names from the given file.
with open('p022_names.txt') as file_object:
    content = (file_object.read()).strip()
    names = content.split('","')

# Clean and sort the names.
names = [name.replace('"', '') for name in names]
names.sort()


# Compute the total score.
N = len(names)

total_score = 0
for k in range(0, N):
    name_score = get_name_score(names[k], letter_values)
    total_score += (k + 1) * name_score

print(total_score)

end = time.time()
print(f"Program runtime: {end - start} seconds")
