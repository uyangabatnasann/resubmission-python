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