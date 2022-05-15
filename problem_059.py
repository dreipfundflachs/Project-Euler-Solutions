#################################
#  PROJECT EULER - PROBLEM 059  #
#################################
import time


def decrypt(text: list[int], key: int) -> str:
    """ Given a key (an integer) and a list of integers (representing ascii
    characters), applies XOR to each pair (key, integer). """
    letters = []
    for i in text:
        letter = chr(i ^ key)
        letters.append(letter)
    return ''.join(letters)


start = time.time()

# Extract the contents of the file.
with open('p059_cipher.txt') as file_object:
    numbers = (file_object.read()).split(',')

# Create three lists from the text, one associated to each of the three keys.
lists: list[list[int]] = [[], [], []]
for k in range(3):
    lists[k] = [int(n) for n in numbers[k::3]]

# Initialize a list to hold the key candidates for each of the lists.
candidates: list[list[int]] = [[], [], []]

# For each list, XOR its elements with each integer which corresponds to a
# lower letter under ASCII, and check if the corresponding integers represents
# a letter or symbol that one would expect to appear in a real text.
for k in range(3):
    # The lowercase letters have ASCII codes between 97 and 122.
    for i in range(97, 123):
        is_candidate = True
        for j in lists[k]:
            int_j = int(j)
            result = i ^ int(j)
            # If the result is unexpected, the key is not a candidate.
            if result < 32 or result > 122 or\
                    result == 61 or result == 64 or 94 <= result <= 96:
                is_candidate = False
                break
        # If i is a possible key, append it to candidates[k].
        if is_candidate:
            candidates[k].append(i)

# print(candidates)

# Will hold all letters in each of the three lists.
letters: list[str] = ["", "", ""]

# Since there is only one candidate for the key in each case, we can now
# proceed to decrypt each of the three parts of the text.
for i in range(2):
    for k in range(3):
        letters[k] = decrypt(lists[k], candidates[k][0])

# Optional: Write the contents of the decrypted text to a file. Also, print the
# answer.
sum_of_ASCII_values = 0
with open('p059_decrypted.txt', 'w') as file_object:
    for n in range(len(letters[0])):
        for k in range(3):
            sum_of_ASCII_values += ord(letters[k][n])
            file_object.write(letters[k][n])

print(sum_of_ASCII_values)
