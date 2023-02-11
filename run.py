# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Creates random choice for computer
import random

# Creates a list of possible options for a game
options = ["rock", "paper", "scissors"]

while True:
    # Gets input from an user
    player = input("Enter your choice ( Rock, Paper, Scissors): ")
    # Creates a random choice from an option list to play against an user
    computer = random.choice(options)
    # Prints what players have chosen
    print(f"You have chosen -> {player} <-\nComputer have chosen ->{computer}<-")
    # Game logic
    if player == computer:
        print(f"Both players have chosen ->{player}<----IT IS A DRAW!---")
    elif player == "rock":
        if computer == "scissors":
            print("ROCK SMASHES SCISSORS!---YOU WIN!---")
        else:
            print("PAPER COVERS ROCK!---YOU LOSE!---")
    elif player == "paper":
        if computer == "rock":
            print("PAPER COVERS ROCK!---YOU WIN!---")
        else:
            print("SCISSORS CUTS PAPER!---YOU LOSE!---")  
    elif player == "scissors":
        if computer == "paper":
            print("SCISSORS CUTS PAPER!---YOU WIN!")
        else:
            print("ROCK SMASHES SCISSORS!---YOU LOSE!---")
    else:
        print("SORRY, INLVALID ENTRY---YOU LOSE---")

    # Creates a new game    
    new_game = input("Start New Game? (y/n): ")
    if new_game.lower() != "y":
        break    