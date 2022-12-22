# Algorithm from /u/i_have_no_biscuits on reddit
# https://www.reddit.com/r/adventofcode/comments/zcxid5/comment/iyz8zkl/?utm_source=share&utm_medium=web2x&context=3


def parse_stack_text(stacktext):
    stacks = [""]*10
    for line in stacktext[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ": stacks[i+1] += box
    return stacks


# Open file
with open("input") as f:
    input_data = f.read()

# Parse stack text and instructions into separate parts
stack_text, instructions = [part.split("\n") for part in input_data.split("\n\n")]
# Parse stack text into rows
stacks = parse_stack_text(stack_text)

p2 = stacks[:]

for line in instructions:
    _, n, _, src, _, dest = line.split()
    n = int(n)
    src = int(src)
    dest = int(dest)

    p2[src], p2[dest] = p2[src][n:], p2[src][:n] + p2[dest]

print("Part 2:", "".join(s[0] for s in p2 if s))

