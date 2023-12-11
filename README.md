# Hangman Game in Python - Project

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

### Description

- *Hangman* is a classic game involding two players - one player thinks of a word, and the other player tries to guess that word within a certain number of attempts.

- This project executes a simple *Hangman* game in Python. It involves creating a list of fruits, randomly selecting a word from the list, and then prompting the player to guess the word by entering one letter at a time. Integrated input validation checks ensure that the player only inputs a single alphabetical character at a time, and a user friendly interface improves the player's experience by showing which letters have been guessed correctly.

- The project aims to exhibit key skills and concepts in Python which include, but are not limited to: functions; for loops, iteration, and control flow;  classes; user-input handling; OOP (object-oriented programming); game logic; error handling; and debugging.

- Throughout this experience I have honed in the skills and concepts mentioned above, and learned how to apply them practically. This project has helped me grow confident in using Python.


### Installation
To install the game:

1. Clone the game repository.
   ```
   git clone https://github.com/travelling-mango/hangman844.git
   ```
2. Navigate to the game directory.
   ```
   cd hangman844
   ```
3. Run the game.
   ```
   python3 hangman_game.py
   ```
4. Enjoy!

### Usage
To play the game:

1. You'll be prompted to guess a letter.
2. Enter a single alphabetical character.
3. If the letter is in the word, the game will reveal its position. If not, you'll lose a life. You have 5 lives.
4. The game ends when you either guess the word or run out of lives.

### File Structure

- `README.md`: Project documentation.
- `hangman_game.py`: Python script containing the Hangman game code.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

