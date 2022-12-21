with open("input", "r") as f:
    lines = f.read().strip().split("\n")

values = []
first_pair = []
second_pair = []
first_assignment = []

i = 0
duplicates = set()
count = []
for line in lines:
    values = line.split(",")
    first_pair = values[0].split("-")
    first_assignment = list(range(int(first_pair[0]), int(first_pair[1]) + 1))
    second_pair = values[1].split("-")
    second_assignment = list(range(int(second_pair[0]), int(second_pair[1]) + 1))

    for item in first_assignment:
        if item in second_assignment:
            duplicates.add(item)

    count.append(len(duplicates))
    duplicates = set()

total_overlapping = filter(lambda x: x != 0, count)
print(len(list(total_overlapping)))
