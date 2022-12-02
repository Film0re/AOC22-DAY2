# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
