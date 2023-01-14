import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Van még' lives, 'életed, és ezeket a betűket használtad fel eddig: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('current word: ', ' '.join(word_list))

        user_letter = input('Írj egy betűt: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nA betűd,', user_letter, 'nincs a szóban.')

        elif user_letter in used_letters:
            print('\nSzenilis vagy? Ezt a betűt már használtad. Keress másikat.')

        else:
            print('\nEz nem egy létező betű.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Meghaltál, bocsesz. Ez volt a szó:', word)
    else:
        print('taps, taps! Sikeres válasz:)', word, '!!')


if __name__ == '__main__':
    hangman()
