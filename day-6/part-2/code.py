with open("input", "r") as f:
    line = f.readline()


def detect_marker(datastream):
    for i in range(len(datastream) - 14):
        sequence = datastream[i:i+14]
        if len(set(sequence)) == 14:
            print(i+14)
            break
    return -1


detect_marker(line)