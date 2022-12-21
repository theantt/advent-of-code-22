import string

with open("day-3-input") as f:
    lines = f.read().strip().split("\n")

priority_dict = {ch: i for i, ch in enumerate(string.ascii_letters, start=1)}

find_priority = []

for i in range(0, len(lines), 3):
    inv_1 = lines[i]
    inv_2 = lines[i+1]
    inv_3 = lines[i+2]

    for ch in inv_1:
        if ch in inv_2 and ch in inv_3:
            find_priority.append(priority_dict[ch])
            break

print(sum(find_priority))
