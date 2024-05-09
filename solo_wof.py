###############################################################################
# Author: Aiden Azarnoush
# Date: 04/25/2021
# Description: Wheel of Fortune is a phrase guessing game based on Hangman.
# The game have four rounds. In each round, a phrase selected at random from
# thephrases.txt file will be presented to the player with each of the letters
# in the phrase displayed as underscores. Beneath the phrase, a status bar
# should be displayed that contains three elements; a list of theunused
# consonants, a list of the unused vowels, and the sum of the player’s cash
# earnings forthe current roun.
# Dedicated to my mother - Simin Nematpour
###############################################################################
#import numpy as np
import random as r
import string

# Constants
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
VOWELS = 'AEIOU'
################################################################################
# This function hide all characters and replace them with underscore
def make_hidden(phrase):
    hidden =''
    for c in phrase:
        if  c.isalpha():
            hidden += '_'
        else:
            hidden += c
    return hidden
################################################################################
# This function update the guess and used consonants and vowels
def update_guess(phrase, cons, vows):
    #
    remaining_letters = set(cons) | set(vows)
    used_letters = set(LETTERS) -  remaining_letters
    rv = ''
    for s in phrase:
        if s in used_letters:
            rv += s
        elif s.isalpha():
            rv += '_'
        else:
            rv += s
    return rv
################################################################################
# this function show the status bar
def status_bar(round, guessed, sum, cons=CONSONANTS, vow=VOWELS):

    amount = '$'+str(format(sum,","))
    print(':'*42, end='')
    print(f' ROUND {round} of 4 ::')
    print('::', end='')
    print( guessed.center(54),end='')
    print('::')
    print(':'*58)
    print('::', end='')
    print( cons.center(27) ,end='')
    print('::',end='')
    print( vow.center(11) , end='')
    print('::',end='')
    print(amount.rjust(11), end='')
    print(' ::')
    print(':'*58)
################################################################################
# this function choose randomly one of the prizes when user wants to choose
# a consonant
def spin_the_wheel():
    wheel = []
    space = [(500,5), (550,1), (600,4), (650,3),
             (700,3), (800,1), (900,1), (2500,1),
             ('BANKRUPT', 2)]
    for i,j in space:
        wheel.extend([i]*j)

    return r.choice(wheel)
################################################################################
# prompt the user and shows different options to choose
def get_choice(phrase, guessed, sum, cons, vows, round):
    while True:
        print('What would you like to do?')
        print('  1 - Spin the wheel')
        print('  2 - Buy a vowel')
        print('  3 - Solve the puzzle')
        print('  4 - Quit the game')
        ans = input('Enter the number of your choice: ')
        if ans not in ['1','2','3','4']:
            # if enter other than 1 to 4, gives an error
            print(f'{ans} is an invalid choice.')
        else:
            break

    if ans == '1':
        return pick_consonant(phrase, guessed, round, sum, cons, vows)
    elif ans == '2':
        return pick_vowel(phrase, guessed, round, sum, cons, vows)
    elif ans == '3':
        return solve(phrase, guessed, round, sum, cons, vows)
    else:
        return quit(phrase, guessed, round, sum, cons, vows)
################################################################################
# this function pick let user to pick a consonant
def pick_consonant(phrase, guessed, round, sum, cons, vows):
    # if there is no consonant left, the program will let the user know
    if cons.isspace():
        print('There are no more consonants to choose.')
        status_bar(round, guessed, sum, cons, vows)
        return cons, vows, guessed, sum, True, True
    else:
        prize = spin_the_wheel() # get the prize by calling spin the wheel
        # if wheel land on bakrupt, it will change sum to 0
        if prize == 'BANKRUPT':
            print(f'The wheel landed on BANKRUPT.')
            print(f'You lost ${sum:,}!')
            sum = 0
            status_bar(round, guessed, sum, cons, vows)
            return cons, vows, guessed, sum, True, True
        else:
            print(f'The wheel landed on ${prize:,}.')
    while True:
        ans = input('Pick a consonant: ')
        ans = ans.upper()
        # make sure user enter a consonant not vowels nor antyhing else
        if len(ans) > 1  or ans.isspace() or ans=='':
            print('Please enter exactly one character.')
        else:
            if ans in VOWELS:
                print('Vowels must be purchased.')
            elif ans in string.punctuation or ans.isdigit():
                print(f'The character {ans} is not a letter.')
            elif ans not in cons:
                print(f'The letter {ans} has already been used.')
            else:
                break
    # check if the chosen letter is in the phrase
    if ans in phrase:
        count = phrase.count(ans)
        if count ==1:
            print(f'There is {count} {ans}, which earns you ${count*prize:,}.')
        else:
            print(f"There are {count} {ans}'s, which earns", end='')
            print(f" you ${count*prize:,}.")
        # update sum
        updated_sum = sum + prize*count
        #update consonant
        updated_cons = ''
        for c in cons:
            if c == ans:
                updated_cons +=' '
            else:
                updated_cons += c
        #update guessed
        updated_guessed = update_guess(phrase, updated_cons, vows)
        # show status bar
        status_bar(round, updated_guessed, updated_sum, updated_cons, vows)
        return updated_cons, vows, updated_guessed, updated_sum, True, True
    else:
        print(f"I'm sorry, there are no {ans}'s.")
        #update consonant
        updated_cons = ''
        for c in cons:
            if c == ans:
                updated_cons +=' '
            else:
                updated_cons += c
        #update guessed
        status_bar(round, guessed, sum, updated_cons, vows)
        return updated_cons, vows, guessed, sum, True, True
################################################################################
# This function let user to buy the vowel and pick one
def pick_vowel(phrase, guessed, round, sum, cons, vows):
    # make sure user had enough money
    if sum < VOWEL_COST:
        print(f'You need at least ${VOWEL_COST} to buy a vowel.')
        status_bar(round, guessed, sum, cons, vows)
        return cons, vows, guessed, sum, True, True
    # make sure vowels are not empty
    elif vows.isspace():
        print('There are no more vowels to buy.')
        status_bar(round, guessed, sum, cons, vows)
        return cons, vows, guessed, sum, True, True

    while True:
        ans = input('Pick a vowel: ')
        ans = ans.upper()
        # making sure the user is entering a vowel not something else
        if len(ans) > 1 or ans=='' or ans.isspace():
            print('Please enter exactly one character.')
        else:
            if ans in CONSONANTS :
                print('Consonants cannot be purchased.')
            elif ans in string.punctuation or ans.isdigit():
                print(f'The character {ans} is not a letter.')
            elif ans not in vows:
                print(f'The letter {ans} has already been purchased.')
            else:
                break

    # update sum
    updated_sum = sum - VOWEL_COST
    if ans in phrase:
        count = phrase.count(ans)
        if count ==1:
            print(f'There is {count} {ans}.')
        else:
            print(f"There are {count} {ans}'s.")

        #update vowels
        updated_vows = ''
        for c in vows:
            if c == ans:
                updated_vows +=' '
            else:
                updated_vows += c
        #update guessed
        updated_guessed = update_guess(phrase, cons, updated_vows)
        # show status bar
        status_bar(round, updated_guessed, updated_sum, cons, updated_vows)
        return cons, updated_vows, updated_guessed, updated_sum, True, True
    else:
        print(f"I'm sorry, there are no {ans}'s.")
        #update vowels
        updated_vows = ''
        for c in vows:
            if c == ans:
                updated_vows +=' '
            else:
                updated_vows += c
        #
        status_bar(round, guessed, updated_sum, cons, updated_vows)
        return cons, updated_vows, guessed, updated_sum, True, True
################################################################################
# this function let user to solve the puzzle
def solve(phrase, guessed, round, sum, cons, vows):
    print('Enter your solution.')
    print(f'  Clues: {guessed}')
    ans = input('  Guess: ')
    ans = ans.upper()
    # if user guessed correctly, he will gain money
    if ans == phrase:
        print('Ladies and gentlemen, we have a winner!')
        if sum < 1000: #if user has less than $1000, moeny awarded will be $1000
            sum = 1000
    else:
        print("I'm sorry. The correct solution was:")
        print(f'{phrase}')
        sum = 0

    print(f'You earned ${sum:,} this round.')
    return cons,vows,guessed,sum, False, True
################################################################################
# This function let user to quit the entire game and set the money to 0
def quit(phrase, guessed, round, sum, cons, vows):
    sum = 0
    print(f'You earned ${sum:,} this round.')
    return cons,vows,guessed,sum, False, False
################################################################################
def main():
    # saving all phrases in phrases list
    phrases = []
    with open('phrases.txt') as fo:
        for line in fo:
            phrases.append(line.rstrip())

    total = 0 #total amount of winning
    for round in range(1,5): # for loop for four round
        sum = 0 # money in each round
        phrase  = r.choice(phrases).upper() # picked phrase by computer
        guessed = make_hidden(phrase) # make it hidden
        # show status bar
        status_bar(round, guessed, sum)
        # Ask user to make a choice
        cons, vows, check = CONSONANTS, VOWELS, True
        while check:
            cons,vows,guessed,sum,check,for_loop = get_choice(phrase, guessed,
                                                        sum, cons, vows,round)
        # add total money in each round to total
        total += sum
        if not for_loop: # check if the user decied to quit
            break
    # Thanks for playing and showing the total money he won
    print('Thanks for playing!')
    print(f'You earned a total of ${total:,}.')


if __name__ == '__main__':
    main()
