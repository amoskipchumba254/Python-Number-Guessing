# Amos number guessing game

# Importing the random module
import random

# intro
print("welcome to the number guessing game!\n")

# define variables
guesses = 0
number = random.randint(1, 100)

# while loop
while(guesses<3):
    u_guess = int(input("Have a guess: "))
    
    if u_guess == number:
        print("Well done, you win!")
        break
    elif u_guess > number:
        print("your guess was too high")
        guesses = guesses + 1
    elif u_guess < number:
        print("your guess was too low.")
        guesses = guesses + 1
    else:
        print("there was an error.")
        
if guesses == 3:
    print("You lose!")
    print("The number was: " + str(number))