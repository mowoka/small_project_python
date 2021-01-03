# Guessing The number

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} "))
        if guess < random_number:
            print('Sorry, guess again, Too low')
        if guess > random_number:
            print('Sorry, guess again, Too high')
    print(f'Congratulation, your gues the number {random_number} correctly!!')


def computer_gues(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'is {guess} too high (H), too Low (L), or Correct (C)??? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!!')

computer_gues(10)