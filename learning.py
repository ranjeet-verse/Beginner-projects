
# print("Welcome to the tip calculator")

# bill = float(input("What was the bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, 13, 14, 15? "))
# split = int(input("How many people to split the bill? "))
# tip_as_percent = tip/100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / split
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")


# print("RZoller coster")
# height = int(input("Enter your height in cm: "))

# if height >= 175:
#     print("You can ride the roller coster")
# else:
#     print("you cannot ride grow up")

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print('Even')
# else:
#     print('odd')

# height = int(input("Enter your height in cm: "))
# bill = 0

# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = int(input("Enter your age: "))
    
#     if age <= 14:
#         bill = 5
#         print("Child ticket: $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth ticket: $7")
#     else:
#         bill = 8
#         print("Adult ticket: $8")
    
#     photo = input("Do you want to take a photo? Y or N: ")
#     if photo.upper() == 'Y':
#         bill += 3
    
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you must be at least 120 cm tall to ride.")


# print("Welcome to python pizza delivery")
# size = input("What size pizza do you want? S, M, or L ")
# pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size.upper() == 'S':
#     bill += 15
#     if pepperoni.upper() == 'Y':
#         bill += 2
#     if extra_cheese.upper() == 'Y':
#         bill += 1
# elif size.upper() == "M":
#     bill += 20
#     if pepperoni.upper() == 'Y':
#         bill += 3
#     if extra_cheese.upper() == 'Y':
#         bill += 1
# elif size.upper() == 'L':
#     bill += 25
#     if pepperoni.upper() == "Y":
#         bill += 3
#     if extra_cheese.upper() == 'Y':
#         bill += 1
# print(f"Your final bill is : ${bill} ")

# print("WElcone to treasure island")
# print("Your mission is to find the treasure")
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" ').lower()

# if choice1.lower() == 'left':



#     choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
#     if choice2.lower() == 'wait':
    
#         choice3 = input("you arrive at the island unharmed. There is ahouse with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
#         if choice3.lower() == 'red':
#             print("it,s a room full of fire. Game over")
#         elif choice3.lower()  == 'blue':
#             print('You entered a romm of beasts. Game over')
#         elif choice3.lower() == 'yellow':
#             print("you found the right one my nigga. YOU WIN")
        
#         else: 
#            print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print('Watch out my nigga you failed')
# else:
#     print('Get your --- home')       

# import random

# coin = random.choice(["Heads", "Tails"])
# print(f"Result: {coin}")

# import random



# friends = ["Alice", "bob", "charlie", "david", "emanuel"]
# print(random.choice(friends))

# states_of_india = [
#     "Andhra Pradesh",
#     "Arunachal Pradesh",
#     "Assam",
#     "Bihar",
#     "Chhattisgarh",
#     "Goa",
#     "Gujarat",
#     "Haryana",
#     "Himachal Pradesh",
#     "Jharkhand",
#     "Karnataka",
#     "Kerala",
#     "Madhya Pradesh",
#     "Maharashtra",
#     "Manipur",
#     "Meghalaya",
#     "Mizoram",
#     "Nagaland",
#     "Odisha",
#     "Punjab",
#     "Rajasthan",
#     "Sikkim",
#     "Tamil Nadu",
#     "Telangana",
#     "Tripura",
#     "Uttar Pradesh",
#     "Uttarakhand",
#     "West Bengal"
# ]

# # Example usage:
# print(len(states_of_india))

# fruits = ["Strawberry", "Nectarine", "Apple", "Peach", "Cherries", "Mango", "Orange"]
# # vegetables = ["Spinach", "Kale", "Tomato", "Celery", "Potato"]

# # dry_dozona = [fruits , vegetables]

# print(fruits[-5])

# making the rock paper scissors game

# import random 

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
# computer_choice = random.randint(0, 2)

# if user_choice >= 3 or user_choice < 0:
#     print("you typed an invalid number, loser")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win")
# elif computer_choice == 0 and user_choice == 2:
#     print("you lose loser")
# elif computer_choice > user_choice:
#     print("you lose loser")
# elif user_choice > computer_choice:
#     print("you win")
# elif computer_choice == user_choice:
#     print("it's a draw")
# print(f"computer chose {computer_choice}")

# fruits = ["Strawberry", "Nectarine", "Apple", "Peach", "Cherries", "Mango", "Orange"]
# for fruit in fruits:
#     print(fruit)
    
    
# students_scores = [12, 65, 34, 23, 90, 45, 78, 56, 89, 100, 43, 67]
# max_score = 0
# for score in students_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

# number = 0
# for n in range(0, 101):
#     number += n
# print(number)

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword generator")
# letters_count = int(input("How many letters would you like in your password? \n"))
# symbols_count = int(input("how many sysmbols would you like? \n"))
# numbers_count = int(input("how many numbers would you like? \n"))


# password_list = []
# for letter in range(letters_count):
#     password_list.append(random.choice(letters))
# for symbol in range(symbols_count):
#     password_list.append(random.choice(symbols))
# for number in range(numbers_count):
#     password_list.append(random.choice(numbers))
# random.shuffle(password_list)
# password = ''.join(password_list)
# print(f"You password is: {password}")












# print("Welcome to the PyPassword generator")
# letters_count = int(input("How many letters would you like in your password? \n"))
# symbols_count = int(input("how many sysmbols would you like? \n"))
# numbers_count = int(input("how many numbers would you like? \n"))

# password_list = random.choices(letters, k=letters_count) + random.choices(symbols, k=symbols_count) + random.choices(numbers, k=numbers_count)
# random.shuffle(password_list)
# password =  ''.join(password_list)
# print(f"Your password is: {password}")


# def greet(name, location):
#     print(f"hello {name}")
#     print(f"how are you {location}")
#     print("Welcome to hangman")

# greet(name:"ramayan", location:"india")
# # def greet_with(name, location):


# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2.lower()
#     true_count = sum(combined_names.count(char) for char in "true")
#     love_count = sum(combined_names.count(char) for char in "love")
#     love_score = int(str(true_count) + str(love_count))

#     return love_score

# calculate_love_score("jack" , "gill")