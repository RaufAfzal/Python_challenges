import sys
import random
from enum import Enum
from modules import clname

def rps(name = "PlayerOne"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        class RPS(Enum):
            ROCK = 1
            SCISSOR = 2
            PAPER = 3

        print(RPS.ROCK)
        print(RPS(2))
        print(RPS.PAPER.value)
        nonlocal name

        player = input("Enter value....\n 1 for Rock \n 2 for scissors \n 3 for paper \n")

        if player not in ["1", "2", "3"]:
            print(f" {name} please enter the valid input and select from 1 or 2 or 3")
            return play_rps()
    

        player = int(player)

        print (f"{name} have selected {str(RPS(player)).replace("RPS." , '')}.")

        computer = random.choice("123")

        computer = int(computer)

        print (f"Computer have selected {str(RPS(computer)).replace("RPS.", '')}.")
        
        def who_wins(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            if player == 1 and computer == 2:
                player_wins +=1
                return(f"{name} wins")
            elif player == 1 and computer == 3:
                computer_wins +=1
                return("Computer wins")
            elif player == 3 and computer == 1:
                player_wins +=1
                return(f"{name} wins")
            elif player == computer:
                return("Game Tie")
            else:
                computer_wins +=1
                return("computer wins")
        
        game_result = who_wins(player, computer)
        print(game_result)

        nonlocal game_count 
        game_count +=1
        print(f'Game Count: {str(game_count)}')

        print(f'Player wins {str(player_wins)}')

        print(f'Computer wins {str(computer_wins)}')

        while True:
            value = input(f"{name} print Y to continue \n\n and Q to qiut")
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
    return play_rps



if __name__ == "__main__":
    args = clname()

rock_paper_scissor = rps(args.name)

rock_paper_scissor()

    





