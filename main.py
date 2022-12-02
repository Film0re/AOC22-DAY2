# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    strategy_guide = {"a": "rock",  # X
                      "b": "paper",  # Y
                      "c": "scissors"}  # z

    scoring = {"X": 1,
               "Y": 2,
               "Z": 3}

    with open("input.txt") as file:
        lines = file.readlines()

    total_score = 0

    for line in lines:
        line = line.strip("\n")
        move_array = line.split(" ")

        opponent_move = move_array[0]
        my_move = move_array[1]

        

    print(total_score)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
