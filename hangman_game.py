"""Hangman Game

A simple implementation of the Hangman game in Python.

Usage:
    python3 hangman_game.py

Author:
    Margo Dmochowska (travelling-mango)

"""

import random

class Hangman:
    """Class representing the Hangman game.

    Attributes:
        word_list (list): List of words to choose from.
        num_lives (int): Number of lives the player has.
        list_of_guesses (list): List to store guessed letters.
        word (str): Word to be guessed, chosen randomly.
        word_guessed (list): List to represent the word with '_' for unrevealed letters.
        num_letters (int): Number of unique letters left to guess in the word.

    Methods:
        check_guess(guess): Check if the guessed letter is in the word.
        ask_for_input(): Prompt user for a letter and process the input.
        display_information(): Display the current state of the game.

    """

    def __init__(self, word_list, num_lives=5):
        """Initialize Hangman object with word list and number of lives."""
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = self.word_guessed.count('_')

    def check_guess(self, guess):
        """Check if the guessed letter is in the word.

        Args:
            guess (str): The letter guessed by the player.

        Returns:
            bool: True if the letter is in the word, False otherwise.

        """
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
        """Prompt user for a letter and process the input."""
        while True:
            guess = input("Guess a letter: ").strip()
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def display_information(self):
        """Display the current state of the game."""
        print(f"Word Guessed: {' '.join(self.word_guessed)}")
        print(f"Number of Unique Letters Left: {self.num_letters}")
        print(f"Number of Lives Left: {self.num_lives}")

def play_game(word_list):
    """Play the Hangman game.

    Args:
        word_list (list): List of words to choose from.

    """
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


