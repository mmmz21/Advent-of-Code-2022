#Day 2: Rock, Paper, Scissors
elf_score = 0
my_score = 0
# A, X = rock
# B, Y = paper
# C, Z, = scissors
winning_games = {'A': 'Y', 'B': 'Z', 'C': 'X'}  # games in which I win
losing_games = {'A': 'Z', 'B': 'X', 'C': 'Y'}
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3, 'win': 6, 'tie': 3}

with open("input.txt", "r") as input:
    rounds = input.readlines()
    for round in rounds:
        elf_move = round[0]
        my_move = round[2]
        if winning_games[elf_move] == my_move:
            my_score += points['win'] + points[my_move]
            elf_score += points[elf_move]
        elif losing_games[elf_move] == my_move:
            my_score += points[my_move]
            elf_score += points['win'] + points[elf_move]
        else:  # tie
            my_score += points['tie'] + points[my_move]
            elf_score += points['tie'] + points[elf_move]

print(elf_score, my_score)
