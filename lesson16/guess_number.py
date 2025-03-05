import sys
import random
from enum import Enum

def guess():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_guess():
        nonlocal player_wins 
        nonlocal python_wins

        playerchoice = input(
                "\nI'm thinking of a number, choose 1, 2 or 3 \n")

        if playerchoice not in ["1", "2", "3"]:
                print("You must enter 1, 2, or 3. \n")
                return play_guess()
        
        player = int(playerchoice)
        
        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("\nYou chose " + str(player) + "\n")
        print("I was thinking of number " + str(computer) + ".\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == computer:
                player_wins += 1
                return "🎉 You win!"
            else:
                python_wins += 1
                return "🐍 Better luck next time... \n"
            
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1


        percent = player_wins/game_count

        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nWinning percentage: " + f"{percent: 0.0%}")

        print("\nPlay again?")
        
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_guess

play = guess()

play()


