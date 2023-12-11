

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = self.word_guessed.count('_')

    def check_guess(self, guess):
        guess = guess.lower()
        found = False
        for i, letter in enumerate(self.word):
            if letter.lower() == guess:
                self.word_guessed[i] = guess
                found = True

        if found:
            print(f"Good guess! '{guess}' is in the word.")
            self.num_letters = self.word_guessed.count('_')
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        return found

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").strip()
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                self.list_of_guesses.append(guess)
                break

    def display_information(self):
        print(f"Word Guessed: {' '.join(self.word_guessed)}")
        print(f"Number of Unique Letters Left: {self.num_letters}")
        print(f"Number of Lives Left: {self.num_lives}")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            game.display_information()
        else:
            print('Congratulations. You won the game!')
            break

if __name__ == "__main__":
    word_list = ["Pear", "Mango", "Raspberry", "Plum", "Orange"]
    play_game(word_list)


