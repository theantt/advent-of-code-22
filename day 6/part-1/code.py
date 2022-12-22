with open("input", "r") as f:
    line = f.readline()


def detect_marker(datastream):
    for i in range(len(datastream) - 3):
        sequence = datastream[i:i+4]
        if len(set(sequence)) == 4:
            print(i+4)
            break
    return -1


detect_marker(line)