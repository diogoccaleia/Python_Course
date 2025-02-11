import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

print("")
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for scissors:\n\n")
player = int(playerchoice)

if player <1 | player > 3:  # ctrl+D to change
    sys.exit("You must enter1, 2, or 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("Python chose " + str(RPS(computer)).replace('RPS.', ''))
print("You chose " + str(RPS(player)).replace('RPS.', ''))
print("")

if player == computer:
    sys.exit('It\'s a tie!')
elif player > computer:
    if player - computer == 1:
        sys.exit('Player wins!!!')
    else:
        sys.exit('Python wins :(')
else:
    if computer - player == 1:
        sys.exit('Python wins :(')
    else:
        sys.exit('Player wins !!!')
        