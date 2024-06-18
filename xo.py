# import random
# row1 = ["","",""]
# row2 = ["","",""]
# row3 = ["","",""]
# name = input("Enter your name : ")
# def sign():
#     while True:
#         sign = input("Select X or O : ").upper()
#         if sign not in ['X','O']:
#             print("Enter a Valid sign only O or X")
#         elif sign in ['X','O']:
#             break
#     return f"So you selected {sign}"
# operator = sign()
# print(operator) 
game_list = [0,1,2]
def display_game(game_list):
    print(f"Heres the current list\n{game_list}")


def position_choice():
    choice = 'wrong'

    while choice not in['0','1','2']:
        choice = input("Pick a position (0,1,2) : ")

        if choice not in ['0','1','2']:
            print("Invalid Choice")
    return int(choice)


def replacement_choice(game_list,position):

    user_placement=input("Type a string to place at position : ")
    game_list[position] = user_placement
    return game_list
print(replacement_choice(game_list,1))