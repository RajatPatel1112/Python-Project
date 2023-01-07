#Using random module to generate random number
"""
Day21 Challenge
Make the number generator completely random between 1 and 100. 
Now, the game will always have the user guess a random number each time
and print how many times it took him/her to guess the number 
"""











print("Guess a number between 1-100\n")
import random
num = random.randint(0,100)
counter = 0
while True:
  guess = int(input("What is your guess?: "))
  if guess > num and guess<=100:
    print("Too High")
  elif guess < num and guess>=0:
    print("Too Low")
  elif guess == num:
    print("Correct!")
    break
  else:
    print("Enter number from 1 to 100")
  counter += 1

print(f"It took you {counter} guessess to get the random number correctly!")
  
