#################################
#  PROJECT EULER - PROBLEM 097  #
#################################
import time


def are_equal_strings(string_1: str, string_2: str) -> bool:
    """ Decides if two strings are equal. """
    n_1, n_2 = len(string_1), len(string_2)
    if n_1 != n_2:
        return False
    elif n_1 == n_2 == 0:
        return True
    else:
        if string_1[0] == string_2[0]:
            return are_equal_strings(string_1[1:], string_2[1:])
        else:
            return False


def are_anagrams(string_1: str, string_2: str) -> bool:
    """ Decides if two given strings are anagrams of each other. To this end,
    the function searches the second string for the presence of the first
    character of the first string. If it is not found, then False is returned.
    Otherwise, (one instance of) this character is removed from both strings
    and a recursive call on the resulting smaller strings is performed. """
    n_1, n_2 = len(string_1), len(string_2)
    if n_1 != n_2:
        return False
    elif n_1 == n_2 == 0:
        return True
    else:
        i = string_2.find(string_1[0])
        if i == -1:
            return False
        else:
            return are_anagrams(string_1[1:], string_2[:i] + string_2[i + 1:])


start = time.time()

# Extract the words from the file provided in the problem statement.
with open("p098_words.txt") as file_object:
    for line in file_object:
        words = [word.replace('"', '') for word in line.split(",")]

pairs: list[tuple] = []
n = len(words)
for i in range(n - 1):
    for j in range(i + 1, n):
        if are_anagrams(words[i], words[j]):
            pairs.append((words[i], words[j]))

print(pairs)
max_length = 0
for (a, b) in pairs:
    if len(a) > max_length:
        max_length = len(a)
        max_a = a
        max_b = b
        print(a, b)

print(max_a, max_b, max_length)

N = 10**9
n = 10**4
squares = []
while n**2 < N:
    squares.append(str(n**2))
    n += 1
print(n, n**2)
print(len(squares))

m = len(squares)
found_solution = False
for i in reversed(range(m)):
    for j in reversed(range(i)):
        if are_anagrams(squares[i], squares[j]):
            print(squares[i])
            found_solution = True
            break
    if found_solution:
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
