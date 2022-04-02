#################################
#  PROJECT EULER - PROBLEM 089  #
#################################
import time

start = time.time()

# Extract the numerals to a list, each entry being a string
numerals = []
with open('p089_roman.txt') as file_object:
    for line in file_object:
        numerals.append(line.strip())

# Here are the patterns which can be replaced by shorter ones (in each case,
# the substitution will have only two characters)
five_patterns = ['VIIII', 'LXXXX', 'DCCCC']
four_patterns = ['IIII', 'XXXX', 'CCCC']

# For each string in the list, moving from the beginning to the end of the
# string, consider each substring of five or four subsequent characters. If it
# matches one of the above, compute the number of characters that could be
# saved in this segment and move the head by 5 or 4 units to the right.
characters_saved = 0
for string in numerals:
    k = 0
    while k <= len(string) - 4:
        if (k + 5 <= len(string)) and string[k:k + 5] in five_patterns:
            characters_saved += 3
            k += 4
            continue
        if string[k:k + 4] in four_patterns:
            characters_saved += 2
            k += 3
            continue
        k += 1

print(characters_saved)
end = time.time()
print(f"Program runtime: {end - start} seconds")
