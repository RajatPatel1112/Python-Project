#Stats Generator
"""
Day24 Challenge
1. Create a subroutine that rolls a dice of any size and returns that number.
2. Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
3. Multiply the number from the six-sided dice and eight-sided dice together and return that 
   subroutine as a character's health stats for a video game.
4. Print out the character's health stats.
   character_health = 6-sided-roll*8-sided-roll
5. Add a loop to give the user the option to generate health stats for another character.

OUTPUT SAMPLE:
⚔️ CHARACTER STAT GENERATOR⚔️

Name your warior: Hercules
Hercules health is 8hp
Do you wanna continue: yes
Name your warior: Agnes
Agnes health is 8hp
Do you wanna continue: no
"""








import random
print("⚔️ CHARACTER STAT GENERATOR⚔️\n")

def dice_roll():
  while True:
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,8)
    roll = roll1*roll2
    name = input("Name your warior: ")
    print(f"{name} health is {roll}hp")
    again = input("Do you wanna continue: ")
    if again == "yes":
      name1 = input("Name your warior: ")
      print(f"{name1} health is {roll}hp")
      again1 = input("Do you wanna continue: ")
      if again1 == "yes":
        continue
      elif again1 == "no":
        break
      else:
        print("Invalid input")
        break
    elif again=="no":
      break
    else:
      print("Invalid input")
      break
      
dice_roll()

  
