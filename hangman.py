
# pick secret_word
# normalize to lowercase
# lives = 6
# guessed_letters = set()
# wrong_letters = set()
# letters_in_word = set(letter for letter in secret_word if letter.isalpha())

# while lives > 0 and not letters_in_word.issubset(guessed_letters):
#     show masked_word built from secret_word:
#         char if (not alpha) or (char in guessed_letters) else '_'
#     show lives and wrong_letters

#     guess = input().strip().lower()

#     if not guess:
#         continue

#     if len(guess) == 1 and guess.isalpha():
#         if guess in guessed_letters or guess in wrong_letters:
#             inform "already guessed"
#             continue
#         if guess in letters_in_word:
#             guessed_letters.add(guess)
#         else:
#             wrong_letters.add(guess)
#             lives -= 1
#     else:
#         # optional full-word guess
#         if guess == secret_word:
#             guessed_letters |= letters_in_word
#         else:
#             lives -= 1

# if letters_in_word.issubset(guessed_letters):
#     print "You win!"
# else:
#     print "You lose. Word was:", secret_word

import random
from hangman_words import word_list
from hangman_art import logo


print(logo)
lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for place in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
under_score = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in under_score:
        print(f"You've already guessed {guess}")
    
    display = ''


    for letter in chosen_word:
        if letter == guess:
           display += letter
           under_score.append(guess)
        elif letter in under_score:
            display += letter
        
        else:
           display += '_'
    
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("loser")
    
    if "_" not in display:
        game_over = True
        print("you win")
    
    print(f"{lives} lives left")


