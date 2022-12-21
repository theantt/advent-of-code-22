import re

with open("day-3-input", "r") as f:
    lines = f.readlines()

# with open("test", "r") as f:
#     lines = f.readlines()
#     # Output should be [p, L, P, v, t, s]

items = []
first_compartment = []
second_compartment = []
item_duplicate = set()
find_priority = []

priority_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

for line in lines:
    items = re.findall(r".", line)  # reset items list on each iteration
    first_compartment.append(items[:len(items) // 2])
    second_compartment.append(items[len(items) // 2:])

for i in range(len(first_compartment)):
    for j in range(len(first_compartment[i])):
        if first_compartment[i][j] in second_compartment[i]:
            print(first_compartment[i][j])
            item_duplicate.add(first_compartment[i][j])


for i in item_duplicate:
    if i in priority_dict:
        find_priority.append(priority_dict.get(i))


priority_sum = sum(find_priority)
print(priority_sum)

# Gives correct answer for test, but not puzzle input
