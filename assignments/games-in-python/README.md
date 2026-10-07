
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Create a classic Hangman game in Python using strings, loops, conditionals, and user input. The student will practice controlling game state, tracking guesses, and presenting feedback to the player.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Set up the core game state by choosing a random word and preparing the display for the player.

#### Requirements
Completed program should:

- Use a predefined list of words and randomly select one for each new game
- Show a hidden word using underscores or blanks for each letter, such as `_ _ _ _ _`
- Keep track of the letters already guessed by the player
- Display the number of remaining attempts clearly

### 🛠️ Guess Handling and Win/Loss Logic

#### Description
Build the main game loop so the player can guess letters, update the word progress, and end the game when the round is complete.

#### Requirements
Completed program should:

- Prompt the user for a single letter guess
- Check whether the guessed letter is in the hidden word
- Reveal matching letters in the correct positions
- Reduce the number of remaining attempts for incorrect guesses
- End the game when the word is fully guessed or attempts reach zero
- Print a clear win or loss message at the end of the round
