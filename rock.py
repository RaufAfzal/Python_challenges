import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        SCISSOR = 2
        PAPER = 3

    print(RPS.ROCK)
    print(RPS(2))
    print(RPS.PAPER.value)

    player = input("Enter value....\n 1 for Rock \n 2 for scissors \n 3 for paper \n")

    if player not in ["1", "2", "3"]:
        print("please enter the valid input and select from 1 or 2 or 3")
        return play_rps()
   

    player = int(player)

    print ("Player have selected " + str(RPS(player)).replace("RPS." , '') + ".")

    computer = random.choice("123")

    computer = int(computer)

    print ("Computer have selected " + str(RPS(computer)).replace("RPS.", '') + " ")
    

    if player == 1 and computer == 2:
        print("Player wins")
    elif player == 1 and computer == 3:
        print("Computer wins")
    elif player == 3 and computer == 1:
        print("Player wins")
    elif player == computer:
        print("Game Tie")
    else:
        print("computer wins")

    while True:
        value = input("Please print Y to continue \n and Q to qiut")
        if value.lower() not in ["y","q"]:
            continue
        else:
            break

    if value.lower() == "y":
       return play_rps()
    else:
        print ("ThankYou for playing!")
        print('see you soon')
        sys.exit("bye")



play_rps()




