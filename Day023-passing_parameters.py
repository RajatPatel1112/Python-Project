#passing parameters in a function
"""
Day23 Challenge
Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). 
Write one subroutine with one parameter that allows us to call a function (such as rollDice).
"""










import random
print("Infinite Dice 🎲\n")
def roll_dice(sides):
  roll = random.randint(1,sides)
  print("You rolled",roll)
  while True:
    new_roll = random.randint(1,sides)
    again = input("Roll again? ")
    if again=="yes":
      print("You rolled",new_roll)
    elif again=="no":
      break
    else:
      print("Incorrect input")
      break
roll_dice(5)
