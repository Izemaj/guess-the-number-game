#Number Guessing Game Objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard'")
random_num = random.randint(0, 100)

def game():
  if level == "easy":
      attempts = 10
  elif level == "hard":
      attempts = 5
  else:
    print("Invalid input")
    return 0
    
  print(f"You have {attempts} attempts to guess the number.")
  guess = int(input("Make a guess: "))
  if 0< guess <= 100:
    while guess != random_num and attempts != 0:
        if guess > random_num:
            print("Too High \n Guess again.")
            print(
                f"You have {attempts} attempts left to guess the number."
            )
            guess = int(input("Make a guess: "))
        else:
            print("Too Low \n Guess again.")
            print(
                f"You have {attempts} attempts left to guess the number."
            )
            guess = int(input("Make a guess: "))
        attempts = attempts - 1
        if attempts == 0:
            print("You have no more attempts left. You lose!")
          
          
    if guess == random_num:
        print(f"The correct number is {random_num} you guessed it!")

  else:
    print("Number is out of range")
    
game()