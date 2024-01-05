# a = [*"| | | |"]
# b = [*"| | | |"]
# c = [*"| | | |"]

game_area = {
    "a" : [*"| | | |"],
    "b" : [*"| | | |"],
    "c" : [*"| | | |"]
}
# 0,4,8
end = False
# putting into ui

def is_it_end():
    if game_area["a"][0] == game_area["a"][1] == game_area["a"][2]:
        if game_area["a"][0] == "X":
            print("\nX wins!\n")

while end == False:

    user_coordinates = [*input("Player: X\nType a coordinates:  ").lower()]

    user_row = user_coordinates[0]
    user_column = int(user_coordinates[1])

    if user_column == 0:
        user_column = 1
    elif user_column == 1:
        user_column = 3
    elif user_column == 2:
        user_column = 5

    mark = "X"

    affected_row = game_area[user_row]
    affected_row[user_column] = mark

    print(f'{" ".join(game_area["a"])}\n{" ".join(game_area["b"])}\n{" ".join(game_area["c"])}')
