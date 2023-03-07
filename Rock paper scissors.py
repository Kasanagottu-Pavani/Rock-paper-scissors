import random

# define the three possible moves
moves = ['rock', 'paper', 'scissors']

# get user input for their move
player_move = input("Choose your move: rock, paper, or scissors? ")

# randomly select the computer's move
computer_move = random.choice(moves)

# print out the player and computer moves
print(f"You played {player_move}. The computer played {computer_move}.")

# determine the winner
if player_move == computer_move:
    print("It's a tie!")
elif player_move == 'rock' and computer_move == 'scissors' or \
     player_move == 'paper' and computer_move == 'rock' or \
     player_move == 'scissors' and computer_move == 'paper':
    print("You win!")
else:
    print("The computer wins!")
