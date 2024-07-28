import random

# throw the dice 

def Roll():
    rollNum = random.randint(1,6)
    print(rollNum)
    return rollNum


# play

while True:
    # quick amount player
    players = input('How many players re going to play (2 - 4 ) ')

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Must be 2 - 4 players ")
    else:
        print("Invalid please try again")

# print("There are" , players, "players")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for i in range(players):
        print("Player", i+1, " turn has staterd \n")

        current_score = 0 

        while True:

            should_roll = input("would you like to roll (y) ")

            if should_roll.lower() != "y":
                break

            value = Roll()

            if value == 1: 
                print("You rolled a 1 turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)

            print("Your score is", current_score)
        
        players_score[i] += current_score
        print("Your total score is: ", players_score[i])