import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword generator")
letters_count = int(input("How many letters would you like in your password? \n"))
symbols_count = int(input("how many sysmbols would you like? \n"))
numbers_count = int(input("how many numbers would you like? \n"))


password_list = []
for letter in range(letters_count):
    password_list.append(random.choice(letters))
for symbol in range(symbols_count):
    password_list.append(random.choice(symbols))
for number in range(numbers_count):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ''.join(password_list)
print(f"You password is: {password}")


# print("Welcome to the PyPassword generator")
# letters_count = int(input("How many letters would you like in your password? \n"))
# symbols_count = int(input("how many sysmbols would you like? \n"))
# numbers_count = int(input("how many numbers would you like? \n"))

# password_list = random.choices(letters, k=letters_count) + random.choices(symbols, k=symbols_count) + random.choices(numbers, k=numbers_count)
# random.shuffle(password_list)
# password =  ''.join(password_list)
# print(f"Your password is: {password}")

