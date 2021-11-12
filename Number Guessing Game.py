# Guessing Game
import random
number = random.randint(1, 10)

name = input("Please enter your name.")

print("Hello, {name}. Enter a number: ".format(name = name))
number_of_guesses = 0
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Number is too low.")
    if guess > number:
        print("Number is too high")
    if guess == number:
        break

if guess == number:
    print("Congrats! You guessed the number {number} in {guesses} tries.".format(number = number, guesses = number_of_guesses))
else:
    print("You did not guess the number. The correct answer was {number}".format(number = number))
