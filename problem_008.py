# PROJECT EULER - PROBLEM 8

def list_product(list):
    """ Takes a list of integers and returns their product """
    p = 1
    for k in list:
        p *= int(k)
    return p


number = ''
with open('problem_8_text.txt') as file_object:
    for line in file_object:
        number += line.strip()

print(number)
p = 1
for k in number[:13]:
    p *= int(k)

max_p = p
for k in range(13, 999):
    p = list_product(number[k - 12: k + 1])
    if max_p < p:
        max_p = p
print(max_p)
