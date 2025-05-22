import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    
    # CHANGED: Added proper game loop structure
    while len(word_letters) > 0 and lives > 0:
        # CHANGED: Improved status display formatting
        print("\nYou have", lives, "lives left")  # CHANGED: Added newline and clearer message
        print("Used letters:", " ".join(sorted(used_letters)))  # CHANGED: Added sorting
        
        # CHANGED: Better word display formatting
        word_display = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_display))  # CHANGED: Added spaces between letters
        
        user_letter = input("Guess a letter: ").upper()  # CHANGED: Added colon for clarity
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")  # CHANGED: Added feedback
            else:
                lives -= 1  # CHANGED: More standard decrement
                print("Incorrect! The letter is not in the word.")  # CHANGED: Better feedback
                
        elif user_letter in used_letters:
            print("You already used that letter. Try again.")  # CHANGED: Fixed typo ("caracter")
        else:
            print("Invalid input. Please enter a single letter.")  # CHANGED: More specific message
    
    # CHANGED: MOVED THIS OUTSIDE THE LOOP - this was the main fix!
    if lives == 0:
        print("\nYou lost! The word was:", word)  # CHANGED: Better message
    else:
        print("\nCongratulations! You guessed the word:", word)  # CHANGED: Better message

hangman()