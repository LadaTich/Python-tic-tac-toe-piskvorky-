
game_area = {
    "a" : [*"| | | |"],
    "b" : [*"| | | |"],
    "c" : [*"| | | |"]
}

end = False

def is_it_end():
    x_wins = False
    o_wins = False

    if game_area["a"][1] == game_area["a"][3] == game_area["a"][5]:
        if game_area["a"][1] == "X":
            x_wins = True
        elif game_area["a"][1] == "O":
            o_wins = True
    elif game_area["b"][1] == game_area["b"][3] == game_area["b"][5]:
        if game_area["b"][1] == "X":
            x_wins = True
        elif game_area["b"][1] == "O":
            o_wins = True
    elif game_area["c"][1] == game_area["c"][3] == game_area["c"][5]:
        if game_area["c"][1] == "X":
            x_wins = True
        elif game_area["c"][1] == "O":
            o_wins = True
    elif game_area["a"][1] == game_area["b"][1] == game_area["c"][1]:
        if game_area["a"][1] == "X":
            x_wins = True
        elif game_area["a"][1] == "O":
            o_wins = True
    elif game_area["a"][3] == game_area["b"][3] == game_area["c"][3]:
        if game_area["a"][3] == "X":
            x_wins = True
        elif game_area["a"][3] == "O":
            o_wins = True
    elif game_area["a"][5] == game_area["b"][5] == game_area["c"][5]:
        if game_area["a"][5] == "X":
            x_wins = True
        elif game_area["a"][5] == "O":
            o_wins = True
    elif game_area["a"][1] == game_area["b"][3] == game_area["c"][5]:
        if game_area["a"][1] == "X":
            x_wins = True
        elif game_area["a"][1] == "O":
            o_wins = True
    elif game_area["a"][5] == game_area["b"][3] == game_area["c"][1]:
        if game_area["a"][5] == "X":
            x_wins = True
        elif game_area["a"][5] == "O":
            o_wins = True
    
    if x_wins:
        print("\nX wins!\n")
        return True
    elif o_wins:
        print("\nO wins!\n")
        return True
    else: 
        return False

def play(mark):
    user_coordinates = [*input(f"\nPlayer: {mark}\nType a coordinates:  ").lower()]

    try:
        user_row = user_coordinates[0]
        user_column = user_coordinates[1]
    except IndexError:
        print("\nWrong input. You have to choose from a/b/c rows and 0/1/2 columns.\nTry it again.\n")
        play(mark)

    if user_row == "a" or user_row == "b" or user_row == "c" and user_column == "0" or user_column == "1" or user_column == "2":
        user_column = int(user_column)

        if user_column == 0:
            user_column = 1
        elif user_column == 1:
            user_column = 3
        elif user_column == 2:
            user_column = 5

        affected_row = game_area[user_row]
        affected_row[user_column] = mark
    else:
        print("\nWrong input. You have to choose from a/b/c rows and 0/1/2 columns.\nTry it again.\n")
        play(mark)


while end == False:

    print(f'\n{" ".join(game_area["a"])}\n{" ".join(game_area["b"])}\n{" ".join(game_area["c"])}\n')

    play("X")

    end = is_it_end()

    if end == False:
        print(f'\n{" ".join(game_area["a"])}\n{" ".join(game_area["b"])}\n{" ".join(game_area["c"])}\n')
        play("O")
        end = is_it_end()
