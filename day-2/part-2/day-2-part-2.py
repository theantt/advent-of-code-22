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
    # Force a draw
    if my_plays[i] == "Y":
        #  Get three points from a draw
        match_points += 3
        
        # Get points for plays
        if opponent_plays[i] == "A":
            # Get one point if you play rock
            match_points += 1
        elif opponent_plays[i] == "B":
            # Get two points if you play paper
            match_points += 2
        elif opponent_plays[i] == "C":
            match_points += 3
    # Win
    elif my_plays[i] == "Z":
        #  Get six points from a win
        match_points += 6
        
        # Get points for plays
        if opponent_plays[i] == "A":
            # Get two points if you play paper
            match_points += 2
        elif opponent_plays[i] == "B":
            # Get three points if you play scissors
            match_points += 3
        elif opponent_plays[i] == "C":
            # Get one point if you play rock
            match_points += 1

    # Lose
    elif my_plays[i] == "X":
        # Get no points from a loss
        
        # Get points for plays
        if opponent_plays[i] == "A":
            # Get three points if you play scissors
            match_points += 3
        elif opponent_plays[i] == "B":
            # Get one point if you play rock
            match_points += 1
        elif opponent_plays[i] == "C":
            # Get two points if you play paper
            match_points += 2

    my_points.append(match_points)
    # Reset points to zero
    match_points = 0
    # Iterate to continue loop
    i += 1

total_score = sum(my_points)
print(total_score)
