
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?:").lower()
        
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        