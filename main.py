# Day 2 of 2022 Advent of Code
# Daniel Dowdle
def main():
    decrypt = {"A": "X",  # X
               "B": "Y",  # Y
               "C": "Z"}  # z

    scoring = {"X": 1,
               "Y": 2,
               "Z": 3}

    # Rock = X (A)
    # Paper = Y (B)
    # Scissors = Z (C)

    x_beats_y = {"X": "Z",  # Rock beats paper
                 "Y": "X",
                 "Z": "Y"}

    with open("input.txt") as file:
        lines = file.readlines()

    partOne(lines, decrypt, scoring, x_beats_y)
    partTwo(lines, scoring, decrypt)


def partTwo(lines, scoring, decrypt):
    # Winning takes in the opponents move
    # and returns the move you should play to win
    winning_move = {"A": "Y",  # Rock loses to paper            X Z
                    "B": "Z",  # Paper loses to scissors        Y X
                    "C": "X"  # scissors loses to rock          Z Y
                    }

    # Takes in the opponent's move
    # and returns the move you should play in order to lose

    losing_move = {"A": "Z",  # Rock beats scissors
                   "B": "X",  # Paper beats rock
                   "C": "Y"}  # Scissors beats paper

    play_book = {"X": "lose",
                 "Y": "draw",
                 "Z": "win"}

    score = 0
    for line in lines:
        line = line.strip("\n")
        guide = line.split(" ")

        opponent_move = guide[0]
        my_outcome = guide[1]

        if play_book[my_outcome] == "win":
            score += scoring[winning_move[opponent_move]]
            score += 6  # 6 points for a win
        elif play_book[my_outcome] == "draw":
            score += scoring[decrypt[opponent_move]]
            score += 3
        elif play_book[my_outcome] == "lose":
            score += scoring[losing_move[opponent_move]]

    print(score)


def partOne(lines, decrypt, scoring, x_beats_y):
    total_score = 0

    for line in lines:
        line = line.strip("\n")
        move_array = line.split(" ")

        opponent_move = decrypt[move_array[0]]
        my_move = move_array[1]

        total_score += scoring[my_move]  # add point value for the move I played

        if my_move == opponent_move:
            total_score += 3  # 3 points for a tie
        elif x_beats_y[my_move] == opponent_move:
            total_score += 6  # 6 points for a win

    print(total_score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
