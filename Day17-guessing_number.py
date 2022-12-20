#Using random module
"""
Day17 Challenge
Start by picking a number between 0 and 100. This will be your first variable.
Create a while loop to keep asking the user to guess your number.
If they are too low, tell them "too low." If they guess too high tell, them "too high."
If the user guesses correctly, tell them they are a winner
Count the number of attempts it took for the user to guess number. Make sure you only show that after they get the answer correct.
"""







print("Guess number between 1 - 100")
num = 50
counter = 0
while True:
  counter += 1
  guess = int(input("Guess the number? "))
  if guess > num and guess < 100:
    print("Too high")
  elif guess < num and guess > 0:
    print("Too low")
  elif guess < 0:
    exit()
  elif guess == 50:
    print("Correct!")
    break
  else:
    print("Plz enter interger between 1-100")  

print(f"It took {counter} guesses to get it correct")
