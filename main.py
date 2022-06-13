Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random

while True:
    options = ["R", "S", "P"]

    computer = random.choice(options)
    player = None

    player = input("R, S, or P?: ").lower()

    for x in options:
       print(player)
    else:
        print("Entry error. Kindly enter a correct option")

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
