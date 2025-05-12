# Solo Wheel of Fortune

## Description

Command-line Wheel of Fortune game in Python with college-themed phrases, cash system, and four progressive rounds.

## Dedication

This project is dedicated to my mother, Simin Nematpour, whose endless support and encouragement made this work possible.

## Game Overview

Solo Wheel of Fortune is based on the classic Hangman game concept with additional elements from the Wheel of Fortune TV show:

- 4 rounds of play
- Each round features a randomly selected phrase
- Players can spin a wheel to select consonants and win cash
- Players can buy vowels using their accumulated cash
- Players can attempt to solve the puzzle at any time
- Risk elements like the BANKRUPT wheel space

> [!NOTE]
> The phrases used in this game are primarily college-themed terms and expressions, making it educational as well as entertaining!

## Features

- Random phrase selection from a text file
- Interactive command-line interface
- Visually appealing status bar showing game progress
- Tracking of consonants and vowels used
- Cash management system
- Four rounds of gameplay with cumulative scoring

## Requirements

- Python 3.x
- A text file named `phrases.txt` containing the phrases to be guessed (included)

## Installation

1. Clone or download this repository to your local machine
2. Ensure you have Python 3.x installed
3. Place the `phrases.txt` file in the same directory as the `solo_wof.py` script

> [!TIP]
> If you want to customize the game, you can modify the `phrases.txt` file to include your own phrases! Just make sure each phrase is on a separate line.

## How to Run

1. Open a terminal or command prompt
2. Navigate to the directory containing the game files
3. Run the game with:

    python solo_wof.py

## Gameplay Instructions

1. **Starting the Game**: The game will automatically begin with Round 1, displaying a hidden phrase as underscores.

2. **Main Menu Options**:
   - **Spin the wheel**: Gives you a random cash value and lets you guess a consonant
   - **Buy a vowel**: Costs $250 from your balance to reveal all instances of a chosen vowel
   - **Solve the puzzle**: Attempt to solve the entire phrase
   - **Quit the game**: Exit the current game

3. **Wheel Outcomes**:
   - Cash values: Add to your balance for each instance of the correctly guessed consonant
   - BANKRUPT: Lose all money accumulated in the current round

> [!TIP]
> For the best strategy, try to guess common consonants like 'T', 'N', 'S', and 'R' early in the game to build up your cash before buying vowels!

4. **Round Completion**:
   - Each round ends when you solve the puzzle or quit
   - A minimum of $1,000 is awarded for solving a puzzle if you have less than that amount
   - Your earnings accumulate across all rounds

5. **Game End**:
   - After completing all 4 rounds or quitting
   - Your total earnings across all rounds are displayed

## File Structure

- `solo_wof.py` - The main game script
- `phrases.txt` - Contains a list of phrases to be used in the game

> [!NOTE]
> The game expects the `phrases.txt` file to be in the same directory as the Python script. If you move the file, you'll need to update the file path in the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Aiden Azarnoush

## 
