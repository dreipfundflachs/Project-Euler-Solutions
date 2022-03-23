# PROJECT EULER PROBLEM 059
import time


def convert_to_binary(a):
    """ Converts an ascii character to a byte, i.e., yields the binary
    representation of its ascii number. """
    binary_rep = bin(ord(a))
    byte = (str(binary_rep))[2:]
    # Complete the left side with 0's if necessary.
    n = len(byte)
    print(n)
    for k in range(8 - n):
        byte = '0' + byte
    return byte


def convert_to_int(b):
    """ Given a byte encoded as a string, yields the corresponding integer.
    A vanilla form of """
    power = 0
    result = 0
    for d in b[::-1]:
        result += 2**power * int(d)
        power += 1
    return result


def xor(a, b):
    """ Computes the result of applying XOR (exclusive or) to two
    bytes a and b. """
    xor_a_b = [0] * 8
    for k in range(8):
        xor_a_b[k] = str((int(a[k]) + int(b[k])) % 2)
    return ''.join(xor_a_b)


def decrypt(text, key):
    """ Given a key (an integer) and a list of integers (representing ascii
    characters), applies XOR to each pair (key, integer) to decript a message.
    """
    letters = []
    key_byte = f'{key:08b}'
    for k in text:
        k_byte = f'{k:08b}'
        letter = chr(convert_to_int(xor(key_byte, k_byte)))
        letters.append(letter)
    return ''.join(letters)



start = time.time()

# Extract the contents of the file.
with open('p059_cipher.txt') as file_object:
    numbers = (file_object.read()).split(',')
# Create three lists from the text, one associated to each of the three keys.
lists = [0, 1, 2]
for k in range(3):
    lists[k] = numbers[k::3]

# Initialize a list to hold the key candidates for each of the lists.
candidates = [[], [], []]

# For each list, take XOR with each integer which corresponds to a lower letter
# under ASCII, and check if the corresponding integers represents a letter or
# symbol that one would expect to appear in a real text.
for k in range(3):
    for i in range(97, 123):
        candidate = True
        for j in lists[k]:
            int_j = int(j)
            byte_i = f'{i:08b}'
            byte_j = f'{int_j:08b}'
            result = convert_to_int(xor(byte_i, byte_j))
            # If the result is unexpected, the key is not a candidate.
            if result < 32 or result > 122 or \
                    result == 61 or result == 64 or result in [94, 96]:
                candidate = False
                break
        # If the i is a possible for being the key, append it to candidates[k]
        if candidate == True:
            candidates[k].append(i)
print(candidates)

# Initialize a list that will hold all letters in each of the three lists.
letters = [0, 0, 0]
# Since there is only one candidate for the key in each case, we can now
# proceed to decrypt each of the three parts of the text.
for i in range(2):
    for k in range(3):
        lists[k] = [int(n) for n in lists[k]]
        letters[k] = decrypt(lists[k], candidates[k][0])

# Write the contents of the text to a file and compute the sum s of the ASCII
# characters.
s = 0
print(len(letters[0]) == len(letters[2]))
with open('p059_decrypted.txt', 'w') as file_object:
    for n in range(len(letters[0])):
        for k in range(3):
            s += ord(letters[k][n])
            file_object.write(letters[k][n])
# Print the answer.
print(s)
