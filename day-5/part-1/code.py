# Algorithm from /u/i_have_no_biscuits on reddit
# https://www.reddit.com/r/adventofcode/comments/zcxid5/comment/iyz8zkl/?utm_source=share&utm_medium=web2x&context=3

""" Working code """

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
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
# Parse stack text into rows
stacks = parse_stack_text(stackt)

p1 = stacks[:]

for line in instructions:
    _, n, _, src, _, dest = line.split()
    n = int(n);
    src = int(src);
    dest = int(dest);

    p1[src], p1[dest] = p1[src][n:], p1[src][:n][::-1] + p1[dest]
print("Part 1:", "".join(s[0] for s in p1 if s))

