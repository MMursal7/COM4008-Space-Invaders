# Exercise 8 - guessing game (my own answer)
# The first lines are the starter code from the lab
import random
target = 7
target = random.uniform(1, 100)
target = int(target)

print(target)  # shows the secret, for testing

# My solution
answer = int(input("Guess the number: "))
while answer != target:
    if answer < target:
        print("guessed too low")
    else:
        print("you have guessed too high")
    answer = int(input("Guess again: "))
print("Correct")
