import random
import time
import os
import sys

#------------------------------GLOBAL VARIABLES--------------------------------

dice = 6

snakes = {98: 12, 77: 39, 69: 1, 31: 23, 20: 15, 61: 45}
ladders = {46: 67, 43: 48, 22: 51, 36: 52, 6: 25, 13: 32}


#----------------------------------FUNCTIONS------------------------------------

def rules():
    print("HELLO THERE!")
    print("WELCOME TO SNAKE AND LADDER GAME!")
    print("---------------------------------")
    print("             RULES:              ")
    print("  i: 2 players per game.")
    print(" ii: if you reach the bottom of the ladder, you climb UPPPP")
    print("iii: if you reach the top of a snake you will go DOWNNNN")
    print()
    input("Press ENTER to continue: ")
    print("GAME STARTS IN...")
    time.sleep(1)
    for i in range(-3,1):
        time.sleep(1)
        print(abs(i))
    sys.stdout.write("\033[2J\033[H")


def names():
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    return player1, player2


def move(dice_number, player_position, player):
    new_position = player_position + dice_number
    print(f"{dice_number} is rolled on the DICE")
    time.sleep(1)
    print(f"{player} moved from {player_position} to {new_position}")
    time.sleep(1.5)
    
    if dice_number == 6:
        print("You get another chance...")
    
    if new_position > 100:
        print("Oops! You need to roll the exact number to reach 100. Stay in your previous position.")
        new_position = player_position
    elif new_position in snakes:
        new_position = snakes[new_position]
        print(f"OOPS! You have moved to {new_position} due to a ~~~~~~~~~:) bite")
    elif new_position in ladders:
        new_position = ladders[new_position]
        print(f"WELL DONE! You have moved to {new_position} by getting on a ############")
    
    return new_position


def check(player_position, player):
    if player_position == 100:
        os.system('clear')
        print("\u03A8 " + player + " HAS WON \u03A8")
        return 0
    elif player_position > 100:
        print("\u03A8 Try harder! \u03A8")


def roll_dice():
    return random.randint(1, dice)

class ANSI_1():
    def background(code):
        return "\33[{code}m".format(code=code) 
    def style_text(code):
        return "\33[{code}m".format(code=code)
    def color_text(code):
        return "\33[{code}m".format(code=code)


def board(player1_pos, player2_pos):
    output = ""
    for i in range(100, 0, -10):
        for j in range(i, i - 10, -1):
            cell = ""
            if player1_pos == j and player2_pos == j:
                cell = '\033[31;1mA \033[32;1mB'
            elif player1_pos == j:
                cell = '  \033[31;1mA \033[0m '
            elif player2_pos == j:
                cell = '  \033[32;1mB \033[0m '
            else:
                cell = f'  {j:2d}  '
            output += cell
        output += '\n\n'
    
    # Clear the terminal
    sys.stdout.write("\033[2J\033[H")
    
    print(output)

#-------------------------------------------------------------------------------

rules()
player1, player2 = names()

print(f"{player1.upper()} vs {player2.upper()}")
time.sleep(2)
os.system('clear')
player1_pos = 0
player2_pos = 0
chance = 1

while True:
    os.system('clear')
    if chance % 2 != 0:
        board(player1_pos, player2_pos)
        print(ANSI_1.background(30) + ANSI_1.color_text(37) + ANSI_1.style_text(37) )
        print("\n\n")
        input(f"{player1}, press ENTER to roll the dice: ")
        dice_number = roll_dice()
        player1_pos = move(dice_number, player1_pos, player1)
        input('Press ENTER to continue:')
    else:
        board(player1_pos, player2_pos)
        print(ANSI_1.background(30) + ANSI_1.color_text(37) + ANSI_1.style_text(37) )
        print("\n\n")
        input(f"{player2}, press ENTER to roll the dice: ")
        dice_number = roll_dice()
        player2_pos = move(dice_number, player2_pos, player2)
        check(player2_pos, player2)
        input('Press ENTER to continue:')

    if player1_pos == 100 or player2_pos == 100:
        break

    if dice_number != 6:
        chance += 1
