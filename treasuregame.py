print("WElcone to treasure island")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" ').lower()

if choice1.lower() == 'left':



    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2.lower() == 'wait':
    
        choice3 = input("you arrive at the island unharmed. There is ahouse with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3.lower() == 'red':
            print("it,s a room full of fire. Game over")
        elif choice3.lower()  == 'blue':
            print('You entered a romm of beasts. Game over')
        elif choice3.lower() == 'yellow':
            print("you found the right one my nigga. YOU WIN")
        
        else: 
           print("You chose a door that doesn't exist. Game Over.")
    else:
        print('Watch out my nigga you failed')
else:
    print('Get your --- home')       
