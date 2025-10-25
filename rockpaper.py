#making the rock paper scissors game

import random 

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number, loser")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose loser")
elif computer_choice > user_choice:
    print("you lose loser")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("it's a draw")
print(f"computer chose {computer_choice}")