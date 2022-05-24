#################################
#  PROJECT EULER - PROBLEM 098  #
#################################
import time


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


def string_type(string: str) -> tuple[int]:
    """ Given a string, returns a tuple consisting of the frequencies of each
    of its letters, sorted in decreasing order. For example:
        string_type("CARE") -> (1, 1, 1, 1)
        string_type("representation") -> (3, 2, 2, 2, 1, 1, 1, 1, 1)
            corresponding to the letters (e, r, n, t, p, s, a, i, o) """
    return tuple(reversed(sorted(string.count(letter) for letter in
                 set(string))))


def match_two_strings(str_1: str, str_2: str) -> bool:
    """ Given two strings, decides if one can be mapped into the other by
    applying a bijection of the set of letters of the first to the set of
    letters of the second one. """
    m = len(str_1)
    if len(str_2) != m:
        return False
    else:
        for char in set(str_1):
            char_indices = [k for k in range(m) if str_1[k] == char]
            matching_char = str_2[char_indices[0]]  # Matching char in str_2.
            mchar_indices = [k for k in range(m) if str_2[k] == matching_char]

            if char_indices != mchar_indices:
                return False
    return True


def match(str_1, str_2, str_3, str_4) -> bool:
    """ Decides if (str_1, str_3) and (str_2, str_4) match in the sense
    described above, and if moreover the bijections which transform
    str_1 into str_3 and str_2 into str_4 are the same. """
    if match_two_strings(str_1, str_3) and match_two_strings(str_2, str_4):
        m = len(str_1)
        dict_1 = {str_1[k]: str_3[k] for k in range(m)}
        dict_2 = {str_2[k]: str_4[k] for k in range(m)}
        if dict_1 == dict_2:
            return True
    return False


start = time.time()


# Extract the words from the file provided in the problem statement.
with open("p098_words.txt") as file_object:
    for line in file_object:
        words = [word.replace('"', '') for word in line.split(",")]

# Search for all pairs of anagrams and store them in a list.
anagram_pairs: list[tuple] = []
n = len(words)
max_length = 0  # Maximum length of a word which has an anagram pair.
for i in range(n - 1):
    for j in range(i + 1, n):
        if are_anagrams(words[i], words[j]):
            anagram_pairs.append((words[i], words[j]))
            max_length = max(max_length, len(words[i]))
# print(anagram_pairs)

# Store all 'types' (given by a tuple which counts the frequencies of each
# letter) of strings which have an anagram pair.
valid_types = set(sorted(list(string_type(a) for (a, b) in anagram_pairs)))

S = 10**max_length  # Upper bound for the squares to be searched.

# Produce all squares < S.
squares = []
k = 1
while k**2 < S:
    squares.append(str(k**2))
    k += 1

number_of_squares = len(squares)
found_solution = False
for i in reversed(range(number_of_squares)):
    # Begin the search from the largest square. If its distribution of digits
    # has a type which matches that of one of the words in the list of
    # anagrams, continue.
    if string_type(squares[i]) in valid_types:
        # Consider a second square smaller than the first.
        for j in reversed(range(i)):
            if are_anagrams(squares[i], squares[j]):
                # For each pair of anagrams, compare the first and second
                # squares to each pair of anagrams stored in our list of pairs.
                # If there is a match according to the rules in the problem
                # statement, we have found the solution.
                for (word_1, word_2) in anagram_pairs:
                    if match(squares[i], squares[j], word_1, word_2) or\
                            match(squares[i], squares[j], word_2, word_1):
                        print(squares[i], squares[j])
                        print(word_1, word_2)
                        found_solution = True
                        break
    if found_solution:
        break

end = time.time()
print(f"Program runtime: {end - start} seconds")
