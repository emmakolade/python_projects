import random
from words import words
import string

def get_a_valid_word(words):
    valid_word = random.choice(words) #random.choice randomly chooese something from a list
    while '-' in valid_word or ' ' in valid_word:
        valid_word = random.choices(words)

    return valid_word.upper()

# to keep track of words we guessed
def hangman():
    valid_word = get_a_valid_word(words)
    letter_word = set(valid_word) # saves all the letters in the word
    alphabet = set(string.ascii_uppercase) # upper case latter
    letters_used = set() # empty set to keep track of what the user has guessed

    lives = 5
    # get input from the user
    while len(letter_word) > 0 and lives > 0:
        # letters used
        print(" you have used these letters: ", ' '.join(letters_used))

        list = [letter if letter in letters_used else '-' for letter in valid_word]
        print('current word: ', ' '.join(list))

    user_letter = input('guess a letter: ').upper()
    if user_letter in alphabet - letters_used:
        letters_used.add(user_letter) # if the imput from user is in alphabet and it hasnt been used yet,
                                     # then add it to the letter used.
        if user_letter in letter_word:
            letter_word.remove(user_letter) # if the letter just guessed is in the word then
                                            # remove the letter from the letter words.
        else:
            lives = lives - 1 # takes away one life if wrong
            print('letter is not in the word')
    elif user_letter in letters_used:
        print("you have used that character. please try again ")
    else:
        print("invalid character")

    # when len == 0 and lives == 0
    if lives == 0:
        print('you died, the word was', valid_word)
    else:
        print('you guessed the word', valid_word)

hangman()
