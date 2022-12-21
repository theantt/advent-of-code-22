with open("day-2-input", "r") as my_input:
    lines = my_input.readlines()

# Initialize lists for opponent and my actions
opponent_plays = []
my_plays = []
my_points = []
match_points = 0

for line in lines:
    values = line.split()
    opponent_plays.append(values[0])
    my_plays.append(values[1])

i = 0
while i < len(my_plays):
    # Get points based on your play
    if my_plays[i] == "Y":
        # Get two points if you play paper
        match_points += 2
    if my_plays[i] == "X":
        # Get one point if you play rock
        match_points += 1
    if my_plays[i] == "Z":
        # Get three points if you play scissors
        match_points += 3
    # Get points based on if you win
    if (
        # Paper beats rock
        ((my_plays[i] == "Y") and (opponent_plays[i] == "A")) or
        # Scissors beats paper
        ((my_plays[i] == "Z") and (opponent_plays[i] == "B")) or
        # Rock beats scissors
        ((my_plays[i] == "X") and (opponent_plays[i] == "C"))
    ):
        match_points += 6
    # Get points based on if you draw
    if (
        # Paper draw
        ((my_plays[i] == "Y") and (opponent_plays[i] == "B")) or
        # Scissors draw
        ((my_plays[i] == "Z") and (opponent_plays[i] == "C")) or
        # Rock draw
        ((my_plays[i] == "X") and (opponent_plays[i] == "A"))
    ):
        match_points += 3

    # Append points for this match to my list of games
    my_points.append(match_points)
    # Reset points to zero
    match_points = 0
    # Iterate to continue loop
    i += 1

total_score = sum(my_points)
print(total_score)
