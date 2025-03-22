#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 21, 2025
# This program generate a new random
# number every time the program
# is started over and asks user to guess
# what the number is

import random


def main():
    # generate random number between 1 and 60
    correct_guess = random.randint(1, 60)

    # asking user to input their guess
    num_guessed = int(input("Enter your guess: "))

    # check if user is correct, if not also display the
    # correct answer
    if num_guessed == correct_guess:
        print("You guessed correctly!")

    else:
        print("You guessed wrong. " "The correct answer was: {}".format(correct_guess))


if __name__ == "__main__":
    main()
