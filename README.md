# Solo Wheel of Fortune

## Description

Solo Wheel of Fortune is a Python-based implementation of the popular TV game show for a single player. This text-based game challenges you to guess hidden phrases letter by letter while strategically managing your winnings. Built as a command-line application, it features a clean interface with a status bar displaying available letters and your current earnings.

The game randomly selects phrases from an included database of college-themed expressions and presents them as underscores. Players navigate through four rounds, making decisions to spin the wheel for consonants, purchase vowels, or solve the entire puzzle. With elements of both skill and chance - including the dreaded BANKRUPT space that can wipe out your round earnings - each game provides a unique challenge.

Perfect for Python beginners looking to understand game logic implementation or fans of word puzzles seeking a quick entertainment break.

## Game Overview

Solo Wheel of Fortune is based on the classic Hangman game concept with additional elements from the Wheel of Fortune TV show:

- 4 rounds of play
- Each round features a randomly selected phrase
- Players can spin a wheel to select consonants and win cash
- Players can buy vowels using their accumulated cash
- Players can attempt to solve the puzzle at any time
- Risk elements like the BANKRUPT wheel space

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

## How to Run

1. Open a terminal or command prompt
2. Navigate to the directory containing the game files
3. Run the game with:

```bash
python solo_wof.py
