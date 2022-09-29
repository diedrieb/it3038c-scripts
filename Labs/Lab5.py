#Guess the number game

import random

number, guess = random.randint(1, 20), 0

while number != guess:
  guess = int(input('Guess a number between 1 and 20 to begin the game:'))

  if (guess > number):
    print('That number is too high! Try again.')
  if (guess < number):
    print('That number is too low! Try again.')
  if (guess == number):
    print('Correct! Nice work.')
