# closure is a funcrion having access to the scope of it's parent 
# function after the parent functionhas returned.

def parent_function(person, coins):
    #coins = 3

    def play_game():
        nonlocal coins 
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
             print("\n" + person + " is out of coins")

    return play_game

diogo = parent_function("Diogo", 3)
ines = parent_function("Inês", 5)

diogo()
diogo()

ines()